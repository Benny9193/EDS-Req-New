# EDS Infrastructure & Documentation Audit

**Date:** 2026-03-27
**Scope:** Azure infrastructure, SQL Server databases, codebase configuration, external services
**Method:** Automated discovery compared against all documentation in `/docs/`, `CLAUDE.md`, and config files

---

## Table of Contents

- [Critical Discrepancies](#critical-discrepancies)
- [Azure Infrastructure - Undocumented Resources](#azure-infrastructure---undocumented-resources)
- [Azure Infrastructure - Inaccurate Documentation](#azure-infrastructure---inaccurate-documentation)
- [SQL Server - Undocumented Databases](#sql-server---undocumented-databases)
- [SQL Server - Object Count Discrepancies](#sql-server---object-count-discrepancies)
- [External Services - Undocumented or Incorrect](#external-services---undocumented-or-incorrect)
- [Code & Configuration - Missing from Docs](#code--configuration---missing-from-docs)
- [Recommended Actions](#recommended-actions)

---

## Critical Discrepancies

These are high-impact errors that would actively mislead a developer or operator.

| # | Issue | Reality | Docs Say | Affected Files |
|---|-------|---------|----------|----------------|
| 1 | **EDSIQ tech stack** | ColdFusion/Lucee/CFWheels with NGINX | Java/Spring Boot | `docs/wiki/architecture/application-stack.md` |
| 2 | **ES production index** | `pricing_consolidated_60` (18.6M docs, 73.2GB) | `pricing_consolidated_53` (empty, 0 docs) | `api/search.py`, `.env.example`, `docs/API_ROUTES.md` |
| 3 | **Frontend entry point** | `frontend/index.html` | `alpine-requisition.html` (file does not exist) | `CLAUDE.md` |
| 4 | **JS directory structure** | Flat `frontend/js/` directory with 18 individual files | `js/stores/` subdirectory with named stores | `CLAUDE.md` |
| 5 | **API client file** | `js/api-client.js` | `js/api.js` (file does not exist) | `CLAUDE.md` |
| 6 | **API endpoint count** | ~65 endpoints across 14 route modules + main.py | "90+ endpoints across 14 route modules" | `docs/API_ROUTES.md` |

---

## Azure Infrastructure - Undocumented Resources

### Resource Groups (5 undocumented)

| Resource Group | Location | Contents |
|----------------|----------|----------|
| `eastus2-edsiq` | eastus2 | Terraform state storage (`tfstateedsiq`) |
| `eastus2-edsiq-aks` | eastus2 | Empty resource group |
| `eds-wp-prod_group` | eastus | WordPress production hosting (2 web apps, MySQL, CDN, storage) |
| `eds-uat-b2c` | eastus | Empty (no resources) |
| `eds-prod-rg-asr` | southcentralus | Azure Site Recovery disaster recovery replicas for 7 VMs |

### Virtual Machines (10 undocumented in eds-prod-rg)

| VM | Size | OS | State | Purpose |
|----|------|----|-------|---------|
| eds-WebRouter | Standard_D4as_v4 | Windows | Running | Web routing |
| eds-Tomcat8 | Standard_D4as_v4 | Windows | Running | Tomcat application server |
| eds-Monitor | Standard_D4as_v4 | Windows | Running | Monitoring |
| eds-AVD2-0 | Standard_D4as_v4 | Windows | Running | Azure Virtual Desktop |
| eds-AVDB-0 | Standard_B4ms | Windows | Running | Azure Virtual Desktop |
| eds-AVDB-1 | Standard_D4as_v4 | Windows | Running | Azure Virtual Desktop |
| eds-AVDH-0 | Standard_D4as_v4 | Windows | Running | Azure Virtual Desktop |
| eds-AVDH-1 | Standard_D4as_v4 | Windows | Running | Azure Virtual Desktop |
| eds-AVDH-2 | Standard_D4as_v4 | Windows | Running | Azure Virtual Desktop |
| eds-ASP | Standard_B2ms | Windows | **Deallocated** | Unknown (potential cleanup candidate) |
| eds-lucee-InstructionPacks | Standard_B2s | Windows | **Deallocated** | Lucee server (potential cleanup candidate) |
| EDSIQ-CF | Standard_E2bds_v5 | Windows | **Deallocated** | EDSIQ ColdFusion (potential cleanup candidate) |

**Note:** The 3 deallocated VMs still have disks, NICs, NSGs, and public IPs allocated, incurring ongoing costs even while stopped.

### WordPress Production Stack (eds-wp-prod_group)

Entirely undocumented. Contains:
- 2 Web Apps: `eds-wp-prod` and `eds-wp-prod-debian` (Linux containers, running)
- MySQL Flexible Server: `eds-pw-prod-public` (Standard_B2s, MySQL 8.0.21)
- Azure Front Door CDN profile
- Communication Services (email)
- Appears to be the ed-data.com marketing/corporate website

### Azure Virtual Desktop (6 running VMs)

Completely undocumented. Infrastructure includes:
- 2 host pools: `eds-AVD`, `eds-AVDB`
- 3 workspaces: `eds-workspace`, `eds-WorkspaceB`, `eds-Multi`
- Application groups
- Represents significant compute cost

### Networking (undocumented)

| Resource | Details |
|----------|---------|
| **VPN Gateways (2)** | `eds-NJ-Gateway` (VpnGw2AZ), `eds-prod-vpn-gateway` (VpnGw2AZ, 3 public IPs) |
| **Bastion Host** | `eds-prod-vnet-bastion` |
| **Application Gateways (3)** | `eds-web-router-prod`, `edsWebRouter` (both prod, potentially redundant), `eds-web-router-uat` |
| **VNets (8 total)** | `eds-prod-vnet`, `eds-web-router-prod-vnet`, `eds-NJ-vNet`, `eds-uat-vnet`, AKS managed (x2), `eds-prod-vnet-asr`, WordPress VNet |
| **Public IPs** | 25 in prod, 5 in UAT, ~30 K8s-managed |
| **NSGs** | 19 in prod, 2 in UAT |

### Storage Accounts (10, none documented)

| Account | Resource Group | SKU | Purpose |
|---------|---------------|-----|---------|
| edscdn | eds-prod-rg | Standard_LRS | CDN storage |
| edsapp | eds-prod-rg | Standard_RAGRS | App storage |
| edsdbprodstorage | eds-prod-rg | Premium_LRS | DB backups (premium, block blob) |
| edsdbprodstorage2 | eds-prod-rg | Standard_RAGRS | DB storage (with private endpoint) |
| eastus2edsiq | eds-prod-rg | Standard_LRS | EDSIQ |
| eastus2pdp | eds-prod-rg | Standard_LRS | PDP |
| potransmitter | eds-prod-rg | Standard_RAGRS | PO Transmitter |
| tfstateedsiq | eastus2-edsiq | Standard_LRS | Terraform state |
| eddataword766dfc596f | eds-uat-rg | Standard_RAGRS | WordPress UAT |
| edswpprod5315d49b87 | eds-wp-prod_group | Standard_RAGRS | WordPress prod |

### Key Vaults (11, none documented)

7 in prod, 4 in UAT. Notable: `kv-districtmanager-prod` and `kv-districtmanager-uat` both exist in eds-prod-rg.

### Container Registries (3, none documented)

| Registry | Login Server | SKU |
|----------|-------------|-----|
| edsProdAKSRegistry | edsprodaksregistry.azurecr.io | Standard |
| edsaksregistry | edsaksregistry.azurecr.io | Standard |
| edscr | edscr.azurecr.io | Standard |

No documentation specifies which is the primary/active registry. EDSIQ deployment references `edsprodaksregistry.azurecr.io`.

### Disaster Recovery / ASR (undocumented)

`eds-prod-rg-asr` in South Central US contains disk replicas for 7 VMs (SQL-Server, EDSIQ-CF, eds-ASP, eds-WebRouter, eds-lucee-InstructionPacks, eds-Tomcat8) plus a replicated VNet.

### Automation (undocumented)

- **Automation Accounts:** `eds-automation` (prod), `eds-automation-uat` with runbooks for NodeIndexer start/stop, EDSIQ pod rotation, health checks
- **Azure Monitor:** Metric alerts for CPU, memory, disk IOPS, network on VMs and AKS
- **Application Insights:** `EDSIQ-ES`
- **Recovery Services Vault:** `vault-lkld6gtq` for VM backup
- **DNS Zones:** `ed-data-app.com` (prod), `ed-data-uat.com`, `mail.edsuat.com` (UAT)
- **Communication Services:** Email services in UAT and WordPress prod
- **NAT Gateway:** `aks-vnet-uat-gateway` for AKS egress
- **Batch Account:** `nodeindexer` in UAT

---

## Azure Infrastructure - Inaccurate Documentation

| Item | Documented | Actual |
|------|-----------|--------|
| Kubernetes version | 1.32.10 (both clusters) | **1.32.11** (both clusters, patched since doc date 2026-03-05) |
| Node pools | Not mentioned | `sdsindex2` pool exists on both clusters (Standard_D8as_v5, Linux, scaled to 0) |
| UAT RG location | "East US 2" implied | RG registered in `eastus` (though AKS cluster itself is in eastus2) |
| Application gateways | Not detailed | 2 in prod (`eds-web-router-prod` and `edsWebRouter`) -- potentially redundant |

---

## SQL Server - Undocumented Databases

The documentation mentions only **EDS** and **dpa_EDSAdmin**. The server hosts **26 databases total** (including system DBs). Here are the **20 undocumented user databases**:

### Production/Business Databases

| Database | Size | Tables | Views | Procs | Purpose |
|----------|------|--------|-------|-------|---------|
| **Catalogs** | 225 GB | 25 | 0 | 45 | Production catalog data |
| **VendorBids** | 109 GB | 41 | 23 | 72 | Vendor bidding system |
| **VendorBids_TEST** | 102 GB | 41 | 23 | 72 | VendorBids test copy |
| **SearchData** | 92 GB | 9 | 0 | 1 | Search index data |
| **SearchData_Test** | 92 GB | 9 | 0 | 1 | SearchData test copy |
| **ContentCentral** | 56 GB | 134 | 7 | 0 | Content/document management |
| **WorkTables** | 31 GB | 264 | 0 | 0 | Work/staging data |
| **Documents** | 7 GB | 39 | 15 | 12 | Document storage |
| **NJ_RTK** | 256 MB | 9 | 6 | 3 | NJ Right to Know data |
| **ProcurementAnalytics** | 144 MB | 13 | 0 | 0 | New (created 2026-03-13) |
| **IDIQ_Platform** | 80 MB | 0 | 0 | 0 | Empty |
| **IDIQ_Platform_UAT** | 144 MB | 98 | 0 | 0 | IDIQ UAT |

### Test/Dev Databases

| Database | Size | Tables | Notes |
|----------|------|--------|-------|
| **EDS_Test** | 1.2 TB | 446 | Full test copy of EDS |
| **EDS_TEST_Old** | 1.1 TB | 439 | Older test copy |
| **test** | 80 MB | 0 | Empty test DB |
| **work** | 16 MB | 1 | Single-table workspace |
| **DeletedPOs** | 16 MB | 1 | Deleted PO archive |

### Infrastructure Databases

| Database | Size | Tables | Notes |
|----------|------|--------|-------|
| **hMailServer** | 16 MB | 34 | Mail system |
| **hMailServerNew** | 16 MB | 34 | Updated mail system |
| **SolarWindsOrion** | 346 MB | 364 | SolarWinds monitoring |

### Server Details

| Property | Value |
|----------|-------|
| SQL Server Version | 14.0.3520.4 (SQL Server 2017 RTM-CU31-GDR) |
| Edition | Developer Edition (64-bit) |
| OS | Windows Server 2022 Datacenter (Hypervisor) |
| Machine Name | SQL-Server |

---

## SQL Server - Object Count Discrepancies

### EDS Database Objects

| Object Type | Actual (2026-03-27) | CLAUDE.md | SCHEMA.md | EDS_SUMMARY.md | Issue |
|-------------|---------------------|-----------|-----------|----------------|-------|
| **Tables** | 439 | 438 | 438 | 438 | +1 (`dbo.Vendors` created 2026-01-22) |
| **Table Columns** | 4,644 | 4,638 | 4,638 | 4,638 | +6 new columns |
| **Views** | 475 | 474 | 474 | 474 | +1 (`vw_ReqTotalsByVendor_TEST` created 2026-03-04) |
| **Stored Procedures** | 396 | 395 | 395 | 395 | +1 (`usp_CheckVendorComplianceForPOs` created 2026-01-23) |
| **Functions** | 232 | -- | 231 | 231 | +1 |
| **Triggers** | **59** | **52** | **52** | **59** | CLAUDE.md and SCHEMA.md exclude 7 view-based triggers |
| **Indexes** | **818** | 815 | 815 | **1,113** | EDS_SUMMARY.md overcounts by 36%; CLAUDE.md is close |
| **Foreign Keys** | 31 | 31 | 31 | 31 | Match |
| **Default Constraints** | 134 | -- | -- | 133 | +1 |

### Trigger Discrepancy Detail

The 52 count in CLAUDE.md and SCHEMA.md only includes triggers on **tables**. There are 7 additional triggers on **views** (INSTEAD OF triggers):

1. `trig_BTRNUpdate`
2. `trig_DCUpdate`
3. `trig_vw_ReqDetail_delete`
4. `trig_vw_ReqDetail_insert`
5. `trig_vw_ReqDetail_update`
6. `vw_BidAnswers_Update`
7. `vw_TMSurveyData_trig`

### Index Discrepancy Detail

| Source | Count | Notes |
|--------|-------|-------|
| Actual | 818 | 345 clustered + 473 nonclustered |
| EDS_SUMMARY.md | 1,113 | Overcounts by ~295 (may have counted index columns or included heaps) |
| SCHEMA.md / CLAUDE.md | 815 | Close to actual (3 indexes added since) |
| EDS_INDEXES.md | 815 | Close to actual |

### EDS Database Size Growth

| Metric | Documented (Jan 2026) | Actual (Mar 2026) | Delta |
|--------|----------------------|-------------------|-------|
| Data Size | 1,222,486 MB (~1.19 TB) | 1,462,209 MB (~1.43 TB) | **+240 GB (20% growth)** |
| Log Size | 53,404 MB | 54,695 MB | +1.3 GB |

### New Objects Since Documentation Date (2026-01-09)

- **Tables:** `dbo.Vendors` (Jan 22), `dbo.DistrictNoteType` (Mar 5)
- **Views:** `dbo.vw_ReqTotalsByVendor_TEST` (Mar 4)
- **Procedures:** `dbo.usp_CheckVendorComplianceForPOs` (Jan 23)
- **Triggers:** `trig_VendorUpdate` on `dbo.Vendors` (Jan 22)
- **30 tables, 9 views, 4 procedures** have been altered since docs were generated

---

## External Services - Undocumented or Incorrect

### Elasticsearch

| Item | Documented | Actual |
|------|-----------|--------|
| **Production index** | `pricing_consolidated_53` | `pricing_consolidated_60` (18.6M docs, 73.2GB). Index 53 is **empty** (0 docs). |
| **Docker version** | ES 8.17.0 (docker-compose.yml) | Production runs **7.15.2** -- major version mismatch |
| **.env.example index** | `pricing_consolidated_51` | Stale reference (3 versions behind) |
| **SDS indices** | Not mentioned | 10 indices: `sds_v3` through `sds_v12` |
| **Autocomplete indices** | Not mentioned | Multiple `pi_autocomplete_*` indices |
| **Query completion** | Not mentioned | `query_completion` indices |
| **Infrastructure doc** | None | No standalone doc for ES VM, indices, backups, maintenance |

Total: **44 indices** on the production ES cluster.

### Redis

| Item | Documented | Actual |
|------|-----------|--------|
| Status | "optional/future" (`docs/ARCHITECTURE.md`, `docs/DEPLOYMENT.md`) | **Deployed and running** in K8s |
| Config | None | Full Redisson cluster config at `eds-edsiq/lucee/redisson-Cluster.yaml` connecting to `redis://redis:6379` |
| K8s manifest | Not referenced | `eds-edsiq/deploy-redis.yaml` with persistent volumes |

### Additional Database Connections

EDSIQ deployment YAML (`eds-edsiq/deploy-edsiq.yaml`) configures connections to **three databases** beyond what CLAUDE.md documents:
- `VendorBids` database
- `DMS` (Document Management System) database with separate `DMSUser` credentials
- `Catalogs` database (referenced in monitoring scripts)

### Scheduled Tasks

| Task | Status |
|------|--------|
| `annual-vendor-table-refresh` | Referenced in CLAUDE.md as running "each December 15" but **no implementation exists** -- no script, no cron job, no GitHub Action |
| Ollama keepalive | `api/routes/ai_chat.py` runs async background ping every 4 minutes -- undocumented |

### Azure DevOps Pipeline

`eds-edsiq/azure-pipelines.yml` exists but is a stub containing only `echo "Hello, world!"`. Appears to be an abandoned CI/CD attempt separate from the GitHub Actions pipeline.

---

## Code & Configuration - Missing from Docs

### Docker Configuration

- **Elasticsearch service** in `docker-compose.yml` not mentioned in CLAUDE.md Docker section
- **12+ environment variables** in docker-compose.yml not in `.env.example`: `ES_URL`, `ES_ENABLED`, `DB_DRIVER`, `DB_TRUST_CERT`, `DB_POOL_MIN`, `DB_POOL_MAX`, `DB_CONNECTION_TIMEOUT`, `LOG_LEVEL`, `API_BASE_URL`, `BUDGET_LIMIT`, `FRONTEND_PORT`, `API_PORT`, `ES_PORT`

### Frontend Structure

CLAUDE.md describes a structure that does not exist:

```
# DOCUMENTED (incorrect):
frontend/
├── alpine-requisition.html     # Does not exist
├── js/stores/                   # Directory does not exist
│   ├── auth, cart, products...  # Files do not exist in this structure
├── js/api.js                    # File does not exist

# ACTUAL:
frontend/
├── index.html                   # Main entry point
├── login.html
├── checkout.html                # Not documented
├── product-detail.html          # Not documented
├── js/
│   ├── api-client.js            # Actual API client
│   ├── app.js, auth.js, cart.js, browse.js, ...  # 18 flat JS files
├── css/
│   └── design-system.css        # CSS custom properties (not Tailwind config)
```

**Additional note:** CLAUDE.md says "Tailwind-based component styles" and references brand colors in a "Tailwind config," but no `tailwind.config.js` exists. Brand colors are defined as CSS custom properties in `design-system.css` and inline in HTML files.

### Test Structure

CLAUDE.md documents 10 test files. The actual count is **31 files** (including conftest and utility files). Undocumented test files:

- `tests/test_config.py`
- `tests/test_db_utils.py`
- `tests/test_investigate_blocking.py`
- `tests/test_deploy_indexes.py`
- `tests/test_recursive_procedures.py`
- `tests/api/test_ai_search.py`
- `tests/api/test_ai_chat.py`
- `tests/api/test_dashboard.py`
- `tests/api/test_reports.py`
- `tests/e2e/test_login_workflow.py`
- `tests/e2e/test_approval_workflow.py`
- `tests/e2e/test_product_browsing.py`
- `tests/e2e/test_checkout_workflow.py`
- `tests/e2e/test_requisition_listing.py`
- `tests/e2e/test_cart_workflow.py`
- `tests/e2e/test_visual_regression.py`
- `tests/e2e/test_critical_flows.py`
- `tests/e2e/screenshot_utils.py`

### pyproject.toml

- **Undocumented optional dependency groups:** `dashboard`, `export`, `gui`, `build`, `all`
- **Undocumented entry points:** `generate-index-scripts`, `deploy-indexes-test`, `deploy-indexes-prod`, `validate-indexes`, `eds-api`
- **Undocumented dependencies:** `elasticsearch[async]>=8.12.0`, `ollama>=0.4.0` in the `api` extra

### Environment Variables

- CLAUDE.md middleware env vars (`EDS_ENV`, `EDS_CORS_ORIGINS`, `EDS_RATE_LIMIT`, `EDS_BEHIND_PROXY`, `EDS_DEBUG`) exist in code but are absent from `.env.example`, `config/dev.env`, and `config/prod.env.example`
- `DB_DATABASE_CATALOG` fallback chain (`DB_DATABASE_CATALOG` -> `DB_DATABASE` -> `"EDS"`) is undocumented
- `docs/CONFIGURATION.md` references `universal-requisition.html` for frontend config; actual config is `frontend/js/config.js`

### CI/CD

- GitHub Actions `deploy.yml` is a stub with placeholder comments ("Add your deployment commands here") but `docs/CI_CD.md` presents it as a functional pipeline

---

## Recommended Actions

### Priority 1 - Critical Fixes

1. **Fix ES index reference** -- Update `api/search.py`, `.env.example`, and `docs/API_ROUTES.md` to reference `pricing_consolidated_60` (or the correct current production index)
2. **Correct EDSIQ tech stack** -- Update `docs/wiki/architecture/application-stack.md` from "Java/Spring Boot" to "ColdFusion/Lucee/CFWheels"
3. **Update CLAUDE.md frontend section** -- Replace nonexistent `alpine-requisition.html`, `js/stores/`, `js/api.js` with actual file structure
4. **Fix trigger count** -- Change 52 to 59 in CLAUDE.md and SCHEMA.md
5. **Fix index count** -- Correct EDS_SUMMARY.md from 1,113 to 818

### Priority 2 - Documentation Gaps

6. **Create database inventory** -- Document all 22 user databases, not just EDS and dpa_EDSAdmin
7. **Create ES infrastructure doc** -- Cover the VM, all 44 indices, version, backups, maintenance
8. **Update Redis status** -- Change from "optional/future" to "deployed" in ARCHITECTURE.md and DEPLOYMENT.md
9. **Document Azure infrastructure** -- WordPress stack, AVD, VPN gateways, DR/ASR, storage accounts, Key Vaults, container registries
10. **Update test structure** -- Reflect 31 actual test files
11. **Add missing env vars** to `.env.example` and config templates

### Priority 3 - Cleanup Opportunities

12. **Investigate 3 deallocated VMs** -- eds-ASP, eds-lucee-InstructionPacks, EDSIQ-CF (costing money for reserved disks/IPs)
13. **Clean orphaned UAT resources** -- NodeIndexer-UAT disk, NIC, NSG, public IP
14. **Consolidate 3 container registries** -- Determine and document primary ACR
15. **Review dual application gateways** in prod for potential redundancy
16. **Implement or remove** `annual-vendor-table-refresh` scheduled task reference
17. **Delete empty resource groups** -- `eastus2-edsiq-aks`, `eds-uat-b2c`

---

*Generated by automated infrastructure audit on 2026-03-27*
