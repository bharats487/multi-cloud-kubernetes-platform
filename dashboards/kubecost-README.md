# Kubecost Cost Optimization Dashboard

Deploy [Kubecost](https://kubecost.com/) to monitor and optimize Kubernetes spend across clusters.

## Steps
1. Deploy Kubecost via Helm using the provided `kubecost-helm-values.yaml` file.
   ```sh
   helm repo add kubecost https://kubecost.github.io/cost-analyzer/
   helm install kubecost kubecost/cost-analyzer -f kubecost-helm-values.yaml
   ```
2. Access the Kubecost dashboard via the service endpoint.
3. Aggregate cost data from multiple clusters for a global view.

---

For advanced usage, see [Kubecost multi-cluster docs](https://docs.kubecost.com/install-and-configure/multi-cluster-aggregation).
