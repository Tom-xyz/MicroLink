from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import socket
from jinja2 import Environment, FileSystemLoader

router = APIRouter()
env = Environment(loader=FileSystemLoader('src/web/templates'))

@router.get("/")
def index():
    template = env.get_template('index.html')
    api_host = socket.gethostbyname("microlink-api")
    return HTMLResponse(template.render(api_host=api_host))
