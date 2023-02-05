"""add content column to posts table

Revision ID: b164b0cf9633
Revises: 8481befd58b8
Create Date: 2023-02-04 21:33:31.213539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b164b0cf9633'
down_revision = '8481befd58b8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
