from ves.db import db

from ves.schemas import (
    UserCreate,
    UserOut,
)

from typing import Optional

async def create_user(user: UserCreate) -> UserOut:
    existing_user = await db.users.find_one(
        filter={"username": user.username}
    )
    if existing_user:
        raise ValueError("Username already exists")
    
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
    