import requests
from fastapi import HTTPException

def get_coordinates(location: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {"q": location, "format": "json", "limit": 1}
    headers = {"User-Agent": "AstrologyApp"}
    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    if data:
        return float(data[0]['lat']), float(data[0]['lon'])
    raise HTTPException(status_code=404, detail="Location not found")

