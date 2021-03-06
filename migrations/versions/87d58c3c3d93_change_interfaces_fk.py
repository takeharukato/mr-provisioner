"""change interfaces FK

Revision ID: 87d58c3c3d93
Revises: 37af89374583
Create Date: 2017-06-18 15:18:51.533339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87d58c3c3d93'
down_revision = '37af89374583'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('interface_machine_id_fkey', 'interface', type_='foreignkey')
    op.create_foreign_key(None, 'interface', 'machine', ['machine_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'interface', type_='foreignkey')
    op.create_foreign_key('interface_machine_id_fkey', 'interface', 'machine', ['machine_id'], ['id'])
    # ### end Alembic commands ###
