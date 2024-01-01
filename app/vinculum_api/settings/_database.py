"""DatabaseSettings."""

from typing import Literal

from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import ValidationInfo

from vinculum_api.settings._base_env import BaseEnvSettings


class DatabaseSettings(BaseEnvSettings):
    """Configures the database for the application.

    Prefix all environment variables with `DB_`, e.g., `DB_URL`.

    Attributes:
    ----------
    ECHO : bool
        Enables SQLAlchemy engine logs.
    URL : PostgresDsn
        URL for database connection.
    """

    class Config:
        env_prefix = "POSTGRES_"
        case_sensitive = True

    ECHO: bool = False
    ECHO_POOL: bool | Literal["debug"] = False
    POOL_DISABLE: bool = False
    POOL_MAX_OVERFLOW: int = 10
    POOL_SIZE: int = 5
    POOL_TIMEOUT: int = 30
    SERVER: str = "foo"
    USER: str = "foo"
    PASSWORD: str = "foo"
    DB: str = "foo"
    URI: PostgresDsn = PostgresDsn("postgresql+asyncpg://foo:foo@localhost:5432/foo")

    @field_validator("URI", mode="before")
    def assemble_db_uri(cls, v: str | None, info: ValidationInfo) -> PostgresDsn:
        if isinstance(v, str):
            return PostgresDsn(v)

        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=info.data.get("USER"),
            password=info.data.get("PASSWORD"),
            host=info.data.get("SERVER"),
            path=info.data.get("DB"),
        )
