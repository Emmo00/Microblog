"""followers table

Revision ID: eaf29031e832
Revises: bdc90614e413
Create Date: 2024-01-01 13:19:18.783958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "eaf29031e832"
down_revision = "bdc90614e413"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "followers",
        sa.Column("follower_id", sa.Integer(), nullable=False),
        sa.Column("followed_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["followed_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["follower_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("follower_id", "followed_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("followers")
    # ### end Alembic commands ###