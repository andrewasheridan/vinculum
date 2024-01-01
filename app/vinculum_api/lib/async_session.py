"""Incrementum session."""
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from aiohttp import ClientSession
from litestar import Litestar


@asynccontextmanager
async def incrementum_session(app: Litestar) -> AsyncGenerator[None, None]:
    """Incrementum session."""
    session: ClientSession | None = getattr(app.state, "incrementum_session", None)
    if session is None:
        # https://github.com/aio-libs/aiohttp/issues/6647
        app.state.incrementum_session = ClientSession(base_url="http://incrementum:8000/", trust_env=True)

    try:
        yield
    finally:
        await app.state.incrementum_session.close()
