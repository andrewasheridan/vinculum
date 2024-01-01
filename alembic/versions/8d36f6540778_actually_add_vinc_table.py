"""Actually add vinc table

Revision ID: 8d36f6540778
Revises: 218526345707
Create Date: 2024-01-01 17:28:06.504680

"""
from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "8d36f6540778"
down_revision: str | None = "218526345707"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "vincula",
        sa.Column("url", sa.String(), nullable=False),
        sa.Column("emoji", sa.String(), nullable=False),
        sa.Column("id", sa.BigInteger().with_variant(sa.Integer(), "sqlite"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        schema="vinculum_api",
    )
    op.create_index(op.f("ix_vinculum_api_vincula_emoji"), "vincula", ["emoji"], unique=False, schema="vinculum_api")


def downgrade() -> None:
    op.drop_index(op.f("ix_vinculum_api_vincula_emoji"), table_name="vincula", schema="vinculum_api")
    op.drop_table("vincula", schema="vinculum_api")
