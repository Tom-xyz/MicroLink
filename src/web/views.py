from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/")
def index():
    return HTMLResponse(content=open("src/web/templates/index.html").read())
