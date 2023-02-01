# TODO: Replace this hack, replace with an endpoint FQDN lookup
# Example: https://api.<project-id>.endpoints.cloud.google.com
def resolve_service_ip(ingress_name, namespace):
    import kubernetes
    from kubernetes import client as kubernetes_client

    kubernetes.config.load_incluster_config()
    api = kubernetes_client.networking.v1_beta1.ExtensionsV1beta1Api()
    ingress = api.read_namespaced_ingress(ingress_name, namespace)
    ingress_host = ingress.status.load_balancer.ingress[0].ip
    return ingress_host
