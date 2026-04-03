from sqlalchemy import Column, Integer, String, Float
from backend.app.db.session import Base


class UserStateDB(Base):
    __tablename__ = "user_states"

    id = Column(Integer, primary_key=True, index=True)
    sleep_hours = Column(Float)
    stress_level = Column(Integer)
    time_of_day = Column(String)


class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    estimated_time = Column(Integer)
    subject = Column(String)
    difficulty = Column(String, nullable=True)