"""Fixing datetime-2

Revision ID: 76c71c4f1efa
Revises: 9b8e67a6e098
Create Date: 2025-07-22 15:58:19.963389

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76c71c4f1efa'
down_revision: Union[str, Sequence[str], None] = '9b8e67a6e098'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
