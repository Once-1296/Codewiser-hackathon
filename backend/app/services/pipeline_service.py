from typing import List, Dict
from backend.app.services.energy_service import EnergyService
from backend.app.services.task_service import TaskService
from backend.app.services.scheduler_service import SchedulerService

from backend.app.utils.logger import get_logger
from backend.app.ml.inference.efficiency_predictor import EfficiencyPredictor

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
        # efficiency predictor (optional, will be None if model not found)
        try:
            self.efficiency_predictor = EfficiencyPredictor()
        except Exception:
            self.efficiency_predictor = None

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
        # pass user's preferred time of day to the scheduler so we can center tougher tasks
        preferred_time = user_state.get("time_of_day") if isinstance(user_state, dict) else None
        schedule = self.scheduler_service.generate_schedule(
            energy=energy,
            tasks=enriched_tasks,
            preferred_time_of_day=preferred_time,
        )
        logger.info("Schedule generated successfully")

        # Step 4: score schedule with efficiency predictor (if available)
        try:
            if self.efficiency_predictor and schedule:
                scored = self.efficiency_predictor.predict_schedule(schedule, user_state, energy)
                return scored
        except Exception:
            logger.exception("Efficiency predictor failed; returning unscored schedule")

        return schedule

