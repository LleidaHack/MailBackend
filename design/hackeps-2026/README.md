# HackEPS 2026 email design proposal

Open index.html to compare email previews at desktop and mobile widths.
Templates contain existing backend variables; previews contain fictional examples.
This folder is not loaded by the mail service. No emails have been sent.

Orange actions and masthead, sky-blue illustrated header, charcoal body and the
actual tenth-edition logo. Uses table layout, inline core styles, system monospace
fonts, small PNG illustrations and text social links. No scripts in email files. Clouds use optional CSS animation; clients without
animation support keep the PNG clouds visible and static. Reduced motion is respected.

Run `python3 build.py` with Python 3.12+ to regenerate drafts and previews. It checks variable names
and first-occurrence order against the originals: the current renderer consumes
positional comma-separated values. Existing templates retain their per-message fields; new templates are documented below.

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

## Application rejection

`event_hacker_rejected` communicates a declined application in Catalan, thanking
the applicant without inventing a reason or promising a place in a future edition.
Suggested subject: **Sobre la teva inscripció · HackEPS**.

Apply migration `20261120_hacker_rejected` (`alembic upgrade head`) to install it
in existing databases. Supply `name,event_name`, in that order, as HTML-escaped
values, encoding commas as `&#44;` for the positional mail API.

The application backend must resolve the template by name and queue this email
when an application is rejected, supplying the recipient and subject separately
and preventing duplicate notifications. Adding this template does not implement
that external rejection trigger or send any mail.

## Official Discord invitation

`event_discord_invite` sends the official Discord server link to participants.
Suggested subject: **Uneix-te al Discord de la HackEPS**.

Apply migration `20261124_discord_invite` (`alembic upgrade head`) to install it
in existing databases. Supply `name,event_name,discord_url`, in that order, as
HTML-escaped values, encoding commas as `&#44;` for the positional mail API.

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

## Pre-event ticket reminder with Wallet links

`event_hacker_ticket_reminder` is a separate template, so callers of the original
`event_hacker_ticket` keep their existing field contract. Install it in existing
databases with migration `20261116_ticket_reminder` (`alembic upgrade head`).
Suggested subject: **Falta poc! Guarda la teva entrada · HackEPS**.

Supply these positional fields in exactly this order:

1. `name`: participant name.
2. `event_name`: event name.
3. `code`: personal check-in code (also shown if images are blocked).
4. `qr_url`: HTTPS URL of the participant’s QR image.
5. `apple_wallet_url`: personal URL that downloads a signed Apple Wallet `.pkpass`.
6. `google_wallet_url`: personal Google Wallet save link.

The caller must provide valid passes for the same ticket as the QR. This service
only renders links; it does not generate, sign or issue Wallet passes. Both links
are required. Use HTML-escaped values (including `&amp;` in URL query strings),
percent-encode literal commas in URLs and avoid commas in the other positional
fields because the existing mail API uses comma-separated values.

Queue this template for confirmed attendees a few days before the event from the
system that owns event dates (for example, three days before; this is a suggested
policy, not a configured schedule). Resolve its template ID by name rather than
hard-coding a database ID. The caller supplies the subject and receiver separately
and should prevent duplicate reminders. MailBackend has no date-based scheduler;
creating mail adds it to the regular queue, so do so only when it is due.

No mail is queued by adding or migrating this template. Preview Wallet URLs are
fictional and do not issue passes. Real Wallet flows and email-client rendering
must be verified with issued passes before sending.

Wallet badge assets: `add-to-apple-wallet.png` is cropped from the user-supplied
reference (16 November 2026), with the surrounding background removed.
`add-to-google-wallet.png` is the English wallet button from Google's official
https://developers.google.com/static/wallet/download-assets/add-to-wallet-png.zip.
Both assets are mirrored under `src/static/images/hackeps-2026` and must be
published alongside the existing email images. The reminder also links to
`$_front_link/perfil`, where participants can retrieve their QR.

## Shared participant, mentor and staff invitation

`event_attendee_ticket` has the positional fields
`name,event_name,role,code,qr_url,ticket_url`. The caller supplies HTML-escaped
values and encodes commas as `&#44;`. The new template deliberately keeps the
existing ticket and reminder contracts intact. Its button opens a personal
backend page containing the QR and available Wallet actions; no login is needed.
It makes no unsupported Google Wallet promise. The page must check eligibility
on every request. Apply `20261116_attendee_ticket` before deploying a backend that
loads this template. Migration is insert-only and preserves historical mail.
