
from typing import List
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, CheckConstraint
from typing import List
from sqlalchemy.orm import relationship
from database import Base



class MailQueue(Base):   ##TODO: CAMBIAR NOMR A Queue
    __tablename__ = 'mail-queue'
    id: int = Column(Integer, primary_key=True, index=True)
    creation_date = Column(Date)
    mail_id = Column(Integer, ForeignKey('mail.id'))
    mail = relationship("Mail")  ##TODO: Investigar millor el relationship.
    priority = Column(Integer, CheckConstraint('priority >= 0 AND priority <= 3'), default=3)

##Definició de prioritats:
    #0: Envio inminent CUA RAPIDA
    #1 : Envio important CUA
    #2 envio normal CUA
    #3 envio baixa prioritat CUA

#TODO: Veure si es un correcte plantejament
    #Hi hauria 4 estats ja que si s'envien emails de publicitat / emails de hacks i altres, es podria distingir entre la importancia.
    # A la hora de enviarlos, tambe es podria fer que si es supera X cuantitat de mails, els vagi alternant el envio.



