# EDS Infrastructure & Documentation Audit

**Date:** 2026-03-27
**Scope:** Azure infrastructure, SQL Server databases, Kubernetes clusters, Elasticsearch, codebase configuration
**Method:** Live infrastructure discovery via Azure CLI, kubectl, SQL queries, curl, and file system inspection — compared against all documentation in `/docs/`, `CLAUDE.md`, and config files

---

## Table of Contents

- [Critical Discrepancies](#critical-discrepancies)
- [Azure Infrastructure — Undocumented Resources](#azure-infrastructure--undocumented-resources)
- [Azure Infrastructure — Inaccurate Documentation](#azure-infrastructure--inaccurate-documentation)
- [Azure Security Concerns](#azure-security-concerns)
- [SQL Server — Undocumented Databases](#sql-server--undocumented-databases)
- [SQL Server — Object Count Discrepancies](#sql-server--object-count-discrepancies)
- [Kubernetes — Discrepancies](#kubernetes--discrepancies)
- [Elasticsearch — Discrepancies](#elasticsearch--discrepancies)
- [Frontend & Codebase — Incorrect Documentation](#frontend--codebase--incorrect-documentation)
- [Environment Variables — Undocumented](#environment-variables--undocumented)
- [Recommended Actions](#recommended-actions)

---

## Critical Discrepancies

High-impact errors that would actively mislead a developer or operator.

| # | Issue | Documentation Says | Reality |
|---|-------|-------------------|---------|
| 1 | **ES production index** | `pricing_consolidated_53` (api/search.py default) / `pricing_consolidated_51` (.env.example) | Both are **empty (0 docs)**. Active index is `pricing_consolidated_60` (18.6M docs, 73.2 GB) |
| 2 | **ES version mismatch** | docker-compose.yml uses ES 8.17.0 | Production runs **ES 7.15.2** — major version incompatibility |
| 3 | **Frontend entry point** | `alpine-requisition.html` | File does not exist. Actual entry point is `index.html` |
| 4 | **JS directory structure** | `js/stores/` subdirectory with named stores | Directory does not exist. 18 flat JS files in `js/` |
| 5 | **API client file** | `js/api.js` | File does not exist. Actual file is `js/api-client.js` |
| 6 | **API endpoint count** | "90+ endpoints across 14 route modules" | ~69 endpoints (63 in routes + 6 in main.py) |
| 7 | **Tailwind CSS** | "Tailwind-based component styles" / "EDS brand colors defined in Tailwind config" | No `tailwind.config.js` exists. CSS is hand-written in `design-system.css` |
| 8 | **Elasticsearch undocumented** | Not mentioned in CLAUDE.md architecture section | Fully integrated production service (254-line client, search routes, docker service, admin endpoints) |
| 9 | **App gateway SSL policy** | Not documented | `edsWebRouter` uses **2015 SSL policy** (outdated, insecure) |
| 10 | **Storage account TLS** | Not documented | `stidiqtfstate` uses **TLS 1.0** (security vulnerability) |

---

## Azure Infrastructure — Undocumented Resources

**502 total Azure resources** across **31 resource groups**. Documentation covers only 2 resource groups (`eds-prod-rg`, `eds-uat-rg`).

### Resource Groups (27 undocumented)

Notable undocumented groups:
| Resource Group | Location | Contents |
|----------------|----------|----------|
| `eastus2-edsiq` | eastus2 | Terraform state storage (`tfstateedsiq`) |
| `eastus2-edsiq-aks` | eastus2 | Empty resource group |
| `eastus2-pdp`, `eastus2-pdp-aks` | eastus2 | PDP application environment |
| `eds-wp-prod_group` | eastus | WordPress production hosting |
| `eds-uat-b2c` | eastus | B2C authentication for UAT |
| `eds-prod-rg-asr` | southcentralus | Azure Site Recovery disaster recovery |
| `nodeindexer-uat_group` | eastus2 | UAT node indexer |
| `rg-idiq-tfstate` | eastus2 | IDIQ Terraform state |
| `Kali` | eastus2 | Security testing VM |
| `AIFoundry` | eastus2 | AI/ML workspace |

### Virtual Machines (14 total, most undocumented)

| VM Name | Size | Purpose | Documented? |
|---------|------|---------|-------------|
| SQL-Server | — | Primary SQL Server | Partially (referenced by hostname) |
| EDS-ES | — | Elasticsearch server | In memory file only |
| eds-WebRouter | Standard_D4as_v4 | Web routing/reverse proxy | No |
| eds-Tomcat8 | Standard_D4as_v4 | Tomcat Java app server | No |
| eds-Monitor | Standard_D4as_v4 | Monitoring | No |
| eds-ASP | Standard_B2ms | ASP.NET application server | No |
| EDSIQ-CF | Standard_E2bds_v5 | EDSIQ ColdFusion server | No |
| eds-lucee-InstructionPacks | Standard_B2s | Lucee/CFML for instruction packs | No |
| eds-AVD2-0 | Standard_D4as_v4 | Azure Virtual Desktop | No |
| eds-AVDB-0 | Standard_B4ms | Azure Virtual Desktop (B pool) | No |
| eds-AVDB-1 | Standard_D4as_v4 | Azure Virtual Desktop (B pool) | No |
| eds-AVDH-0 | Standard_D4as_v4 | Azure Virtual Desktop (H pool) | No |
| eds-AVDH-1 | Standard_D4as_v4 | Azure Virtual Desktop (H pool) | No |
| eds-AVDH-2 | Standard_D4as_v4 | Azure Virtual Desktop (H pool) | No |

**6 Azure Virtual Desktop VMs** are completely undocumented.

### Container Registries (3, all undocumented)

| Registry | Login Server | SKU | Admin Enabled |
|----------|-------------|-----|---------------|
| edsProdAKSRegistry | edsprodaksregistry.azurecr.io | Standard | Yes |
| edsaksregistry | edsaksregistry.azurecr.io | Standard | No |
| edscr | edscr.azurecr.io | Standard | Yes |

No documentation specifies which is the primary/active registry.

### Storage Accounts (16, all undocumented)

Key accounts:
| Account | Resource Group | Purpose |
|---------|---------------|---------|
| edscdn | eds-prod-rg | CDN storage |
| edsapp | eds-prod-rg | App storage (geo-replicated) |
| edsdbprodstorage | eds-prod-rg | DB storage (Premium, Data Lake enabled) |
| edsdbprodstorage2 | eds-prod-rg | Secondary DB storage |
| potransmitter | eds-prod-rg | PO transmitter data |
| eastus2edsiq | eds-prod-rg | EDSIQ application storage |
| eastus2pdp | eds-prod-rg | PDP storage |
| tfstateedsiq | eastus2-edsiq | Terraform state |
| stidiqtfstate | rg-idiq-tfstate | IDIQ Terraform state (**TLS 1.0!**) |

### Key Vaults (11, all undocumented)

7 in prod, 4 in UAT. Notable: `kv-districtmanager-uat` is in `eds-prod-rg` instead of `eds-uat-rg` — possible misplacement.

### Networking (undocumented)

| Resource Type | Count | Details |
|--------------|-------|---------|
| Application Gateways | 3 | `eds-web-router-prod`, `edsWebRouter` (legacy, 2015 SSL), `eds-web-router-uat` |
| VPN Gateways | 2 | `eds-NJ-Gateway` (site-to-site to NJ office), `eds-prod-vpn-gateway` (active-active with BGP) |
| DNS Zones | 3 | `ed-data-app.com`, `ed-data-uat.com`, `mail.edsuat.com` |

### Other Undocumented Resources

- **Automation Accounts:** `eds-automation` (prod), `eds-automation-uat`
- **Recovery Services Vault:** VM backup vault
- **Site Recovery:** Disk replicas for 7 VMs in South Central US
- **WordPress Stack:** 2 web apps, MySQL Flexible Server, Azure Front Door CDN

---

## Azure Security Concerns

| # | Issue | Severity | Details |
|---|-------|----------|---------|
| 1 | **TLS 1.0 on storage account** | HIGH | `stidiqtfstate` uses MinimumTlsVersion TLS 1.0 — all others use TLS 1.2 |
| 2 | **Outdated SSL policy on app gateway** | HIGH | `edsWebRouter` uses `AppGwSslPolicy20150501` (2015) vs `20220101` on others |
| 3 | **ES exposed without auth** | HIGH | Elasticsearch at 20.122.81.233:9200 is unauthenticated, no TLS, public IP |
| 4 | **ACR admin enabled** | MEDIUM | 2 of 3 container registries have admin access enabled |
| 5 | **Duplicate app gateway** | MEDIUM | Two app gateways in prod — older one may be legacy/redundant |

---

## SQL Server — Undocumented Databases

The server hosts **26 databases** (22 user + 4 system). CLAUDE.md documents only **2** (EDS and dpa_EDSAdmin).

### Production/Business Databases (undocumented)

| Database | Size | Tables | Views | Procs | Purpose |
|----------|------|--------|-------|-------|---------|
| **Catalogs** | 224 GB | 25 | 0 | 45 | Production catalog data |
| **VendorBids** | 109 GB | 41 | 23 | 72 | Vendor bidding system |
| **VendorBids_TEST** | 99 GB | 41 | 23 | 72 | VendorBids test copy |
| **SearchData** | 92 GB | 9 | 0 | 1 | Search index data |
| **SearchData_Test** | 92 GB | 9 | 0 | 1 | SearchData test copy |
| **ContentCentral** | 56 GB | 134 | 7 | 0 | Content/document management |
| **WorkTables** | 31 GB | 264 | 0 | 0 | Work/staging data |
| **Documents** | 6.8 GB | 39 | 15 | 12 | Document storage |
| **NJ_RTK** | 256 MB | 9 | 6 | 3 | NJ Right to Know data |
| **ProcurementAnalytics** | 144 MB | 13 | 0 | 0 | New (created 2026-03-13) |
| **IDIQ_Platform** | 80 MB | 0 | 0 | 0 | Empty (created 2026-02-26) |
| **IDIQ_Platform_UAT** | 144 MB | 98 | 0 | 0 | IDIQ UAT (created 2026-02-26) |

### Test/Dev Databases (undocumented)

| Database | Size | Notes |
|----------|------|-------|
| **EDS_Test** | 1.22 TB | Full test copy of EDS |
| **EDS_TEST_Old** | 1.12 TB | Older test copy |
| **test** | 80 MB | Empty test DB |
| **work** | 16 MB | Single-table workspace |
| **DeletedPOs** | 16 MB | Deleted PO archive |

### Infrastructure Databases (undocumented)

| Database | Size | Notes |
|----------|------|-------|
| **SolarWindsOrion** | 346 MB | SolarWinds monitoring |
| **hMailServer** | 16 MB | Mail system |
| **hMailServerNew** | 16 MB | Updated mail system |

### SQL Server Details

| Property | Documented | Actual |
|----------|-----------|--------|
| Edition | SQL Server 2017 Developer Edition | **Match** — SQL Server 2017 (RTM-CU31-GDR) Developer Edition (64-bit) |
| Version | Not specified | 14.0.3520.4, CU31-GDR (Feb 2026 patch) |
| OS | Not specified | Windows Server 2022 Datacenter (Hypervisor) |
| Machine Name | Not specified | SQL-Server |

---

## SQL Server — Object Count Discrepancies

### EDS Database Objects

| Object Type | Documented (CLAUDE.md) | Actual (Live) | Delta |
|-------------|----------------------|---------------|-------|
| **Tables** | 438 | **439** | +1 (`DistrictNoteType`, created 2026-03-05) |
| **Views** | 474 | **475** | +1 (`vw_ReqTotalsByVendor_TEST`, created 2026-03-04) |
| **Stored Procedures** | 395 | **396** | +1 (`usp_CheckVendorComplianceForPOs`, created 2026-01-23) |
| **Functions** | Not documented | **232** | N/A |
| **Triggers** | 52 | **59** | **+7** (includes view-based INSTEAD OF triggers + `trig_VendorUpdate`) |
| **Indexes** | 815 | **1,115** | **+300** (37% increase, EDS_INDEXES.md is significantly stale) |
| **Columns** | 4,638 | **11,510** | **+6,872** (data dictionary covers <50% of actual columns) |
| **Foreign Keys** | 31 | **31** | Match |

### Index Count Discrepancy Detail

| Source | Count | Notes |
|--------|-------|-------|
| Actual (live query) | 1,115 | 345 clustered + nonclustered |
| EDS_SUMMARY.md | 1,113 | Close to actual |
| CLAUDE.md / SCHEMA.md / EDS_INDEXES.md | 815 | **300 behind** — likely excluded system/filtered indexes |

### Column Count Discrepancy Detail

The data dictionary (`EDS_DATA_DICTIONARY.md`) documents 4,638 columns but the database contains 11,510. The dictionary appears to have been generated with filters or has not been refreshed since many schema changes. This is the largest documentation gap.

### EDS Database Size Growth

| Metric | Documented (Jan 2026) | Actual (Mar 2026) | Delta |
|--------|----------------------|-------------------|-------|
| Data Size | ~1.19 TB | **~1.48 TB** | **+240 GB (20% growth in 2 months)** |

### Recently Created/Modified Objects (since 2026-01-01)

**56 objects** modified in 2026. Key additions:
- **Table:** `DistrictNoteType` (Mar 5), `Vendors` (Jan 22, recreated)
- **View:** `vw_ReqTotalsByVendor_TEST` (Mar 4)
- **Procedure:** `usp_CheckVendorComplianceForPOs` (Jan 23)
- **Function:** `uf_IsRequisitionLocked2` (Feb 19)
- **Trigger:** `trig_VendorUpdate` (Jan 22)

**Modified today (2026-03-27):** `DMSVendorDocuments`, `DMSVendorBidDocuments` and their triggers.

---

## Kubernetes — Discrepancies

### Version

| Cluster | Documented | Actual |
|---------|-----------|--------|
| eds-aks-prod | 1.32.10 | **1.32.11** |
| eds-aks-uat | 1.32.10 | **1.32.11** |

### Node Counts

Node counts **match** documentation: 13 prod (8 Linux, 5 Windows), 12 UAT (7 Linux, 5 Windows).

Both clusters have an **undocumented `sdsindex2` node pool** (Standard_D8as_v5, Linux) scaled to 0 nodes.

### Undocumented Deployments & Services

**Production:**
| Namespace | Resource | Type | Details |
|-----------|----------|------|---------|
| `eds-cron` | `cron-nodeindexer-index-data` | CronJob | Daily at 7 AM UTC. Entire namespace undocumented. |
| `eds-java-service` | `eds-vendorpos` | Service (LB) | External IP 20.72.71.253. No visible deployment — potentially orphaned. |
| `eds-sds` | `sds-index-builder-2` | Service (LB) | External IP 9.169.181.204. Second index builder, undocumented. |
| `eds-vendorbids` | `eds-vendorbids-download-handler` | Service (LB) | External IP 4.152.74.36. Undocumented. |

**UAT:**
| Namespace | Resource | Type | Details |
|-----------|----------|------|---------|
| `idiq-uat` | `uat-idiq-app` | Deployment | 2/2 replicas. Docs said "no deployments yet." |
| `idiq-uat` | `uat-idiq-redis` | Deployment | 1/1 replica. Redis backing store for IDIQ. |
| `idiq-uat` | `uat-idiq-ingress` | Ingress | Host: `idiq.ed-data-uat.com` |
| `eds-web-app` | `cron-check-system-logs` | CronJob | Hourly. Undocumented. |

### Stale Documentation

`idiq-uat` described as "13 days old, no deployments yet" — now 35 days old with **active workloads**.

---

## Elasticsearch — Discrepancies

### Version Mismatch

| Location | ES Version |
|----------|-----------|
| Production VM (20.122.81.233) | **7.15.2** |
| docker-compose.yml (local dev) | **8.17.0** |

ES 8.x has breaking changes from 7.x (security defaults, API changes). Local dev could mask compatibility issues.

### Active Index Problem

All code defaults point to **empty indices**:

| File | Default Index | Doc Count |
|------|--------------|-----------|
| `api/search.py` (line 23) | `pricing_consolidated_53` | **0 (empty)** |
| `.env.example` (line 25) | `pricing_consolidated_51` | **0 (empty)** |
| Memory doc | `pricing_consolidated_51` | **0 (empty)** |
| **Actual active index** | `pricing_consolidated_60` | **18,633,822 docs (73.2 GB)** |

Any deployment using default settings would query an empty index and return zero results.

### Full Index Inventory (44 indices total)

| Index | Docs | Size | Notes |
|-------|------|------|-------|
| `pricing_consolidated_uat_2` | 30.3M | 106.2 GB | UAT, has data |
| `pricing_consolidated_60` | 18.6M | 73.2 GB | **Production active** |
| `pi_autocomplete_uat_active_*` | 48.2M | 14.9 GB | UAT autocomplete |
| `pi_autocomplete_prod_active_*` | 15.9M | 5.5 GB | Prod autocomplete |
| `sds_v12` | 2.7M | 7.1 GB | Safety data sheets (latest) |
| `sds-uat-v22` | 2.3M | 4.5 GB | SDS UAT |
| `sds_v3` through `sds_v11` | varies | ~10 GB | SDS older versions (cleanup candidates) |
| `pricing_consolidated_51` | **0** | 208 B | Empty |
| `pricing_consolidated_53` | **0** | 208 B | Empty |
| `query_completion` / `_v3` | 2K–20K | ~10 MB | Query suggestions |

**Undocumented index types:** SDS indices, autocomplete indices, query completion indices.

### Cluster Health

- **Status:** Yellow (expected for single-node — 61 unassigned replica shards)
- **Security:** No authentication, no TLS, public IP

---

## Frontend & Codebase — Incorrect Documentation

### Frontend File Structure

| CLAUDE.md Claims | Actual |
|-----------------|--------|
| `alpine-requisition.html` — Main app entry point | **Does not exist.** Entry point is `index.html` |
| `js/stores/` — Alpine stores directory | **Does not exist.** Flat structure in `js/` |
| `js/api.js` — API client | **Does not exist.** Actual file is `js/api-client.js` |
| "Tailwind-based component styles" | No `tailwind.config.js` exists. CSS in `design-system.css` |

**Actual HTML files:** `index.html`, `login.html`, `checkout.html`, `product-detail.html`

**Actual JS files (18):** `api-client.js`, `app.js`, `approvals.js`, `auth-guard.js`, `auth.js`, `autocomplete.js`, `browse.js`, `cart.js`, `checkout.js`, `config.js`, `dashboard.js`, `login.js`, `orders.js`, `product-detail.js`, `product-helpers.js`, `reports.js`, `saved-lists.js`, `ui.js`

### Test Structure

CLAUDE.md lists ~11 test files. Actual: **24 test files**.

Undocumented test files:
- `tests/api/`: `test_ai_chat.py`, `test_ai_search.py`, `test_dashboard.py`, `test_reports.py`
- `tests/e2e/`: `test_approval_workflow.py`, `test_cart_workflow.py`, `test_checkout_workflow.py`, `test_critical_flows.py`, `test_login_workflow.py`, `test_product_browsing.py`, `test_requisition_listing.py`, `test_visual_regression.py`
- `tests/`: `test_config.py`, `test_db_utils.py`, `test_deploy_indexes.py`, `test_investigate_blocking.py`, `test_recursive_procedures.py`

### Docker Services

CLAUDE.md lists 2 services. Actual: **3 services** (frontend, api, **elasticsearch** — undocumented).

### pyproject.toml

**Undocumented optional dependency groups:** `dashboard` (Streamlit), `export` (openpyxl), `gui` (nicegui, pywebview), `build` (pyinstaller), `all` (meta-group)

**Undocumented dependencies in `api` extra:** `elasticsearch[async]>=8.12.0`, `ollama>=0.4.0`

**Undocumented entry points:** `eds-agent-gui`, 10 monitoring script entry points

### Scheduled Tasks

`annual-vendor-table-refresh` referenced in CLAUDE.md as running "each December 15" — **no implementation exists** (no script, no cron job, no GitHub Action).

### CI/CD

`deploy.yml` GitHub Action is a **stub** with placeholder comments but `docs/CI_CD.md` presents it as a functional pipeline.

---

## Environment Variables — Undocumented

CLAUDE.md documents ~9 env vars. `.env.example` contains **20+**. Undocumented variables:

| Variable | Purpose |
|----------|---------|
| `LLM_PROVIDER` | AI provider (claude, ollama, openai) |
| `ANTHROPIC_API_KEY` | Claude API key |
| `OLLAMA_HOST` | Ollama server URL |
| `ES_ENABLED` | Elasticsearch toggle |
| `ES_URL` | Elasticsearch URL |
| `ES_INDEX` | Elasticsearch index name |
| `API_BASE_URL` | Frontend config |
| `BUDGET_LIMIT` | Frontend budget limit |
| `FRONTEND_PORT` | Docker compose port |
| `API_PORT` | Docker compose port |
| `ES_PORT` | Docker compose port |
| `DB_POOL_MIN` / `DB_POOL_MAX` | Connection pool settings |
| `DB_CONNECTION_TIMEOUT` | DB connection timeout |
| `DB_DRIVER` | ODBC driver name |
| `DB_TRUST_CERT` | Trust server certificate |
| `LOG_LEVEL` | Logging level |

---

## Recommended Actions

### Priority 1 — Security (Immediate)

1. **Fix TLS 1.0 on `stidiqtfstate`** — Upgrade to TLS 1.2:
   ```bash
   az storage account update --name stidiqtfstate --min-tls-version TLS1_2
   ```
2. **Update `edsWebRouter` SSL policy** from `AppGwSslPolicy20150501` to `AppGwSslPolicy20220101`
3. **Secure Elasticsearch** — Add authentication and TLS, or restrict to private IP

### Priority 2 — Critical Documentation Fixes

4. **Fix ES index references** — Update `api/search.py`, `.env.example` to `pricing_consolidated_60`
5. **Fix CLAUDE.md frontend section** — Replace `alpine-requisition.html` → `index.html`, `js/stores/` → flat structure, `js/api.js` → `js/api-client.js`
6. **Remove Tailwind claims** — Replace with actual CSS architecture (`design-system.css`)
7. **Add Elasticsearch to architecture** — Document as a core production service
8. **Fix endpoint count** — Change "90+" to "~69"
9. **Fix trigger count** — Change 52 to 59
10. **Update K8s version** — Change 1.32.10 to 1.32.11

### Priority 3 — Documentation Gaps

11. **Create database inventory** — Document all 22 user databases
12. **Create Azure infrastructure inventory** — VMs, storage accounts, key vaults, ACRs, networking
13. **Regenerate data dictionary** — Current covers <50% of actual columns (4,638 vs 11,510)
14. **Update EDS_INDEXES.md** — 300 indexes added since documentation (815 → 1,115)
15. **Update test structure** — Reflect 24 actual test files
16. **Document all env vars** — Add 15+ missing variables to CLAUDE.md
17. **Update IDIQ UAT status** — Now has active deployments
18. **Document `eds-cron` namespace** — Contains daily `cron-nodeindexer-index-data` job

### Priority 4 — Cleanup Opportunities

19. **Investigate orphaned `eds-vendorpos` service** — Has public IP LoadBalancer but no visible deployment
20. **Evaluate 3 container registries** — Consolidate to one, disable admin on remaining
21. **Evaluate duplicate app gateway** — `edsWebRouter` (legacy) vs `eds-web-router-prod`
22. **Clean empty ES indices** — `pricing_consolidated_51`, `_53` (0 docs, 208 bytes each)
23. **Clean old SDS indices** — `sds_v3` through `sds_v7` (superseded by `sds_v12`)
24. **Review test databases** — `EDS_Test` (1.22 TB) and `EDS_TEST_Old` (1.12 TB) consuming 2.3 TB
25. **Delete empty resource groups** — `eastus2-edsiq-aks`, `eds-uat-b2c`
26. **Implement or remove** `annual-vendor-table-refresh` scheduled task reference

---

*Generated by automated infrastructure audit on 2026-03-27. All findings verified against live systems via Azure CLI, kubectl, SQL queries, curl, and file system inspection.*
