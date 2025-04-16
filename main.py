import requests
from fastapi import FastAPI, HTTPException
import os
import json
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Free Astrology API Key
api_key = os.getenv("ASTROLOGY_API_KEY")

# Fixed timezone (since you don't want to dynamically handle it)
FIXED_TIMEZONE = 5.5


class AstrologyResponse(BaseModel):
    observation: list[str]
# Pydantic model to accept request data
class AstrologyRequest(BaseModel):
    location: str  # Location for coordinates
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int


# Function to get astrology response
def response_astrology(lat: float, lon: float, year: int, month: int, day: int, hour: int, minute: int, second: int):
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
        "timezone": FIXED_TIMEZONE,  # Using fixed timezone
        "config": {
            "observation_point": "topocentric",
            "ayanamsha": "lahiri"
        }
    })

    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()  # Returning the response in JSON format
    else:
        raise HTTPException(status_code=response.status_code, detail="Error while fetching astrology data")


# Function to get coordinates (latitude, longitude) from location
def get_coordinates(location: str):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": location,
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "AstrologyApp"  # Nominatim requires identifying header
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if data:
        lat = float(data[0]['lat'])
        lon = float(data[0]['lon'])
        return lat, lon
    else:
        raise HTTPException(status_code=404, detail="Location not found")



def get_astrology_insight(json_data):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=f'Act as a highly experienced Astrologer . Access the input data and give a detailed answer based on astrology. \n {json_data}',
        config={
            'response_mime_type': 'application/json',
            'response_schema': AstrologyResponse,
        },
    )
    # Use the response as a JSON string.
    print(response.text)

    # Use instantiated objects.
    my_recipes: list[Recipe] = response.parsed
    return my_recipes
# FastAPI route to get astrology chart by location and other data (via POST)
@app.post("/get-astrology-chart/")
def get_astrology_chart(request: AstrologyRequest):
    # Get coordinates for the location
    try:
        lat, lon = get_coordinates(request.location)
    except HTTPException as e:
        raise e

    # Get astrology data for the obtained coordinates and other data
    astrology_data = response_astrology(
        lat,
        lon,
        request.year,
        request.month,
        request.day,
        request.hour,
        request.minute,
        request.second
    )
    print("*"*100)
    print(astrology_data)
    print("*"*100)
    if isinstance(astrology_data, dict) and "output" in astrology_data:
        Astrology_response = get_astrology_insight(astrology_data["output"])
    else:
        raise ValueError("Invalid astrology data format")

    return Astrology_response
