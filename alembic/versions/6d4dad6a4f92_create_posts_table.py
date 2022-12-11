"""create posts table

Revision ID: 6d4dad6a4f92
Revises: 
Create Date: 2022-07-21 21:47:43.272977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d4dad6a4f92'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_table("posts")
    pass
