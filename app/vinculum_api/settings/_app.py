__all__ = ["AppSettings"]
from vinculum_api.settings._base_env import BaseEnvSettings


class AppSettings(BaseEnvSettings):
    """
    Generic application settings.

    These settings are returned as json by the
    healthcheck endpoint, so do not include any sensitive values here, or if
    you do ensure to exclude them from serialization in the `Config` object.

    Attributes:
    ----------
    BUILD_NUMBER : str
        Identity of the CI build of current app instance.
    DEBUG : bool
        If `True` runs `Litestar` in debug mode.
    ENVIRONMENT : str
        "dev", "prod", etc.
    LOG_LEVEL : str
        Stdlib log level names, "DEBUG", "INFO", etc.
    NAME : str
        App name.
    """

    class Config:
        env_prefix = "APP_"
        case_sensitive = True

    BUILD_NUMBER: str = "0"
    DEBUG: bool = False
    ENVIRONMENT: str = "local"
    LOG_LEVEL: str = "INFO"
    NAME: str = "vinculum-api"

    @property
    def slug(self) -> str:
        """
        A slugified name.

        Returns:
        -------
        str
            `self.NAME`, all lowercase and hyphens instead of spaces.
        """
        return "-".join(s.lower() for s in self.NAME.split())
