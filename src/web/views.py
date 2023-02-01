from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
from src.config import Config

router = APIRouter()
env = Environment(loader=FileSystemLoader("src/web/templates"))


@router.get("/")
def index():
    template = env.get_template("index.html")
    return HTMLResponse(template.render(host=Config.HOST))
