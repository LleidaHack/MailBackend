from typing import Optional
from pydantic import Field, validator
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class ClientSettings(BaseSettings):
    url: str = Field(..., description="Backend client URL", env="CLIENT__URL")
    service_token: str = Field(default="HOLA",
                               description="Service authentication token",
                               env="CLIENT__SERVICE_TOKEN")


class DatabaseSettings(BaseSettings):
    url: str = Field(...,
                     description="Database connection URL",
                     env="DATABASE__URL")


class MailSettings(BaseSettings):
    username: str = Field(...,
                          description="SMTP username",
                          env="MAIL__USERNAME")
    password: str = Field(...,
                          description="SMTP password",
                          env="MAIL__PASSWORD")
    from_mail: str = Field(...,
                           description="From email address",
                           env="MAIL__FROM_MAIL")
    port: int = Field(default=465, description="SMTP port", env="MAIL__PORT")
    server: str = Field(default="smtp.gmail.com",
                        description="SMTP server",
                        env="MAIL__SERVER")
    from_name: str = Field(default="InfoLleidaHack",
                           description="From name",
                           env="MAIL__FROM_NAME")
    send_mails: bool = Field(default=False,
                             description="Enable sending emails",
                             env="MAIL__SEND_MAILS")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",
                                      env_file_encoding="utf-8",
                                      env_nested_delimiter="__",
                                      case_sensitive=False,
                                      extra="allow")

    # General settings
    front_url: str = Field(
        default="https://frontend.integration.lleidahack.dev/hackeps",
        description="Frontend URL",
        env="FRONT_URL")
    back_url: str = Field(default="http://localhost:8000/",
                          description="Backend URL",
                          env="BACK_URL")
    static_folder: str = Field(default="static",
                               description="Static files folder path",
                               env="STATIC_FOLDER")
    contact_mail: str = Field(default="contacte@lleidahack.dev",
                              description="Contact email address",
                              env="CONTACT_MAIL")
    initial_templates_path: str = Field(
        default="src,utils,internal_templates,initial_templates",
        description="Initial templates path",
        env="INITIAL_TEMPLATES_PATH")

    # Environment
    env: str = Field(default="main",
                     description="Environment name (main/integration)",
                     env="ENV")

    # Nested settings
    client: ClientSettings
    database: DatabaseSettings
    mail: MailSettings

    def __init__(self, **kwargs):
        # Handle environment-specific defaults
        env = os.environ.get('ENV', 'main')

        if env == 'integration':
            # Integration environment defaults
            mail_postgres_password = os.environ.get(
                'INTEGRATION_MAIL_POSTGRES_PASSWORD', 'testpass123')
            kwargs.setdefault(
                'database', {
                    'url':
                    f"postgresql://lleidahack_mail_user:{mail_postgres_password}@db-mail-integration:5432/lleidahack_mail_integration"
                })
            kwargs.setdefault(
                'client', {
                    'url':
                    'http://backend-integration:8000/',
                    'service_token':
                    os.environ.get('CLIENT__SERVICE_TOKEN', 'HOLA')
                })
        else:
            # Main environment defaults - require env vars for sensitive data
            db_url = os.environ.get('DATABASE__URL')
            if not db_url:
                raise ValueError(
                    "DATABASE__URL environment variable is required for production"
                )

            kwargs.setdefault('database', {'url': db_url})
            kwargs.setdefault(
                'client', {
                    'url':
                    os.environ.get('CLIENT__URL', 'http://localhost:8000/'),
                    'service_token':
                    os.environ.get('CLIENT__SERVICE_TOKEN', 'HOLA')
                })

        # Mail settings always require environment variables for sensitive data
        if not kwargs.get('mail'):
            mail_username = os.environ.get('MAIL__USERNAME')
            mail_password = os.environ.get('MAIL__PASSWORD')
            mail_from = os.environ.get('MAIL__FROM_MAIL')

            if env != 'integration' and not all(
                [mail_username, mail_password, mail_from]):
                raise ValueError(
                    "MAIL__USERNAME, MAIL__PASSWORD, and MAIL__FROM_MAIL environment variables are required"
                )

            kwargs.setdefault(
                'mail', {
                    'username':
                    mail_username or 'info@lleidahack.dev',
                    'password':
                    mail_password or 'changeme',
                    'from_mail':
                    mail_from or 'info@lleidahack.dev',
                    'port':
                    int(os.environ.get('MAIL__PORT', 465)),
                    'server':
                    os.environ.get('MAIL__SERVER', 'smtp.gmail.com'),
                    'from_name':
                    os.environ.get('MAIL__FROM_NAME', 'InfoLleidaHack'),
                    'send_mails':
                    os.environ.get('MAIL__SEND_MAILS', 'false').lower()
                    == 'true'
                })

        super().__init__(**kwargs)


# Global settings instance
settings = Settings()
