
#TODO: Fer que cualsevol correu que s'envii, es guardi a la base de dades
#Crear model per tal de guardar els correus

from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from database import Base



class Mail(Base):
    __tablename__ = 'mail-log'
    id: int = Column(Integer, primary_key=True, index=True)
    user_id_reciver = Column(Integer, nullable=False, unique=True) 
    user_id_sender = Column(Integer, nullable=False, unique=True)  
    mail_name = Column(String)
    date = Column(Date)  
    html = Column(String)
    

