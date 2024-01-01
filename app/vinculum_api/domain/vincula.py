"""Vincula."""
__all__ = ["Vinculum", "VinculumRepository", "Base"]

from typing import Annotated, final, override

from advanced_alchemy import SQLAlchemyAsyncRepository
from advanced_alchemy.base import BigIntBase
from advanced_alchemy.extensions.litestar import SQLAlchemyDTO
from litestar.dto import DTOConfig
from sqlalchemy import String
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


class Base(BigIntBase):
    """Base.

    Adds an `id` primary key.

    """


Base.metadata.schema = "vinculum_api"


@final
class Vinculum(Base):
    """Vinculum."""

    @override
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return "vincula"

    url: Mapped[str] = mapped_column(String)
    emoji: Mapped[str] = mapped_column(String, index=True)


@final
class VinculumRepository(SQLAlchemyAsyncRepository[Vinculum]):
    """VinculumRepository."""

    model_type = Vinculum
    """The ORM model this repository operates on."""


write_config = DTOConfig(exclude={"id"})
WriteDTO = SQLAlchemyDTO[Annotated[Vinculum, write_config]]
ReadDTO = SQLAlchemyDTO[Vinculum]
