"""Add the private Discord invitation email for mentors."""
from pathlib import Path

from alembic import op
import sqlalchemy as sa

revision = "20261126_discord_mentor"
down_revision = "20261124_discord_invite"
branch_labels = None
depends_on = None


def upgrade():
    name = "event_discord_invite_mentor"
    markup = (Path(__file__).resolve().parents[2] /
              "src/utils/internal_templates/initial_templates" /
              f"{name}.html").read_text(encoding="utf-8")
    op.get_bind().execute(
        sa.text("""
            INSERT INTO template
                (creator_id, name, description, html, created_date, is_active, internal)
            SELECT 0, :name, :name, :html, CURRENT_DATE, true, true
            WHERE NOT EXISTS (SELECT 1 FROM template WHERE name = :name)
        """), {
            "name": name,
            "html": markup
        })


def downgrade():
    # Preserve references from queued and historical mail.
    pass
