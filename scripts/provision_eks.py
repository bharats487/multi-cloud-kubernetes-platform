import os
import subprocess

def provision_eks(cluster_name, region, vpc_id, subnets):
    os.chdir(os.path.join(os.path.dirname(__file__), '../infrastructure/terraform/aws'))
    subprocess.run(['terraform', 'init'], check=True)
    subprocess.run([
        'terraform', 'apply', '-auto-approve',
        f'-var=cluster_name={cluster_name}',
        f'-var=region={region}',
        f'-var=vpc_id={vpc_id}',
        f'-var=subnets={subnets}'
    ], check=True)

if __name__ == "__main__":
    # Example usage: fill in your values
    provision_eks(
        cluster_name="demo-eks",
        region="us-east-1",
        vpc_id="vpc-xxxxxxx",
        subnets="[\"subnet-xxxx\",\"subnet-yyyy\"]"
    )
