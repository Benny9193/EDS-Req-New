# EDS Kubernetes Cluster Documentation

**Last Updated:** 2026-03-05
**Subscription:** Pay-As-You-Go (65c7cd1b-21ee-4be1-a85c-b72c5dfb12f0)
**Tenant:** EDUCATIONAL DATA SERVICES (ed-data.com)
**Kubernetes Version:** 1.32.11 (both clusters)
**Region:** East US 2

---

## Cluster Overview

| Cluster | Resource Group | FQDN | Nodes | Purpose |
|---------|---------------|------|-------|---------|
| eds-aks-prod | eds-prod-rg | eds-aks-prod-dns-aredx0ow.hcp.eastus2.azmk8s.io | 13 | Production |
| eds-aks-uat | eds-uat-rg | eds-aks-uat-dns-nzj3vjnd.hcp.eastus2.azmk8s.io | 12 | UAT / Staging |

### Quick Access

```bash
# Switch contexts
kubectx eds-aks-prod       # Production
kubectx eds-aks-uat        # UAT

# Switch namespace
kubens eds-web-app         # Example
```

---

## Node Pools

### Production Cluster (eds-aks-prod) - 13 Nodes

#### Linux Nodes (8)

| Node Pool | VM Size | vCPUs | Memory | OS | Node Count | Purpose |
|-----------|---------|-------|--------|----|------------|---------|
| admin | Standard_B2ms | 2 | 8 GiB | Azure Linux 3.0 | 1 | Admin portal |
| agentpool | Standard_B4ms | 4 | 16 GiB | Ubuntu 22.04 | 1 | System (CriticalAddonsOnly taint) |
| lucee | Standard_B4ms | 4 | 16 GiB | Ubuntu 22.04 | 2 | Lucee/CFML web apps (EDS-IQ, DMS) |
| po | Standard_B4ms | 4 | 16 GiB | Ubuntu 22.04 | 1 | Purchase orders |
| querylite | Standard_D4as_v5 | 4 | 16 GiB | Ubuntu 22.04 | 1 | Query Lite |
| sds | Standard_B4ms | 4 | 16 GiB | Ubuntu 22.04 | 1 | SDS application |
| sdsindex | Standard_D4s_v3 | 4 | 16 GiB | Ubuntu 22.04 | 1 | SDS index builders |

#### Windows Nodes (5)

| Node Pool | VM Size | vCPUs | Memory | OS | Node Count | Purpose |
|-----------|---------|-------|--------|----|------------|---------|
| noinde | Standard_D8s_v3 | 8 | 32 GiB | Windows Server 2022 | 1 | Node indexer |
| w2022 | Standard_B4ms | 4 | 16 GiB | Windows Server 2022 | 4 | Java services, vendor bids, ASP.NET |

### UAT Cluster (eds-aks-uat) - 12 Nodes

#### Linux Nodes (7)

| Node Pool | VM Size | vCPUs | Memory | OS | Node Count | Purpose |
|-----------|---------|-------|--------|----|------------|---------|
| admin | Standard_B2ms | 2 | 8 GiB | Ubuntu 22.04 | 1 | Admin portal |
| agent | Standard_D4s_v3 | 4 | 16 GiB | Azure Linux 3.0 | 1 | System / general workloads |
| lucee | Standard_B4ms | 4 | 16 GiB | Ubuntu 22.04 | 1 | Lucee/CFML web apps |
| po | Standard_B4ms | 4 | 16 GiB | Ubuntu 22.04 | 1 | Purchase orders |
| querylite | Standard_D4as_v5 | 4 | 16 GiB | Ubuntu 22.04 | 1 | Query Lite |
| sds | Standard_B2ms | 2 | 8 GiB | Ubuntu 22.04 | 1 | SDS application |
| sdsindex | Standard_B2ms | 2 | 8 GiB | Ubuntu 22.04 | 1 | SDS index builders |

#### Windows Nodes (5)

