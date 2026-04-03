from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

# 1. Define the "Contract" using a Pydantic model
class HealthResponse(BaseModel):
    message: str
    data: dict

@router.get("/health", response_model=HealthResponse)
def health_check():
    # 2. Return the model instance, not just a dict
    return HealthResponse(
        message="Service is healthy",
        data={"status": "ok"}
    )
