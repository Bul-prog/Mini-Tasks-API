from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class StatusEnum(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"


class TaskCreateDTO(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    status: StatusEnum


class TaskDTO(TaskCreateDTO):
    id: int