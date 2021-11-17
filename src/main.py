from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.api.routes import api_router
from src.core.config import get_settings

settings = get_settings()

app = FastAPI(
    version="1.0.0",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)

app.router.include_router(api_router, prefix=settings.API_PREFIX)
