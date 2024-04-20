from fastapi import (
    APIRouter, 
    HTTPException,
)
from src.schemas import UserCreate
from src.crud import create_user

router = APIRouter()

@router.post("/users/", response_model=UserCreate)
async def create_user_route(user: UserCreate):
    return await create_user(user)