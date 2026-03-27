# SQL Server Monitoring - API Reference

This document provides comprehensive API documentation for the shared modules used across the SQL Server performance monitoring scripts.

---

## Table of Contents

- [db_utils Module](#db_utils-module)
  - [DatabaseConnection Class](#databaseconnection-class)
  - [Convenience Functions](#convenience-functions)
  - [Exceptions](#exceptions)
- [config Module](#config-module)
  - [Config Dataclasses](#config-dataclasses)
  - [Functions](#config-functions)
- [logging_config Module](#logging_config-module)
  - [Functions](#logging-functions)
  - [LogContext Class](#logcontext-class)

---

## db_utils Module

Provides secure, reusable database connection and query execution with SQL injection prevention.

### DatabaseConnection Class

```python
from db_utils import DatabaseConnection
```

#### Constructor

```python
DatabaseConnection(
    database: str = None,      # Database name (default: from DB_DATABASE env var)
    server: str = None,        # Server address (default: from DB_SERVER env var)
    username: str = None,      # Username (default: from DB_USERNAME env var)
    password: str = None,      # Password (default: from DB_PASSWORD env var)
    timeout: int = 30          # Connection timeout in seconds
)
```

#### Context Manager Usage (Recommended)

```python
with DatabaseConnection() as db:
    results = db.execute_query(
        "SELECT * FROM users WHERE status = ?",
        params=("active",)
    )
```

#### Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `connect()` | None | None | Establish database connection |
| `disconnect()` | None | None | Close connection and release resources |
| `execute_query(query, params, fetch_all)` | query: str, params: tuple, fetch_all: bool | List[tuple] | Execute SELECT query with parameters |
| `execute_non_query(query, params, commit)` | query: str, params: tuple, commit: bool | int (rows affected) | Execute INSERT/UPDATE/DELETE/DDL |
| `execute_many(query, params_list, commit)` | query: str, params_list: List[tuple], commit: bool | int | Batch execute with multiple parameter sets |
| `fetch_one(query, params)` | query: str, params: tuple | tuple or None | Fetch single row |
| `fetch_scalar(query, params)` | query: str, params: tuple | Any | Fetch single value |

#### Properties

| Property | Type | Description |
|----------|------|-------------|
| `is_connected` | bool | Whether connection is established |

#### Example: Safe Parameterized Query

```python
from db_utils import DatabaseConnection

with DatabaseConnection() as db:
    # SAFE: Parameters prevent SQL injection
    results = db.execute_query(
        "SELECT * FROM users WHERE age > ? AND status = ?",
        params=(21, "active")
    )

    # Fetch single value
    count = db.fetch_scalar("SELECT COUNT(*) FROM users WHERE status = ?", ("active",))

    # Execute non-query
    rows = db.execute_non_query(
        "UPDATE users SET last_login = GETDATE() WHERE id = ?",
        params=(user_id,)
    )
```

### Convenience Functions

```python
from db_utils import execute_query, execute_non_query, get_connection
```

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `execute_query(query, params, database)` | query: str, params: tuple, database: str | List[tuple] | One-off query with auto-connection |
| `execute_non_query(query, params, database)` | query: str, params: tuple, database: str | int | One-off statement with auto-connection |
| `get_connection(database)` | database: str | DatabaseConnection | Context manager for connection |

### Exceptions

```python
from db_utils import DatabaseConnectionError, DatabaseQueryError
```

| Exception | Description |
|-----------|-------------|
| `DatabaseConnectionError` | Raised when connection fails (missing credentials, driver, network) |
| `DatabaseQueryError` | Raised when query execution fails |

---

## config Module

Configuration management with YAML file support and environment variable overrides.

### Config Dataclasses

```python
from config import Config, get_config
```

#### Config Structure

```
Config
├── database: DatabaseConfig
│   ├── name: str = "dpa_EDSAdmin"
│   └── timeout: int = 30
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
│       ├── critical_buffer_gets: int = 10000000
│       ├── high_buffer_gets: int = 1000000
│       └── min_buffer_gets: int = 100000
├── analysis: AnalysisConfig
│   ├── missing_indexes_days: int = 30
│   ├── slow_queries_days: int = 7
│   ├── blocking_days: int = 30
│   ├── io_issues_hours: int = 24
│   ├── top_results: int = 50
│   └── report_top: int = 10
├── output: OutputConfig
│   ├── directory: str = "output/performance"
│   ├── exports_directory: str = "output/exports"
│   └── log_directory: str = "logs"
├── alerts: AlertConfig
│   ├── email: str = "dba-team@company.com"
│   ├── mail_profile: str = "Default"
│   └── enabled: bool = True
└── logging: LoggingConfig
    ├── level: str = "INFO"
    ├── format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    ├── max_file_size_mb: int = 10
    └── backup_count: int = 5
```

### Config Functions

```python
from config import get_config, reload_config, get_threshold, validate_params
```

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `get_config()` | None | Config | Get global config instance (lazy loaded) |
| `reload_config()` | None | Config | Force reload configuration |
| `get_threshold(category, level)` | category: str, level: str | int | Get threshold value |
| `get_database_config()` | None | Dict | Get database config as dict |
| `get_output_path(subdir)` | subdir: str | Path | Get output directory path |
| `validate_params(**kwargs)` | days, min_saving, hours, latency_ms | None | Validate parameters, raises ValueError |

#### Example Usage

```python
from config import get_config, get_threshold, validate_params

# Access config values
config = get_config()
db_name = config.database.name
critical = config.thresholds.missing_index.critical

# Use convenience function
threshold = get_threshold('missing_index', 'critical')  # Returns 95
blocking_threshold = get_threshold('blocking', 'high_seconds')  # Returns 300

# Validate user input
validate_params(days=30, min_saving=80)  # OK
validate_params(days=500)  # Raises ValueError: days must be 1-365
```

#### Environment Variable Overrides

| Variable | Overrides |
|----------|-----------|
| `DB_DATABASE` | `config.database.name` |
| `DB_TIMEOUT` | `config.database.timeout` |
| `THRESHOLD_MISSING_INDEX_CRITICAL` | `config.thresholds.missing_index.critical` |
| `THRESHOLD_BLOCKING_CRITICAL_SECONDS` | `config.thresholds.blocking.critical_seconds` |
| `ALERT_EMAIL` | `config.alerts.email` |
| `LOG_LEVEL` | `config.logging.level` |

---

## logging_config Module

Structured logging with file rotation and console output.

### Logging Functions

```python
from logging_config import setup_logging, get_logger
```

| Function | Parameters | Returns | Description |
|----------|------------|---------|-------------|
| `setup_logging(script_name, log_level, console_output, file_output)` | script_name: str, log_level: str, console_output: bool, file_output: bool | Logger | Create configured logger |
| `get_logger(name)` | name: str | Logger | Get existing logger or create basic one |
| `configure_root_logger(level)` | level: str | None | Configure root logger for libraries |
| `silence_logger(name, level)` | name: str, level: int | None | Raise log level for noisy loggers |

#### Example Usage

```python
from logging_config import setup_logging

# Setup logging for a script
logger = setup_logging('analyze_performance')

# Use the logger
logger.info("Starting analysis")
logger.warning("Found %d issues", issue_count)
logger.error("Operation failed: %s", error_msg)
logger.debug("Processing item %d", item_id)

# Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
```

### LogContext Class

Context manager for logging operation timing.

```python
from logging_config import LogContext

with LogContext(logger, "Processing data"):
    # ... processing code ...
# Logs: "Starting: Processing data"
# Logs: "Completed: Processing data (1.23s)"
```

### log_execution Decorator

```python
from logging_config import log_execution

@log_execution(logger, "Processing items")
def process_items(items):
    # ... processing code ...
```

---

## Common Usage Patterns

### Script Template

```python
#!/usr/bin/env python3
"""Script description."""

import sys
import os

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from config import get_config, validate_params
from logging_config import setup_logging


class MyProcessor:
    def __init__(self, database='dpa_EDSAdmin'):
        self.database = database
        self._db = None
        self.logger = setup_logging('my_processor')

    def connect(self):
        try:
            self._db = DatabaseConnection(database=self.database)
            self._db.connect()
            self.logger.info("Connected to %s", self.database)
        except DatabaseConnectionError as e:
            self.logger.error("Connection failed: %s", e)
            raise

    def disconnect(self):
        if self._db:
            self._db.disconnect()
            self.logger.info("Disconnected")

    def process(self):
        # Safe parameterized query
        results = self._db.execute_query(
            "SELECT * FROM table WHERE value > ?",
            params=(threshold,)
        )
        return results


def main():
    processor = MyProcessor()
    processor.connect()
    try:
        results = processor.process()
    finally:
        processor.disconnect()


if __name__ == "__main__":
    main()
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-01 | Initial release with db_utils, config, logging_config |

---

**Maintained by:** DBA Team
