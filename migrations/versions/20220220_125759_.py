"""empty message

Revision ID: d3b3b80a69ea
Revises: 29054ba7cf42
Create Date: 2022-02-20 12:57:59.979206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3b3b80a69ea'
down_revision = '29054ba7cf42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.Column('study_image', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('attendee', 'event_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('attendee', 'attendee_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('attendee', 'attendee_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('attendee', 'event_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_table('images')
    op.drop_table('albums')
    # ### end Alembic commands ###
