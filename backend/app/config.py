from dotenv import load_dotenv
import os

load_dotenv()

CRIC_API_KEY = os.getenv("CRIC_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
