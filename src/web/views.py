from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

from src.utils import read_load_balancer_ip

router = APIRouter()
env = Environment(loader=FileSystemLoader("src/web/templates"))


@router.get("/")
def index():
    template = env.get_template("index.html")
    api_host = read_load_balancer_ip("microlink-api", "default")
    return HTMLResponse(template.render(api_host=api_host))
