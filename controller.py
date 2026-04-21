from fastapi import APIRouter, HTTPException
from typing import List
from dto import TaskDTO, TaskCreateDTO
from service import task_service

router = APIRouter()


@router.post("/tasks", response_model=TaskDTO)
def create_task(task: TaskCreateDTO):
    return task_service.create(task)


@router.get("/tasks", response_model=List[TaskDTO])
def get_tasks():
    return task_service.get_all()


# ⭐ бонус
@router.get("/tasks/{task_id}", response_model=TaskDTO)
def get_task(task_id: int):
    task = task_service.get_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task