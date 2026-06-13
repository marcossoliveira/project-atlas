from fastapi import APIRouter

router = APIRouter()

@router.get("")
def health():
    """Endpoint to check service health"""
    return {"status": "ok"}
