
#TODO: Fer que cualsevol correu que s'envii, es guardi a la base de dades
#Crear model per tal de guardar els correus

from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base



class Mail(Base):
    __tablename__ = 'mail'
    id: int = Column(Integer, primary_key=True, index = True)
    ##reciver_id = Column(Integer, nullable=True, unique=True) 
    sender_id = Column(Integer, nullable=False)
    template_id:int = Column(Integer, ForeignKey('mail-template.id'))
    subject = Column(String)
    receiver_mail = Column(String, index = True)
    date = Column(Datetime, default = func.now())  
    html = Column(String)
    fields = Column(String) ##TODO: Hauria de ser un json (@ton)
    sent = Column(Boolean, default = False)
    template = relationship("template")  ##TODO:DONE cambiar nom a template
    
