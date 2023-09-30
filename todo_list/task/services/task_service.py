from todo_list.task.dto.task_dto import TaskDTO
from todo_list.task.dto.tasks_dto import TasksDTO
from todo_list.task.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def get_all_tasks(self):
        tasks = self.repo.get_all_tasks()
        return TasksDTO.from_model_list(tasks)

    def add_new_task(self, add_task_dto):
        task = self.repo.add_new_task(add_task_dto)
        return TaskDTO.from_model(task)

    def delete_task(self, delete_task_dto):
        return self.repo.delete_task(delete_task_dto)

    def update_task(self, update_task_dto):
        updated_task = self.repo.update_task(update_task_dto)
        return TaskDTO.from_model(updated_task)