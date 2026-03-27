# Azure Infrastructure

> **Last updated**: 2026-03-27 (infrastructure audit)
>
> EDS runs across **31 resource groups** with **502 total Azure resources** in East US 2 (primary) and South Central US (DR).

---

## Resource Groups

### Documented (Production & UAT)

| Resource Group | Location | Purpose |
|----------------|----------|---------|
| `eds-prod-rg` | eastus2 | Primary production — AKS, VMs, networking, storage |
| `eds-uat-rg` | eastus2 | UAT/staging — AKS cluster, testing workloads |

### Additional Groups

| Resource Group | Location | Purpose |
|----------------|----------|---------|
| `eastus2-edsiq` | eastus2 | EDSIQ Terraform state storage |
| `eastus2-edsiq-aks` | eastus2 | Empty (legacy or planned) |
| `eastus2-pdp` / `eastus2-pdp-aks` | eastus2 | PDP (Procurement Data Platform) environment |
| `eds-wp-prod_group` | eastus | WordPress production hosting |
| `eds-uat-b2c` | eastus | Azure AD B2C authentication for UAT |
| `eds-prod-rg-asr` | southcentralus | Azure Site Recovery (disaster recovery) |
| `nodeindexer-uat_group` | eastus2 | UAT node indexer |
| `rg-idiq-tfstate` | eastus2 | IDIQ Terraform state |
| `Kali` | eastus2 | Security testing VM |
| `AIFoundry` | eastus2 | AI/ML workspace |

---

## Virtual Machines (14)

### Application Servers

| VM Name | Size | Status | Purpose |
|---------|------|--------|---------|
| SQL-Server | — | Running | Primary SQL Server (22 databases, ~4.5 TB) |
| EDS-ES | — | Running | Elasticsearch 7.15.2 (44 indices, ~200 GB) |
| eds-WebRouter | Standard_D4as_v4 | Running | Web routing / reverse proxy |
| eds-Tomcat8 | Standard_D4as_v4 | Running | Tomcat application server |
| eds-Monitor | Standard_D4as_v4 | Running | Monitoring services |

### Deallocated VMs (still incurring disk/IP costs)

| VM Name | Size | Purpose | Action |
|---------|------|---------|--------|
| eds-ASP | Standard_B2ms | Legacy ASP.NET server | Review for deletion |
| EDSIQ-CF | Standard_E2bds_v5 | Legacy EDSIQ ColdFusion server | Review for deletion |
| eds-lucee-InstructionPacks | Standard_B2s | Lucee/CFML instruction packs | Review for deletion |

### Azure Virtual Desktop (6 VMs)

| VM Name | Size | Pool |
|---------|------|------|
| eds-AVD2-0 | Standard_D4as_v4 | Pool 2 |
| eds-AVDB-0 | Standard_B4ms | Pool B |
| eds-AVDB-1 | Standard_D4as_v4 | Pool B |
| eds-AVDH-0 | Standard_D4as_v4 | Pool H |
| eds-AVDH-1 | Standard_D4as_v4 | Pool H |
| eds-AVDH-2 | Standard_D4as_v4 | Pool H |

---

## Kubernetes (AKS)

Two clusters, both Kubernetes **1.32.11**, mixed Linux/Windows node pools:

| Cluster | Resource Group | Nodes | Purpose |
|---------|---------------|-------|---------|
| `eds-aks-prod` | eds-prod-rg | 13 (8 Linux, 5 Windows) | Production |
| `eds-aks-uat` | eds-uat-rg | 12 (7 Linux, 5 Windows) | UAT/staging |

Both clusters have an `sdsindex2` node pool (Standard_D8as_v5, Linux) scaled to 0.

See [`kubernetes-clusters.md`](kubernetes-clusters.md) for full node pool, deployment, and service details.

### Notable K8s Workloads

| Namespace | Resource | Details |
|-----------|----------|---------|
| `eds-cron` (prod) | `cron-nodeindexer-index-data` | Daily at 7 AM UTC |
| `eds-java-service` (prod) | `eds-vendorpos` | External LB @ 20.72.71.253 |
| `eds-sds` (prod) | `sds-index-builder-2` | External LB @ 9.169.181.204 |
| `eds-vendorbids` (prod) | `eds-vendorbids-download-handler` | External LB @ 4.152.74.36 |
| `idiq-uat` (uat) | `uat-idiq-app` | 2 replicas, IDIQ platform |
| `idiq-uat` (uat) | `uat-idiq-redis` | 1 replica, Redis backing store |
| `eds-web-app` (uat) | `cron-check-system-logs` | Hourly system log check |

---

## Container Registries (3)

