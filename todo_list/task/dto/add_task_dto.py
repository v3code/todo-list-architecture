from dataclasses import dataclass


@dataclass
class AddTaskDTO:
    name: str
    user_id: int
    workspace_id: int
    completed: bool = False