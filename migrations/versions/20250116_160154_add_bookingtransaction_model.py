"""Add BookingTransaction model

Revision ID: 41a1ca3fd965
Revises: a08e393323df
Create Date: 2025-01-16 16:01:54.793919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41a1ca3fd965'
down_revision = 'a08e393323df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('borrowing_transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('borrow_date', sa.Date(), nullable=False),
    sa.Column('due_date', sa.Date(), nullable=False),
    sa.Column('return_date', sa.Date(), nullable=True),
    sa.Column('status', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], name='fk_booking_transactions_book_id'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_booking_transactions_user_id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('borrowing_transactions')
    # ### end Alembic commands ###
