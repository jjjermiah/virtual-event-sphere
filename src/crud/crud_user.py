from src.db import db

from src.schemas import (
    UserCreate,
    UserOut,
)

from typing import Optional

async def create_user(user: UserCreate) -> UserOut:
    new_user = user.model_dump()
    await db.users.insert_one(new_user)
    return UserOut(**new_user)

async def get_user_by_username(username: str) -> Optional[UserOut]:
    user = await db.users.find_one(
        filter={"username": username}
    )
    if user:
        return UserOut(**user)
    
    return None
    