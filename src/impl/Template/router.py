from typing import List
from fastapi import APIRouter

from src.impl.Template.schema import TemplateCreate as TemplateCreateSchema
from src.impl.Template.schema import TemplateUpdate as TemplateUpdateSchema
from src.impl.Template.schema import TemplateGet as TemplateGetSchema
from src.impl.Template.schema import TemplateGetAll as TemplateGetAllSchema
from src.impl.Template.service import TemplateService

router = APIRouter(
    prefix="/emplate",
    tags=["template"],
)

template_service = TemplateService()


@router.get("/all", response_model=List[TemplateGetSchema])
def get_all():
    return template_service.get_all()


@router.get("/{id}", response_model=TemplateGetSchema)
def get(id: int):
    return template_service.get_by_id(id)


@router.put("/{id}")
def update(id: int, payload: TemplateUpdateSchema):
    return template_service.update(id, payload)


@router.post("/", response_model=TemplateGetAllSchema)
def create(payload: TemplateCreateSchema):
    return template_service.create(payload)


@router.put("/{id}/activate")
def activate(id: int):
    return template_service.activate(id)


@router.put("/{id}/deactivate")
def deactivate(id: int):
    return template_service.deactivate(id)
