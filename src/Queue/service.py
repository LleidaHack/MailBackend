from fastapi import HTTPException
from sqlalchemy.orm import Session
from schema import MailQueueBase
from model import Queue
from config import Configuration
from Mail.model import Mail as MailLog

FRONT_LINK = Configuration.get('OTHERS', 'FRONT_URL')
BACK_LINK = Configuration.get('OTHERS', 'BACK_URL')
CONTACT_MAIL = Configuration.get('OTHERS', 'CONTACT_MAIL')
STATIC_FOLDER = Configuration.get('OTHERS',
                                  'BACK_URL') + '/' + Configuration.get(
                                      'OTHERS', 'STATIC_FOLDER') + '/images'



async def new_mail( payload:MailQueueBase, db: Session):
    new_mail = Queue( **payload.dict())   ##comprobar la forma d'aquest diccionari i del esquema del MailQueueBase es diferent
    db.add(new_mail)
    db.commit()
    db.refresh(new_mail)
    return new_mail



