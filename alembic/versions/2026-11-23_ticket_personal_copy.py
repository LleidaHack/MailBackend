"""Clarify that entrance tickets are personal and non-transferable."""

import sqlalchemy as sa
from alembic import op

revision = "20261123_ticket_personal"
down_revision = "20261120_hacker_rejected"
branch_labels = None
depends_on = None


def upgrade():
    # Replace only the existing copy; retain IDs, custom content and references.
    for old, new in (
        (
            "L’entrada és personal: no comparteixis el QR ni els enllaços de Wallet.",
            "L’entrada és personal i intransferible. No comparteixis el QR ni els enllaços de Wallet.",
        ),
        (
            "Has rebut aquesta entrada com a participant confirmat, mentor o membre del staff de l’esdeveniment.<br>",
            "",
        ),
    ):
        op.get_bind().execute(
            sa.text(
                "UPDATE template SET html = REPLACE(html, :old, :new) "
                "WHERE name IN ('event_attendee_ticket', 'event_attendee_ticket_wallets') "
                "AND internal = true"
            ),
            {"old": old, "new": new},
        )


def downgrade():
    # Do not overwrite copy subsequently edited by an organizer.
    pass
