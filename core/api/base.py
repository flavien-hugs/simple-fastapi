from fastapi import APIRouter

from core.api.v1.users.route_cleaner import route_cleaners
from core.api.v1.users.route_login import route_login
from core.api.v1.users.route_user import route_users

api_router = APIRouter()


api_router.include_router(route_cleaners, prefix="/cleaner", tags=["cleaner"])
api_router.include_router(route_users, prefix="/user", tags=["user"])
api_router.include_router(route_login, prefix="/login", tags=["login"])
