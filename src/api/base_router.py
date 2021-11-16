from fastapi import APIRouter

from src.api.v1 import test

api_router = APIRouter()
api_router.include_router(test.router, prefix="/ping", tags=["Ping"])
