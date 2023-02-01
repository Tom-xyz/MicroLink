# TODO: Replace this hack, replace with an endpoint FQDN lookup
# Example: https://api.<project-id>.endpoints.cloud.google.com
def resolve_service_ip(ingress_name, namespace):
    import kubernetes
    kubernetes.config.load_incluster_config()
    api_ext = kubernetes.client.ExtensionsV1beta1Api()
    ingress = api_ext.read_namespaced_ingress(ingress_name, namespace)
    ingress_host = ingress.status.load_balancer.ingress[0].ip
    return ingress_host
