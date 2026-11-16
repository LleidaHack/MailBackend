"""Use entrance wording in the existing internal ticket template."""
from alembic import op
import sqlalchemy as sa

revision = "20261116_ticket_wording"
down_revision = "20261116_direct_wallets"
branch_labels = None
depends_on = None


def upgrade():
    # Preserve template IDs, custom content and all queued/historical references.
    op.get_bind().execute(
        sa.text(
            "UPDATE template SET html = REPLACE(html, :old, :new) "
            "WHERE name = :name AND internal = true"
        ),
        {
            "old": "El teu tiquet de check-in",
            "new": "La teva entrada",
            "name": "event_hacker_ticket",
        },
    )


def downgrade():
    # Do not overwrite copy subsequently edited by an organizer.
    pass
