from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent


class ConnectCh(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8123
    username: str = "default"
    database: str = "moex"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter='__',
        env_file_encoding='utf-8',
        env_file=BASE_DIR / "config" / ".env"
    )

    clickhouse: ConnectCh = ConnectCh()
    rabbit_url: str = "amqp://guest:guest@127.0.0.1:5672/en0"


settings = Settings()
