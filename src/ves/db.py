from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from src.ves.core.config.settings import (
    MONGO_DB,
    MONGO_URI,
)

if (MONGO_URI is None):
    raise ValueError("MONGO_URI is not set")

client = AsyncIOMotorClient(MONGO_URI)

if (MONGO_DB is None):
    raise ValueError("MONGO_DB is not set")

db: AsyncIOMotorDatabase = client[MONGO_DB]