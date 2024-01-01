__all__ = ["APISettings"]

from vinculum_api.settings._base_env import BaseEnvSettings


class APISettings(BaseEnvSettings):
    """API specific configuration.

    Prefix all environment variables with `API_`, e.g., `API_CACHE_EXPIRATION`.

    Attributes:
    ----------
    CACHE_EXPIRATION : int
        Default cache key expiration in seconds.
    DEFAULT_PAGINATION_LIMIT : int
        Max records received for collection routes.
    """

    class Config:
        env_prefix = "API_"
        case_sensitive = True

    CACHE_EXPIRATION: int = 60
    DB_SESSION_DEPENDENCY_KEY: str = "db_session"
    DEFAULT_PAGINATION_LIMIT: int = 100
    DEFAULT_USER_NAME: str = "__default_user__"
    HEALTH_PATH: str = "/health"
    SECRET_KEY: str = "abc123"
    USER_DEPENDENCY_KEY: str = "user"
