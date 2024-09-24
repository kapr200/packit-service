"""Add AnityaMultipleVersionsModel

Revision ID: 002ab85fa213
Revises: fd785af95c19
Create Date: 2024-09-11 08:25:51.759649

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "002ab85fa213"
down_revision = "fd785af95c19"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "anitya_multiple_versions",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("versions", sa.ARRAY(sa.String()), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["anitya_projects.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_anitya_multiple_versions_project_id"),
        "anitya_multiple_versions",
        ["project_id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_anitya_multiple_versions_project_id"),
        table_name="anitya_multiple_versions",
    )
    op.drop_table("anitya_multiple_versions")
    # ### end Alembic commands ###