import pytest
from src.api.views import shorten_url, resolve_short_url


@pytest.mark.asyncio
async def test_shorten_url(fake_redis, domain_patch, hash_patch):
    long_url = "https://www.example.com"
    result = await shorten_url(long_url)

    assert result["short_url"] == "http://localhost:8000/12345678"
    assert (await fake_redis.get("12345678")).decode() == long_url


@pytest.mark.asyncio
async def test_resolve_short_url(fake_redis, domain_patch, hash_patch):
    short_code = "12345678"
    short_url = f"http://localhost:8000/{short_code}"
    long_url = "https://www.example.com"

    await fake_redis.set(short_code, long_url)
    resolve_result = await resolve_short_url(short_url)
    assert resolve_result["long_url"] == long_url
    assert (await fake_redis.get(short_code)).decode() == long_url


@pytest.mark.asyncio
async def test_resolve_short_url_invalid(fake_redis, domain_patch, hash_patch):
    short_url = "http://localhost:8000/invalid_id"
    result = await resolve_short_url(short_url)
    assert result["error"] == "Short URL not found"
