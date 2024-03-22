from fastapi import HTTPException
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session
from schema import MailQueueBase
from model import Queue
from config import Configuration
# from Mail.model import Mail as MailLog
from src.utils.Base.BaseService import BaseService
from src.impl.Mail.service import MailService
from src.impl.Queue.model import MailQueue as MailQueueModel

FRONT_LINK = Configuration.get('OTHERS', 'FRONT_URL')
BACK_LINK = Configuration.get('OTHERS', 'BACK_URL')
CONTACT_MAIL = Configuration.get('OTHERS', 'CONTACT_MAIL')
STATIC_FOLDER = Configuration.get('OTHERS',
                                  'BACK_URL') + '/' + Configuration.get(
                                      'OTHERS', 'STATIC_FOLDER') + '/images'


class QueueService(BaseService):
    mail_service = None

    def get_by_id(self, id: int):
        pass

    def get_all(self):
        pass

    @BaseService.needs_service(MailService)
    def send_next(self):
        mail = self.db.query(MailQueueModel).order_by(
            desc(MailQueueModel.priority)).order_by(
                asc(MailQueueModel.creation_date)).first()
        if mail is None:
            raise Exception()
        self.mail_service.send(mail)


##TODO : Veure si podem fer que la entrada de la funcio send_email sigui un payload i despres asignar valors.
async def new_mail(payload: MailQueueBase, db: Session):
    new_mail = MailQueque(**payload.dict())
    db.add(new_mail)
    db.commit()
    db.refresh(new_mail)
    return new_mail


##SON 2 Models diferents el MailQuequeBase i el MailLog. si conferteixo mail en diccionari, no tindra les mateixes entrades que MailLog.
##TODO: REVISAR !!!
