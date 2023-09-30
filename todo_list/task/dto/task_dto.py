from dataclasses import dataclass

from todo_list.task.models.task import Task


@dataclass
class TaskDTO:
    id: int
    name: str
    workspace_id: int
    completed: bool

    @staticmethod
    def from_model(model: Task):
        return TaskDTO(
            model.id,
            model.name,
            model.workspace_id,
            model.completed
        )