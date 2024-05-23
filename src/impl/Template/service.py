from fastapi import HTTPException
from fastapi_sqlalchemy import db

from src.impl.Template.model import Template as ModelTemplate
from src.impl.Template.schema import TemplateCreate, TemplateUpdate
from src.utils.Base.BaseService import BaseService
from src.utils.service_utils import set_existing_data


class TemplateService(BaseService):
    name = 'template_service'

    def get_all(self):
        return db.session.query(ModelTemplate).all()

    def get_by_id(self, id) -> ModelTemplate:
        template = db.session.query(ModelTemplate).filter(
            ModelTemplate.id == id).first()
        if not template:
            raise HTTPException(status_code=404, detail="Template not found")
        return template

    def create(self, template: TemplateCreate):
        db_template = ModelTemplate(**template.dict())
        db.session.add(db_template)
        db.session.commit()
        db.session.refresh(db_template)
        return db_template

    def update(self, template_id: int, template: TemplateUpdate):
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
