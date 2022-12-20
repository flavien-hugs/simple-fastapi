from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.api.base import api_router
from core.config.config import settings
from core.db.base import Base
from core.db.session import engine


def create_tables():
    print("Create database tables")
    Base.metadata.create_all(bind=engine)


def include_routers(app):
    app.include_router(api_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_routers(app)
    return app


app = start_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8070"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
