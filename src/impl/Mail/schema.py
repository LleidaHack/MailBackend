from datetime import date
from typing import Optional

from src.utils.Base.BaseSchema import BaseSchema


class MailGet(BaseSchema):
    id: int
    sender_id: int
    receiver_id: str  #a list of int separated by ,
    template_id: int
    subject: str
    receiver_mail: Optional[str]  #a list of int separated by ,
    # html: str
    fields: str  ##TODO: Hauria de ser un json (@ton)
    sent: bool


    # template
class MailGetAll(MailGet):
    pass


class MailCreate(BaseSchema):
    sender_id: Optional[int] = 0
    receiver_id: Optional[str] = ''  #a list of int separated by ,
    template_id: int
    subject: str
    receiver_mail: Optional[str] = ''  #a list of int separated by ,
    # html: str
    fields: str  ##TODO: Hauria de ser un json (@ton)


class MailUpdate(BaseSchema):
    pass
