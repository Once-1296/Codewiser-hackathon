from pydantic import BaseModel, Field


class UserState(BaseModel):
    sleep_hours: float = Field(..., ge=0, le=24)
    stress_level: int = Field(..., ge=1, le=5)
    time_of_day: str