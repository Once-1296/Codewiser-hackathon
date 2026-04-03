from fastapi import FastAPI

from backend.app.api.routes import health, schedule, tasks, user

app = FastAPI(title="Cognitive Study Planner API")


# Register routers
app.include_router(health.router)
app.include_router(schedule.router)
app.include_router(tasks.router)
app.include_router(user.router)

from backend.app.db.session import Base, engine

# create tables
Base.metadata.create_all(bind=engine)