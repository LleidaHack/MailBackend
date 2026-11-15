"""Add company account invitations and participant place-release reminders."""
from pathlib import Path

from alembic import op
import sqlalchemy as sa

revision = "20261115_invites"
down_revision = "20260917_emails"
branch_labels = None
depends_on = None

TEMPLATES = ("company_account_invite", "event_hacker_release_reminder")
ROOT = Path(__file__).resolve().parents[2]


def upgrade():
    connection = op.get_bind()
    for name in TEMPLATES:
        markup = (ROOT / "src/utils/internal_templates/initial_templates" / f"{name}.html").read_text(encoding="utf-8")
        # Fresh installations already seed every member of InternalTemplates.
        connection.execute(sa.text("""
            INSERT INTO template
                (creator_id, name, description, html, created_date, is_active, internal)
            SELECT 0, :name, :name, :html, CURRENT_DATE, true, true
            WHERE NOT EXISTS (SELECT 1 FROM template WHERE name = :name)
        """), {"name": name, "html": markup})


def downgrade():
    connection = op.get_bind()
    for name in TEMPLATES:
        connection.execute(sa.text("DELETE FROM template WHERE name = :name"), {"name": name})
