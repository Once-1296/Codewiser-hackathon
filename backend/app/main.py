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

#exceptions
from fastapi import Request
from fastapi.responses import JSONResponse
from backend.app.core.exceptions import AppException

@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=400,
        content={"error": exc.message}
    )