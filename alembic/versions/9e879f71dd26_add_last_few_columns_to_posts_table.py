"""add last few columns to posts table

Revision ID: 9e879f71dd26
Revises: e6946b3af34e
Create Date: 2023-02-04 21:48:33.416857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e879f71dd26'
down_revision = 'e6946b3af34e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts', 'created_at')
    pass
