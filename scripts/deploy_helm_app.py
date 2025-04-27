import os
import subprocess

def deploy_helm_app(release_name, chart_path, namespace="default", values_file=None):
    cmd = [
        "helm", "upgrade", "--install", release_name, chart_path,
        "--namespace", namespace, "--create-namespace"
    ]
    if values_file:
        cmd.extend(["-f", values_file])
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    # Example usage: fill in your values
    deploy_helm_app(
        release_name="hello-app",
        chart_path="../apps/helm-chart",
        namespace="default",
        values_file="../apps/helm-chart/values.yaml"
    )
