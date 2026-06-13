from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(
        min_length=3,
        max_length=500,
        description="Pergunta enviada pelo usuário",
    )


class ExternalResult(BaseModel):
    source: str
    data: dict


class AskResponse(BaseModel):
    question: str
    results: list[ExternalResult]