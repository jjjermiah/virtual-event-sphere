from fastapi import FastAPI
from contextlib import asynccontextmanager
from ves.api.v1 import users



@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("Starting application...")
        yield
    finally:
        print("Stopping application...")

app = FastAPI(lifespan=lifespan)
app.include_router(
    router=users.router, 
    prefix="/api",
    tags=["users"]
)

@app.get(path="/")
async def read_root():
    return {"Hello": "World"}
