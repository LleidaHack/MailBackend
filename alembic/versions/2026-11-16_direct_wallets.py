"""Direct Apple download and optional Google Wallet email variant."""

from pathlib import Path
from alembic import op
import sqlalchemy as sa

revision = "20261116_direct_wallets"
down_revision = "20261116_ticket_branding"
branch_labels = None
depends_on = None


def upgrade():
    root = (Path(__file__).resolve().parents[2] /
            "src/utils/internal_templates/initial_templates")
    for name in ("event_attendee_ticket", "event_attendee_ticket_wallets"):
        values = {
            "name": name,
            "html": (root / f"{name}.html").read_text(encoding="utf-8"),
        }
        op.get_bind().execute(
            sa.text("""
            INSERT INTO template (creator_id, name, description, html, created_date, is_active, internal)
            SELECT 0, :name, :name, :html, CURRENT_DATE, true, true
            WHERE NOT EXISTS (SELECT 1 FROM template WHERE name = :name AND internal = true)
        """),
            values,
        )
        op.get_bind().execute(
            sa.text(
                "UPDATE template SET html = :html WHERE name = :name AND internal = true"
            ),
            values,
        )


def downgrade():
    # Queued and historic email references must remain valid.
    pass
