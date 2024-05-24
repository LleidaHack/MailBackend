#TODO: Fer que cualsevol correu que s'envii, es guardi a la base de dades
#Crear model per tal de guardar els correus

from sqlalchemy import (Boolean, CheckConstraint, Column, Date, DateTime,
                        ForeignKey, Integer, String)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.impl.Template.model import Template as TemplateModel
from src.utils.Base.BaseModel import BaseModel


class Mail(BaseModel):
    __tablename__ = 'mail'
    id: int = Column(Integer, primary_key=True, index=True)
    ##reciver_id = Column(Integer, nullable=True, unique=True)
    creation_date = Column(DateTime, default=func.now())
    update_date = Column(DateTime, default=func.now())
    sender_id = Column(Integer, nullable=False, default=0)
    reciver_id = Column(String, nullable=False, default=0)  # separated by ,
    template_id: int = Column(Integer, ForeignKey('template.id'))
    subject = Column(String)
    reciver_mail = Column(String)  # separated by ,
    fields = Column(String)  ##TODO: Hauria de ser un json (@ton)
    sent = Column(Boolean, default=False)
    template: TemplateModel = relationship(TemplateModel)
    priority = Column(Integer,
                      CheckConstraint('priority >= 0 AND priority <= 3'),
                      default=3)
