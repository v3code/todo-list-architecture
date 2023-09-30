from todo_list.core.fake_database.fake_db import FakeDB
from todo_list.task.models.task import Task


class TaskRepository:
    def __init__(self, db: FakeDB):
        self.db = db

    def get_all_tasks(self):
        return self.db.get_table("tasks")

    def add_new_task(self, add_task_dto):
        task = Task(
            name=add_task_dto.name,
            user_id=add_task_dto.user_id,
            workspace_id=add_task_dto.workspace_id,
            completed=add_task_dto.completed
        )
        self.db.add_table(task)
        return task

    def get_task_idx_by_id(self, task_id: int):
        tasks = self.db.get_table(table=Task.get_table_name())
        for idx, task in enumerate(tasks):
            if task.id == task_id:
                return idx

    def delete_task(self, delete_task_dto):
        idx = self.get_task_idx_by_id(delete_task_dto.id)
        self.db.delete_data(table=Task.get_table_name(), idx=idx)

    def update_task(self, update_task_dto):
        new_task = Task(
            update_task_dto.name,
            update_task_dto.user_id,
            update_task_dto.workspace_id,
            update_task_dto.completed
        )
        idx = self.get_task_idx_by_id(update_task_dto.id)
        self.db.update_data(table=Task.get_table_name(), idx=idx, data=new_task)
