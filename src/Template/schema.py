from pydantic import BaseModel, ValidationError, validator
from typing import Optional

class MailTemplateCreate(BaseModel):
    name: str
    description: str
    html: str
    fields: list[str]

    @validator('html')
    def html_must_have_body(cls, v):
        if '<body>' not in v:
            raise ValueError('HTML must have a <body> tag')
        return v
    
class MailTemplateUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    html: Optional[str]
    fields: Optional[list[str]]  ##TODO: Consultar a ton a ver com fiquem els fields

    @validator('html')
    def html_must_have_body(cls, v):
        if '<body>' not in v:
            raise ValueError('HTML must have a <body> tag')
        return v
    
class MailTemplate(MailTemplateCreate):
    name: str
    description: str
    html: str
    fields: list[str]
    is_active: bool

    class Config:
        orm_mode = True


class MailTemplateActive(BaseModel):
    is_active: bool
    
