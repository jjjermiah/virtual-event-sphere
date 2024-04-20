import asyncio

from schemas.schema_user import UserOut
from src.schemas import UserCreate
from src.crud import (
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
    await asyncio.sleep(2)  # Sleep for 2 seconds
    return await create_user(user)

@router.get("/users/{username}", response_model=UserCreate)
async def get_user_by_username_route(
    username: str = Path(default=..., example = "johndoe")
) -> UserOut:
    user = await get_user_by_username(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user