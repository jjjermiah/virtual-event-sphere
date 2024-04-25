from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from contextlib import asynccontextmanager
from ves.api.v1 import users, events


from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("Starting application...")
        redis = aioredis.from_url("redis://localhost")
        FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
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
