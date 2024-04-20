from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api.v1 import users



@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("Starting application...")
        yield
    finally:
        print("Stopping application...")

app = FastAPI(lifespan=lifespan)
app.include_router(users.router, prefix="/api")