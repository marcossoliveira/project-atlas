from fastapi import APIRouter, Depends

from app.api.v1.ask.schemas import AskRequest, AskResponse
from app.api.v1.ask.service import AskService

router = APIRouter()


def get_ask_service() -> AskService:
    return AskService()


@router.post("", response_model=AskResponse)
async def ask(
    payload: AskRequest,
    service: AskService = Depends(get_ask_service),
):
    return await service.ask(payload)