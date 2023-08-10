from kubernetes import client, config
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    try:
        # Load Kubernetes configuration
        try:
            config.load_incluster_config()
        except:
            config.load_kube_config()

        # Create a Kubernetes API client
        api_instance = client.CoreV1Api()

        # Get a list of all namespaces
        namespace_list = api_instance.list_namespace()

        services_info = []

        for namespace in namespace_list.items:
            namespace_name = namespace.metadata.name

            # Get a list of all services in the namespace
            service_list = api_instance.list_namespaced_service(namespace_name)

            for service in service_list.items:
                service_info = {
                    "namespace": namespace_name,
                    "name": service.metadata.name,
                    "ip": service.spec.cluster_ip,
                    "port": service.spec.ports[0].port
                }
                services_info.append(service_info)

        return render_template('service_list.html', services=services_info)

    except client.rest.ApiException as e:
        return "Error fetching service information: " + str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)
 
