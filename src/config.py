import os

from src.utils import resolve_service_ip


class Config:
    if os.environ.get("APP_STAGE") == "dev":
        HOST = "http://localhost"
    else:
        # TODO: Use a real domain name
        # Resolving to the ingress external IP address for now
        HOST = resolve_service_ip("web-and-api-ingress", "default")

    REDIS_URL = "redis://redis-service:6379"
