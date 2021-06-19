from fastapi import Depends, FastAPI, HTTPException
from starlette.requests import Request
from app.core import config
import uvicorn
from app.db.session import Session
from app.api.apirouter import api_router
# from app.core.worker import celery_app

App = FastAPI(title=config.PROJECT_NAME, description="MAT REST APIs", version="1.0.0")

App.include_router(api_router, prefix=config.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(App, host="127.0.0.1", port=8081)