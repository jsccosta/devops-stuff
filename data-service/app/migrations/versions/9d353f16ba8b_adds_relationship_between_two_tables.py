"""adds relationship between two tables

Revision ID: 9d353f16ba8b
Revises: a89ff553f405
Create Date: 2024-02-28 22:36:48.116608

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d353f16ba8b'
down_revision: Union[str, None] = 'a89ff553f405'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company_metrics', sa.Column('company_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'company_metrics', 'company', ['company_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'company_metrics', type_='foreignkey')
    op.drop_column('company_metrics', 'company_id')
    # ### end Alembic commands ###
