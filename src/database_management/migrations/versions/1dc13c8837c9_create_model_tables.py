"""create_model_tables

Revision ID: 1dc13c8837c9
Revises: 
Create Date: 2023-07-03 22:51:10.537227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dc13c8837c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('models',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('model_version_id', sa.String(length=2048), nullable=False),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'model_version_id'),
    sa.UniqueConstraint('model_version_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('models')
    # ### end Alembic commands ###
