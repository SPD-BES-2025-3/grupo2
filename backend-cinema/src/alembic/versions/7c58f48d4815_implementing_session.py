"""Implementing session

Revision ID: 7c58f48d4815
Revises: 4bedb84a47de
Create Date: 2025-07-22 13:54:23.074990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c58f48d4815'
down_revision: Union[str, Sequence[str], None] = '4bedb84a47de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
