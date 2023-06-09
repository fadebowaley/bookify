"""empty message

Revision ID: e7b48f85bd70
Revises: 4fea89e0476c
Create Date: 2023-07-05 22:08:58.354292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7b48f85bd70'
down_revision = '4fea89e0476c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event_groups', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event_groups', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
