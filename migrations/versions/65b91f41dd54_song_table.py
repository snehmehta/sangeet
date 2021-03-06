"""song table

Revision ID: 65b91f41dd54
Revises: c00b2c515005
Create Date: 2020-08-14 14:55:03.576423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65b91f41dd54'
down_revision = 'c00b2c515005'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('song', sa.Column('artist', sa.String(length=40), nullable=True))
    op.add_column('song', sa.Column('title', sa.String(length=40), nullable=True))
    op.create_index(op.f('ix_song_artist'), 'song', ['artist'], unique=False)
    op.create_index(op.f('ix_song_title'), 'song', ['title'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_song_title'), table_name='song')
    op.drop_index(op.f('ix_song_artist'), table_name='song')
    op.drop_column('song', 'title')
    op.drop_column('song', 'artist')
    # ### end Alembic commands ###
