from google import genai
from core.config import GEMINI_API_KEY
from models.request_models import AstrologyResponse

def get_astrology_insight(json_data):
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=f"Act as a highly experienced Astrologer. Access the input data and give a detailed answer based on astrology. \n {json_data}",
        config={
            'response_mime_type': 'application/json',
            'response_schema': AstrologyResponse,
        },
    )
    return response.parsed