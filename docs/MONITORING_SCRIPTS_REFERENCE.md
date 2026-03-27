# EDS Monitoring Scripts Reference

**Purpose**: Complete technical reference for all SQL Server performance monitoring scripts, tools, and automation in the EDS project.

**Source Database**: `dpa_EDSAdmin` (SolarWinds DPA monitoring repository)
**Target Databases**: `EDS`, `Catalogs`, `VendorBids`, `ContentCentral`
**Python Version**: 3.9+
**Last Updated**: 2026-03-27

---

## Table of Contents

1. [Overview](#1-overview)
2. [Shared Utilities](#2-shared-utilities)
3. [Performance Analysis Scripts](#3-performance-analysis-scripts)
4. [Index Management Scripts](#4-index-management-scripts)
5. [Blocking Investigation](#5-blocking-investigation)
6. [SQL Agent Alert Jobs](#6-sql-agent-alert-jobs)
7. [Alert Dashboard](#7-alert-dashboard)
8. [Schema Explorer](#8-schema-explorer)
9. [Elasticsearch Integration](#9-elasticsearch-integration)
10. [Documentation Generation Scripts](#10-documentation-generation-scripts)
11. [Utility and Maintenance Scripts](#11-utility-and-maintenance-scripts)
12. [CLI Entry Points](#12-cli-entry-points)
13. [Configuration Reference](#13-configuration-reference)
14. [Output File Reference](#14-output-file-reference)
15. [Workflow Guide](#15-workflow-guide)

---

## 1. Overview

The `scripts/` directory contains two distinct categories of tooling that share the same infrastructure libraries but serve different purposes.

### 1.1 Categories

| Category | Description | Scripts |
|---|---|---|
| **Performance Monitoring** | Analyze dpa_EDSAdmin data, detect issues, generate recommendations | 10 |
| **Index Management** | Full lifecycle from extraction through production deployment | 5 |
| **Blocking Investigation** | Deep-dive blocking analysis and remediation | 1 |
| **SQL Agent Jobs** | SQL Server automated alerting via Database Mail | 3 |
| **Alert Dashboard** | Daily monitoring dashboard generation | 2 |
| **Schema Explorer** | Interactive Streamlit-based SQL Server schema browser | 1 |
| **Elasticsearch Integration** | Product catalog indexing pipeline | 1 |
| **Documentation Generation** | Scripts that produced the docs in `/docs/` | ~30 |
| **Utility / SQL** | One-off utilities, maintenance SQL, shell scripts | ~6 |

### 1.2 Architecture

All monitoring scripts share three infrastructure modules:

```
scripts/
├── db_utils.py          # Database connectivity layer
├── config.py            # Configuration management (config.yaml + env vars)
├── logging_config.py    # Structured logging with file rotation
│
├── [performance analysis]
├── [index management]
├── [alert jobs]
├── [dashboard]
│
├── sql_agent_jobs/      # SQL Server Agent job installation scripts
│   ├── blocking_alert_job.sql
│   ├── missing_index_alert_job.sql
│   └── io_latency_alert_job.sql
│
└── alert_dashboard.sql  # Generated dashboard query (run in SSMS daily)
```

### 1.3 Data Source

The monitoring scripts read exclusively from `dpa_EDSAdmin`, a SolarWinds Database Performance Analyzer (DPA) repository. The key tables queried are:

| Table | Contents |
|---|---|
| `CON_WHATIF_SRC_1` | Missing index recommendations (what-if analysis) |
| `CON_FQ_OBJECT_1` | Fully-qualified object names for missing index targets |
| `CONST_1` | SQL text store (keyed by hash) |
| `CON_BLOCKING_SUM_1` | Blocking event summaries by hour |
| `CONM_1` | Dimension name lookup (programs, databases, events) |
| `CON_IO_DETAIL_1` | I/O latency detail measurements |
| `CONSS_1` | SQL statement execution statistics |
| `CON_QUERY_PLAN_1` | Query plan capture with buffer get counts |

---

## 2. Shared Utilities

### 2.1 `db_utils.py`

Provides secure, reusable database connectivity via pyodbc. All monitoring scripts import from this module rather than managing connections directly.

**File**: `C:\EDS\scripts\db_utils.py`

#### DatabaseConnection Class

The primary class, supporting context manager usage:

```python
with DatabaseConnection(database='dpa_EDSAdmin') as db:
    rows = db.execute_query(
        "SELECT TOP 10 * FROM CON_WHATIF_SRC_1 WHERE D >= ?",
        params=(cutoff_date,)
    )
```

**Constructor Parameters**:

| Parameter | Type | Default | Description |
|---|---|---|---|
| `database` | str | `DB_DATABASE` env var or `dpa_EDSAdmin` | Database name to connect to |
| `server` | str | `DB_SERVER` env var | SQL Server hostname or IP |
| `username` | str | `DB_USERNAME` env var | SQL authentication username |
| `password` | str | `DB_PASSWORD` env var | SQL authentication password |
| `timeout` | int | `30` | Connection timeout in seconds |

**Connection Behavior**: The constructor auto-detects the available ODBC driver, preferring newer drivers in this order: ODBC Driver 18 → ODBC Driver 17 → SQL Server Native Client 11.0 → SQL Server. All connections use `Encrypt=yes; TrustServerCertificate=yes`.

**Methods**:

| Method | Returns | Description |
|---|---|---|
| `connect()` | None | Establish connection (called automatically by context manager) |
| `disconnect()` | None | Close connection and release resources |
| `execute_query(query, params, fetch_all)` | `List[Tuple]` | Run a parameterized SELECT query |
| `execute_non_query(query, params, commit)` | `int` | Run INSERT/UPDATE/DELETE/DDL; returns rows affected |
| `execute_many(query, params_list, commit)` | `int` | Batch execution with multiple parameter sets |
| `fetch_one(query, params)` | `Optional[Tuple]` | Fetch exactly one row |
| `fetch_scalar(query, params)` | `Any` | Fetch the first column of the first row |
| `is_connected` | `bool` | Property; True if connection is active |

All query methods use parameterized queries (`?` placeholders) to prevent SQL injection.

**Exception Classes**:

| Exception | Raised When |
|---|---|
| `DatabaseConnectionError` | Connection to SQL Server fails |
| `DatabaseQueryError` | Query or statement execution fails |

#### Module-Level Convenience Functions

```python
from db_utils import execute_query, execute_non_query, get_connection

# One-off query (opens and closes connection automatically)
rows = execute_query("SELECT COUNT(*) FROM CON_WHATIF_SRC_1", database='dpa_EDSAdmin')

# Context manager alternative
with get_connection(database='EDS') as db:
    db.execute_non_query("UPDATE Items SET Active = 1 WHERE ItemId = ?", (42,))
```

---

### 2.2 `config.py`

Configuration management with a three-level priority system: environment variables (highest) override `config.yaml`, which overrides compiled defaults (lowest).

**File**: `C:\EDS\scripts\config.py`

#### Configuration Loading

```python
from config import get_config, get_threshold, get_database_config, get_output_path

cfg = get_config()               # Returns global Config instance (lazy-loaded)
threshold = get_threshold('missing_index', 'critical')  # Returns 95
db_config = get_database_config()  # Returns {'name': 'dpa_EDSAdmin', 'timeout': 30}
path = get_output_path()           # Returns Path to output/performance/
path = get_output_path('exports')  # Returns Path to output/exports/
path = get_output_path('logs')     # Returns Path to logs/
```

#### Configuration Structure

The `Config` dataclass has the following nested structure:

```
Config
├── database: DatabaseConfig
│   ├── name: str = "dpa_EDSAdmin"
│   └── timeout: int = 30
│
├── thresholds: Thresholds
│   ├── missing_index: MissingIndexThresholds
│   │   ├── critical: int = 95
│   │   ├── high: int = 80
│   │   ├── medium: int = 50
│   │   └── min_executions: int = 100
│   ├── blocking: BlockingThresholds
│   │   ├── critical_seconds: int = 3600
│   │   ├── high_seconds: int = 300
│   │   └── medium_seconds: int = 60
│   ├── io_latency: IOLatencyThresholds
│   │   ├── critical_ms: int = 200
│   │   ├── high_ms: int = 100
│   │   └── medium_ms: int = 50
│   └── slow_query: SlowQueryThresholds
│       ├── critical_buffer_gets: int = 10_000_000
│       ├── high_buffer_gets: int = 1_000_000
│       └── min_buffer_gets: int = 100_000
│
├── analysis: AnalysisConfig
│   ├── missing_indexes_days: int = 30
│   ├── slow_queries_days: int = 7
│   ├── blocking_days: int = 30
│   ├── io_issues_hours: int = 24
│   ├── top_results: int = 50
│   └── report_top: int = 10
│
├── dashboard: DashboardConfig
│   ├── refresh_interval: int = 30
│   └── health_score: HealthScore
│       ├── critical_index_penalty: int = 20
│       ├── high_index_penalty: int = 10
│       ├── blocking_penalty: int = 15
│       ├── io_latency_penalty: int = 10
│       └── slow_query_penalty: int = 5
│
├── output: OutputConfig
│   ├── directory: str = "output/performance"
│   ├── exports_directory: str = "output/exports"
│   └── log_directory: str = "logs"
│
├── alerts: AlertConfig
│   ├── email: str = "dba-team@company.com"
│   ├── mail_profile: str = "Default"
│   └── enabled: bool = True
│
└── logging: LoggingConfig
    ├── level: str = "INFO"
    ├── format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    ├── max_file_size_mb: int = 10
    └── backup_count: int = 5
```

#### Environment Variable Overrides

| Environment Variable | Overrides |
|---|---|
| `DB_DATABASE` | `config.database.name` |
| `DB_TIMEOUT` | `config.database.timeout` |
| `THRESHOLD_MISSING_INDEX_CRITICAL` | `config.thresholds.missing_index.critical` |
| `THRESHOLD_BLOCKING_CRITICAL_SECONDS` | `config.thresholds.blocking.critical_seconds` |
| `ALERT_EMAIL` | `config.alerts.email` |
| `LOG_LEVEL` | `config.logging.level` |

#### Parameter Validation

```python
from config import validate_params

validate_params(days=30, min_saving=80)   # Raises ValueError if out of range
# days: 1-365, min_saving: 0-100, hours: 1-8760, latency_ms: 0-10000
```

---

### 2.3 `logging_config.py`

Structured logging with simultaneous console and rotating file output. Every monitoring script calls `setup_logging()` at startup.

**File**: `C:\EDS\scripts\logging_config.py`

#### Usage

```python
from logging_config import setup_logging, get_logger, LogContext, log_execution

# Standard script initialization
logger = setup_logging('analyze_performance')  # Creates logs/analyze_performance.log

# Module-level logger
logger = get_logger(__name__)

# Timed operation block
with LogContext(logger, "Querying missing indexes"):
    rows = db.execute_query(query)
# Logs: "Starting: Querying missing indexes"
# Logs: "Completed: Querying missing indexes (1.23s)"

# Decorator
@log_execution(logger, "Processing items")
def process_items(items):
    ...
```

#### `setup_logging()` Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `script_name` | str | required | Used as logger name and log file name |
| `log_level` | str | from config | Override: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` |
| `console_output` | bool | `True` | Write to stdout |
| `file_output` | bool | `True` | Write to `logs/{script_name}.log` |

**Log Rotation**: Files rotate at `max_file_size_mb` (default 10 MB) with `backup_count` (default 5) rotated files kept. The `LOG_LEVEL` environment variable overrides the config setting.

---

## 3. Performance Analysis Scripts

These scripts query `dpa_EDSAdmin` to surface actionable performance data. They are designed for both interactive use and scheduled automation.

### 3.1 Script Inventory

| Script | CLI Command | Primary Output |
|---|---|---|
| `capture_performance_baseline.py` | `capture-baseline` | `baseline_YYYY-MM-DD.json`, `.txt` |
| `analyze_performance_issues.py` | `analyze-performance` | CSV files + `performance_report.txt` |
| `extract_missing_indexes.py` | `extract-indexes` | CSV, Excel, JSON |
| `generate_final_performance_report.py` | `generate-report` | Markdown report, Excel, JSON |

---

### 3.2 `capture_performance_baseline.py`

Captures a point-in-time performance snapshot for before/after comparison. Run this before making any optimization changes, then again after to measure improvement.

**File**: `C:\EDS\scripts\capture_performance_baseline.py`

**Usage**:
```bash
capture-baseline
# or
python scripts/capture_performance_baseline.py
```

**No arguments.** Connects to `dpa_EDSAdmin` and queries the last 7 days (30 days for missing indexes).

**Metrics Captured**:

| Category | Metrics |
|---|---|
| Query Execution | Total queries, total executions, avg buffer gets/exec, total disk reads, total buffer gets |
| Blocking Events | Total events, total blocking minutes, max single event minutes, avg blocking minutes |
| I/O Latency | Avg/max/min read latency (ms), avg/max/min write latency (ms) |
| Missing Indexes | Total count, high-impact count (>=90%), critical count (>=99%), avg estimated saving % |

**Output Files**:

| File | Format | Description |
|---|---|---|
| `output/performance/baseline_YYYY-MM-DD.json` | JSON | Machine-readable metrics for comparison |
| `output/performance/baseline_YYYY-MM-DD.txt` | Text | Human-readable formatted report |

**Typical Workflow**:
```bash
# Step 1: Capture baseline before optimization
capture-baseline

# Step 2: Implement indexes, blocking fixes, etc.

# Step 3: Generate comparison report after optimization
generate-report --baseline output/performance/baseline_2025-12-04.json
```

---

### 3.3 `analyze_performance_issues.py`

Comprehensive performance analysis across four dimensions: missing indexes, slow queries, blocking events, and I/O issues. The primary "triage" script for identifying what to fix.

**File**: `C:\EDS\scripts\analyze_performance_issues.py`

**Usage**:
```bash
analyze-performance --all
analyze-performance --missing-indexes
analyze-performance --slow-queries
analyze-performance --blocking
analyze-performance --io-issues
analyze-performance --days 14 --log-level DEBUG
```

**Arguments**:

| Argument | Type | Default | Description |
|---|---|---|---|
| `--all` | flag | off | Run all four analyses (default if no flag given) |
| `--missing-indexes` | flag | off | Analyze missing index recommendations only |
| `--slow-queries` | flag | off | Analyze slow queries only |
| `--blocking` | flag | off | Analyze blocking events only |
| `--io-issues` | flag | off | Analyze I/O latency only |
| `--days` | int | from config | Override default lookback period |
| `--log-level` | choice | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR` |

**Analysis Details**:

**Missing Indexes** (default: 30-day lookback, 80%+ estimated saving):
- Queries `CON_WHATIF_SRC_1` joined with `CON_FQ_OBJECT_1` and `CONST_1`
- Returns top 50 by estimated saving percentage, then by execution count
- Fields: ID, DateIdentified, SQLHash, Executions, WaitTimeMS, EstimatedSaving%, Database, Schema, Table, IndexName, SQLPreview

**Slow Queries** (default: 7-day lookback, 100K+ buffer gets):
- Queries `CONSS_1` aggregated by SQL hash
- Returns top 50 by total buffer gets
- Fields: SQLHash, TotalExecutions, TotalDiskReads, TotalBufferGets, TotalRowsReturned, AvgBufferGetsPerExec, AvgDiskReadsPerExec, SQLPreview

**Blocking Events** (default: 30-day lookback, 1+ hour minimum):
- Queries `CON_BLOCKING_SUM_1` joined with `CONM_1`
- Returns top 50 by blockee time descending
- Dimension types: P=Program, D=Database, E=Event/Wait Type

**I/O Issues** (default: 24-hour lookback, 50ms+ latency):
- Queries `CON_IO_DETAIL_1`
- Returns top 100 by date descending, filtered to problematic latency periods

**Output Files**:

| File | Description |
|---|---|
| `output/performance/missing_indexes.csv` | Missing index recommendations |
| `output/performance/slow_queries.csv` | Slow query statistics |
| `output/performance/blocking_events.csv` | Blocking event history |
| `output/performance/io_issues.csv` | I/O latency measurements |
| `output/performance/performance_report.txt` | Executive summary (top 5 of each category) |

---

### 3.4 `generate_final_performance_report.py`

Generates a comprehensive before/after performance report by comparing a baseline snapshot against current metrics. Intended as the culminating report after a performance optimization initiative.

**File**: `C:\EDS\scripts\generate_final_performance_report.py`

**Usage**:
```bash
generate-report
generate-report --baseline output/performance/baseline_2025-12-04.json
generate-report --output-dir custom_output/
```

**Arguments**:

| Argument | Default | Description |
|---|---|---|
| `--baseline` | Auto-detected (most recent in output dir) | Path to baseline JSON from `capture-baseline` |
| `--output-dir` | `output/performance` | Directory to read baseline from if not specified |

**What It Computes**:

For each metric, improvement is calculated as `(baseline - current) / baseline * 100`:

| Metric | Direction | Calculation Source |
|---|---|---|
| High-impact missing indexes (>95% saving) | Lower is better | `CON_WHATIF_SRC_1` |
| Blocking hours per week | Lower is better | `CON_BLOCKING_SUM_1` |
| Average I/O read latency (ms) | Lower is better | `CON_IO_DETAIL_1` |
| Slow query count (>10M buffer gets) | Lower is better | `CON_QUERY_PLAN_1` |

**Output Files**:

| File | Description |
|---|---|
| `docs/PERFORMANCE_OPTIMIZATION_REPORT.md` | Full markdown report with before/after tables |
| `output/performance/final_metrics_comparison.json` | Machine-readable comparison data |
| `output/performance/final_metrics_comparison.xlsx` | Formatted Excel spreadsheet (requires `openpyxl`) |

The markdown report follows a standard format: executive summary table, per-metric section with problem statement and action taken, implementation timeline, and ongoing recommendations.

---

## 4. Index Management Scripts

The index management workflow follows a strict four-phase pipeline. Each phase has a dedicated script and produces outputs consumed by the next phase.

### 4.1 Pipeline Overview

```
Phase 1: Extract Recommendations
    extract_missing_indexes.py  →  missing_indexes_full.json

Phase 2: Generate SQL Scripts
    generate_index_scripts.py   →  create_missing_indexes_top_10.sql
                                →  drop_missing_indexes_top_10.sql (rollback)
                                →  index_implementation_plan.md

Phase 3: Deploy to Test
    deploy_indexes_test.py      →  index_deployment_test_log.json
                                →  index_deployment_test_summary.txt

Phase 4a: Validate
    validate_index_performance.py  →  index_validation_results.json
                                   →  index_validation_report.md

Phase 4b: Deploy to Production (after validation passes)
    deploy_indexes_production.py   →  index_deployment_production_log.json
                                   →  index_deployment_production_summary.txt
```

### 4.2 `extract_missing_indexes.py`

Queries `dpa_EDSAdmin` for top missing index recommendations and exports in three formats for downstream consumption.

**File**: `C:\EDS\scripts\extract_missing_indexes.py`

**Usage**:
```bash
extract-indexes
extract-indexes --days 30 --min-saving 90
extract-indexes --days 7 --min-saving 95 --log-level DEBUG
```

**Arguments**:

| Argument | Default | Description |
|---|---|---|
| `--days` | `30` | Lookback period in days (1-365) |
| `--min-saving` | `90` | Minimum estimated saving percentage (0-100) |
| `--log-level` | `INFO` | Logging verbosity |

**Query**: Selects top 50 from `CON_WHATIF_SRC_1` joined to `CON_FQ_OBJECT_1` (object details) and `CONST_1` (SQL text), ordered by estimated saving DESC then executions DESC.

**Full Fields Extracted**:

| Field | Source | Description |
|---|---|---|
| ID | `CON_WHATIF_SRC_1.ID` | Recommendation identifier |
| DateIdentified | `CON_WHATIF_SRC_1.D` | When DPA first identified this |
| QueryHash | `CON_WHATIF_SRC_1.SQL_HASH` | Hash identifying the triggering query |
| Executions | `CON_WHATIF_SRC_1.SQL_EXECS` | How many times the query ran |
| WaitTimeMS | `CON_WHATIF_SRC_1.SQL_WAIT` | Cumulative wait time without index |
| EstimatedSavingPercent | `CON_WHATIF_SRC_1.EST_SAVING` | DPA's what-if improvement estimate |
| DatabaseName | `CON_FQ_OBJECT_1.ODATABASE` | Target database |
| SchemaName | `CON_FQ_OBJECT_1.OSCHEMA` | Target schema |
| TableName | `CON_FQ_OBJECT_1.ONAME` | Target table |
| IndexColumns | `CON_FQ_OBJECT_1.OINDEX_COLUMNS` | Suggested index key columns |
| IncludedColumns | `CON_FQ_OBJECT_1.OINDEX_INCLUDED_COLUMNS` | Suggested INCLUDE columns |
| SQLText | `CONST_1.ST` | First 1000 chars of triggering SQL |

**Output Files**:

| File | Format | Description |
|---|---|---|
| `output/performance/missing_indexes_top_50.csv` | CSV | Subset of fields for quick review |
| `output/performance/missing_indexes_top_50.xlsx` | Excel | Formatted with header styling (requires `openpyxl`) |
| `output/performance/missing_indexes_full.json` | JSON | Full data including SQL text; consumed by `generate_index_scripts.py` |

---

### 4.3 `generate_index_scripts.py`

Reads the JSON from `extract_missing_indexes.py` and generates ready-to-execute CREATE INDEX SQL scripts along with matching DROP INDEX rollback scripts and an implementation plan document.

**File**: `C:\EDS\scripts\generate_index_scripts.py`

**Usage**:
```bash
generate-index-scripts
generate-index-scripts --top 10
generate-index-scripts --top 25
```

**Arguments**:

| Argument | Default | Description |
|---|---|---|
| `--top` | `10` | Number of top recommendations to generate scripts for |

**Input**: `output/performance/missing_indexes_full.json` (must run `extract-indexes` first).

**Generated CREATE INDEX Statement Format**:

```sql
USE [DatabaseName];
GO

CREATE NONCLUSTERED INDEX [IX_TableName_Columns]
ON [schema].[table] ([col1], [col2])
INCLUDE ([col3], [col4])
WITH (
    ONLINE = ON,           -- Zero downtime (Enterprise Edition only)
    FILLFACTOR = 90,       -- Leave 10% free space for future inserts
    PAD_INDEX = ON,        -- Apply fillfactor to index pages
    SORT_IN_TEMPDB = ON,   -- Reduce load on user database
    STATISTICS_NORECOMPUTE = OFF
);
GO
```

Index names are generated as `IX_{TableName}_{KeyColumns}` (truncated to 50 chars for key column portion) if DPA did not supply a name.

**Output Files**:

| File | Description |
|---|---|
| `output/performance/create_missing_indexes_top_N.sql` | CREATE INDEX script for top N |
| `output/performance/drop_missing_indexes_top_N.sql` | Matching DROP INDEX rollback script |
| `output/performance/create_missing_indexes_all.sql` | CREATE INDEX script for all extracted recommendations |
| `output/performance/index_implementation_plan.md` | Markdown plan with 4-phase deployment approach, risk mitigation, success metrics |

**Important Notes**:
- `ONLINE = ON` requires SQL Server Enterprise or Developer Edition. The production deployer checks edition before running.
- The rollback script (`drop_missing_indexes_top_N.sql`) uses `DROP INDEX IF EXISTS` to be idempotent.
- Review each generated script before executing. The index name algorithm is deterministic — CREATE and DROP scripts use the same name generation, ensuring they always match.

---

### 4.4 `deploy_indexes_test.py`

Executes the generated CREATE INDEX script in a test or development environment. Supports dry-run mode for validation without execution. Maintains connection cache to avoid reconnecting when deploying across multiple databases.

**File**: `C:\EDS\scripts\deploy_indexes_test.py`

**Usage**:
```bash
deploy-indexes-test
deploy-indexes-test --script create_missing_indexes_top_10.sql
deploy-indexes-test --script create_missing_indexes_top_10.sql --dry-run
```

**Arguments**:

| Argument | Default | Description |
|---|---|---|
| `--script` | `create_missing_indexes_top_10.sql` | Filename within `output/performance/` |
| `--dry-run` | false | Parse and validate SQL without executing |

**Pre-Execution Checks** (per database):
- Estimates index size as approximately 15% of table size (via `sys.allocation_units`)
- Checks available database file space (via `sys.database_files`)
- Logs estimated size before each index creation

**Execution**: Each CREATE INDEX batch is executed as a non-query via `db.execute_non_query()`. The script records start time, end time, and duration for each index.

**Deployment Log Structure** (`index_deployment_test_log.json`):
```json
{
  "deployment_date": "2025-12-05T10:30:00",
  "script": "create_missing_indexes_top_10.sql",
  "total_indexes": 10,
  "successful": 9,
  "failed": 1,
  "dry_run": 0,
  "results": [
    {
      "database": "EDS",
      "schema": "dbo",
      "table": "Items",
      "index_name": "IX_Items_VendorId_Active",
      "estimated_improvement": 99.985,
      "start_time": "2025-12-05T10:30:05",
      "end_time": "2025-12-05T10:30:47",
      "status": "success",
      "duration_seconds": 42.1,
      "error": null
    }
  ]
}
```

**Exit Code**: Returns 1 if any index creation failed, 0 if all succeeded.

**Output Files**:

| File | Description |
|---|---|
| `output/performance/index_deployment_test_log.json` | Per-index results (input for `validate-indexes`) |
| `output/performance/index_deployment_test_summary.txt` | Human-readable summary |

---

### 4.5 `validate_index_performance.py`

Reads the deployment log from `deploy_indexes_test.py` and validates each deployed index by checking existence, usage statistics, fragmentation, and size. Generates a markdown report categorizing indexes as in-use, created-but-not-used, not-found, or errored.

**File**: `C:\EDS\scripts\validate_index_performance.py`

**Usage**:
```bash
validate-indexes
validate-indexes --log index_deployment_test_log.json
validate-indexes --log-level DEBUG
```

**Arguments**:

| Argument | Default | Description |
|---|---|---|
| `--log` | `index_deployment_test_log.json` | Deployment log filename within `output/performance/` |
| `--log-level` | `INFO` | Logging verbosity |

**Validation Checks Per Index** (via SQL Server DMVs):

| Check | DMV/Table | Metric |
|---|---|---|
| Existence | `sys.indexes`, `sys.tables`, `sys.schemas` | Type, disabled flag, hypothetical flag, statistics date |
| Usage | `sys.dm_db_index_usage_stats` | User seeks, scans, lookups, updates, last access timestamps |
| Fragmentation | `sys.dm_db_index_physical_stats` | Avg fragmentation %, fragment count, page count |
| Size | `sys.allocation_units` via `sys.partitions` | Total size in MB |

**Index Status Classification**:

| Status | Condition |
|---|---|
| `in_use` | `total_reads` (seeks + scans + lookups) > 0 |
| `created_not_used` | Exists but no reads yet |
| `fragmented` | Exists, no reads, fragmentation >30% |
| `not_found` | Cannot be found in `sys.indexes` |
| `error` | Connection or query error during validation |

**Output Files**:

| File | Description |
|---|---|
| `output/performance/index_validation_results.json` | Structured validation data per index |
| `output/performance/index_validation_report.md` | Markdown report with tables by status |

**Recommendation**: Run this script 24-48 hours after test deployment to allow queries to use the new indexes. An index that remains in `created_not_used` status for 7+ days may not be needed.

---

### 4.6 `deploy_indexes_production.py`

Production-grade deployer with additional safety controls: SQL Server edition check, duplicate index detection, an interactive confirmation prompt requiring the user to type `DEPLOY`, and comprehensive deployment logging.

**File**: `C:\EDS\scripts\deploy_indexes_production.py`

**Usage**:
```bash
deploy-indexes-prod
deploy-indexes-prod --script create_missing_indexes_top_10.sql
deploy-indexes-prod --confirm    # Skip interactive prompt (use with caution)
```

**Arguments**:

| Argument | Default | Description |
|---|---|---|
| `--script` | `create_missing_indexes_top_10.sql` | Filename within `output/performance/` |
| `--confirm` | false | Skip interactive `DEPLOY` confirmation prompt |

**Pre-Deployment Validation Checks** (run before any execution):

1. **SQL Edition Check**: Queries `SERVERPROPERTY('Edition')` to detect whether `ONLINE = ON` is supported (Enterprise or Developer editions only). If not supported, logs a warning — the script does not automatically modify the SQL; the DBA must edit the generated scripts to remove `ONLINE = ON` before using Standard Edition.
2. **Duplicate Index Check**: Queries `sys.indexes` per database to confirm none of the target index names already exist. If any exist, the check fails and deployment is aborted.
3. **Disk Space Check**: Verifies available space in `sys.database_files` with a 50% buffer above required space.

**Interactive Confirmation**:
```
PRODUCTION DEPLOYMENT CONFIRMATION
================================================================================
You are about to deploy 10 indexes to PRODUCTION

Indexes to be created:
  - EDS.dbo.Items.IX_Items_VendorId_Active
  - EDS.dbo.CrossRefs.IX_CrossRefs_ItemId_CatalogId
  ... and 8 more

================================================================================
WARNING: This will modify production databases!
================================================================================

Type 'DEPLOY' to confirm:
```

**Output Files**:

| File | Description |
|---|---|
| `output/performance/index_deployment_production_log.json` | Full deployment log (same structure as test log, plus `"environment": "PRODUCTION"`) |
| `output/performance/index_deployment_production_summary.txt` | Human-readable summary with post-deployment task checklist |

---

## 5. Blocking Investigation

### 5.1 `investigate_blocking_event.py`

Deep-dive analysis of blocking events on a specific date. The script generates three output artifacts: a raw JSON analysis, a markdown investigation report, and a remediation plan document.

**File**: `C:\EDS\scripts\investigate_blocking_event.py`

**Usage**:
```bash
investigate-blocking --date 2025-05-10
investigate-blocking --date 2025-05-10 --hours 24
investigate-blocking --date 2025-01-06 --hours 12
```

**Arguments**:

| Argument | Required | Default | Description |
|---|---|---|---|
| `--date` | Yes | — | Date to investigate (YYYY-MM-DD format) |
| `--hours` | No | `24` | Number of hours to analyze from the start of that date |

**Analysis Performed**:

The script queries `CON_BLOCKING_SUM_1` for the specified date/time window and computes:

1. **Overall Summary**: Total event count, cumulative blockee hours, blocker hours, root impact hours, and maximum single event duration.

2. **Breakdown by Dimension Type**: Groups events by DPA dimension type:
   - `P` = Program/Application (the application connecting to SQL Server)
   - `D` = Database
   - `E` = Event/Wait Type
   - `U` = User

3. **Top 10 Blockers**: Ranks unique blocker entities by total blockee time they caused, showing event count, total blockee hours, and maximum single event hours.

**Severity Assessment**: If total blockee hours exceed 100, the report marks the event as CRITICAL and highlights immediate action items.

**Output Files**:

| File | Description |
|---|---|
| `output/performance/blocking_event_YYYY-MM-DD_analysis.json` | Raw analysis data with all events |
| `output/performance/blocking_event_YYYY-MM-DD_report.md` | Structured investigation report with root cause analysis and recommended actions tiered by immediacy |
| `output/performance/blocking_remediation_plan.md` | Standalone remediation playbook covering 5 strategies |

**Remediation Plan Contents** (`blocking_remediation_plan.md`):

| Strategy | Description |
|---|---|
| 1. READ_COMMITTED_SNAPSHOT | Enable row versioning to eliminate read/write blocking |
| 2. Transaction Duration Optimization | Batch commits, minimize lock hold time |
| 3. Query Hints | NOLOCK for reporting, READPAST for queue processing (with guidance on when not to use each) |
| 4. Blocking Alerts | SQL Agent job T-SQL template |
| 5. Index Optimization | Cross-reference with missing index recommendations |

The remediation plan includes a 4-week implementation timeline and success metrics targeting <1 hour/day total blocking and <5 minute max single event.

---

### 5.2 `enable_snapshot_isolation.sql`

A standalone SQL script that enables `READ_COMMITTED_SNAPSHOT` isolation on the EDS user databases. This is the primary blocking mitigation for read/write conflicts. Run this once after completing the investigation and gaining DBA approval.

**File**: `C:\EDS\scripts\enable_snapshot_isolation.sql`

**Databases Targeted**: `EDS`, `Catalogs`, `VendorBids`, `ContentCentral`

**Pre-Implementation Checks**:
- Verifies tempdb has adequate free space (script recommends 50 GB minimum)
- Shows current snapshot isolation status for all user databases before making changes

**Command Pattern** (for each database):
```sql
ALTER DATABASE [EDS]
SET READ_COMMITTED_SNAPSHOT ON
WITH ROLLBACK IMMEDIATE;
```

`WITH ROLLBACK IMMEDIATE` kills any active connections to the database at the moment of the `ALTER`. Schedule this during a low-traffic window.

**Post-Implementation Monitoring Queries** (embedded in script comments):
- `sys.dm_tran_version_store_space_usage` — tempdb version store consumption by database
- `sys.dm_tran_active_snapshot_database_transactions` — long-running snapshot transactions
- `tempdb.sys.database_files` — tempdb file growth over time

**Rollback**: A commented-out rollback block is included at the end of the file. To revert, uncomment and run the `SET READ_COMMITTED_SNAPSHOT OFF` statements.

---

## 6. SQL Agent Alert Jobs

Three SQL Server Agent jobs provide proactive alerting without requiring DBA manual monitoring. All three use Database Mail (`sp_send_dbmail`) to send HTML-formatted email alerts.

**Location**: `C:\EDS\scripts\sql_agent_jobs\`

### 6.1 Prerequisites

Before installing any alert job:
1. Database Mail must be configured on the SQL Server instance.
2. The mail profile name must match what is configured (default: `Default` — update if different).
3. Email addresses must be updated from the placeholder values in each script.
4. The scripts must be executed directly in SSMS or via `sqlcmd` against `msdb`.

Each script is idempotent: if the job already exists, it drops and recreates it. The `DBATeam` operator is only created if it does not already exist.

---

### 6.2 `blocking_alert_job.sql`

**Purpose**: Alert the DBA team when active blocking exceeds 5 minutes.

**File**: `C:\EDS\scripts\sql_agent_jobs\blocking_alert_job.sql`

| Property | Value |
|---|---|
| Job Name | `Alert - Blocking Events` |
| Schedule | Every 15 minutes, 24/7 |
| Alert Operator | `DBATeam` (email: `dba-team@company.com`) |
| Threshold | `BLEETIMESECS > 300` (5+ minutes blocking) in last 15 minutes |
| Alert Method | HTML email via Database Mail |
| Job Owner | `sa` |

**Logic**: Queries `dpa_EDSAdmin.dbo.CON_BLOCKING_SUM_1` for events in the last 15 minutes where blockee time exceeds 300 seconds. If any qualify, sends an HTML email with a summary table showing the top 5 blocking events (time, type, name, blockee hours).

**Alert Email Contains**:
- Server name and alert time
- Total blocking event count and cumulative blocking minutes
- Top 5 events table: time, dimension type, entity name, blockee hours

**Post-Installation Steps**:
1. Update email address (line: `@email_address = N'dba-team@company.com'`)
2. Verify Database Mail profile name (line: `@profile_name = 'Default'`)
3. Test: `EXEC msdb.dbo.sp_start_job @job_name = 'Alert - Blocking Events'`
4. Verify: `EXEC msdb.dbo.sp_help_jobhistory @job_name = 'Alert - Blocking Events'`

---

### 6.3 `missing_index_alert_job.sql`

**Purpose**: Send a daily morning digest of newly identified high-impact missing index recommendations.

**File**: `C:\EDS\scripts\sql_agent_jobs\missing_index_alert_job.sql`

| Property | Value |
|---|---|
| Job Name | `Alert - Missing Indexes` |
| Schedule | Daily at 8:00 AM |
| Alert Operator | `DBATeam` (email: `dba-team@company.com`) |
| Threshold | `EST_SAVING > 95%` identified in last 24 hours |
| Alert Method | HTML email via Database Mail |
| Job Owner | `sa` |

**Logic**: Counts rows in `dpa_EDSAdmin.dbo.CON_WHATIF_SRC_1` with `D >= DATEADD(day, -1, GETDATE())` and `EST_SAVING > 95`. If any qualify, sends an HTML email listing the top 10.

**Alert Email Contains**:
- New high-impact index count (>95% estimated improvement)
- Top 10 table: date identified, database, table, estimated saving %, execution count
- Recommended action checklist (extract → review plans → generate scripts → test → schedule production)

**Design Note**: This job fires only when the threshold is met. On healthy days with no new high-impact recommendations, no email is sent. This avoids alert fatigue from "all-clear" messages.

---

### 6.4 `io_latency_alert_job.sql`

**Purpose**: Alert the on-call DBA when I/O latency spikes to levels that indicate a storage emergency. This is the most time-sensitive alert and runs most frequently.

**File**: `C:\EDS\scripts\sql_agent_jobs\io_latency_alert_job.sql`

| Property | Value |
|---|---|
| Job Name | `Alert - I/O Latency` |
| Schedule | Every 5 minutes, 24/7 |
| Alert Operator | `DBAOnCall` (email: `dba-oncall@company.com`) |
| CC Recipient | `DBATeam` (`dba-team@company.com`) |
| Threshold | Avg read latency >100ms OR max read latency >500ms in last 10 minutes |
| Alert Method | High-priority HTML email via Database Mail |
| Job Owner | `sa` |

**Severity Classification**:

| Severity | Trigger |
|---|---|
| CRITICAL | Max read latency >500ms |
| HIGH | Avg read latency >200ms |
| WARNING | Avg read latency >100ms (but max <500ms) |

**Logic**: Aggregates `AVG` and `MAX` of `READ_LATENCY` and `WRITE_LATENCY` from `dpa_EDSAdmin.dbo.CON_IO_DETAIL_1` for the last 10 minutes. Sends alert only when threshold is exceeded.

**Alert Email Contains**:
- Severity level and color-coded status
- Avg and max read/write latency for last 10 minutes, with per-metric status
- Latency interpretation guide (excellent <10ms, acceptable 10-50ms, concerning 50-100ms, critical >100ms)
- 6-step recommended action checklist (check SAN, disk queue lengths, blocking, tempdb, RAID cache, monitor)
- Ready-to-run diagnostic query for `CON_IO_DETAIL_1`

**Post-Installation**: Configure pager or SMS integration via the `@pager_address` parameter on the `DBAOnCall` operator for true on-call escalation.

**Warning**: With a 5-minute schedule, if I/O issues persist, this job will send a high-volume of emails. Consider adding alert suppression logic (track last alert time in a dedicated table) if sustained latency issues are expected.

---

## 7. Alert Dashboard

### 7.1 `generate_alert_dashboard.py`

Generates two files from templates: the `alert_dashboard.sql` SQL query used for daily monitoring, and the `DAILY_MONITORING_GUIDE.md` operations guide. Both files are regenerated each time this script runs.

**File**: `C:\EDS\scripts\generate_alert_dashboard.py`

**Usage**:
```bash
generate-dashboard
python scripts/generate_alert_dashboard.py
```

**No arguments.**

**Output Files**:

| File | Description |
|---|---|
| `scripts/alert_dashboard.sql` | Complete SQL dashboard query |
| `docs/guides/DAILY_MONITORING_GUIDE.md` | Operations guide for the dashboard |

**When to Regenerate**: Re-run if threshold values in `config.yaml` change, if section logic needs updating, or after adding new monitoring dimensions. The script is idempotent — output files are always overwritten.

---

### 7.2 `alert_dashboard.sql`

The primary daily operations tool. Run this in SSMS or via `sqlcmd` each morning to get an overnight performance summary. The file is generated by `generate_alert_dashboard.py` and checked into source control.

**File**: `C:\EDS\scripts\alert_dashboard.sql`

**Target Database**: `dpa_EDSAdmin`

**Execution**:
```bash
# Via sqlcmd
sqlcmd -S eds-sqlserver.eastus2.cloudapp.azure.com -d dpa_EDSAdmin `
       -U EDSAdmin -P <password> `
       -i scripts/alert_dashboard.sql

# Via PowerShell
Invoke-Sqlcmd -ServerInstance "eds-sqlserver.eastus2.cloudapp.azure.com" `
              -Database "dpa_EDSAdmin" `
              -InputFile "scripts/alert_dashboard.sql"
```

**Dashboard Sections**:

**Section 1 — New Missing Indexes (Last 24 Hours)**:
- Shows top 20 with >=50% estimated saving
- Classifies each as CRITICAL (>95%), HIGH (80-95%), MEDIUM (50-80%)
- Summary line: count of CRITICAL (>95%) new indexes

**Section 2 — Blocking Events (Last 24 Hours)**:
- Shows top 15 events with >1 minute blockee time
- Classifies as CRITICAL (>1 hour), HIGH (5-60 min), MEDIUM (1-5 min)
- Summary line: count and total hours

**Section 3 — I/O Latency Spikes (Last 24 Hours)**:
- Shows top 20 periods with >50ms read or write latency
- Classifies as CRITICAL (>200ms), HIGH (>100ms), MEDIUM (50-100ms)
- Summary line: high latency event count, max and avg

**Section 4 — Slow Queries (Last 24 Hours)**:
- Shows top 15 queries with >10M buffer gets
- Classifies as CRITICAL (>100M), HIGH (10M-100M)
- Summary line: distinct slow query count

**Section 5 — Database Health Summary**:
Computes a 0-100 health score with penalty deductions:

| Condition | Penalty |
|---|---|
| New high-impact indexes >10 | -20 |
| New high-impact indexes >5 | -10 |
| Total blocking hours >5 | -25 |
| Total blocking hours >1 | -10 |
| High I/O latency events >100 | -25 |
| High I/O latency events >50 | -15 |
| Slow queries >20 | -20 |
| Slow queries >10 | -10 |

**Health Score Interpretation**:

| Score | Status | Action |
|---|---|---|
| 90-100 | EXCELLENT | No action required |
| 75-89 | GOOD | Address during regular maintenance |
| 60-74 | FAIR | Prioritize remediation this week |
| 40-59 | POOR | Immediate action required |
| 0-39 | CRITICAL | Escalate to senior DBA |

---

## 8. Schema Explorer

### 8.1 `schema_explorer.py`

An interactive Streamlit web application for browsing SQL Server database schemas. Unlike the monitoring scripts which query `dpa_EDSAdmin`, this tool connects to any configured SQL Server database and provides a visual exploration interface.

**File**: `C:\EDS\scripts\schema_explorer.py`

**Usage**:
```bash
streamlit run scripts/schema_explorer.py
streamlit run scripts/schema_explorer.py --server.port 8081
```

**Requirements** (in addition to base dependencies):
```bash
pip install streamlit pandas openpyxl graphviz
# For dependency visualization:
# Also install Graphviz system package from https://graphviz.org/download/
```

**Features**:

| Feature | Description |
|---|---|
| Database/Schema/Table Browser | Navigate the full object hierarchy |
| Column Explorer | Types, constraints, nullable flags, extended property descriptions |
| Index Browser | All indexes per table with columns and type |
| Foreign Key Relationships | Inbound and outbound FK relationships |
| Stored Procedure Browser | Browse and view SP definitions |
| Function and Trigger Browser | Browse UDFs and triggers |
| Object Search | Full-text search across all database object names |
| ERD/Relationship Diagrams | Visual relationship diagram generation |
| Excel/CSV Export | Export table schemas to spreadsheets |
| Schema Comparison | Compare schemas between two databases |
| Data Preview | SELECT TOP N from any table |
| Visual Dependency Graphs | Graphviz-based dependency visualization (optional) |

**Configuration**: Reads connection parameters from `.env` file at project root — same `DB_SERVER`, `DB_USERNAME`, `DB_PASSWORD` variables used by the monitoring scripts.

---

## 9. Elasticsearch Integration

### 9.1 `index_elasticsearch.py`

Reads product catalog data from the EDS SQL Server database and indexes denormalized documents into Elasticsearch for the Universal Requisition full-text search feature. This script is distinct from the monitoring scripts — it connects to the `EDS` production database (not `dpa_EDSAdmin`).

**File**: `C:\EDS\scripts\index_elasticsearch.py`

**Usage**:
```bash
python -m scripts.index_elasticsearch
python -m scripts.index_elasticsearch --batch-size 5000
python -m scripts.index_elasticsearch --es-url http://20.122.81.233:9200
python -m scripts.index_elasticsearch --no-recreate
```

**Arguments**:

| Argument | Default | Description |
|---|---|---|
| `--batch-size` | `5000` | Products per SQL Server fetch batch |
| `--es-url` | `ES_URL` env var or `http://localhost:9200` | Elasticsearch cluster URL |
| `--no-recreate` | false | Append to existing index instead of dropping and recreating |

**Environment Variables**:

| Variable | Default | Description |
|---|---|---|
| `ES_URL` | `http://localhost:9200` | Elasticsearch cluster URL |
| `DB_SERVER` | `eds-sqlserver.eastus2.cloudapp.azure.com` | SQL Server hostname |
| `DB_DATABASE_CATALOG` | `EDS` | Product database (falls back to `DB_DATABASE`) |
| `DB_USERNAME` | `EDSAdmin` | SQL authentication username |
| `DB_PASSWORD` | — | SQL authentication password |
| `DB_DRIVER` | `ODBC Driver 18 for SQL Server` | ODBC driver name |

**Target Index**: `eds_products` — index settings (mappings, analyzers) are imported from `api.search.PRODUCT_INDEX_SETTINGS`.

**Data Pipeline** (per batch):

1. Fetch up to `batch_size` products from `Items` joined to `Vendors`, `Units`, `Category` where `Active = 1` and `ListPrice > 0`.
2. Fetch bid/price plan associations from `CrossRefs` joined to `Catalog` for all `ItemId` values in the batch.
3. Fetch first available image URL from `CrossRefs` per item.
4. Build denormalized Elasticsearch document combining all three data sources.
5. Bulk index via `elasticsearch.helpers.bulk()` with error logging.

**Elasticsearch Document Structure**:

```json
{
  "item_id": 12345,
  "item_code": "SS-001234",
  "name": "Product Description",
  "description": "Product Description",
  "short_description": "Short desc",
  "vendor_id": 9,
  "vendor_name": "School Specialty, LLC",
  "vendor_part_number": "SS-001234",
  "category_id": 42,
  "category_name": "Art Supplies",
  "list_price": 12.99,
  "unit_of_measure": "Each",
  "active": true,
  "image_url": "https://...",
  "bid_prices": [
    {"bid_id": 100, "catalog_price": 10.50, "vendor_id": 9}
  ],
  "bid_ids": [100, 200],
  "indexed_at": "2026-03-27T08:00:00+00:00"
}
```

**Progress Reporting**: Logs per-batch stats including product count, bid price associations, image URLs found, and batch duration.

**Production Instance**: The EDS Elasticsearch cluster runs on Azure VM `20.122.81.233:9200` with Elasticsearch 7.15.2. See `docs/wiki/user-activity/` for connection details.

---

## 10. Documentation Generation Scripts

The majority of files in `scripts/` are historical one-time scripts that generated the comprehensive documentation in `/docs/`. They are preserved for re-running when schema changes occur and as reference for how the documentation was built.

### 10.1 Script Inventory

| Script | Output Document(s) |
|---|---|
| `generate_data_dictionary.py` | `docs/EDS_DATA_DICTIONARY.md` |
| `generate_erd.py` | `docs/EDS_ERD.md` |
| `generate_sproc_docs.py` | `docs/EDS_STORED_PROCEDURES.md` |
| `generate_sp_documentation.py` | `docs/EDS_PROCEDURES_GUIDE.md` |
| `generate_sp_dependencies.py` | `docs/EDS_PROCEDURE_DEPENDENCIES.md` |
| `generate_views_docs.py` | `docs/EDS_VIEWS.md` |
| `generate_summary_report.py` | `docs/EDS_SUMMARY.md` |
| `generate_trigger_diagram.py` | `docs/EDS_TRIGGERS.md` |
| `generate_html_report.py` | HTML report variants |
| `generate_master_pdf.py` | `docs/pdf/` — compiled PDF exports |
| `generate_pdf.py` | Per-document PDF generation |
| `generate_docx.py` | Word document exports |
| `document_stored_procedures.py` | SP detail documentation |
| `document_views.py` | View detail documentation |
| `document_view_columns.py` | View column documentation |
| `document_indexes.py` | `docs/EDS_INDEXES.md` |
| `document_archive_schema.py` | `docs/EDS_ARCHIVE_ANALYSIS.md` |
| `document_sp_parameters.py` | SP parameter documentation |
| `document_recursive_procs.py` | `docs/EDS_RECURSIVE_PROCEDURES.md` |
| `document_remaining_columns.py` | Column coverage completion |
| `document_final_columns.py` | Final column documentation pass |
| `analyze_performance_issues.py` | Performance analysis reports |
| `analyze_business_domains.py` | `docs/EDS_BUSINESS_DOMAINS.md` |
| `analyze_archive_schema.py` | Archive schema analysis |
| `analyze_root_procedures.py` | `docs/EDS_ROOT_PROCEDURES.md` |
| `analyze_circular_deps.py` | `docs/EDS_CIRCULAR_DEPS.md` |
| `analyze_undocumented_columns.py` | Column coverage gap analysis |
| `investigate_infinite_loops.py` | `docs/EDS_INFINITE_LOOP_ANALYSIS.md` |
| `add_column_descriptions.py` (v1-v4, final) | Extended properties in SQL Server |
| `generate_extended_properties.py` | Extended property generation |
| `check_coverage.py` | Documentation coverage metrics |
| `refresh_documentation.py` | Documentation refresh coordinator |
| `export_to_excel.py` | Excel schema exports |

### 10.2 Common Pattern

All documentation generation scripts follow this pattern:

```python
from db_utils import DatabaseConnection
from logging_config import setup_logging

def generate_documentation(database='EDS', output_dir='docs'):
    logger = setup_logging('generate_something')
    db = DatabaseConnection(database=database)
    db.connect()

    # Query sys.* catalog views or application tables
    objects = db.execute_query("""
        SELECT name, definition, create_date
        FROM sys.procedures
        ORDER BY name
    """)

    # Write markdown to output_dir
    with open(f'{output_dir}/DOCUMENT.md', 'w') as f:
        f.write(...)

    db.disconnect()
```

The documentation scripts connect to the `EDS` production database (not `dpa_EDSAdmin`) and query SQL Server catalog views (`sys.procedures`, `sys.views`, `sys.columns`, `sys.indexes`, etc.) as well as `INFORMATION_SCHEMA` views.

### 10.3 `validate_implementation.py`

A meta-validation script that checks whether all 16 performance monitoring scripts, SQL Agent jobs, documentation files, and output files exist and are in place. Use this after setting up a new environment or after a major change.

**Usage**:
```bash
python scripts/validate_implementation.py
python scripts/validate_implementation.py --verbose
python scripts/validate_implementation.py --check scripts
python scripts/validate_implementation.py --check database
python scripts/validate_implementation.py --check jobs
```

**Validation Categories**:
- `scripts` — Verifies all required `.py` files exist
- `database` — Tests connectivity to `dpa_EDSAdmin`
- `jobs` — Checks SQL Agent job existence (queries `msdb.dbo.sysjobs`)
- `documentation` — Verifies docs files exist
- `baselines` — Checks for baseline JSON files in `output/performance/`

**Output**: `output/performance/implementation_validation_report.txt`

---

## 11. Utility and Maintenance Scripts

### 11.1 SQL Utilities

| File | Purpose |
|---|---|
| `search_indexes.sql` | Ad-hoc index search queries for SQL Server |
| `po_split_sp_patch.sql` | One-time patch for purchase order splitting stored procedure |

### 11.2 Shell Scripts

| File | Purpose |
|---|---|
| `run_tests.sh` | Run the Python test suite |
| `deploy.sh` | Deployment automation shell script |
| `dev-setup.sh` | Development environment setup |

### 11.3 Specialized Analysis Scripts

| Script | Purpose |
|---|---|
| `orleans_top_items_report.py` | Generate top-items report for Orleans district |
| `po_splitting_analysis.py` | Analyze purchase order splitting patterns |

---

## 12. CLI Entry Points

Installed via `pip install -e .` from `pyproject.toml`. All entry points call the `main()` function of the corresponding module.

| Command | Module | Primary Function |
|---|---|---|
| `capture-baseline` | `scripts.capture_performance_baseline` | Capture point-in-time metrics snapshot |
| `analyze-performance` | `scripts.analyze_performance_issues` | Full performance analysis (4 dimensions) |
| `extract-indexes` | `scripts.extract_missing_indexes` | Extract missing index recommendations to CSV/Excel/JSON |
| `generate-index-scripts` | `scripts.generate_index_scripts` | Generate CREATE/DROP INDEX SQL scripts |
| `deploy-indexes-test` | `scripts.deploy_indexes_test` | Deploy indexes to test environment |
| `deploy-indexes-prod` | `scripts.deploy_indexes_production` | Deploy indexes to production (with confirmation) |
| `investigate-blocking` | `scripts.investigate_blocking_event` | Investigate a specific blocking date |
| `validate-indexes` | `scripts.validate_index_performance` | Validate deployed index usage and health |
| `generate-report` | `scripts.generate_final_performance_report` | Generate before/after comparison report |
| `generate-dashboard` | `scripts.generate_alert_dashboard` | Regenerate dashboard SQL and monitoring guide |
| `eds-agent` | `agent.main` | DBA Agent CLI (natural language SQL) |
| `eds-agent-gui` | `agent.gui.app` | DBA Agent GUI |
| `eds-api` | `api.main` | Universal Requisition API server |

**Installation**:
```bash
# Install with monitoring extras only
pip install -e ".[export]"    # Adds openpyxl for Excel output

# Install with dashboard
pip install -e ".[dashboard]" # Adds streamlit

# Install everything
pip install -e ".[all]"
```

---

## 13. Configuration Reference

### 13.1 `config.yaml`

Located at `C:\EDS\config.yaml` (project root). Loaded automatically by `config.py`. All values have compiled defaults so the file is optional, but strongly recommended for production use.

```yaml
database:
  name: dpa_EDSAdmin    # Primary monitoring database
  timeout: 30           # Connection timeout in seconds

thresholds:
  missing_index:
    critical: 95        # >= 95% estimated saving is CRITICAL
    high: 80            # >= 80% is HIGH
    medium: 50          # >= 50% is MEDIUM
    min_executions: 100 # Ignore recommendations from rarely-run queries

  blocking:
    critical_seconds: 3600  # 1 hour = CRITICAL
    high_seconds: 300       # 5 minutes = HIGH
    medium_seconds: 60      # 1 minute = MEDIUM

  io_latency:
    critical_ms: 200   # >= 200ms read latency = CRITICAL
    high_ms: 100       # >= 100ms = HIGH
    medium_ms: 50      # >= 50ms = MEDIUM

  slow_query:
    critical_buffer_gets: 10000000   # 10M logical reads = CRITICAL
    high_buffer_gets: 1000000        # 1M = HIGH
    min_buffer_gets: 100000          # Minimum to report

analysis:
  missing_indexes_days: 30    # Default lookback for index analysis
  slow_queries_days: 7        # Default lookback for slow query analysis
  blocking_days: 30           # Default lookback for blocking analysis
  io_issues_hours: 24         # Default lookback for I/O analysis
  top_results: 50             # Max rows returned per analysis
  report_top: 10              # Items in summary sections

dashboard:
  refresh_interval: 30        # Streamlit auto-refresh seconds
  health_score:
    critical_index_penalty: 20
    high_index_penalty: 10
    blocking_penalty: 15
    io_latency_penalty: 10
    slow_query_penalty: 5

output:
  directory: output/performance      # Main output (CSVs, JSONs, reports)
  exports_directory: output/exports  # Excel exports
  log_directory: logs               # Log files

alerts:
  email: dba-team@company.com   # Update to your team email
  mail_profile: Default          # Database Mail profile name
  enabled: true

logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  max_file_size_mb: 10
  backup_count: 5
```

### 13.2 `.env` File

Located at `C:\EDS\.env`. Required for database connectivity. Copy from `.env.example` to get started.

```bash
# SQL Server connection (used by all monitoring scripts)
DB_SERVER=eds-sqlserver.eastus2.cloudapp.azure.com
DB_DATABASE=dpa_EDSAdmin        # Monitoring database (scripts default)
DB_DATABASE_CATALOG=EDS         # Production catalog (index_elasticsearch.py)
DB_USERNAME=EDSAdmin
DB_PASSWORD=<secret>

# Optional overrides
DB_TIMEOUT=30
LOG_LEVEL=INFO
ALERT_EMAIL=dba-team@company.com

# Threshold overrides (override config.yaml values)
THRESHOLD_MISSING_INDEX_CRITICAL=95
THRESHOLD_BLOCKING_CRITICAL_SECONDS=3600

# Elasticsearch (for index_elasticsearch.py)
ES_URL=http://20.122.81.233:9200
```

### 13.3 Configuration Priority

When the same setting can be set in multiple places, the priority order is:

```
Environment variable  (highest - always wins)
    ↓
config.yaml value
    ↓
Compiled default in config.py  (lowest - fallback)
```

This design allows:
- Production deployments to use environment variables for secrets
- `config.yaml` for team-standard operational thresholds
- Compiled defaults as safe fallbacks when the config file is absent

---

## 14. Output File Reference

All scripts write to paths within the project root. Directories are created automatically if they do not exist.

### 14.1 Performance Analysis Outputs (`output/performance/`)

| File | Generated By | Description |
|---|---|---|
| `baseline_YYYY-MM-DD.json` | `capture-baseline` | Point-in-time metric snapshot (JSON) |
| `baseline_YYYY-MM-DD.txt` | `capture-baseline` | Human-readable baseline report |
| `missing_indexes.csv` | `analyze-performance` | Missing index recommendations |
| `slow_queries.csv` | `analyze-performance` | Slow query statistics |
| `blocking_events.csv` | `analyze-performance` | Blocking event history |
| `io_issues.csv` | `analyze-performance` | I/O latency measurements |
| `performance_report.txt` | `analyze-performance` | Executive summary (top 5 of each) |
| `missing_indexes_top_50.csv` | `extract-indexes` | Top 50 missing indexes |
| `missing_indexes_top_50.xlsx` | `extract-indexes` | Excel version (styled) |
| `missing_indexes_full.json` | `extract-indexes` | Full data with SQL text (input for script generator) |
| `create_missing_indexes_top_N.sql` | `generate-index-scripts` | CREATE INDEX script |
| `drop_missing_indexes_top_N.sql` | `generate-index-scripts` | Rollback DROP INDEX script |
| `create_missing_indexes_all.sql` | `generate-index-scripts` | All recommendations |
| `index_implementation_plan.md` | `generate-index-scripts` | 4-phase deployment plan |
| `index_deployment_test_log.json` | `deploy-indexes-test` | Per-index deployment results |
| `index_deployment_test_summary.txt` | `deploy-indexes-test` | Human-readable test deployment summary |
| `index_validation_results.json` | `validate-indexes` | Per-index validation data |
| `index_validation_report.md` | `validate-indexes` | Markdown validation report |
| `index_deployment_production_log.json` | `deploy-indexes-prod` | Production deployment results |
| `index_deployment_production_summary.txt` | `deploy-indexes-prod` | Human-readable production summary |
| `blocking_event_YYYY-MM-DD_analysis.json` | `investigate-blocking` | Raw blocking analysis data |
| `blocking_event_YYYY-MM-DD_report.md` | `investigate-blocking` | Markdown investigation report |
| `blocking_remediation_plan.md` | `investigate-blocking` | Remediation playbook |
| `final_metrics_comparison.json` | `generate-report` | Before/after comparison (JSON) |
| `final_metrics_comparison.xlsx` | `generate-report` | Before/after comparison (Excel) |
| `implementation_validation_report.txt` | `validate_implementation.py` | Implementation checklist results |

### 14.2 Documentation Outputs (`docs/`)

| File | Generated By Script |
|---|---|
| `docs/PERFORMANCE_OPTIMIZATION_REPORT.md` | `generate-report` |
| `docs/guides/DAILY_MONITORING_GUIDE.md` | `generate-dashboard` |
| `docs/EDS_DATA_DICTIONARY.md` | `generate_data_dictionary.py` |
| `docs/EDS_STORED_PROCEDURES.md` | `generate_sproc_docs.py` |
| `docs/EDS_VIEWS.md` | `generate_views_docs.py` |
| `docs/EDS_INDEXES.md` | `document_indexes.py` |
| `docs/EDS_ERD.md` | `generate_erd.py` |
| `docs/EDS_TRIGGERS.md` | `generate_trigger_diagram.py` |
| `docs/EDS_SUMMARY.md` | `generate_summary_report.py` |

### 14.3 Log Files (`logs/`)

Each script creates a dedicated rotating log file:

| Log File | Script |
|---|---|
| `logs/analyze_performance.log` | `analyze_performance_issues.py` |
| `logs/capture_performance_baseline.log` | `capture_performance_baseline.py` |
| `logs/extract_missing_indexes.log` | `extract_missing_indexes.py` |
| `logs/generate_final_performance_report.log` | `generate_final_performance_report.py` |
| `logs/deploy_indexes_test.log` | `deploy_indexes_test.py` |
| `logs/deploy_indexes_production.log` | `deploy_indexes_production.py` |
| `logs/validate_index_performance.log` | `validate_index_performance.py` |
| `logs/investigate_blocking_event.log` | `investigate_blocking_event.py` |
| `logs/generate_alert_dashboard.log` | `generate_alert_dashboard.py` |

Log files rotate at 10 MB and keep 5 backup files (configurable in `config.yaml`).

---

## 15. Workflow Guide

### 15.1 Standard Index Optimization Workflow

This is the recommended sequence for implementing missing index recommendations. Each step depends on the previous step's output files.

```
Week 1: Discovery
─────────────────
1. capture-baseline
   → Saves baseline_YYYY-MM-DD.json

2. analyze-performance --all
   → Saves CSV reports, performance_report.txt

3. extract-indexes --days 30 --min-saving 90
   → Saves missing_indexes_full.json

4. generate-index-scripts --top 10
   → Saves create_missing_indexes_top_10.sql

Week 2: Test Deployment
───────────────────────
5. deploy-indexes-test --dry-run   # Validate script parsing first

6. deploy-indexes-test             # Execute in test environment
   → Saves index_deployment_test_log.json

7. validate-indexes                # Run 24-48 hours after deployment
   → Saves index_validation_report.md

Week 3-4: Production
─────────────────────
8. deploy-indexes-prod             # Requires typing 'DEPLOY' to confirm
   → Saves index_deployment_production_log.json

9. validate-indexes --log index_deployment_production_log.json

10. generate-report --baseline output/performance/baseline_YYYY-MM-DD.json
    → Saves PERFORMANCE_OPTIMIZATION_REPORT.md
```

### 15.2 Blocking Event Investigation Workflow

```
1. Detect blocking (via alert email from 'Alert - Blocking Events' job,
   or from alert_dashboard.sql Section 2)

2. investigate-blocking --date YYYY-MM-DD --hours 24
   → Saves analysis JSON, investigation report, remediation plan

3. Review output/performance/blocking_event_YYYY-MM-DD_report.md
   - Note the top blocker (program, database, or event type)
   - Follow recommended actions for the severity level

4. If blocking is recurring:
   - Run enable_snapshot_isolation.sql in a maintenance window
   - Review the remediation plan for application-level fixes

5. Monitor for 7 days:
   - Check alert_dashboard.sql Section 2 daily
   - Verify blocking hours decreasing
```

### 15.3 Daily Monitoring Workflow

```
Morning (8:00 AM):
1. Review alert emails from overnight SQL Agent jobs
   - 'Alert - I/O Latency' (every 5 min) — critical storage issues
   - 'Alert - Blocking Events' (every 15 min) — session contention
   - 'Alert - Missing Indexes' (8 AM daily digest)

2. Run alert_dashboard.sql in SSMS against dpa_EDSAdmin
   OR: sqlcmd -S server -d dpa_EDSAdmin -i scripts/alert_dashboard.sql

3. Assess health score:
   - 90+: No action needed
   - 75-89: Schedule maintenance items
   - 60-74: Prioritize this week
   - <60: Immediate investigation required

4. Triage CRITICAL items from each section

Weekly (Friday afternoon):
1. Run validate-indexes to confirm deployed indexes remain healthy
2. Review alert frequency for false positives; tune thresholds in config.yaml
3. Capture trend data and compare health scores across the week

Monthly (First Monday):
1. generate-report   # Comprehensive before/after comparison
2. Index maintenance: identify fragmented indexes (>30%), drop unused
3. Review SQL Agent job history for patterns
```

### 15.4 Threshold Tuning

The thresholds in `config.yaml` are starting points appropriate for a system with EDS's query volume. Over time, adjust based on observed data:

- **Too many CRITICAL missing index alerts**: Raise `thresholds.missing_index.critical` from 95 to 98
- **I/O alerts firing too often for normal operations**: Raise `thresholds.io_latency.high_ms` from 100 to 150
- **Blocking alerts missing real issues**: Lower `thresholds.blocking.high_seconds` from 300 to 120
- **Health score never reaches EXCELLENT**: Adjust penalty values in `dashboard.health_score`

After changing `config.yaml`, re-run `generate-dashboard` to regenerate `alert_dashboard.sql` with the updated thresholds embedded. The SQL Agent jobs require manual updates since their T-SQL is compiled into the job step at installation time.

---

*For related documentation, see:*
- *`/docs/guides/DAILY_MONITORING_GUIDE.md` — Operational monitoring workflow*
- *`/docs/wiki/performance/known-issues/` — Documented performance issues*
- *`/docs/wiki/troubleshooting/blocking.md` — Blocking resolution procedures*
- *`/docs/wiki/troubleshooting/runbooks/` — Emergency runbooks*
- *`/agent/CLAUDE.md` — DBA Agent for natural language database queries*
