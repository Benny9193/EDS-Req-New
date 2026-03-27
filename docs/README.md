# EDS Documentation Index

> Comprehensive documentation for the EDS (Educational Data Services) system

**Last updated:** March 27, 2026

---

## Quick Links

| Document | Description |
|----------|-------------|
| [Data Dictionary](EDS_DATA_DICTIONARY.md) | Complete table and column reference (438 tables, 4,638 columns) |
| [Stored Procedures](EDS_STORED_PROCEDURES.md) | All 395 procedures with source code |
| [Views](EDS_VIEWS.md) | All 474 views with SQL definitions |
| [ERD Diagrams](EDS_ERD.md) | Entity relationship diagrams (Mermaid) |
| [Wiki Home](wiki/index.md) | Navigable knowledge base |
| [Excel Data Dictionary](EDS_DATA_DICTIONARY.xlsx) | Searchable Excel workbook (6 sheets) |

---

## Core System Docs

| Document | Description |
|----------|-------------|
| [ARCHITECTURE.md](ARCHITECTURE.md) | Universal Requisition app architecture (client, API, database) |
| [DEVELOPMENT.md](DEVELOPMENT.md) | Local development environment setup (Python 3.12+) |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Docker & Kubernetes deployment instructions |
| [TESTING.md](TESTING.md) | Testing guide (unit, API, E2E, integration with pytest) |
| [TESTING_REFERENCE.md](TESTING_REFERENCE.md) | Detailed testing reference: fixtures, mocking patterns, every test file documented |
| [CI_CD.md](CI_CD.md) | CI/CD pipeline documentation (test.yml, deploy.yml, troubleshooting) |
| [CONFIGURATION.md](CONFIGURATION.md) | Configuration reference (.env, config.yaml, priority order) |
| [FRONTEND_TROUBLESHOOTING.md](FRONTEND_TROUBLESHOOTING.md) | Frontend/application troubleshooting (CORS, localStorage, API) |

## Application Docs

| Document | Description |
|----------|-------------|
| [FRONTEND_ARCHITECTURE.md](FRONTEND_ARCHITECTURE.md) | Complete frontend architecture guide (Alpine.js, modules, state, auth, CSS) |
| [API_ROUTES.md](API_ROUTES.md) | Complete API routes reference (90+ endpoints across 14 route modules) |
| [UNIVERSAL_REQUISITION.md](UNIVERSAL_REQUISITION.md) | Requisition interface user & developer guide |
| [API_REFERENCE.md](API_REFERENCE.md) | Python monitoring tools API reference (db_utils, config, logging) |
| [MONITORING_SCRIPTS_REFERENCE.md](MONITORING_SCRIPTS_REFERENCE.md) | Complete reference for all 58 monitoring scripts, CLI entry points, configuration, output files, and workflows |
| [AGENT_CLI.md](AGENT_CLI.md) | DBA Agent CLI usage and commands |
| [AGENT_TECHNICAL_REFERENCE.md](AGENT_TECHNICAL_REFERENCE.md) | DBA Agent technical deep dive (RAG, memory, tools, security, export, GUI) |
| [demo-script.md](demo-script.md) | Demo walkthrough script |
| [frontend-comparison-walkthrough.md](frontend-comparison-walkthrough.md) | Frontend version comparison guide |

---

## Database Schema & Structure

| Document | Description |
|----------|-------------|
| [SCHEMA.md](SCHEMA.md) | Schema guide with ERD diagrams and organizational hierarchy |
| [EDS_SUMMARY.md](EDS_SUMMARY.md) | Executive summary of database objects and statistics |
| [EDS_DATA_DICTIONARY.md](EDS_DATA_DICTIONARY.md) | Complete generated table/column reference |
| [EDS_ERD.md](EDS_ERD.md) | Entity relationship diagrams (Mermaid) |
| [EDS_INDEXES.md](EDS_INDEXES.md) | Index documentation (815 indexes, 59 unused) |
| [EDS_STATUS_CODES.md](EDS_STATUS_CODES.md) | Status codes and lookup tables |

### Schema Statistics

| Metric | Count |
|--------|-------|
| **Tables** | 438 |
| **Columns** | 4,638 |
| **Stored Procedures** | 395 |
| **Views** | 474 |
| **Indexes** | 815 |
| **Foreign Keys** | 31 |

---

## Stored Procedures & Views

