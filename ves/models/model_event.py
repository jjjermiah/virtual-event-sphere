from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Event(BaseModel):
    id: Optional[int] = Field(default=None, alias='id')
    name: str
    description: str
    # date: datetime.date
    # time: datetime.time
    
    