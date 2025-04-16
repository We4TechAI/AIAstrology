from fastapi import APIRouter
from models.request_models import AstrologyRequest
from services.astrology_service import fetch_astrology_data
from utils.location_utils import get_coordinates
from utils.gemini_utils import get_astrology_insight

router = APIRouter()

@router.post("/chart")
def get_astrology_chart(request: AstrologyRequest):
    lat, lon = get_coordinates(request.location)
    astrology_data = fetch_astrology_data(lat, lon, request.year, request.month, request.day, request.hour, request.minute, request.second)
    if isinstance(astrology_data, dict) and "output" in astrology_data:
        return get_astrology_insight(astrology_data["output"])
    raise ValueError("Invalid astrology data format")