"""Fixing datetime

Revision ID: 9b8e67a6e098
Revises: 7c58f48d4815
Create Date: 2025-07-22 14:23:28.165838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b8e67a6e098'
down_revision: Union[str, Sequence[str], None] = '7c58f48d4815'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
