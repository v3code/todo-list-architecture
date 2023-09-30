from dataclasses import dataclass
from typing import List

from todo_list.task.dto.task_dto import TaskDTO
from todo_list.task.models.task import Task


@dataclass
class TasksDTO:
    tasks: List[TaskDTO]

    @staticmethod
    def from_model_list(models: List[Task]):
        return TasksDTO([TaskDTO.from_model(model) for model in models])
