"""Schedule generation routes for orchestration of planning logic."""

from __future__ import annotations

from fastapi import APIRouter, Depends

from backend.app.api.deps import get_pipeline_service
from backend.app.schemas.common import APIResponse
from backend.app.schemas.schedule import ScheduleGenerationRequest, SchedulePlan
from backend.app.services.pipeline_service import PipelineService

router = APIRouter(prefix="/schedule", tags=["schedule"])


@router.post("/generate", response_model=APIResponse[SchedulePlan])
def generate_schedule(
    request: ScheduleGenerationRequest,
    pipeline_service: PipelineService = Depends(get_pipeline_service),
) -> APIResponse[SchedulePlan]:
    """Run the scheduling pipeline and return a generated plan."""

    schedule_plan = pipeline_service.generate_schedule(request)
    return APIResponse(message="Schedule generated", data=schedule_plan)

