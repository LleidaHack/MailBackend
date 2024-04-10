#TODO: Fer que cualsevol correu que s'envii, es guardi a la base de dades
#Crear model per tal de guardar els correus

from typing import List
from click import DateTime
from sqlalchemy import CheckConstraint, Column, Integer, String, ForeignKey, Boolean, Datetime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.utils.database import Base
from src.impl.Template.model import Template as TemplateModel


class Mail(Base):
    __tablename__ = 'mail'
    id: int = Column(Integer, primary_key=True, index=True)
    ##reciver_id = Column(Integer, nullable=True, unique=True)
    creation_date = Column(DateTime, default=func.now())
    sender_id = Column(Integer, nullable=False)
    reciver_id = Column(Integer, nullable=False)
    template_id: int = Column(Integer, ForeignKey('mail-template.id'))
    subject = Column(String)
    receiver_mail = Column(String, index=True)
    date = Column(Datetime, default=func.now())
    html = Column(String)
    fields = Column(String)  ##TODO: Hauria de ser un json (@ton)
    sent = Column(Boolean, default=False)
    template: TemplateModel = relationship(TemplateModel)
    priority = Column(Integer,
                      CheckConstraint('priority >= 0 AND priority <= 3'),
                      default=3)
