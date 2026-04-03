from pydantic import BaseModel


class ScheduleItem(BaseModel):
    time_slot: str
    task: str
    expected_efficiency: float
    difficulty: str | None = None