from asyncio import sleep

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_utils.tasks import repeat_every

from src.configuration.Configuration import Configuration
from src.impl.Mail.service import MailService
from src.versions.v1 import router as v1_router

mail_service = MailService()

tags_metadata = {}
app = FastAPI(title="LleidaHack Mail API",
              description="LleidaHack Mail API",
              version="1.0",
              docs_url='/docs',
              redoc_url='/redoc',
              openapi_url='/openapi.json',
              openapi_tags=tags_metadata,
              debug=True)

app.add_middleware(DBSessionMiddleware, db_url=Configuration.database.url)
app.include_router(v1_router)

for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.tags[-1].replace(' ', '').lower() if len(
            route.tags) > 0 else ''
        route.operation_id += '_' + route.name


@app.on_event("startup")
@repeat_every(seconds=60 * 60 * 24)
def send_pending_mails():
    while True:
        try:
            mail_service.send_next()
            sleep(60)
        except Exception:
            break
