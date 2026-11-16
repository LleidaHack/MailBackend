"""Restore approved ticket layout and hide visible bearer identifiers."""
from pathlib import Path
from alembic import op
import sqlalchemy as sa

revision = "20261116_ticket_branding"
down_revision = "20261116_attendee_ticket"
branch_labels = None
depends_on = None


def upgrade():
    root = Path(__file__).resolve(
    ).parents[2] / "src/utils/internal_templates/initial_templates"
    for name in ("event_attendee_ticket", "event_hacker_ticket_reminder",
                 "event_hacker_ticket"):
        markup = (root / f"{name}.html").read_text(encoding="utf-8")
        op.get_bind().execute(
            sa.text(
                "UPDATE template SET html = :html WHERE name = :name AND internal = true"
            ), {
                "html": markup,
                "name": name
            })


def downgrade():
    # Preserve corrected content and every queued/historical mail reference.
    pass