| Node Pool | VM Size | vCPUs | Memory | OS | Node Count | Purpose |
|-----------|---------|-------|--------|----|------------|---------|
| noinde | Standard_D8s_v3 | 8 | 32 GiB | Windows Server 2022 | 1 | Node indexer |
| w2022 | Standard_B4ms | 4 | 16 GiB | Windows Server 2022 | 4 | Java services, vendor bids, ASP.NET |

### Key Differences: Prod vs UAT Node Sizing

| Pool | Prod VM | UAT VM | Notes |
|------|---------|--------|-------|
| agentpool/agent | Standard_B4ms | Standard_D4s_v3 | UAT uses D-series (consistent perf) |
| lucee | B4ms x2 | B4ms x1 | Prod has 2x Lucee nodes for HA |
| sds | Standard_B4ms | Standard_B2ms | UAT half the resources |
| sdsindex | Standard_D4s_v3 | Standard_B2ms | UAT significantly smaller |

---

## Resource Utilization (Snapshot: 2026-03-05)

### Production

| Node | Pool | CPU Used | CPU% | Memory Used | Memory% |
|------|------|----------|------|-------------|---------|
| aks-admin-... | admin | 128m | 6% | 2,142 Mi | 29% |
| aks-agentpool-... | agentpool | 358m | 9% | 4,247 Mi | 27% |
| aks-lucee-...000 | lucee | 324m | 8% | 5,187 Mi | 34% |
| aks-lucee-...006 | lucee | 420m | 10% | 6,118 Mi | 40% |
| aks-po-... | po | 337m | 8% | 3,350 Mi | 21% |
| aks-querylite-... | querylite | 189m | 4% | 3,302 Mi | 21% |
| aks-sds-... | sds | 201m | 5% | 2,467 Mi | 16% |
| aks-sdsindex-... | sdsindex | 365m | 9% | 3,319 Mi | 21% |
| aksnoinde000000 | noinde (Win) | 30m | 0% | 2,216 Mi | 7% |
| aksw2022000000 | w2022 (Win) | 12m | 0% | 2,525 Mi | 18% |
| aksw2022000001 | w2022 (Win) | 16m | 0% | 2,605 Mi | 19% |
| aksw2022000002 | w2022 (Win) | 20m | 0% | 2,441 Mi | 17% |
| aksw2022000005 | w2022 (Win) | 22m | 0% | 4,443 Mi | 32% |
| **Totals** | | **2,422m** | **~6%** | **44,362 Mi** | **~23%** |

### UAT

| Node | Pool | CPU Used | CPU% | Memory Used | Memory% |
|------|------|----------|------|-------------|---------|
| aks-admin-... | admin | 176m | 9% | 3,113 Mi | 43% |
| aks-agent-... | agent | 305m | 7% | 2,501 Mi | 16% |
| aks-lucee-... | lucee | 216m | 5% | 4,781 Mi | 31% |
| aks-po-... | po | 224m | 5% | 3,783 Mi | 24% |
| aks-querylite-... | querylite | 189m | 4% | 3,379 Mi | 22% |
| aks-sds-... | sds | 199m | 10% | 2,801 Mi | 38% |
| aks-sdsindex-... | sdsindex | 184m | 9% | 2,614 Mi | 36% |
| aksnoinde000000 | noinde (Win) | 52m | 0% | 2,735 Mi | 9% |
| aksw2022000009 | w2022 (Win) | 16m | 0% | 2,575 Mi | 18% |
| aksw202200000a | w2022 (Win) | 18m | 0% | 3,557 Mi | 25% |
| aksw202200000b | w2022 (Win) | 13m | 0% | 2,020 Mi | 14% |
| aksw202200000c | w2022 (Win) | 14m | 0% | 2,673 Mi | 19% |
| **Totals** | | **1,606m** | **~5%** | **36,532 Mi** | **~23%** |

---

## Application Workloads

### Production Deployments

