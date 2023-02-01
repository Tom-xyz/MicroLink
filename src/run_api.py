from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.views import router as api_router

app = FastAPI()

# TODO: Restrict CORS to the domain name
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)
