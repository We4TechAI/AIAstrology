import random
import requests
from core.config import RAPID_API_KEY

bible_verses = [
    "John 3:16", "Psalm 23:1", "Romans 8:28", "Philippians 4:13",
    "Genesis 1:1", "Proverbs 3:5", "Matthew 6:33", "Isaiah 40:31",
    "1 Corinthians 13:4", "Jeremiah 29:11"
]

def get_random_bible_verse():
    reference = random.choice(bible_verses)
    url = f"https://bible-api.com/{reference.replace(' ', '+')}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "reference": data.get("reference"),
            "text": data.get("text").strip(),
            "translation": data.get("translation_name")
        }
    return {"error": "Failed to fetch verse"}

def get_random_gita_chapter():
    chapter_id = random.randint(1, 18)
    url = f"https://bhagavad-gita3.p.rapidapi.com/v2/chapters/{chapter_id}/"
    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "bhagavad-gita3.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch chapter"}