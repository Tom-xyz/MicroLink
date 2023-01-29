from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/")
def index():
    return HTMLResponse(content=open("templates/index.html").read())
