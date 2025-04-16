import os
from dotenv import load_dotenv

load_dotenv()

ASTROLOGY_API_KEY = os.getenv("ASTROLOGY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")

FIXED_TIMEZONE = 5.5