from fastapi import FastAPI
from fastapi_cors import CORS
from src.api.views import router as api_router

app = FastAPI()
CORS(app)
app.include_router(api_router)
