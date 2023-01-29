from fastapi import FastAPI
from web.views import router as web_router

app = FastAPI()
app.include_router(web_router)
