from typing import List
from fastapi import APIRouter
from src.impl.Mail.service import MailService

from src.impl.Mail.schema import MailGet as MailGetSchema
from src.impl.Mail.schema import MailCreate as MailCreateSchema
from src.impl.Mail.schema import MailUpdate as MailUpdateSchema
router = APIRouter(
    prefix="/mail",
    tags=["Mail"],
)

mail_service = MailService()

@router.get("/all", response_model=List[MailGetSchema])
def get_all():
    return mail_service.get_all()

@router.get("/{id}", response_model=MailGetSchema)
def get(id: int):
    return mail_service.get_by_id(id)

@router.post("/", response_model=MailGetSchema)
def create(payload: MailCreateSchema):
    return mail_service.create(payload)

@router.put("/{id}", response_model=MailGetSchema)
def update(id: int, payload: MailUpdateSchema):
    return mail_service.update(id, payload)


@router.put("/send/{id}")
def send_by_id(id: int):
    return mail_service.send_by_id(id)

@router.put("/send/next")
def send_next_mail():
    return mail_service.send_next()

