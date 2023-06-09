"""empty message

Revision ID: c76c1a1d494e
Revises: e84030157c4a
Create Date: 2023-04-24 18:56:05.157643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c76c1a1d494e'
down_revision = 'e84030157c4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('daily_attendances', schema=None) as batch_op:
        batch_op.alter_column('office_entry_time',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
        batch_op.alter_column('office_exit_time',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('daily_attendances', schema=None) as batch_op:
        batch_op.alter_column('office_exit_time',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
        batch_op.alter_column('office_entry_time',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)

    # ### end Alembic commands ###
