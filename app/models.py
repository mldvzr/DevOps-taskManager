from datetime import datetime
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = datetime.now()