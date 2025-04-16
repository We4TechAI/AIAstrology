from fastapi import APIRouter
from services.quote_service import fetch_random_quote

router = APIRouter()

@router.get("/random")
def get_random_quote():
    return fetch_random_quote()
