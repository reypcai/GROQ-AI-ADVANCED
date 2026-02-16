import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "groq/compound-mini")
INTERNAL_API_KEY = os.getenv("INTERNAL_API_KEY", "local_secure_key")

if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY")