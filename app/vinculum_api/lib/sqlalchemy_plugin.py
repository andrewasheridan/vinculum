"""SqlAlchemy Plugin."""
__all__ = ["plugin"]
from typing import cast

from advanced_alchemy.extensions.litestar import SQLAlchemyPlugin
from advanced_alchemy.extensions.litestar.plugins.init.config.common import (
    SESSION_SCOPE_KEY,
    SESSION_TERMINUS_ASGI_EVENTS,
)
from litestar.contrib.sqlalchemy.plugins.init.config import SQLAlchemyAsyncConfig
from litestar.types.asgi_types import Message, Scope
from litestar.utils.scope.state import delete_litestar_scope_state, get_litestar_scope_state
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from vinculum_api import settings

_engine = create_async_engine(
    url=settings.db.URI.unicode_string(),
    echo=settings.db.ECHO,
    echo_pool=settings.db.ECHO_POOL,
    max_overflow=settings.db.POOL_MAX_OVERFLOW,
    pool_size=settings.db.POOL_SIZE,
    pool_timeout=settings.db.POOL_TIMEOUT,
    poolclass=NullPool if settings.db.POOL_DISABLE else None,
)
"""Configure via DatabaseSettings.

Overrides default JSON
serializer to use `msgspec`. See [`create_async_engine()`][sqlalchemy.ext.asyncio.create_async_engine]
for detailed instructions.
"""

_async_session_factory = async_sessionmaker(_engine, expire_on_commit=False, class_=AsyncSession)
"""Database session factory.

See [`async_sessionmaker()`][sqlalchemy.ext.asyncio.async_sessionmaker].
"""


async def _before_send_handler(message: Message, scope: Scope) -> None:
    """Inspects the status of response and commits, or rolls back the database.

    Custom `before_send_handler` for SQLAlchemy plugin that i

    Args:
        message: ASGI message
        _:
        scope: ASGI scope
    """
    session = cast("AsyncSession | None", get_litestar_scope_state(scope, SESSION_SCOPE_KEY))
    try:
        if session is not None and message["type"] == "http.response.start":
            if 200 <= message["status"] < 300:
                await session.commit()
            else:
                await session.rollback()
    finally:
        if session is not None and message["type"] in SESSION_TERMINUS_ASGI_EVENTS:
            await session.close()
            delete_litestar_scope_state(scope, SESSION_SCOPE_KEY)


_config = SQLAlchemyAsyncConfig(
    session_dependency_key=settings.api.DB_SESSION_DEPENDENCY_KEY,
    engine_instance=_engine,
    session_maker=_async_session_factory,
    before_send_handler=_before_send_handler,
)

plugin = SQLAlchemyPlugin(config=_config)
