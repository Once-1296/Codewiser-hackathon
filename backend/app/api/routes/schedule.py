from fastapi import APIRouter, Depends

from backend.app.api.deps import get_pipeline_service
from backend.app.services.pipeline_service import PipelineService

from backend.app.schemas.common import (
    GenerateScheduleRequest,
    GenerateScheduleResponse
)

router = APIRouter(prefix="/schedule", tags=["schedule"])


@router.post("/generate", response_model=GenerateScheduleResponse)
def generate_schedule(
    payload: GenerateScheduleRequest,
    pipeline: PipelineService = Depends(get_pipeline_service)
):
    result = pipeline.generate_plan(
        user_state=payload.user_state.model_dump(),
        tasks=[task.model_dump() for task in payload.tasks]
    )

    return {"schedule": result}