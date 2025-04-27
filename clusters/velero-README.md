# Disaster Recovery: Velero Backup & Restore

[Velero](https://velero.io/) enables backup, restore, and migration of Kubernetes resources and persistent volumes.

## Steps
1. Deploy Velero via Helm using the provided `velero-helm-values.yaml`:
   ```sh
   helm repo add vmware-tanzu https://vmware-tanzu.github.io/helm-charts
   helm install velero vmware-tanzu/velero -f velero-helm-values.yaml --namespace velero --create-namespace
   ```
2. Trigger a backup:
   ```sh
   velero backup create demo-backup --include-namespaces default
   ```
3. Restore to any cluster:
   ```sh
   velero restore create --from-backup demo-backup
   ```

---

For multi-cloud DR, configure Velero in each cluster and use a shared or replicated object storage bucket accessible from all clouds.
