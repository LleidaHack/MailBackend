from fastapi import APIRouter

from src.impl.Mail import router as Mail
from src.impl.Template import router as Template

router = APIRouter(prefix="/v1")

@router.get("/health", tags=['health'])
async def check():
    return {"status": True}


router.include_router(Template.router)
router.include_router(Mail.router)