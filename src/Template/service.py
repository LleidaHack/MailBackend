from fastapi import HTTPException
from sqlalchemy.orm import Session
from Template.model import Template as MailTemplate
from schema import MailTemplateCreate, MailTemplateUpdate, MailTemplateActive

def create_template(db: Session, template: MailTemplateCreate, data: TokenData):
    db_template = MailTemplate(**template.dict())
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return db_template

def get_template(db: Session, template_id: int, data: TokenData):
    template = db.query(MailTemplate).filter(MailTemplate.id == template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Template not found")
    return template

def get_all_templates(db: Session, data: TokenData):
    templates = db.query(MailTemplate).order_by(MailTemplate.id).all()
    return templates

def update_template(db: Session, template_id: int, template: MailTemplateUpdate, data: TokenData):
    db_template = db.query(MailTemplate).filter(MailTemplate.id == template_id).first()
    if not db_template:
        raise HTTPException(status_code=404, detail="Template not found")
    for key, value in template.dict().items():
        setattr(db_template, key, value)
    db.commit()
    db.refresh(db_template)
    return db_template


def update_template_status(db: Session, template_id: int, active_template: MailTemplateActive, data: TokenData): 
    db_template = db.query(MailTemplate).filter(MailTemplate.id == template_id).first()
    if not db_template:
        raise HTTPException(status_code=404, detail="Template not found")
    db_template.is_active = active_template.is_active
    db.commit()
    db.refresh(db_template)
    return db_template

##TODO: FER UNA PER ACTIVAR I UNA ALTRA PER DESACTIVAR



