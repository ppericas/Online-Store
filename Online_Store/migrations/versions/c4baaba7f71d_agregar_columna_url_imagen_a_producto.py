"""Agregar columna url_imagen a Producto

Revision ID: c4baaba7f71d
Revises: 
Create Date: 2024-05-22 19:26:45.154965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4baaba7f71d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('productos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('url_imagen', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('productos', schema=None) as batch_op:
        batch_op.drop_column('url_imagen')

    # ### end Alembic commands ###