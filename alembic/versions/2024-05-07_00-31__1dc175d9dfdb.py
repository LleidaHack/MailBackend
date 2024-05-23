"""empty message

Revision ID: 1dc175d9dfdb
Revises: 386edb3fbafa
Create Date: 2024-05-07 00:31:08.781774

"""
from os.path import join

import sqlalchemy as sa

from alembic import op
from src.configuration.Configuration import Configuration
from src.utils.internal_templates.InternalTemplates import InternalTemplates

# revision identifiers, used by Alembic.
revision = '1dc175d9dfdb'
down_revision = '386edb3fbafa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    path = join(*Configuration.initial_templates_path.split(','))
    for _ in InternalTemplates:
        template_file_path = join(path, f"{_.value}.html")
        with open(template_file_path, 'r', encoding='utf-8') as file:
            html = file.read().replace("\'", '\'\'')
            op.execute(
                'INSERT INTO Template(creator_id, name, description, html, created_date, is_active, internal) '
                +
                f"VALUES(0, '{_.value}', '{_.value}', E'{html}', {sa.func.current_date()}, {True}, {True})"
            )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    for _ in InternalTemplates:
        op.execute(f"DELETE FROM Template WHERE name = '{_.value}'")
    # ### end Alembic commands ###
