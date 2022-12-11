"""create users table

Revision ID: 6d59fff6623f
Revises: 232bf8bf96aa
Create Date: 2022-07-26 20:14:02.696910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d59fff6623f'
down_revision = '232bf8bf96aa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table("users")
    pass
