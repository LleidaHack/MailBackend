from typing import Optional
from pydantic import Field, validator
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class MailSettings(BaseSettings):
    username: str = Field(default="username",
                          description="Mail service username",
                          env="MAIL__USERNAME")
    password: str = Field(default="password",
                          description="Mail service password",
                          env="MAIL__PASSWORD")
    from_mail: str = Field(
        default="from@example.com",
        description="Email address used in the 'From' header",
        env="MAIL__FROM")
    port: int = Field(default=587,
                      description="Mail service port",
                      env="MAIL__PORT")
    server: str = Field(default="smtp.example.com",
                        description="Mail service SMTP server",
                        env="MAIL__SERVER")
    from_name: str = Field(default="Example Service",
                           description="Name used in the 'From' header",
                           env="MAIL__FROM_NAME")
    send_mails: bool = True


class DatabaseSettings(BaseSettings):
    url: str = Field(...,
                     description="Database connection URL",
                     env="DATABASE__URL")


class ClientSettings(BaseSettings):
    url: str = Field(...,
                     description="Mail service URL",
                     env="CLIENTS__MAIL_CLIENT__URL")


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
        default="src/templates/emails/initial.html",
        description="Path to the initial email template",
        env="INITIAL_TEMPLATES_PATH")

    # Nested settings
    mail: MailSettings = Field(default_factory=MailSettings)
    database: DatabaseSettings
    clients: ClientSettings

    def __init__(self, **kwargs):
        # Handle environment-specific defaults
        # env = os.environ.get('ENV', 'main')

        super().__init__(**kwargs)


# Global settings instance
settings = Settings()
