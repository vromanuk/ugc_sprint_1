from fastapi import APIRouter, Depends

from src.models.test import Test
from src.services.test import TestService, get_test_service

router = APIRouter()


@router.get("/",
            response_model=Test,
            summary="Тестовая ручка")
async def test(test_service: TestService = Depends(get_test_service)):
    return test_service.ping()
