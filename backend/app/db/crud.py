from sqlalchemy.orm import Session
from backend.app.db import models


# -------------------------
# USER
# -------------------------

def create_user_state(db: Session, user_data: dict):
    user = models.UserStateDB(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_latest_user_state(db: Session):
    return db.query(models.UserStateDB).order_by(models.UserStateDB.id.desc()).first()


# -------------------------
# TASKS
# -------------------------

def create_tasks(db: Session, tasks: list):
    db_tasks = [models.TaskDB(**task) for task in tasks]
    db.add_all(db_tasks)
    db.commit()
    return db_tasks


def get_all_tasks(db: Session):
    return db.query(models.TaskDB).all()