"""Migration

Revision ID: 7c9b4d5c11e2
Revises: cddea033c038
Create Date: 2018-09-10 14:54:59.056019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c9b4d5c11e2'
down_revision = 'cddea033c038'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitchs', sa.Column('posted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitchs', 'posted')
    # ### end Alembic commands ###
