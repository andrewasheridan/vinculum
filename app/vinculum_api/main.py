"""Main."""
__all__: list[str] = []

from litestar import Litestar
from uvicorn import run

from vinculum_api import settings
from vinculum_api.lib import incrementum_session, sqlalchemy_plugin
from vinculum_api.routers import create_vincula_router


def create_app() -> Litestar:
    return Litestar(
        debug=settings.app.DEBUG,
        route_handlers=[create_vincula_router()],
        lifespan=[incrementum_session],
        plugins=[sqlalchemy_plugin.plugin],
    )


app = create_app()

if __name__ == "__main__":
    run(
        app,
        host=settings.server.HOST,
        log_level=settings.server.LOG_LEVEL,
        port=settings.server.PORT,
        reload=settings.server.RELOAD,
        timeout_keep_alive=settings.server.KEEPALIVE,
    )
