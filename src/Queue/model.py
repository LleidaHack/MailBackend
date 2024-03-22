
from typing import List
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, CheckConstraint
from typing import List
from sqlalchemy.orm import relationship
from database import Base



class Queue(Base):   ##TODO:DONE CAMBIAR NOMR A Queue
    __tablename__ = 'mail-queue'
    id: int = Column(Integer, primary_key=True, index=True)
    creation_date = Column(Date)
    mail_id = Column(Integer, ForeignKey('mail.id'))
    mail = relationship("Mail")  ##TODO: Esta be aixo??
    priority = Column(Integer, CheckConstraint('priority >= 0 AND priority <= 3'), default=3)

##Definició de prioritats:
    #0: Envio inminent CUA RAPIDA
    #1 : Envio important CUA
    #2 envio normal CUA
    #3 envio baixa prioritat CUA



