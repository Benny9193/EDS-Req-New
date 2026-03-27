# SQL Server Performance Monitoring Tools

A collection of Python scripts for monitoring and optimizing SQL Server performance, specifically designed for the `dpa_EDSAdmin` database.

## Features

- **Performance Analysis** - Identify slow queries, missing indexes, and I/O bottlenecks
- **Index Management** - Extract, generate, and deploy missing indexes with safety checks
- **Blocking Investigation** - Analyze blocking events and generate remediation plans
- **Baseline Capture** - Record performance metrics for before/after comparisons
- **Reporting** - Generate comprehensive performance reports and dashboards

## Installation

### Prerequisites

- Python 3.9+
- SQL Server ODBC Driver 17
- Access to `dpa_EDSAdmin` database

### Install from source

```bash
# Clone the repository
git clone https://github.com/company/sql-server-monitoring.git
cd sql-server-monitoring

# Install in development mode
pip install -e ".[dev]"

# Or install with all optional dependencies
pip install -e ".[all]"
```

### Environment Setup

Create a `.env` file in the project root with your database credentials:

```env
DB_SERVER=your-server.database.windows.net
DB_DATABASE=dpa_EDSAdmin
DB_USERNAME=your_username
DB_PASSWORD=your_password
```

## Quick Start

### 1. Capture Performance Baseline

```bash
capture-baseline
# Or: python scripts/capture_performance_baseline.py
```

### 2. Analyze Performance Issues

```bash
analyze-performance --days 30
# Or: python scripts/analyze_performance_issues.py --days 30
```

### 3. Extract Missing Indexes

```bash
extract-indexes --min-saving 80
# Or: python scripts/extract_missing_indexes.py --min-saving 80
```

### 4. Generate Index Scripts

```bash
generate-index-scripts
# Or: python scripts/generate_index_scripts.py
```

### 5. Deploy Indexes (Test Environment)

```bash
deploy-indexes-test --dry-run
# Or: python scripts/deploy_indexes_test.py --dry-run
```

### 6. Investigate Blocking Events

```bash
investigate-blocking --date 2025-01-09
# Or: python scripts/investigate_blocking_event.py --date 2025-01-09
```

### 7. Generate Final Report

```bash
generate-report
# Or: python scripts/generate_final_performance_report.py
```

## Available Commands

| Command | Script | Description |
|---------|--------|-------------|
| `capture-baseline` | `capture_performance_baseline.py` | Capture current performance metrics |
| `analyze-performance` | `analyze_performance_issues.py` | Analyze performance issues |
| `extract-indexes` | `extract_missing_indexes.py` | Extract missing index recommendations |
| `generate-index-scripts` | `generate_index_scripts.py` | Generate CREATE INDEX SQL scripts |
| `deploy-indexes-test` | `deploy_indexes_test.py` | Deploy indexes to test environment |
| `deploy-indexes-prod` | `deploy_indexes_production.py` | Deploy indexes to production |
| `investigate-blocking` | `investigate_blocking_event.py` | Investigate blocking events |
| `validate-indexes` | `validate_index_performance.py` | Validate index performance |
| `generate-report` | `generate_final_performance_report.py` | Generate comprehensive report |
| `generate-dashboard` | `generate_alert_dashboard.py` | Generate alert dashboard |

## Configuration

Settings are managed in `config.yaml`:

```yaml
database:
  name: dpa_EDSAdmin
  timeout: 30

thresholds:
  missing_index:
    critical: 95
    high: 80
    medium: 50
    min_executions: 100
  blocking:
    critical_seconds: 3600
    high_seconds: 300
    medium_seconds: 60

analysis:
  missing_indexes_days: 30
  slow_queries_days: 7
  top_results: 50
```

Environment variables can override config values:
- `DB_DATABASE` - Database name
- `THRESHOLD_MISSING_INDEX_CRITICAL` - Critical threshold percentage
- `LOG_LEVEL` - Logging level (DEBUG, INFO, WARNING, ERROR)

## Project Structure

```
sql-server-monitoring/
├── scripts/
│   ├── db_utils.py              # Database connection utilities
│   ├── config.py                # Configuration management
│   ├── logging_config.py        # Structured logging
│   ├── analyze_performance_issues.py
│   ├── capture_performance_baseline.py
│   ├── deploy_indexes_test.py
│   ├── deploy_indexes_production.py
│   ├── extract_missing_indexes.py
│   ├── generate_alert_dashboard.py
│   ├── generate_final_performance_report.py
│   ├── generate_index_scripts.py
│   ├── investigate_blocking_event.py
│   └── validate_index_performance.py
├── tests/
│   ├── conftest.py              # Pytest fixtures
│   ├── test_config.py
│   ├── test_db_utils.py
│   ├── test_deploy_indexes.py
│   └── test_investigate_blocking.py
├── docs/
│   └── API_REFERENCE.md         # API documentation
├── output/                      # Generated reports
├── logs/                        # Log files
├── config.yaml                  # Configuration
├── pyproject.toml               # Package configuration
└── README.md
```

## Development

### Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=scripts --cov-report=html

# Run specific test file
pytest tests/test_db_utils.py -v
```

### Code Quality

The codebase follows these practices:
- Parameterized SQL queries to prevent SQL injection
- Context managers for database connections
- Structured logging with file rotation
- Type hints for function signatures
- Comprehensive error handling

## API Reference

See [docs/API_REFERENCE.md](docs/API_REFERENCE.md) for detailed API documentation of shared modules:

- **db_utils** - Database connection and query execution
- **config** - Configuration management with YAML and environment overrides
- **logging_config** - Structured logging setup

## Output Files

Scripts generate output in the `output/` directory:

| File Pattern | Description |
|--------------|-------------|
| `performance_baseline_*.json` | Baseline metrics snapshot |
| `missing_indexes_*.md` | Missing index analysis report |
| `create_indexes_*.sql` | Generated CREATE INDEX scripts |
| `blocking_investigation_*.md` | Blocking event analysis |
| `performance_report_*.md` | Final performance report |

## License

MIT License - See LICENSE file for details.

## Maintainers

DBA Team - dba-team@company.com