| Document | Type | Description |
|----------|------|-------------|
| [EDS_STORED_PROCEDURES.md](EDS_STORED_PROCEDURES.md) | Reference | All 395 SPs with parameters and source code |
| [EDS_PROCEDURES_GUIDE.md](EDS_PROCEDURES_GUIDE.md) | Guide | Business context, usage examples, workflow context |
| [EDS_VIEWS.md](EDS_VIEWS.md) | Reference | All 474 views with SQL definitions and dependencies |
| [EDS_VIEWS_GUIDE.md](EDS_VIEWS_GUIDE.md) | Guide | Views with naming conventions and domain organization |

---

## Dependencies & Analysis

| Document | Description |
|----------|-------------|
| [EDS_PROCEDURE_DEPENDENCIES.md](EDS_PROCEDURE_DEPENDENCIES.md) | SP call chains, table access patterns, workflow orchestration, detailed metrics |
| [EDS_ROOT_PROCEDURES.md](EDS_ROOT_PROCEDURES.md) | 77 entry point procedures by category |
| [EDS_CIRCULAR_DEPS.md](EDS_CIRCULAR_DEPS.md) | Circular dependency analysis (0 circular, 34 recursive) |
| [EDS_RECURSIVE_PROCEDURES.md](EDS_RECURSIVE_PROCEDURES.md) | 34 self-calling procedures (tree traversal, org hierarchy) |
| [EDS_INFINITE_LOOP_ANALYSIS.md](EDS_INFINITE_LOOP_ANALYSIS.md) | Infinite loop pattern analysis (1 HIGH, 78 LOW severity) |
| [EDS_TRIGGERS.md](EDS_TRIGGERS.md) | 52 triggers (45 INSERT, 39 UPDATE, 10 DELETE) |

---

## Data Management & Governance

| Document | Description |
|----------|-------------|
| [EDS_DATA_OWNERSHIP.md](EDS_DATA_OWNERSHIP.md) | Data stewardship roles and RACI matrix |
| [EDS_ETL_INTEGRATIONS.md](EDS_ETL_INTEGRATIONS.md) | External system integration points (SSO, financial, vendor) |
| [EDS_ACCESS_CONTROL.md](EDS_ACCESS_CONTROL.md) | Multi-layered access control (auth, RBAC, row-level, column-level) |
| [EDS_ARCHIVE_STRATEGY.md](EDS_ARCHIVE_STRATEGY.md) | Data retention/archival strategy (policy, compliance, design) |
| [EDS_ARCHIVE_ANALYSIS.md](EDS_ARCHIVE_ANALYSIS.md) | Archive vs active schema comparison (49 archived tables) |

---

## Business & Operations

| Document | Description |
|----------|-------------|
| [EDS_BUSINESS_DOMAINS.md](EDS_BUSINESS_DOMAINS.md) | Overview of tables by functional area |
| [EDS_BUSINESS_WORKFLOWS.md](EDS_BUSINESS_WORKFLOWS.md) | Key business processes (bidding, orders, vendors, catalogs, budgets) |
| [kubernetes-clusters.md](kubernetes-clusters.md) | AKS cluster documentation (prod/UAT, nodes, workloads) |
| [guides/DAILY_MONITORING_GUIDE.md](guides/DAILY_MONITORING_GUIDE.md) | SQL-based daily monitoring queries and dashboard |

---

## Domain-Specific Deep Dives

| Document | Description |
|----------|-------------|
| [tables/TIER1_TABLES.md](tables/TIER1_TABLES.md) | 25 critical tables (CrossRefs 150.6M, Items 30.1M, Detail 30.8M rows) |
| [domains/BIDDING_DOMAIN.md](domains/BIDDING_DOMAIN.md) | Bidding & procurement (51 tables, ~506M rows, lifecycle diagrams) |
| [domains/ORDERS_DOMAIN.md](domains/ORDERS_DOMAIN.md) | Orders & purchasing (47 tables, ~395M rows) |
| [domains/VENDORS_USERS_DOMAIN.md](domains/VENDORS_USERS_DOMAIN.md) | Vendors & users (51 tables, ~24M rows, hierarchy diagrams) |
| [domains/INVENTORY_FINANCE_DOMAIN.md](domains/INVENTORY_FINANCE_DOMAIN.md) | Inventory & finance (~40 tables, ~260M rows) |

---

## Wiki (Navigable Knowledge Base)

The [wiki](wiki/index.md) provides a structured, navigable view of EDS documentation:

