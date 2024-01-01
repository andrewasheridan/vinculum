"""VinculumController."""
from typing import final

from litestar import Controller, get, post
from litestar.di import Provide

from vinculum_api.domain import Vinculum
from vinculum_api.services import VinculumService


@final
class VinculumController(Controller):
    """VinculumController."""

    path = "/vincula"
    """The path fragment for the controller.
    
    vincula (noun): plural of vinculum.
    """

    dependencies = {"vinculum_service": Provide(dependency=VinculumService, sync_to_thread=False)}
    """A string keyed dictionary of dependency :class:`Provider <.di.Provide>` instances."""

    @post("/")
    async def create_vinculum(self, url: str, vinculum_service: VinculumService) -> Vinculum:
        """Create a Vinculum w/ a short emoji URL."""
        return await vinculum_service.create_with_url(url)

    @get("/e/{emoji:str}")
    async def get_vinculum(self, emoji: str, vinculum_service: VinculumService) -> Vinculum | None:
        """Get an existing Vinculum."""
        return await vinculum_service.get_by_emoji(emoji)
