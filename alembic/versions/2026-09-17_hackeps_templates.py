"""Publish HackEPS tenth-edition templates without changing message field order."""
from pathlib import Path
import json
from alembic import op
import sqlalchemy as sa

revision = "20260917_emails"
down_revision = "1dc175d9dfdb"
branch_labels = None
depends_on = None
ROOT = Path(__file__).resolve().parents[2]


def update_templates(templates):
    connection = op.get_bind()
    for name, markup in templates.items():
        connection.execute(sa.text("UPDATE template SET html=:html WHERE name=:name"), {"name": name, "html": markup})


def upgrade():
    update_templates({p.stem: p.read_text(encoding="utf-8") for p in
                      (ROOT / "src/utils/internal_templates/initial_templates").glob("*.html")})


def downgrade():
    update_templates(json.loads((ROOT / "alembic/template_snapshots/before_hackeps_2026.json").read_text(encoding="utf-8")))
