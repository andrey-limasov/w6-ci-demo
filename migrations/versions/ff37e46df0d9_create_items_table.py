"""create items table

Revision ID: ff37e46df0d9
Revises:
Create Date: 2026-10-28 12:10:07.615463

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ff37e46df0d9"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "items",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("items")
