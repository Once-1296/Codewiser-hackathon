from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from backend.app.schemas.task import Task
from backend.app.db.session import get_db
from backend.app.db import crud

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=List[Task])
def create_tasks(tasks: List[Task], db: Session = Depends(get_db)):
    crud.create_tasks(db, [task.model_dump() for task in tasks])
    return tasks