from pydantic import HttpUrl, AnyHttpUrl, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class AdvertisementClientConfig(BaseSettings):
    host: str = "localhost"
    port: int = 51500


class GrpcClients(BaseSettings):
    avertisement: AdvertisementClientConfig = AdvertisementClientConfig()


class ClientSettings(BaseSettings):
    grpc: GrpcClients = GrpcClients()
