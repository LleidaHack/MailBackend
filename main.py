from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

from src.configuration.Configuration import Configuration
from src.versions.v1 import router as v1_router

tags_metadata = {}
app = FastAPI(title="LleidaHack Mail API",
              description="LleidaHack Mail API",
              version="1.0",
              docs_url='/docs',
              redoc_url='/redoc',
              openapi_url='/openapi.json',
              openapi_tags=tags_metadata,
              debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.add_middleware(DBSessionMiddleware, db_url=Configuration.database.url)
app.include_router(v1_router)
for route in app.routes:
    if isinstance(route, APIRoute):
        route.operation_id = route.tags[-1].replace(' ', '').lower() if len(
            route.tags) > 0 else ''
        route.operation_id += '_' + route.name
