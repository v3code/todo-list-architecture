from todo_list.app import app
from flask import jsonify, request

from todo_list.db import db
from todo_list.task.dto.add_task_dto import AddTaskDTO
from todo_list.task.repositories.task_repository import TaskRepository
from todo_list.task.services.task_service import TaskService

TASK_ROUTE = '/task'
task_repo = TaskRepository(db)
task_service = TaskService(task_repo)


@app.get(TASK_ROUTE)
def get_all_tasks():
    tasks = task_service.get_all_tasks()
    return jsonify(tasks)

@app.post(TASK_ROUTE)
def add_task():
    data = request.get_json()
    add_task_dto = AddTaskDTO(**data)
    task = task_service.add_new_task(add_task_dto)
    return jsonify(task)