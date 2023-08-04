"""add content column to posts table

Revision ID: 07055e66cca2
Revises: 1797364c26d8
Create Date: 2023-08-04 13:46:38.949826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "07055e66cca2"
down_revision: Union[str, None] = "1797364c26d8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
