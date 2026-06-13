from fastapi import APIRouter

from app.api.v1.ask.router import router as ask_router
from app.api.v1.health.router import router as health_router

router = APIRouter()

router.include_router(ask_router, prefix="/ask", tags=["Ask"])
router.include_router(health_router, prefix="/health", tags=["Health"])