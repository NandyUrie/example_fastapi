"""add user table

Revision ID: a381fc3651b8
Revises: a8f6173a5e81
Create Date: 2024-05-19 19:13:19.825019

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a381fc3651b8'
down_revision: Union[str, None] = 'a8f6173a5e81'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                     sa.Column('id', sa.Integer(), nullable=False),
                     sa.Column('email', sa.String(), nullable=False),
                     sa.Column('password', sa.String(), nullable=False),
                     sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email'))


def downgrade() -> None:
    op.drop_table('users')
    pass