| Registry | Login Server | SKU | Admin Enabled | Notes |
|----------|-------------|-----|---------------|-------|
| edsProdAKSRegistry | edsprodaksregistry.azurecr.io | Standard | **Yes** | Production images |
| edsaksregistry | edsaksregistry.azurecr.io | Standard | No | Secondary |
| edscr | edscr.azurecr.io | Standard | **Yes** | Tertiary |

> **TODO**: Determine which registry is primary and consolidate if possible. Admin access should be disabled on registries not requiring it.

---

## Networking

### Application Gateways (3)

| Gateway | Purpose | Notes |
|---------|---------|-------|
| `eds-web-router-prod` | Production routing | Current |
| `edsWebRouter` | Legacy routing | **Uses 2015 SSL policy** — upgrade to `20220101` |
| `eds-web-router-uat` | UAT routing | Current |

### VPN Gateways (2)

| Gateway | Type | Purpose |
|---------|------|---------|
| `eds-NJ-Gateway` | Site-to-site | VPN to NJ office |
| `eds-prod-vpn-gateway` | Active-active with BGP | Primary VPN |

### DNS Zones (3)

| Zone | Purpose |
|------|---------|
| `ed-data-app.com` | Production domain |
| `ed-data-uat.com` | UAT domain |
| `mail.edsuat.com` | UAT mail |

### Bastion

- `eds-prod-vnet-bastion` — secure VM access without public IPs

---

## Storage Accounts (16)

### Production

| Account | Resource Group | Purpose | Notes |
|---------|---------------|---------|-------|
| edscdn | eds-prod-rg | CDN static content | |
| edsapp | eds-prod-rg | Application storage | Geo-replicated |
| edsdbprodstorage | eds-prod-rg | DB backups/storage | Premium, Data Lake enabled |
| edsdbprodstorage2 | eds-prod-rg | Secondary DB storage | |
| potransmitter | eds-prod-rg | PO transmitter data | |
| eastus2edsiq | eds-prod-rg | EDSIQ application storage | |
| eastus2pdp | eds-prod-rg | PDP storage | |

### Terraform State

| Account | Resource Group | Purpose | Notes |
|---------|---------------|---------|-------|
| tfstateedsiq | eastus2-edsiq | EDSIQ Terraform state | |
| stidiqtfstate | rg-idiq-tfstate | IDIQ Terraform state | **TLS 1.0 — must upgrade to 1.2** |

---

## Key Vaults (11)

7 in production (`eds-prod-rg`), 4 in UAT (`eds-uat-rg`).

> **Note**: `kv-districtmanager-uat` is located in `eds-prod-rg` instead of `eds-uat-rg` — potential misplacement, review whether it should be moved.

---

## Disaster Recovery / Site Recovery

| Component | Details |
|-----------|---------|
| **Recovery Services Vault** | VM backup vault in `eds-prod-rg` |
| **Site Recovery** | 7 VM disk replicas in South Central US (`eds-prod-rg-asr`) |
| **Target Region** | South Central US |

---

## WordPress Stack

| Resource | Details |
|----------|---------|
| Resource Group | `eds-wp-prod_group` (East US) |
| Web Apps | 2 App Service instances |
| Database | MySQL Flexible Server |
| CDN | Azure Front Door |

---

## Automation

| Account | Resource Group | Key Runbooks |
|---------|---------------|-------------|
| `eds-automation` | eds-prod-rg | NodeIndexer, EDSIQ pod rotation, health checks |
| `eds-automation-uat` | eds-uat-rg | UAT automation |

---

## Security Concerns

| # | Issue | Severity | Details |
|---|-------|----------|---------|
| 1 | TLS 1.0 on storage account | **HIGH** | `stidiqtfstate` — upgrade MinimumTlsVersion to TLS 1.2 |
| 2 | Outdated SSL policy | **HIGH** | `edsWebRouter` uses 2015 policy — upgrade to `AppGwSslPolicy20220101` |
| 3 | ES unauthenticated | **HIGH** | Elasticsearch at 20.122.81.233:9200 has no auth, no TLS, public IP |
| 4 | ACR admin enabled | MEDIUM | 2 of 3 registries have admin access — disable where possible |
| 5 | Duplicate app gateway | MEDIUM | `edsWebRouter` (legacy) may be redundant alongside `eds-web-router-prod` |

---

## Cost Optimization Opportunities

1. **Deallocated VMs** (eds-ASP, EDSIQ-CF, eds-lucee-InstructionPacks) — still paying for managed disks and reserved IPs. Delete if no longer needed.
2. **Empty resource groups** (`eastus2-edsiq-aks`) — clean up.
3. **3 container registries** — consolidate to 1 or 2.
4. **`sdsindex2` node pool** at 0 nodes on both clusters — delete if retired.
