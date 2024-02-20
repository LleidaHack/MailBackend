from fastapi import HTTPException
from sqlalchemy.orm import Session
from schema import MailQueueBase
from model import MailQueque
from config import Configuration
from Mail.model import Mail as MailLog

FRONT_LINK = Configuration.get('OTHERS', 'FRONT_URL')
BACK_LINK = Configuration.get('OTHERS', 'BACK_URL')
CONTACT_MAIL = Configuration.get('OTHERS', 'CONTACT_MAIL')
STATIC_FOLDER = Configuration.get('OTHERS',
                                  'BACK_URL') + '/' + Configuration.get(
                                      'OTHERS', 'STATIC_FOLDER') + '/images'

##TODO : Veure si podem fer que la entrada de la funcio send_email sigui un payload i despres asignar valors.
async def new_mail( payload:MailQueueBase, db: Session):
    new_mail = MailQueque( **payload.dict())
    db.add(new_mail)
    db.commit()
    db.refresh(new_mail)
    return new_mail


##SON 2 Models diferents el MailQuequeBase i el MailLog. si conferteixo mail en diccionari, no tindra les mateixes entrades que MailLog.
##TODO: REVISAR !!!


