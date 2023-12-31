"""FinalNew1

Revision ID: d3a69b275157
Revises: 078de5263634
Create Date: 2023-10-27 16:23:57.135050

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd3a69b275157'
down_revision: Union[str, None] = '078de5263634'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bookings', 'room_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('bookings', 'user_id',
                    existing_type=sa.INTEGER(),
                    nullable=False)
    op.alter_column('hotels', 'services',
                    existing_type=postgresql.JSON(astext_type=sa.Text()),
                    nullable=True)
    op.alter_column('rooms', 'services',
                    existing_type=postgresql.JSON(astext_type=sa.Text()),
                    nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rooms', 'services',
                    existing_type=postgresql.JSON(astext_type=sa.Text()),
                    nullable=False)
    op.alter_column('hotels', 'services',
                    existing_type=postgresql.JSON(astext_type=sa.Text()),
                    nullable=False)
    op.alter_column('bookings', 'user_id',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    op.alter_column('bookings', 'room_id',
                    existing_type=sa.INTEGER(),
                    nullable=True)
    # ### end Alembic commands ###
