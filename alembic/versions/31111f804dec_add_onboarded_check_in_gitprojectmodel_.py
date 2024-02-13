"""Add onboarded check in GitProjectModel table

Revision ID: 31111f804dec
Revises: a3a17014c282
Create Date: 2024-02-02 09:18:57.399510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "31111f804dec"
down_revision = "ab4c11acf5e1"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "git_projects", sa.Column("onboarded_downstream", sa.Boolean(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("git_projects", "onboarded_downstream")
    # ### end Alembic commands ###
