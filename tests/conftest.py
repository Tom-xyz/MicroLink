# conftest.py
import os
from unittest.mock import MagicMock
import pytest
from fakeredis.aioredis import FakeRedis

@pytest.fixture
def fake_redis(monkeypatch):
    fake_redis = FakeRedis()
    monkeypatch.setattr("src.api.views.redis_client", fake_redis)
    return fake_redis

@pytest.fixture
def hash_patch(monkeypatch):
    hash_mock = MagicMock()
    hash_digest_mock = MagicMock()
    hash_digest_mock.return_value = "12345678"
    hash_mock.return_value.hexdigest = hash_digest_mock
    monkeypatch.setattr("src.api.views.hashlib.sha1", hash_mock)
    return hash_mock

@pytest.fixture
def domain_patch(monkeypatch):
    monkeypatch.setattr("src.config.Config.DOMAIN_NAME", "http://localhost:8000")