| Section | Description |
|---------|-------------|
| [Getting Started](wiki/getting-started/index.md) | Quick reference, glossary |
| [Business Context](wiki/business/index.md) | What is EDS, entities, workflows |
| [Schema by Domain](wiki/schema/index.md) | Tables organized by functional domain |
| [Architecture](wiki/architecture/index.md) | System overview, app stack, DB architecture, integrations |
| [Performance](wiki/performance/index.md) | Known issues, incident reports |
| [Troubleshooting](wiki/troubleshooting/index.md) | Database: slow queries, blocking, deadlocks, runbooks |
| [Operations](wiki/operations/daily-monitoring.md) | Morning health check and DBA on-call checklist |
| [User Activity](wiki/user-activity/index.md) | Application users, usage patterns |

---

## SQL Server Documentation

### [EDS_EXTENDED_PROPERTIES.sql](EDS_EXTENDED_PROPERTIES.sql)
SQL script to add inline documentation to SQL Server:
- 381 table descriptions, 1,596 column descriptions
- Uses `MS_Description` extended properties
- Appears in SSMS Object Explorer and documentation tools

---

## Templates

Documentation templates for creating new docs consistently:

| Template | Purpose |
|----------|---------|
| [templates/table-template.md](templates/table-template.md) | New table documentation |
| [templates/procedure-template.md](templates/procedure-template.md) | New stored procedure documentation |
| [templates/view-template.md](templates/view-template.md) | New view documentation |
| [templates/domain-template.md](templates/domain-template.md) | New domain documentation |

---

## PDF Exports

Compiled PDF versions of documentation are available in [`pdf/`](pdf/).

---

## Scripts Reference

> For full coverage of all 58 monitoring and tooling scripts, including CLI usage, configuration, output files, and step-by-step workflows, see [MONITORING_SCRIPTS_REFERENCE.md](MONITORING_SCRIPTS_REFERENCE.md).

Documentation generation scripts in `../scripts/`:

| Script | Output |
|--------|--------|
| `generate_data_dictionary.py` | `EDS_DATA_DICTIONARY.md` |
| `generate_sproc_docs.py` | `EDS_STORED_PROCEDURES.md` |
| `generate_views_docs.py` | `EDS_VIEWS.md` |
| `generate_erd.py` | `EDS_ERD.md` |
| `analyze_business_domains.py` | `EDS_BUSINESS_DOMAINS.md` |
| `analyze_archive_schema.py` | `EDS_ARCHIVE_ANALYSIS.md` |
| `export_to_excel.py` | `EDS_DATA_DICTIONARY.xlsx` |
| `generate_extended_properties.py` | `EDS_EXTENDED_PROPERTIES.sql` |
| `generate_sp_dependencies.py` | `EDS_PROCEDURE_DEPENDENCIES.md` |

### Regenerating Documentation

```bash
# Regenerate all documentation
python scripts/generate_data_dictionary.py -d EDS
python scripts/generate_sproc_docs.py -d EDS
python scripts/generate_views_docs.py -d EDS
python scripts/generate_erd.py -d EDS
python scripts/analyze_business_domains.py -d EDS
python scripts/analyze_archive_schema.py -d EDS
python scripts/export_to_excel.py -d EDS
python scripts/generate_extended_properties.py -d EDS
```

---

## Key Findings

### Database Health

1. **Low Referential Integrity**: Only 31 foreign keys for 438 tables
   - Many relationships are enforced by application logic
   - 219 implicit relationships detected by naming convention

2. **Missing Primary Keys**: 94 tables lack primary keys
   - Most are in the archive schema
   - Consider adding PKs for data integrity

3. **Archive Schema**: 49 tables have archived copies
   - Archive holds historical data for retention
   - 2 orphaned archive tables should be reviewed

### Performance Concerns

From performance analysis:
- 50 missing index recommendations
- 50 slow queries identified (up to 27.5B buffer reads)
- 44 blocking events detected
- 100 I/O latency issues

See `../output/performance/` for detailed reports.

---

## Maintenance

### Keeping Documentation Current

Run documentation scripts after schema changes:
```bash
# Quick refresh of key docs
python scripts/generate_data_dictionary.py -d EDS
python scripts/export_to_excel.py -d EDS
```

### Adding Table Descriptions

1. Edit `TABLE_DESCRIPTIONS` dict in `generate_extended_properties.py`
2. Regenerate: `python scripts/generate_extended_properties.py -d EDS`
3. Execute SQL script in SSMS

---

*Documentation generated by SQL Server Monitoring Tools*