| Namespace | Deployment | Replicas | Node Pool | Service Type | External IP |
|-----------|-----------|----------|-----------|-------------|-------------|
| eds-web-app | eds-edsiq | 1/1 | lucee | LoadBalancer | 52.251.10.10 |
| eds-web-app | eds-edsiq-2 | 1/1 | lucee | LoadBalancer | 4.153.197.31 |
| eds-web-app | eds-dms | 1/1 | lucee | LoadBalancer | 20.10.230.104 |
| eds-web-asp | eds-edsiq-asp | 1/1 | w2022 (Win) | LoadBalancer | 20.96.100.30 |
| eds-admin-portal | eds-admin-portal | 1/1 | admin | LoadBalancer | 4.153.107.44 |
| eds-po | eds-po | 1/1 | po | LoadBalancer | 52.177.80.178 |
| eds-querylite | eds-querylite | 1/1 | querylite | LoadBalancer | 172.193.27.238 |
| eds-sds | eds-sds | 1/1 | sds | LoadBalancer | 4.153.101.19 |
| eds-sds | sds-index-builder | 3/3 | sdsindex | LoadBalancer | 4.153.191.95 |
| eds-vendorbids | eds-vendorbids | 1/1 | w2022 (Win) | LoadBalancer | 4.152.73.254 |
| eds-database | eds-nodeindexer | 1/1 | noinde (Win) | LoadBalancer | 172.175.208.125 |
| eds-java-service | eds-documentviewer | 1/1 | w2022 (Win) | LoadBalancer | 20.186.83.121 |
| eds-java-service | eds-export-handler | 1/1 | w2022 (Win) | LoadBalancer | 52.247.77.47 |
| eds-java-service | eds-potransmitter | 1/1 | w2022 (Win) | LoadBalancer | 4.152.239.185 |
| eds-java-service | eds-report-handler | 1/1 | w2022 (Win) | LoadBalancer | 20.96.132.103 |

### UAT Deployments

| Namespace | Deployment | Replicas | Node Pool | Service Type | External IP |
|-----------|-----------|----------|-----------|-------------|-------------|
| eds-web-app | eds-edsiq | 1/1 | lucee | LoadBalancer | 4.153.172.224 |
| eds-web-asp | eds-edsiq-asp | 1/1 | w2022 (Win) | LoadBalancer | 4.153.129.215 |
| eds-admin-portal | eds-admin-portal | 1/1 | admin | LoadBalancer | 4.153.87.17 |
| eds-po | eds-po | 1/1 | po | LoadBalancer | 52.177.250.87 |
| eds-querylite | eds-querylite | 1/1 | querylite | LoadBalancer | 52.252.20.246 |
| eds-sds | eds-sds | 1/1 | sds | LoadBalancer | 52.254.118.52 |
| eds-sds | sds-index-builder | 1/1 | sdsindex | LoadBalancer | 20.57.107.111 |
| eds-vendorbids | eds-vendorbids | 1/1 | w2022 (Win) | LoadBalancer | 4.152.97.9 |
| eds-database | eds-nodeindexer | 1/1 | noinde (Win) | LoadBalancer | 20.161.211.247 |
| eds-java-service | eds-documentviewer | 1/1 | w2022 (Win) | LoadBalancer | 52.254.30.172 |
| eds-java-service | eds-potransmitter | 0/0 | - | LoadBalancer | 20.161.214.96 |
| eds-java-service | eds-report-handler | 1/1 | w2022 (Win) | LoadBalancer | 4.153.244.35 |
| districtmanager-uat | districtmanager-backend | 1/1 | agent | ClusterIP | (internal) |
| districtmanager-uat | districtmanager-frontend | 1/1 | agent | ClusterIP | (internal) |
| districtmanager-uat | ingress-nginx-controller | 1/1 | agent | LoadBalancer | 20.15.60.5 |

### UAT-Only Namespaces
- **districtmanager-uat** - District Manager app with nginx ingress (deployed 55 days ago)
- **idiq-uat** - IDIQ platform with active workloads:
  - `uat-idiq-app` (2 replicas) — IDIQ application
  - `uat-idiq-redis` (1 replica) — Redis backing store
  - `uat-idiq-ingress` — Ingress at `idiq.ed-data-uat.com`

