from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from core.config.settings import (
    MONGO_DB,
    MONGO_URI,
)

client = AsyncIOMotorClient(MONGO_URI)

db: AsyncIOMotorDatabase = client[MONGO_DB]