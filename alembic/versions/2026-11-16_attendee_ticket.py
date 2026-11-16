"""Add a shared personal ticket email for hackers, mentors and staff."""
from pathlib import Path

from alembic import op
import sqlalchemy as sa

revision = "20261116_attendee_ticket"
down_revision = "20261116_ticket_reminder"
branch_labels = None
depends_on = None


def upgrade():
    name = "event_attendee_ticket"
    markup = (Path(__file__).resolve().parents[2] /
              "src/utils/internal_templates/initial_templates" /
              f"{name}.html").read_text(encoding="utf-8")
    # Fresh installations already seed every member of InternalTemplates.
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
    # Preserve the template: queued and historical mail may reference it.
    pass