### Cron Jobs

**eds-cron namespace (prod):**
- **cron-nodeindexer-index-data** — Daily at 7 AM UTC, node indexer data refresh

**eds-sds namespace:**
- **cron-sync-sds** - SDS sync cron job
  - Prod: 5 recent jobs, all **Running**
  - UAT: 5 recent jobs, all **Pending** (stuck on Windows node `aksnoinde000000`)

**eds-web-app namespace (uat):**
- **cron-check-system-logs** — Hourly system log check

---

## Networking

### IP Ranges

| Cluster | VNet CIDR | Service CIDR |
|---------|-----------|-------------|
| Prod | 10.224.0.0/16 | 10.0.0.0/16 |
| UAT | 172.16.0.0/16 | 10.0.0.0/16 |

### Network Policies
- **Calico** (Tigera) installed on both clusters for network policy enforcement
- **Gatekeeper** (OPA) installed on both clusters for admission control

### Ingress
- **Prod**: All services use individual LoadBalancer IPs (no shared ingress controller)
- **UAT**: Same pattern, except `districtmanager-uat` uses an nginx ingress controller with a single LoadBalancer IP (20.15.60.5)
- **UAT** also has `app-routing-system` namespace with nginx (AKS managed add-on)

---

## System Components

Both clusters run these system-level workloads:

| Component | Purpose |
|-----------|---------|
| Calico + Tigera Operator | Network policy engine |
| Gatekeeper (OPA) | Admission controller / policy enforcement |
| CoreDNS (autoscaled) | Cluster DNS |
| Azure CNS | Azure Container Networking |
| Azure IP Masq Agent | IP masquerading for pod traffic |
| CSI Azure Disk/File | Persistent volume drivers |
| Konnectivity Agent | API server tunnel |
| Metrics Server | Resource metrics for HPA/kubectl top |
| AMA Logs + Metrics | Azure Monitor agent (logs and Prometheus) |
| Retina Agent | Network observability (Linux + Windows) |
| Azure Policy | Azure Policy integration |
| Cloud Node Manager | Azure cloud provider integration |

### UAT Additional Components
- **Secrets Store CSI Driver** + Azure Key Vault Provider
- **Azure Workload Identity** webhook controller
- **Application Gateway Ingress Controller** (AGIC)
- **Cost Analysis Agent**

---

## Observations & Notes

1. **Low CPU utilization** - Both clusters average ~5-6% CPU. Windows nodes are nearly idle (<1% CPU). Consider right-sizing or consolidating.

2. **UAT cron jobs stuck** - 5 `cron-sync-sds` pods are in `Pending` state on the Windows node `aksnoinde000000`. These may be misconfigured (SDS cron runs on Linux in prod).

3. **UAT potransmitter scaled to 0** - `eds-potransmitter` deployment in UAT is scaled to 0 replicas (intentionally disabled).

4. **Prod has more Lucee capacity** - 2 Lucee nodes vs 1 in UAT. Prod also runs `eds-dms` and `eds-edsiq-2` which don't exist in UAT.

5. **No HPA detected** - All workloads appear to use fixed replica counts. Consider HorizontalPodAutoscaler for variable workloads.

6. **Every service is a LoadBalancer** - Each deployment gets its own public IP. This consumes Azure public IPs and increases attack surface. Consider consolidating behind a shared ingress controller.

7. **No taints on workload nodes** - Only the system `agentpool` node in prod has a `CriticalAddonsOnly` taint. All other nodes accept any pod scheduling.

8. **UAT has newer infra features** - Secrets Store CSI, Workload Identity, AGIC, and Cost Analysis are present in UAT but not prod. Consider rolling these to prod.

9. **Mixed OS images** - Most Linux nodes run Ubuntu 22.04, but `admin` (prod) and `agent` (UAT) run Azure Linux 3.0 (Mariner).
