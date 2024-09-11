from pydantic import HttpUrl, AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    elasticsearch: AnyHttpUrl
