import hashlib
import redis

# Create a redis client
r = redis.Redis(host='localhost', port=6379, db=0)

async def generate_short_url(long_url: str):
    # Generate a unique hash for the long URL
    hash = hashlib.sha1(long_url.encode()).hexdigest()[:8]

    # Check if the hash already exists in Redis
    if r.exists(hash):
        # Retrieve the existing long URL from Redis
        long_url = r.get(hash)
    else:
        # Store the mapping between the long and short URLs in Redis
        r.set(hash, long_url)

    # Construct the shortened URL
    short_url = f"http://short.ly/{hash}"
    return short_url
