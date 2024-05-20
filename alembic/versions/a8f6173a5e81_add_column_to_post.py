"""add column to post

Revision ID: a8f6173a5e81
Revises: 9a601a69e7da
Create Date: 2024-05-19 19:07:16.687472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a8f6173a5e81'
down_revision: Union[str, None] = '9a601a69e7da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
