"""add vinc table

Revision ID: 218526345707
Revises: a03ac4a1ad5d
Create Date: 2024-01-01 17:24:14.644517

"""
from typing import Sequence

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "218526345707"
down_revision: str | None = "a03ac4a1ad5d"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute("create schema vinculum_api")


def downgrade() -> None:
    op.execute("drop schema vinculum_api")
