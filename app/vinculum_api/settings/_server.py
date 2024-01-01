__all__ = ["ServerSettings"]
from vinculum_api.settings._base_env import BaseEnvSettings


class ServerSettings(BaseEnvSettings):
    class Config:
        env_prefix = "UVICORN_"
        case_sensitive = True

    HOST: str = "localhost"
    LOG_LEVEL: str = "info"
    PORT: int = 8001
    RELOAD: bool = True
    KEEPALIVE: int = 65
    TIMEOUT: int = 65
