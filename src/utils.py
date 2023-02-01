
import kubernetes
# TODO: Replace this hack, replace with an endpoint FQDN lookup
# Example: https://api.<project-id>.endpoints.cloud.google.com
def resolve_service_ip(ingress_name, namespace):
    kubernetes.config.load_incluster_config()
    client = kubernetes.client.ApiClient()
    api_instance = kubernetes.client.NetworkingV1Api(client)
    service = api_instance.read_namespaced_ingress(ingress_name, namespace)
    api_host = service.status.load_balancer.ingress[0].ip
    return api_host