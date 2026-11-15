"""Align company invitation copy with the portal setup flow."""
from pathlib import Path

from alembic import op
import sqlalchemy as sa

revision = "20261115_company_copy"
down_revision = "20261115_invites"
branch_labels = None
depends_on = None


def upgrade():
    markup = (Path(__file__).resolve().parents[2] /
              "src/utils/internal_templates/initial_templates/company_account_invite.html").read_text(encoding="utf-8")
    op.get_bind().execute(sa.text(
        "UPDATE template SET html = :html WHERE name = 'company_account_invite'"
    ), {"html": markup})


def downgrade():
    # Retain the corrected copy and all queued messages.
    pass
