from typing import List
from fastapi import APIRouter

from Template.schema import TemplateCreate as TemplateCreateSchema
from Template.schema import TemplateUpdate as TemplateUpdateSchema
from Template.schema import TemplateGet as TemplateGetSchema
import Template.service as service_template

router = APIRouter(
    prefix="/mailTemplate",
    tags=["MailTemplate"],
)


@router.get("/all", response_model=List[TemplateGetSchema])
def get_all():
    return service_template.get_all(
    )  ##Veure que fer amb el tema del token al final..


@router.get("/{id}", response_model=[TemplateGetSchema])
def get(id: int):
    return service_template.get_by_id(id)


@router.put("/{userId}")
def update(id: int, payload: TemplateUpdateSchema):
    return service_template.update(id, payload)


@router.post("/", response_model=TemplateGetSchema)
def create(payload: TemplateCreateSchema):
    return service_template.create(payload)


@router.put("/activate/{id}")
def activate(id: int):
    return service_template.activate(id)


@router.put("/deactivate/{id}")
def deactivate(id: int):
    return service_template.deactivate(id)
