from pydantic import BaseModel
from typing import List
from backend.app.schemas.user import UserState
from backend.app.schemas.task import Task
from backend.app.schemas.schedule import ScheduleItem


class GenerateScheduleRequest(BaseModel):
    user_state: UserState
    tasks: List[Task]


class GenerateScheduleResponse(BaseModel):
    schedule: List[ScheduleItem]