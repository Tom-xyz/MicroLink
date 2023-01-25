from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import aioredis
import hashlib

app = FastAPI()

async def get_redis_pool():
    return await aioredis.create_redis_pool('redis://localhost')

@app.get('/')
def index():
    return HTMLResponse(content=open("templates/index.html").read())

@app.post("/shorten")
async def shorten_url(long_url: str):
    async with get_redis_pool() as redis:
        # Generate a unique hash for the long URL
        hash = hashlib.sha1(long_url.encode()).hexdigest()[:8]

        # Check if the hash already exists in Redis
        if await redis.exists(hash):
            # Retrieve the existing long URL from Redis
            long_url = await redis.get(hash)
        else:
            # Store the mapping between the long and short URLs in Redis
            await redis.set(hash, long_url)

        # Construct the shortened URL
        short_url = f"http://short.ly/{hash}"
        return {"short_url": short_url}

@app.get("/{short_url}")
async def resolve_short_url(short_url: str):
    async with get_redis_pool() as redis:
        # Extract the hash from the short URL
        hash = short_url.split("/")[-1]

        # Check if the hash exists in Redis
        if await redis.exists(hash):
            # Retrieve the corresponding long URL from Redis
            long_url = await redis.get(hash)
            return {"long_url": long_url.decode()}
        else:
            return {"error": "Short URL not found"}
