import os

class Config:
    if os.environ.get('APP_STAGE') == 'dev':
        DOMAIN_NAME = "http://localhost:8000"
    else:
        DOMAIN_NAME = "http://microlink.ly"

    REDIS_URL = "redis://redis-service:6379"
