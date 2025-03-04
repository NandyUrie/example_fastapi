"""create post table

Revision ID: 9a601a69e7da
Revises: 
Create Date: 2024-05-19 18:52:18.376910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a601a69e7da'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
    ,sa.Column('title', sa.String(), nullable=False))

def downgrade() -> None:
    op.drop_table('posts')
