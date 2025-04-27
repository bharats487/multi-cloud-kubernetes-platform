import os
import subprocess

def provision_aks(cluster_name, location, resource_group_name, dns_prefix):
    os.chdir(os.path.join(os.path.dirname(__file__), '../infrastructure/terraform/azure'))
    subprocess.run(['terraform', 'init'], check=True)
    subprocess.run([
        'terraform', 'apply', '-auto-approve',
        f'-var=cluster_name={cluster_name}',
        f'-var=location={location}',
        f'-var=resource_group_name={resource_group_name}',
        f'-var=dns_prefix={dns_prefix}'
    ], check=True)

if __name__ == "__main__":
    # Example usage: fill in your values
    provision_aks(
        cluster_name="demo-aks",
        location="eastus",
        resource_group_name="your-resource-group",
        dns_prefix="demoaks"
    )
