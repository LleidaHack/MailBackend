# HackEPS 2026 email design proposal

Open index.html to compare eleven email previews at desktop and mobile widths.
Templates contain existing backend variables; previews contain fictional examples.
This folder is not loaded by the mail service. No emails have been sent.

Orange actions and masthead, sky-blue illustrated header, charcoal body and the
actual tenth-edition logo. Uses table layout, inline core styles, system monospace
fonts, small PNG illustrations and text social links. No scripts in email files. Clouds use optional CSS animation; clients without
animation support keep the PNG clouds visible and static. Reduced motion is respected.

Run `python3 build.py` with Python 3.12+ to regenerate drafts and previews. It checks variable names
and first-occurrence order against the originals: the current renderer consumes
positional comma-separated values. No new per-message fields are required.

For later integration, publish assets under the configured static folder at
`hackeps-2026/hackeps-logo.png`, `hackeps-2026/hacker.png`,
`hackeps-2026/cloud-left.png` and `hackeps-2026/cloud-right.png`, copy approved drafts
into `src/utils/internal_templates/initial_templates`, then refresh stored templates
through the existing backend template-update process.

Browser previews checked at desktop and 375 px mobile widths. Outlook, Gmail and
Apple Mail delivery rendering remains untested. Before activation, validate real
client rendering, asset URLs and escaping of user-supplied contact fields. This
proposal does not change the renderer or activate templates.

Preview links use example.test and fictional tokens, never real account tokens.

## Company invitations and place-release reminders

The two additional templates are registered in `InternalTemplates` and installed
in existing databases by migration `20261115_invites` (`alembic upgrade head`).
Their per-message fields must be supplied in this order:

| Template | Fields | Suggested subject |
| --- | --- | --- |
| `company_account_invite` | `company_name`, `registration_url` | Creeu el vostre compte d’usuari · HackEPS |
| `event_hacker_release_reminder` | `name`, `event_name`, `token` | No podràs venir? Allibera la teva plaça · HackEPS |

Use the actual account-registration URL for `registration_url`. The release
reminder uses the existing `/assistance?confirm=false&token=…` flow; provide each
participant's own assistance token. Participants who will attend need take no
action. Subjects are supplied by the caller, separately from the HTML template.
Adding these templates does not queue or send any messages.
