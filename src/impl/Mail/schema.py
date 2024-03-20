import datetime
from pydantic import BaseModel

class MailSchema(BaseModel):
    id: int
    user_id_reciver: int
    user_id_sender: int
    mail_name: str
    date: datetime
    html: str