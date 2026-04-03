from backend.app.services.pipeline_service import PipelineService
from backend.app.db.session import get_db

def get_pipeline_service() -> PipelineService:
    """
    Dependency injector for PipelineService.
    """
    return PipelineService()