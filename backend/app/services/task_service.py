from typing import List, Dict
from backend.app.ml.inference.task_classifier import TaskClassifier


class TaskService:
    """
    Handles task classification logic.
    """

    def __init__(self) -> None:
        self.classifier = TaskClassifier()

    def classify_tasks(self, tasks: List[Dict]) -> List[Dict]:
        enriched_tasks = []

        for task in tasks:
            difficulty = self.classifier.classify(task)

            enriched_task = {
                **task,
                "difficulty": difficulty
            }

            enriched_tasks.append(enriched_task)

        return enriched_tasks