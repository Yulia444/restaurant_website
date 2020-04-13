"""empty message

Revision ID: 5ba9fc68a503
Revises: c19ed319c62b
Create Date: 2020-04-10 23:36:40.945423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ba9fc68a503'
down_revision = 'c19ed319c62b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=16), nullable=True),
    sa.Column('title', sa.String(length=72), nullable=True),
    sa.Column('review', sa.Text(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###