import os

class Config:
    if os.environ.get('APP_STAGE') == 'dev':
        DOMAIN_NAME = "http://localhost:8000"
        REDIS_URL = "redis://localhost:6379"
    else:
        DOMAIN_NAME = "http://microlink.ly"
        REDIS_URL = "redis://redis:6379"
