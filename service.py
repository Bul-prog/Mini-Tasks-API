from typing import List, Optional
from dto import TaskDTO, TaskCreateDTO


class TaskService:
    def __init__(self):
        self.tasks: List[TaskDTO] = []
        self.counter = 1

    def create(self, data: TaskCreateDTO) -> TaskDTO:
        task = TaskDTO(id=self.counter, **data.dict())
        self.tasks.append(task)
        self.counter += 1
        return task

    def get_all(self) -> List[TaskDTO]:
        return self.tasks

    def get_by_id(self, task_id: int) -> Optional[TaskDTO]:
        return next((t for t in self.tasks if t.id == task_id), None)


# один экземпляр сервиса (in-memory storage)
task_service = TaskService()