from pydantic import BaseModel, Field


class Task(BaseModel):
    title: str
    estimated_time: int = Field(..., gt=0)  # minutes
    subject: str


class TaskWithDifficulty(Task):
    difficulty: str