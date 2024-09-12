from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from app.configs.graphql.clients import ClientSettings


class GraphqlSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
        env_prefix="graphl_",
        env_nested_delimiter="_",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="allow",
    )
    host: str = "0.0.0.0"
    port: int = 8000
    clients: ClientSettings = ClientSettings()
