from pydantic import BaseModel, ValidationError, validator
from typing import Optional

class MailQueueBase(BaseModel):
    mail_reciver: str
    user_id_sender: int
    mail_name: str
    html: str
    fields: str
    priority: int = 3  ##3 es poca prioritat per default

    @validator('mail_reciver')
    def mail_reciver_must_be_email(cls, v):
        assert '@' in v, 'Invalid email'
        return v

    @validator('fields', pre=True)
    def fields_must_be_list(cls, v):
        if v is None:
            return []
        return v