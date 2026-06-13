import asyncio

from fastapi import HTTPException

from app.api.v1.ask.schemas import AskRequest, AskResponse, ExternalResult
from app.config import settings


class AskService:
    async def ask(self, payload: AskRequest) -> AskResponse:
        try:
            result_a, result_b = await asyncio.wait_for(
                asyncio.gather(
                    self._call_service_a(payload.question),
                    self._call_service_b(payload.question),
                ),
                timeout=settings.operation_timeout_seconds,
            )

            return AskResponse(
                question=payload.question,
                results=[result_a, result_b],
            )

        except TimeoutError:
            raise HTTPException(
                status_code=504,
                detail="The operation took too long to respond",
            )

    async def _call_service_a(self, question: str) -> ExternalResult:
        await asyncio.sleep(1)

        return ExternalResult(
            source="service_a",
            data={
                "answer": f"Response A for: {question}",
            },
        )

    async def _call_service_b(self, question: str) -> ExternalResult:
        await asyncio.sleep(2)

        return ExternalResult(
            source="service_b",
            data={
                "answer": f"Response B for: {question}",
            },
        )