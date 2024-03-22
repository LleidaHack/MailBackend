from typing import List, Union
from sqlalchemy.orm import Session
from fastapi import Depends, Response, APIRouter

from Template.schema import TemplateCreate, TemplateUpdate, TemplateActive, Template
import Template.service as service_template



router = APIRouter(
    prefix="/template",
    tags=["MailTemplate"],
)

@router.get("/all", response_model = List[Template])
async def get_all_templates(db: Session = Depends(get_db),
                    token: str = Depends(JWTBearer())):
    return await service_template.get_all_templates(db, get_data_from_token(token))  ##Veure que fer amb el tema del token al final..

@router.get("/{userId}", response_model = [Template] )
async def get_template(template_id: int,
                   db: Session = Depends(get_db),
                   token=Depends(JWTBearer())):
    return await service_template.get_template(db, template_id, get_data_from_token(token))

@router.put("/{userId}")
async def update_template(template_id: int,
                       payload: TemplateCreate,
                       db: Session = Depends(get_db),
                       token=Depends(JWTBearer())):
     return await service_template.update_template(db, template_id, payload, get_data_from_token(token))

@router.post("/", response_model=Template)
async def create_template(payload: TemplateCreate,
                            db: Session = Depends(get_db),
                            token=Depends(JWTBearer())):
    return await service_template.create_template(db, payload, get_data_from_token(token))