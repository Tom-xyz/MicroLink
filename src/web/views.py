from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import kubernetes
from jinja2 import Environment, FileSystemLoader

router = APIRouter()
env = Environment(loader=FileSystemLoader('src/web/templates'))

@router.get("/")
def index():
    template = env.get_template('index.html')
    api_host = read_api_load_balancer_ip()
    return HTMLResponse(template.render(api_host=api_host))

# TODO: Replace this with a Google endpoint FQDN lookup
# Example: https://api.<project-id>.endpoints.cloud.google.com
def read_api_load_balancer_ip():
    kubernetes.config.load_incluster_config()
    api_v1 = kubernetes.client.CoreV1Api()
    service = api_v1.read_namespaced_service("microlink-api", "default")
    api_host = service.status.load_balancer.ingress[0].ip
    return api_host