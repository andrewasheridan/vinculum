"""VinculumService."""
from typing import final

from aiohttp import ClientSession
from litestar.datastructures import State
from sqlalchemy.ext.asyncio import AsyncSession

from exemplars.incrementum import Incrementum
from vinculum_api.domain import Vinculum, VinculumRepository
from vinculum_api.lib import Service, number_to_emoji


@final
class VinculumService(Service[Vinculum]):
    """VinculumService."""

    def __init__(self, state: State, db_session: AsyncSession) -> None:
        """Create the VinculumService."""
        super().__init__(repository=VinculumRepository(session=db_session, auto_commit=True))  # type: ignore[arg-type]
        self._incrementum_session: ClientSession = state.incrementum_session

    async def get_by_emoji(self, emoji: str) -> Vinculum | None:
        """Get by emoji."""
        return await self.repository.get_one_or_none(emoji=emoji)

    async def create_with_url(self, url: str, /) -> Vinculum:
        """Create an emoji-url from the given url."""
        _ = url
        number = await self._get_number_for_url()
        emoji = number_to_emoji(number)
        return await self.create(Vinculum(id=number, url=url, emoji=emoji))

    async def _get_number_for_url(self) -> int:
        nomen = "vincula"  # TODO: Make constant
        async with self._incrementum_session.get(f"/v1/incrementa/{nomen}/deinde") as response:
            data = await response.json()
            incrementum = Incrementum(**data)

        return incrementum.valorem
