from src.schemas import UserCreate

async def create_user(user: UserCreate):
    return user