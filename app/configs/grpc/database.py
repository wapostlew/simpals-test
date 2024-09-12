from pydantic import HttpUrl, AnyHttpUrl, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    elasticsearch: str = "http://elastic:9200"
