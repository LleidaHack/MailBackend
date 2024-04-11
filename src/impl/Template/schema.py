from pydantic import BaseModel, ValidationError, validator
from typing import List, Optional

from sqlalchemy import Date

from utils.Base.BaseSchema import BaseSchema


class TemplateGet(BaseSchema):
    name: str
    description: str
    html: str
    created_date: Date


class TemplateGetAll(BaseSchema):
    id: int
    creator_id: int
    is_active: bool


class TemplateCreate(BaseModel):
    name: str
    description: str
    html: str

    @validator('html')
    def html_must_have_body(cls, v):
        if '<body>' not in v.html or '</body>' not in v.html:
            raise ValueError('HTML must have a <body> tag')
        return True


class TemplateUpdate(BaseSchema):
    name: Optional[str]
    description: Optional[str]
    html: Optional[str]

    @validator('html')
    def html_must_have_body(cls, v):
        if '<body>' not in v.html:
            raise ValueError('HTML must have a <body> tag')
        return True
