"""Settings."""
__all__ = ["app", "server"]

from vinculum_api.settings._api import APISettings
from vinculum_api.settings._app import AppSettings
from vinculum_api.settings._database import DatabaseSettings
from vinculum_api.settings._server import ServerSettings

api = APISettings()
app = AppSettings()
db = DatabaseSettings()
server = ServerSettings()
