from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import requests
from jinja2 import Environment, FileSystemLoader

router = APIRouter()
env = Environment(loader=FileSystemLoader('src/web/templates'))

@router.get("/")
def index():
    template = env.get_template('index.html')
    api_host = read_api_load_balancer_ip()
    return HTMLResponse(template.render(api_host=api_host))

# TODO: Replace this with a FQDN lookup
def read_api_load_balancer_ip():
    response = requests.get("http://api")
    api_host = response.headers['host']
    return api_host