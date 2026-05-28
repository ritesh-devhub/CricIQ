from fastapi import FastAPI
from backend.services.cricapi_service import get_current_matches

app = FastAPI(
    title="CricIQ API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "CricIQ Backend Running"
    }

@app.get("/matches")
def matches():
    return get_current_matches()