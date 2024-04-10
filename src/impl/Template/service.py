from fastapi import HTTPException
from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session
from Template.model import Template as MailTemplate
from schema import MailTemplateCreate, MailTemplateUpdate, MailTemplateActive
from src.utils.Base.BaseService import BaseService
from src.impl.Template.model import Template as ModelTemplate
from utils.service_utils import set_existing_data


class TemplateService(BaseService):

    def get_all(self):
        return db.session.query(MailTemplate).all()

    def get_by_id(self, id) -> MailTemplate:
        template = db.session.query(MailTemplate).filter(
            MailTemplate.id == id).first()
        if not template:
            raise HTTPException(status_code=404, detail="Template not found")
        return template

    def create(self, template: MailTemplateCreate):
        db_template = MailTemplate(**template.dict())
        db.session.add(db_template)
        db.session.commit()
        db.session.refresh(db_template)
        return db_template

    def update(self, template_id: int, template: MailTemplateUpdate):
        db_template = self.get_by_id(template_id)
        set_existing_data(db_template, template)
        db.session.commit()
        db.session.refresh(db_template)
        return db_template

    def activate(self, id: int):
        db_obj = self.get_by_id(id)
        if db_obj.is_active:
            raise Exception(
                "Generation Prompt: Please complete the code generation.")
        db_obj.is_active = True
        db.session.commit()
        db.session.refresh(db_obj)
        return db_obj

    def deactivate(self, id: int):
        db_obj = self.get_by_id(id)
        if not db_obj.is_active:
            raise Exception(
                "Generation Prompt: Please complete the code generation.")
        db_obj.is_active = False
        db.session.commit()
        db.session.refresh(db_obj)
        return db_obj
