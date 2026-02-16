from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.groq_client import generate_response
from app.rate_limiter import check_rate_limit
from app.auth import verify_api_key

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/chat")
def chat(request: PromptRequest, api_key: str = Depends(verify_api_key)):

    if not check_rate_limit():
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    response = generate_response(request.prompt)
    return {"response": response}