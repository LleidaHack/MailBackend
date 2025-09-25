from typing import Optional
from pydantic import Field, validator, AliasChoices
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class MailSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",
                                      env_file_encoding="utf-8",
                                      env_nested_delimiter="__",
                                      case_sensitive=False,
                                      extra="ignore")
    username: str = Field(default="username",
                          description="Mail service username",
                          alias=AliasChoices("MAIL__USERNAME"))
    password: str = Field(default="password",
                          description="Mail service password",
                          alias=AliasChoices("MAIL__PASSWORD"))
    from_mail: str = Field(
        default="from@example.com",
        description="Email address used in the 'From' header",
        alias=AliasChoices("MAIL__FROM")
    )
    port: int = Field(
        default=587, 
        description="Mail service port",
        alias=AliasChoices("MAIL__PORT")
    )
    server: str = Field(
        default="smtp.example.com", 
        description="Mail service SMTP server",
        alias=AliasChoices("MAIL__SERVER")
    )
    from_name: str = Field(
        default="Example Service", 
        description="Name used in the 'From' header",
        alias=AliasChoices("MAIL__FROM_NAME")
    )
    send_mails: bool = True


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",
                                      env_file_encoding="utf-8",
                                      env_nested_delimiter="__",
                                      case_sensitive=False,
                                      extra="ignore")
    url: str = Field(...,
                     description="Database connection URL",
                     alias=AliasChoices("DATABASE__URL"))


#class ClientSettings(BaseSettings):
#    url: str = Field(...,
#                     description="Mail service URL",
#                     alias=AliasChoices("CLIENTS__MAIL_CLIENT__URL"))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",
                                      env_file_encoding="utf-8",
                                      env_nested_delimiter="__",
                                      case_sensitive=False,
                                      extra="ignore")

    # General settings

    front_url: str = Field(
        default="https://frontend.integration.lleidahack.dev/hackeps",
        description="Frontend URL",
        alias=AliasChoices("FRONT_URL"))
    back_url: str = Field(default="http://localhost:8000/",
                          description="Backend URL",
                          alias=AliasChoices("BACK_URL"))
    static_folder: str = Field(default="static",
                               description="Static files folder path",
                               alias=AliasChoices("STATIC_FOLDER"))
    contact_mail: str = Field(default="contacte@lleidahack.dev",
                              description="Contact email address",
                              alias=AliasChoices("CONTACT_MAIL"))
    initial_templates_path: str = Field(
        default="src/templates/emails/initial.html",
        description="Path to the initial email template",
        alias=AliasChoices("INITIAL_TEMPLATES_PATH"))
    #url: str = Field(...,
    #                 description="Mail service URL",
    #                 alias=AliasChoices("CLIENTS__MAIL_CLIENT__URL"))
    # Nested settings
    port:int = Field(
        default=8001, 
        description="back_port",
        alias=AliasChoices("PORT")
    )
    database: DatabaseSettings
    mail: MailSettings
    #clients: ClientSettings

    def __init__(self, **kwargs):
        # Handle environment-specific defaults
        # env = os.environ.get('ENV', 'main')

        super().__init__(**kwargs)
#        self.databse=DatabaseSettings()
#        self.mail=MailSettings()
#        self.clients=ClientSettings()


# Global settings instance
settings = Settings()
