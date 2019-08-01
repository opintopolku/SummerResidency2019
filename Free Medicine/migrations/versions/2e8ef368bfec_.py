"""empty message

Revision ID: 2e8ef368bfec
Revises: 0931acd9e651
Create Date: 2019-07-25 14:44:25.046492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e8ef368bfec'
down_revision = '0931acd9e651'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('disease_category', sa.Column('disease_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'disease_category', 'disease', ['disease_id'], ['id'])
    op.add_column('disease_stage', sa.Column('disease_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'disease_stage', 'disease', ['disease_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'disease_stage', type_='foreignkey')
    op.drop_column('disease_stage', 'disease_id')
    op.drop_constraint(None, 'disease_category', type_='foreignkey')
    op.drop_column('disease_category', 'disease_id')
    # ### end Alembic commands ###
