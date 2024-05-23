from fastapi import APIRouter

from src.impl.Mail.router import router as mail_router
from src.impl.Template.router import router as template_router

router = APIRouter(
    prefix="/v1",
)
router.include_router(mail_router)
router.include_router(template_router)