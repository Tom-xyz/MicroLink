import kubernetes

# TODO: Replace this is a hack, replace with a Google endpoint FQDN lookup
# Example: https://api.<project-id>.endpoints.cloud.google.com
def read_load_balancer_ip(service_name, namespace):
    kubernetes.config.load_incluster_config()
    api_v1 = kubernetes.client.CoreV1Api()
    service = api_v1.read_namespaced_service(service_name, namespace)
    api_host = service.status.load_balancer.ingress[0].ip
    return api_host