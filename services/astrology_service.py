import json
import requests
from fastapi import HTTPException
from core.config import ASTROLOGY_API_KEY, FIXED_TIMEZONE

def fetch_astrology_data(lat, lon, year, month, day, hour, minute, second):
    url = "https://json.freeastrologyapi.com/d6-chart-info"
    payload = json.dumps({
        "year": year,
        "month": month,
        "date": day,
        "hours": hour,
        "minutes": minute,
        "seconds": second,
        "latitude": lat,
        "longitude": lon,
        "timezone": FIXED_TIMEZONE,
        "config": {
            "observation_point": "topocentric",
            "ayanamsha": "lahiri"
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': ASTROLOGY_API_KEY
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    raise HTTPException(status_code=response.status_code, detail="Error while fetching astrology data")
