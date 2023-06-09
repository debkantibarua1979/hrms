"""empty message

Revision ID: f8cb55412aa5
Revises: 61ee689bfbff
Create Date: 2023-04-29 17:10:33.876232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8cb55412aa5'
down_revision = '61ee689bfbff'
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
