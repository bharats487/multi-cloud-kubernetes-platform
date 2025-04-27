# Multi-Cloud Load Balancing Example: ExternalDNS

This example shows how to use [ExternalDNS](https://github.com/kubernetes-sigs/external-dns) to automate DNS-based load balancing across clusters in different clouds.

## Steps
1. Deploy ExternalDNS via Helm in each cluster using the provided `external-dns-helm-values.yaml`.
2. Configure your DNS provider (e.g., Route53, CloudDNS, Azure DNS) and update the values file accordingly.
3. Use a shared domain (e.g., `yourdomain.com`) and create DNS records that point to each cluster's load balancer IP.
4. For true multi-cloud failover/load balancing, consider using a global DNS service (e.g., AWS Route53 Latency/Failover records, Cloudflare Load Balancer).

---

**Note:** For advanced multi-cloud traffic management, consider a service mesh (Istio, Linkerd) with multi-cluster support.
