from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from contextlib import asynccontextmanager
from ves.api.v1 import users, events



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
app.include_router(
    router=events.router, 
    prefix="/api",
    tags=["events"]
)

@app.get(path="/", response_class=HTMLResponse)
async def read_root():
    # Return a clickable link to the api docs as html
    return """
    <html>
        <head>
            <title>API Docs</title>
        </head>
        <body>
            <h1>API Docs</h1>
            <a href="/docs">API Documentation</a>
        </body> 
    </html>
    """
