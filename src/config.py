import os

class Config:
    if os.environ.get('APP_ENV') == 'dev':
        DOMAIN_NAME = "http://localhost:8000"
    else:
        DOMAIN_NAME = "http://microlink.ly"
