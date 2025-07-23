"""Corrige tipos de data e hora em sessoes

Revision ID: fa7b11936659
Revises: 76c71c4f1efa
Create Date: 2025-07-22 15:59:43.330558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa7b11936659'
down_revision: Union[str, Sequence[str], None] = '76c71c4f1efa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
