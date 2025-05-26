# app/schemas/task.py
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str
    deadline: datetime

class TaskOut(TaskCreate):
    id: int
    completed: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True) # Updated Pydantic v2 syntax