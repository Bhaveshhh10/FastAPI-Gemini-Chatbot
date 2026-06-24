from fastapi import APIRouter, HTTPException
from schemas.chat_schema import ChatRequest
from services.gemini_service import generate_response

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    try:
        reply = generate_response(
            request.message,
            request.mode
        )

        return {
            "status": "success",
            "reply": reply
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )