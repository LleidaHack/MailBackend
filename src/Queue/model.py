
from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, CheckConstraint
from typing import List
from sqlalchemy.orm import relationship
from database import Base



class MailQueque(Base):
    __tablename__ = 'mail-queue'
    id: int = Column(Integer, primary_key=True, index=True)
    mail_reciver = Column(String, nullable=False)
    user_id_sender = Column(Integer, nullable=False)
    mail_name = Column(String)
    creation_date = Column(Date)
    html = Column(String, nullable=False)
    fields: List[str] # calculated
    priority = Column(Integer, CheckConstraint('priority >= 0 AND priority <= 3'), default=3)

##Definició de prioritats:
    # 0: Envio inminent
    #1 : Envio important
    #2 envio normal
    #3 envio baixa prioritat

#TODO: Veure si es un correcte plantejament
    #Hi hauria 4 estats ja que si s'envien emails de publicitat / emails de hacks i altres, es podria distingir entre la importancia.
    # A la hora de enviarlos, tambe es podria fer que si es supera X cuantitat de mails, els vagi alternant el envio.



