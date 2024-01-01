"""Controllers."""
__all__ = ["create_vincula_router"]

from litestar import Router

from vinculum_api.controllers import VinculumController


def create_vincula_router() -> Router:
    """Create the router."""
    return Router(
        path="/v1",
        route_handlers=[VinculumController],
    )
