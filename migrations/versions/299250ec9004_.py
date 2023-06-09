"""empty message

Revision ID: 299250ec9004
Revises: c406da159b70
Create Date: 2023-04-29 17:24:08.601272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '299250ec9004'
down_revision = 'c406da159b70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_image', sa.String(length=80), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.drop_column('user_image')

    # ### end Alembic commands ###
