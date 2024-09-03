from pydantic import BaseModel, PostgresDsn
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    api: str = "/api"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 10
    max_overflow: int = 100


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(
            ".env_template",
            ".env",
        ),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="SHOP_APP__",
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()
