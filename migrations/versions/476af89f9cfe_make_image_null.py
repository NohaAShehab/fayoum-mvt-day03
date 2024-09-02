"""make image null

Revision ID: 476af89f9cfe
Revises: f6413fae65ce
Create Date: 2024-09-02 13:12:59.527658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '476af89f9cfe'
down_revision = 'f6413fae65ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)

    # ### end Alembic commands ###
