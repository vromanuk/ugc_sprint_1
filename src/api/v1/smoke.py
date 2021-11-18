from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Тестовая ручка")
async def smoke():
    return {"msg": "ok"}
