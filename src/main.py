from fastapi import FastAPI
from src.api.v1 import users

app = FastAPI()
app.include_router(users.router, prefix="/api/v1")

@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello VirtualEventSphere!"}

