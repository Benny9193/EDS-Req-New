# Elasticsearch Infrastructure

> **Last updated**: 2026-03-27 (infrastructure audit)

---

## Server

| Property | Value |
|----------|-------|
| **Host** | `20.122.81.233` (Azure VM `EDS-ES`, East US 2) |
| **Port** | 9200 |
| **Version** | 7.15.2 |
| **Cluster Name** | elasticsearch |
| **Node Name** | EDS-ES |
| **Authentication** | **None** (unauthenticated, public IP) |
| **TLS** | **None** |
| **Cluster Status** | Yellow (expected for single-node — 61 unassigned replica shards) |

> **Security Warning**: ES is exposed on a public IP without authentication or TLS. This is a **HIGH** severity issue. Consider restricting access via NSG rules or deploying behind a reverse proxy with auth.

---

## Version Mismatch

| Environment | ES Version | Notes |
|-------------|-----------|-------|
| **Production** (VM) | **7.15.2** | Single-node cluster |
| **Local dev** (docker-compose.yml) | **8.17.0** | Major version mismatch |

ES 8.x has breaking changes from 7.x:
- Security enabled by default (auth, TLS)
- Deprecated `_type` field removed
- Some query DSL changes
- Different default behavior for `track_total_hits`

**Risk**: Code developed/tested locally against 8.x may fail against 7.x in production. Either:
1. Pin docker-compose.yml to `7.15.2` to match production, or
2. Plan a production upgrade to 8.x

---

## Active Production Index

| Property | Value |
|----------|-------|
| **Index Name** | `pricing_consolidated_60` |
| **Document Count** | 18,633,822 |
| **Size** | 73.2 GB |
| **Content** | Denormalized product + bid + pricing data |
| **Field Style** | camelCase (from EDSIQ ColdFusion indexer) |

Key fields: `shortDescription`, `fullDescription`, `itemCode`, `vendorName`, `bidHeaderId`, `vendorCode`, `unitPrice`, `categoryPath`

### Code References

| File | Config | Notes |
|------|--------|-------|
| `api/search.py:23` | `ES_INDEX` env var, default `pricing_consolidated_60` | Main ES client |
| `api/routes/search.py` | Uses `search.ES_INDEX` | Search endpoints |
| `api/routes/products.py` | Uses `search.ES_INDEX` | Product search fallback |
| `.env.example:25` | `pricing_consolidated_60` (commented) | Template |

---

## Full Index Inventory (44 indices)

### Pricing Indices

| Index | Docs | Size | Status |
|-------|------|------|--------|
| `pricing_consolidated_60` | 18.6M | 73.2 GB | **Active production** |
| `pricing_consolidated_uat_2` | 30.3M | 106.2 GB | UAT (larger than prod — full catalog?) |
| `pricing_consolidated_53` | 0 | 208 B | **Empty** — former default, cleanup candidate |
| `pricing_consolidated_51` | 0 | 208 B | **Empty** — stale .env.example reference, cleanup candidate |

### Autocomplete Indices

| Index Pattern | Docs | Size | Environment |
|---------------|------|------|-------------|
| `pi_autocomplete_prod_active_*` | 15.9M | 5.5 GB | Production |
| `pi_autocomplete_uat_active_*` | 48.2M | 14.9 GB | UAT |

### SDS (Safety Data Sheets) Indices

| Index | Docs | Size | Notes |
|-------|------|------|-------|
| `sds_v12` | 2.7M | 7.1 GB | **Latest version** |
| `sds-uat-v22` | 2.3M | 4.5 GB | UAT |
| `sds_v3` through `sds_v11` | varies | ~10 GB total | Older versions — **cleanup candidates** |

### Query Completion Indices

| Index | Docs | Size |
|-------|------|------|
| `query_completion` | ~2K | ~5 MB |
| `query_completion_v3` | ~20K | ~5 MB |

### Summary

| Category | Count | Total Size |
|----------|-------|------------|
| Pricing | 4 | ~179 GB |
| Autocomplete | 2+ | ~20 GB |
| SDS | 12+ | ~22 GB |
| Query completion | 2 | ~10 MB |
| **Total** | **~44** | **~221 GB** |

---

## Indexing

The EDSIQ ColdFusion application produces the `pricing_consolidated_*` indices. The index number increments with each full reindex (51 → 53 → 60, etc.).

The SDS index builder runs in Kubernetes (`eds-sds` namespace, `sds-index-builder-2` service).

The autocomplete indices are built from the pricing data by a separate process.

---

## Cleanup Recommendations

1. **Delete empty pricing indices** (`pricing_consolidated_51`, `pricing_consolidated_53`) — 0 documents, no value
2. **Delete old SDS versions** (`sds_v3` through `sds_v11`) — `sds_v12` is current, ~10 GB recoverable
3. **Resolve version mismatch** — pin docker-compose to 7.15.2 or plan production upgrade
4. **Add authentication** — at minimum, restrict access via Azure NSG to known IPs
5. **Enable TLS** — encrypt data in transit
