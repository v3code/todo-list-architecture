from todo_list.core.fake_database.model_base import BaseModel


class Task(BaseModel):
    __tablename__ = "tasks"

    def __init__(self, name: str, user_id: int, workspace_id: int, completed: bool = False):
        self.name = name
        self.user_id = user_id
        self.workspace_id = workspace_id
        self.completed = completed
        self.init()
