import requests
from backend.app.config import CRIC_API_KEY

BASE_URL = "https://api.cricapi.com/v1"

def get_current_matches():

    url = f"{BASE_URL}/currentMatches"

    params = {
        "apikey": CRIC_API_KEY,
        "offset": 0
    }

    response = requests.get(
        url,
        params=params
    )

    return response.json()