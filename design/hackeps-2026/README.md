# HackEPS 2026 email design proposal

Open index.html to compare eight email previews at desktop and mobile widths.
Templates contain existing backend variables; previews contain fictional examples.
This folder is not loaded by the mail service. No emails have been sent.

Orange actions and masthead, sky-blue illustrated header, charcoal body and the
actual tenth-edition logo. Uses table layout, inline core styles, system monospace
fonts, small PNG illustrations and text social links. No scripts in email files.

Run `python3 build.py` to regenerate drafts and previews. It checks variable names
and first-occurrence order against the originals: the current renderer consumes
positional comma-separated values. No new per-message fields are required.

For later integration, publish assets under the configured static folder at
`hackeps-2026/hackeps-logo.png` and `hackeps-2026/hacker.png`, copy approved drafts
into `src/utils/internal_templates/initial_templates`, then refresh stored templates
through the existing backend template-update process.

Browser previews checked at desktop and 375 px mobile widths. Outlook, Gmail and
Apple Mail delivery rendering remains untested. Before activation, validate real
client rendering, asset URLs and escaping of user-supplied contact fields. This
proposal does not change the renderer or activate templates.

Preview links use example.test and fictional tokens, never real account tokens.
