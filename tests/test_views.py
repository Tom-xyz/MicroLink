import pytest

@pytest.mark.asyncio
async def test_shorten_url(client):
    long_url = "https://www.example.com"
    response = client.post("/shorten_url", params={"long_url": long_url})
    assert response.status_code == 200
    short_url = response.json()["short_url"]
    # check that the long_url is stored in redis
    # assert mock_redis.get(short_url.split("/")[-1]).decode() == long_url


def test_resolve_short_url(client):
    long_url = "https://www.example.com"
    short_url = client.post("/shorten_url", params={"long_url": long_url}).json()[
        "short_url"
    ]
    short_url_id = short_url.split("/")[-1]
    response = client.get(f"/{short_url_id}")
    assert response.status_code == 200
    print("DEBUGING")
    print(response.json())
    assert response.json()["long_url"] == long_url


def test_resolve_short_url_invalid(client):
    response = client.get("/invalid_id")
    assert response.status_code == 200
    assert response.json() == {"error": "Short URL not found"}
