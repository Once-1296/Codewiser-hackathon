from typing import List, Dict
from backend.app.services.energy_service import EnergyService
from backend.app.services.task_service import TaskService
from backend.app.services.scheduler_service import SchedulerService

from backend.app.utils.logger import get_logger

logger = get_logger(__name__)

class PipelineService:
    """
    Orchestrates full flow:
    user → energy → task classification → scheduling
    """

    def __init__(self) -> None:
        self.energy_service = EnergyService()
        self.task_service = TaskService()
        self.scheduler_service = SchedulerService()

    def generate_plan(self, user_state: Dict, tasks: List[Dict]) -> List[Dict]:

        logger.info("Starting pipeline execution")
        # print(user_state)
        # print(tasks)
        # Step 1: energy
        energy = self.energy_service.predict_energy(user_state)
        logger.info(f"Predicted energy: {energy}")

        # Step 2: classify tasks
        enriched_tasks = self.task_service.classify_tasks(tasks)
        logger.info(f"Classified {len(enriched_tasks)} tasks")

        # Step 3: schedule
        schedule = self.scheduler_service.generate_schedule(
            energy=energy,
            tasks=enriched_tasks
        )
        # print(schedule)
        logger.info("Schedule generated successfully")

        return schedule

