
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class User(BaseModel):
    id: Optional[int] = Field(default=None, alias='id')
    username: str
    name: str
    email: EmailStr
    
    
    
     