from fastapi import APIRouter
from .api_v1 import customer_info_api

api_router = APIRouter()


api_router.include_router(customer_info_api.router, tags = ["Customers"])