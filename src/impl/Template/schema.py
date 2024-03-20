from pydantic import BaseModel, ValidationError, validator
from typing import List, Optional

from src.Template.validator import validate_html


class MailTemplateCreate(BaseModel):
    name: str
    description: str
    html: str

    @validator('html')
    def html_must_have_body(cls, v):
        return validate_html(cls, v)


class MailTemplateUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    html: Optional[str]

    @validator('html')
    def html_must_have_body(cls, v):
        return validate_html(cls, v)


class MailTemplate(MailTemplateCreate):  ##TODO: FICAR TEMPLATEGET
    name: str
    description: str
    html: str
    is_active: bool

    class Config:
        orm_mode = True


class MailTemplateActive(BaseModel):
    is_active: bool


##TODO: CAMBIAR NOM A TEMPLATE

##TODO: ELS IMPORTS AMB EL SRC (ABSOLUT)
