"""Create phone number for user column

Revision ID: ea34ba269e40
Revises: 
Create Date: 2025-07-30 22:48:26.321796

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea34ba269e40'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable = True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("users", 'phone_number')
