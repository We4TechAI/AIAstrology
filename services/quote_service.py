import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def fetch_random_quote():
    response = requests.get("https://api.quotable.io/random", verify=False)
    if response.status_code == 200:
        data = response.json()
        return {
            "quote": data.get("content"),
            "author": data.get("author")
        }
    return {"error": "Failed to fetch quote"}