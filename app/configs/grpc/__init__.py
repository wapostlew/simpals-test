from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from app.configs.grpc.database import DatabaseSettings


class GrpcSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
        env_prefix="grpc_",
        env_nested_delimiter="_",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="allow",
    )
    host: str = "[::]"
    port: int = 50051
    db: DatabaseSettings
