from fastapi import HTTPException
from sqlalchemy.orm import Session
from Template.model import Template as MailTemplate
from schema import MailTemplateCreate, MailTemplateUpdate, MailTemplateActive
from src.utils.Base.BaseService import BaseService
from src.impl.Template.model import Template as ModelTemplate


class TemplateService(BaseService):

    def get_all(self):
        pass

    def get_by_id(self, id):
        template = self.db.query(MailTemplate).filter(
            MailTemplate.id == id).first()
        if not template:
            raise HTTPException(status_code=404, detail="Template not found")
        return template

    def create_template(self, template: MailTemplateCreate, data: TokenData):
        db_template = MailTemplate(**template.dict())
        self.db.add(db_template)
        self.db.commit()
        self.db.refresh(db_template)
        return db_template

    def get_template(self, template_id: int, data: TokenData):
        template = self.db.query(MailTemplate).filter(
            MailTemplate.id == template_id).first()
        if not template:
            raise HTTPException(status_code=404, detail="Template not found")
        return template

    def get_all_templates(db: Session, data: TokenData):
        templates = db.query(MailTemplate).order_by(MailTemplate.id).all()
        return templates

    def update_template(self, template_id: int, template: MailTemplateUpdate,
                        data: TokenData):
        db_template = self.get_by_id(template_id)
        for key, value in template.dict().items():
            setattr(db_template, key, value)
        self.db.commit()
        self.db.refresh(db_template)
        return db_template

    def update_template_status(self, template_id: int,
                               active_template: MailTemplateActive,
                               data: TokenData):
        db_template = self.get_by_id(template_id)
        db_template.is_active = active_template.is_active
        db.commit()
        db.refresh(db_template)
        return db_template

    ##TODO: FER UNA PER ACTIVAR I UNA ALTRA PER DESACTIVAR
