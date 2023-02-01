import os

from src.utils import resolve_service_ip


class Config:
    if os.environ.get("APP_STAGE") == "dev":
        HOST = "http://localhost"
    else:
        # TODO: Use a real domain name
        # HOST = "http://microlink.ly"
        # Resolving the domain name to an IP address for now
        HOST = resolve_service_ip("microlink-web", "default")

    REDIS_URL = "redis://redis-service:6379"
