import asyncio
from ves.schemas.schema_user import UserOut
from ves.schemas import UserCreate
from ves.crud import (
    create_user,
    get_user_by_username,
)

from fastapi import (
    APIRouter, 
    HTTPException,
    Path,
)

router = APIRouter()

@router.post("/users/", response_model=UserCreate)
async def create_user_route(user: UserCreate) -> UserOut:   
    try:
        new_user = await create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return new_user
    

@router.get("/users/{username}", response_model=UserCreate)
async def get_user(
    username: str = Path(default=..., example = "johndoe")
) -> UserOut:
    user = await get_user_by_username(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user