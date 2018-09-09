"""Migration

Revision ID: 617d5de6b53f
Revises: 
Create Date: 2018-09-09 12:54:42.770380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '617d5de6b53f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=255), nullable=True),
    sa.Column('category_description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('pitchs', sa.Column('category_id', sa.Integer(), nullable=True))
    op.drop_column('pitchs', 'category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitchs', sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('pitchs', 'category_id')
    op.drop_table('categories')
    # ### end Alembic commands ###
