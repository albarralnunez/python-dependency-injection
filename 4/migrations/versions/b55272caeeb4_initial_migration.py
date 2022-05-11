"""initial_migration

Revision ID: b55272caeeb4
Revises: 
Create Date: 2019-11-28 15:02:17.853338

"""
from uuid import uuid4

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.

revision = 'b55272caeeb4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "programmer",
        sa.Column("uuid", sa.Text(), primary_key=True),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("skills", sa.JSON()),
    )
    op.execute(f"INSERT INTO programmer (uuid, name, skills) VALUES ('{uuid4()}', 'Daniel SQL', '[0,1]')")
    op.execute(f"INSERT INTO programmer (uuid, name, skills) VALUES ('{uuid4()}', 'Manuel SQL', '[1, 2]')")


def downgrade():
    op.drop_table("programmer")
