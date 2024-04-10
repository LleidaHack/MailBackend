import argparse
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from configuration.Configuration import Configuration

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.add_middleware(DBSessionMiddleware, db_url=Configuration.database.url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--local')
    parser.add_argument('-i', '--integration')
    parser.add_argument('-m', '--main')
    args = parser.parse_args()

    Configuration()
    #run server
    uvicorn.run(app)
else:
    Configuration()
