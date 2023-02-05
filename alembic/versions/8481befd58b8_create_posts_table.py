"""create posts table

Revision ID: 8481befd58b8
Revises: 
Create Date: 2023-02-02 10:11:40.452230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8481befd58b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
