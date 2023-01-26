# conftest.py
import unittest
from unittest.mock import MagicMock, Mock, AsyncMock, patch
import pytest
from fakeredis.aioredis import FakeRedis
from fastapi.testclient import TestClient
import asyncio



event_loop = asyncio.get_event_loop()
if event_loop is None:
    event_loop = asyncio.new_event_loop()
patch('asyncio.get_event_loop', event_loop)


@pytest.fixture
def mock_redis(mocker):
    fake_redis = FakeRedis.from_url
    mocker.patch("redis.asyncio.from_url", fake_redis)


@pytest.fixture()
def app(mock_redis):
    from src.views import app

    return app


@pytest.fixture
def client(app):
    return TestClient(app)
