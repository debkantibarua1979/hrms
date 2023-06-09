"""empty message

Revision ID: c406da159b70
Revises: ded9c1f21b42
Create Date: 2023-04-29 17:22:47.680042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c406da159b70'
down_revision = 'ded9c1f21b42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_image', sa.String(length=80), nullable=True))
        batch_op.create_unique_constraint(None, ['user_image'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employees', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('user_image')

    # ### end Alembic commands ###
