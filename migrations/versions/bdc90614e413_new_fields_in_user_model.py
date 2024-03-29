"""new fields in user model

Revision ID: bdc90614e413
Revises: 77903c29e451
Create Date: 2023-12-31 23:11:16.788974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bdc90614e413"
down_revision = "77903c29e451"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.add_column(sa.Column("about_me", sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column("last_seen", sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_column("last_seen")
        batch_op.drop_column("about_me")

    # ### end Alembic commands ###
