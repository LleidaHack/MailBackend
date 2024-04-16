import argparse
from os import path
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
import uvicorn

from src.configuration.Configuration import Configuration

tags_metadata = {}

app = FastAPI(title="LleidaHack API",
              description="LleidaHack API",
              version="2.0",
              docs_url='/docs',
              redoc_url='/redoc',
              openapi_url='/openapi.json',
              openapi_tags=tags_metadata,
              debug=True,
              swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["localhost:8000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
#     expose_headers=["*"],
# )

app.add_middleware(DBSessionMiddleware, db_url=Configuration.database.url)
from src.impl.Mail.router import router as mail_router
from src.impl.Template.router import router as template_router

app.include_router(mail_router)
app.include_router(template_router)
CONFIG_PATH = path.join('src', 'configuration')
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--local', action="store_true")
    parser.add_argument('-i', '--integration', action="store_true")
    parser.add_argument('-m', '--main', action="store_true")
    args = parser.parse_args()
    if sum([args.local, args.integration, args.main]) > 1:
        raise Exception("You provided more than one enviroment")
    file = None
    if sum([args.local, args.integration, args.main]) > 0:
        if args.local:
            file = 'local.yaml'
        elif args.integration:
            file = 'integration.yaml'
        elif args.main:
            file = 'main.yaml'
        file = path.join(CONFIG_PATH, file)
    if not path.exists(file):
        raise FileNotFoundError(f"Configuration file {file} not found")
    Configuration(file)
    #run server
    uvicorn.run(app)
else:
    Configuration()
