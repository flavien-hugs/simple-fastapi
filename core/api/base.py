from fastapi import APIRouter

from core.api.v1.users.cleaner import user_routes as cleaner_route
from core.api.v1.users.customer import user_routes as customer_router

api_router = APIRouter()


api_router.include_router(cleaner_route.cleaners_router, prefix="/cleaner", tags=["cleaner"])
api_router.include_router(customer_router.customers_router, prefix="/customer", tags=["customer"])
