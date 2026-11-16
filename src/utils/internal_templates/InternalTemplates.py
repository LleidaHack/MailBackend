from enum import Enum


class InternalTemplates(Enum):
    USER_CREATED = 'user_created'
    COMPANY_ACCOUNT_INVITE = 'company_account_invite'
    CONTACT = 'contact'
    RESET_PASSWORD = 'reset_password'

    EVENT_SLACK_INVITE = 'event_slack_invite'
    EVENT_REGISTRATION_REMINDER = 'event_registration_reminder'

    EVENT_HACKER_REGISTERED = 'event_hacker_registered'
    EVENT_HACKER_ACCEPTED = 'event_hacker_accepted'

    EVENT_HACKER_REMINDER = "event_hacker_reminder"
    EVENT_HACKER_TICKET = "event_hacker_ticket"
    EVENT_HACKER_TICKET_REMINDER = "event_hacker_ticket_reminder"
    EVENT_HACKER_RELEASE_REMINDER = "event_hacker_release_reminder"
    # EVENT_HACKER_REJECTED = 'event_hacker_accepted'
    # EVENT_HACKER_CONFIRMATION = 'event_hacker_confirmation'
