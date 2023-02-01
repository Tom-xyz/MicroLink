# TODO: Replace this hack, replace with an endpoint FQDN lookup
# Example: https://api.<project-id>.endpoints.cloud.google.com
def resolve_service_ip(service_name, namespace):
    import kubernetes
    kubernetes.config.load_incluster_config()
    api_v1 = kubernetes.client.CoreV1Api()
    service = api_v1.read_namespaced_service(service_name, namespace)
    api_host = service.status.load_balancer.ingress[0].ip
    return api_host