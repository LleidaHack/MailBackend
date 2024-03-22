from pydantic import BaseModel, ValidationError, validator
from typing import List, Optional

from src.Template.validator import validate_html

class TemplateCreate(BaseModel):
    name: str
    description: str
    html: str

    @validator('html')
    def html_must_have_body(cls, v):
        return validate_html(cls, v)
    
class TemplateUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    html: Optional[str]

    @validator('html')
    def html_must_have_body(cls, v):
        return validate_html(cls, v)
    
class TemplateGet(BaseModel):  ##TODO:DONE (COMPROBAR) FICAR TEMPLATEGET
    name: str
    description: str
    html: str
    is_active: bool

    class Config:
        orm_mode = True
    



class TemplateActiveStatus(BaseModel):
    is_active: bool
    
##TODO:DONE (COMPROBAR) CAMBIAR NOM A TEMPLATE
    
    ##TODO: ELS IMPORTS AMB EL SRC (ABSOLUT)
