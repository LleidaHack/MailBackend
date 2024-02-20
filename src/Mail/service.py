from fastapi import HTTPException
from sqlalchemy.orm import Session
from Mail import model
from schema import MailSchema

##La idea de aquesta funcio es guardar el correu a la base de dades. Com que no tindrá router, en realitat el archiu no hauria de ser service, no?? :(
async def save_mail_log( payload:MailSchema, db: Session):
    new_mail = model.Mail( **payload.dict())
    db.add(new_mail)
    db.commit()
    db.refresh(new_mail)
    return new_mail

