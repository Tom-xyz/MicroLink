import os

from src.utils import read_load_balancer_ip


class Config:
    if os.environ.get("APP_STAGE") == "dev":
        DOMAIN_NAME = "http://localhost:8000"
    else:
        # TODO: Use a real domain name
        # DOMAIN_NAME = "http://microlink.ly"
        # Resolving the domain name to an IP address
        DOMAIN = read_load_balancer_ip("microlink-web", "default")

    REDIS_URL = "redis://redis-service:6379"
