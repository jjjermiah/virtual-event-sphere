from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr

class UserOut(BaseModel):
    username: str
    name: str
    email: EmailStr
    
    class Config:
        from_attributes = True