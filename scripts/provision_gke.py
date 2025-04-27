import os
import subprocess

def provision_gke(cluster_name, project, region, network, subnetwork, ip_range_pods, ip_range_services):
    os.chdir(os.path.join(os.path.dirname(__file__), '../infrastructure/terraform/gcp'))
    subprocess.run(['terraform', 'init'], check=True)
    subprocess.run([
        'terraform', 'apply', '-auto-approve',
        f'-var=cluster_name={cluster_name}',
        f'-var=project={project}',
        f'-var=region={region}',
        f'-var=network={network}',
        f'-var=subnetwork={subnetwork}',
        f'-var=ip_range_pods={ip_range_pods}',
        f'-var=ip_range_services={ip_range_services}'
    ], check=True)

if __name__ == "__main__":
    # Example usage: fill in your values
    provision_gke(
        cluster_name="demo-gke",
        project="your-gcp-project",
        region="us-central1",
        network="default",
        subnetwork="default",
        ip_range_pods="pods",
        ip_range_services="services"
    )
