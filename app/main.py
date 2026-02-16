from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Groq AI Advanced System")

app.include_router(router)