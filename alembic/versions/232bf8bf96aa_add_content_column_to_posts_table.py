"""add content column to posts table

Revision ID: 232bf8bf96aa
Revises: 6d4dad6a4f92
Create Date: 2022-07-26 19:34:31.311494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '232bf8bf96aa'
down_revision = '6d4dad6a4f92'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
