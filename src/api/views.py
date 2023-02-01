from fastapi import APIRouter
import redis.asyncio as redis
import hashlib
from src.config import Config
from starlette.responses import RedirectResponse

router = APIRouter()
redis_client = redis.from_url(Config.REDIS_URL)


@router.post("/shorten_url")
async def shorten_url(long_url: str):
    async with redis_client:
        # Generate a unique hash for the long URL
        hash = hashlib.sha1(long_url.encode()).hexdigest()[:8]

        # Check if the hash already exists in Redis
        if await redis_client.exists(hash):
            # Retrieve the existing long URL from Redis
            long_url = await redis_client.get(hash)
        else:
            # Store the mapping between the long and short URLs in Redis
            await redis_client.set(hash, long_url)

        # Construct the shortened URL
        short_url = f"{Config.HOST}/{hash}"
        return {"short_url": short_url}


@router.get("/{short_url}")
async def resolve_short_url(short_url: str):
    async with redis_client:
        # Extract the hash from the short URL
        hash = short_url.split("/")[-1]

        # Check if the hash exists in Redis
        if await redis_client.exists(hash):
            # Retrieve the corresponding long URL from Redis and redirect the client
            long_url = await redis_client.get(hash)
            return RedirectResponse(long_url)
        else:
            return {"error": "Short URL not found"}


@router.get("/")
async def health_check():
    return {"status": "ok"}
