from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.schemas.user import UserState
from backend.app.db.session import get_db
from backend.app.db import crud

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/logs", response_model=UserState)
def log_user(user: UserState, db: Session = Depends(get_db)):
    crud.create_user_state(db, user.model_dump())
    return user