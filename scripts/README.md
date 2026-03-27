# EDS Scripts Directory

Utility scripts for database analysis, documentation generation, and deployment.

---

## Quick Start

```bash
# Ensure you're in the project root
cd /mnt/c/EDS

# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows

# Set up environment
cp .env.example .env
# Edit .env with your database credentials

# Run a script
python scripts/generate_data_dictionary.py
```

---

## Scripts by Category

### Database Analysis

| Script | Purpose | Output |
|--------|---------|--------|
| `analyze_business_domains.py` | Categorize tables by business domain | `docs/EDS_BUSINESS_DOMAINS.md` |
| `analyze_archive_schema.py` | Analyze archive schema tables | `docs/EDS_ARCHIVE_ANALYSIS.md` |
| `analyze_circular_deps.py` | Find circular dependencies in SPs | `docs/EDS_CIRCULAR_DEPS.md` |
| `analyze_root_procedures.py` | Identify root stored procedures | `docs/EDS_ROOT_PROCEDURES.md` |
| `analyze_performance_issues.py` | Analyze query performance | Console output |
| `analyze_undocumented_columns.py` | Find columns without descriptions | Console output |

### Documentation Generation

| Script | Purpose | Output |
|--------|---------|--------|
| `generate_data_dictionary.py` | Generate full data dictionary | `docs/EDS_DATA_DICTIONARY.md` |
| `generate_erd.py` | Generate entity relationship docs | `docs/EDS_ERD.md` |
| `generate_summary_report.py` | Generate database summary | `docs/EDS_SUMMARY.md` |
| `generate_sp_dependencies.py` | Document SP dependencies | `docs/EDS_PROCEDURE_DEPENDENCIES.md` |
| `generate_html_report.py` | Interactive HTML documentation | `docs/EDS_INTERACTIVE.html` |
| `generate_trigger_diagram.py` | Document trigger relationships | `docs/EDS_TRIGGERS.md` |
| `generate_extended_properties.py` | Export SQL Server descriptions | `docs/EDS_EXTENDED_PROPERTIES.sql` |

### Column Documentation

| Script | Purpose | Output |
|--------|---------|--------|
| `add_column_descriptions.py` | Add descriptions to columns | Updates SQL Server |
| `add_column_descriptions_v2.py` | Enhanced version with AI | Updates SQL Server |
| `add_column_descriptions_v3.py` | Batch processing version | Updates SQL Server |
| `add_column_descriptions_v4.py` | Final optimized version | Updates SQL Server |
| `add_column_descriptions_final.py` | Production-ready version | Updates SQL Server |
| `document_final_columns.py` | Document remaining columns | Updates SQL Server |
| `document_remaining_columns.py` | Handle edge cases | Updates SQL Server |

### Stored Procedure Documentation

| Script | Purpose | Output |
|--------|---------|--------|
| `document_stored_procedures.py` | Document all stored procs | `docs/EDS_STORED_PROCEDURES.md` |
| `document_sp_parameters.py` | Document SP parameters | Updates existing docs |
| `document_recursive_procs.py` | Analyze recursive procedures | `docs/EDS_RECURSIVE_PROCEDURES.md` |
| `generate_sp_documentation.py` | Generate SP reference | Markdown files |
| `generate_sproc_docs.py` | Simplified SP docs | Markdown files |

### View Documentation

| Script | Purpose | Output |
|--------|---------|--------|
| `document_views.py` | Document database views | `docs/EDS_VIEWS.md` |
| `document_view_columns.py` | Document view columns | Updates existing docs |
| `generate_views_docs.py` | Generate view reference | Markdown files |

### Index Management

| Script | Purpose | Output |
|--------|---------|--------|
| `document_indexes.py` | Document existing indexes | `docs/EDS_INDEXES.md` |
| `generate_index_scripts.py` | Generate index creation SQL | SQL files |
| `extract_missing_indexes.py` | Find missing index suggestions | Console/SQL |
| `deploy_indexes_test.py` | Deploy indexes (test mode) | Test execution |
| `deploy_indexes_production.py` | Deploy indexes (production) | Production execution |
| `validate_index_performance.py` | Validate index effectiveness | Console report |

### Performance Analysis

| Script | Purpose | Output |
|--------|---------|--------|
| `capture_performance_baseline.py` | Capture performance metrics | `output/` directory |
| `investigate_blocking_event.py` | Analyze blocking incidents | Console report |
| `investigate_infinite_loops.py` | Find potential infinite loops | `docs/EDS_INFINITE_LOOP_ANALYSIS.md` |
| `generate_final_performance_report.py` | Full performance report | `output/PERFORMANCE_RECOMMENDATIONS.md` |
| `validate_implementation.py` | Validate optimizations | Console report |

### Utilities

| Script | Purpose | Output |
|--------|---------|--------|
| `config.py` | Shared configuration | (imported by other scripts) |
| `db_utils.py` | Database connection utilities | (imported by other scripts) |
| `logging_config.py` | Logging configuration | (imported by other scripts) |
| `check_coverage.py` | Check documentation coverage | Console report |
| `refresh_documentation.py` | Refresh all documentation | Multiple files |
| `export_to_excel.py` | Export data dictionary to Excel | `docs/EDS_DATA_DICTIONARY.xlsx` |
| `schema_explorer.py` | Interactive schema browser | Console UI |

### Deployment

| Script | Purpose | Usage |
|--------|---------|-------|
| `deploy.sh` | Production deployment | `./scripts/deploy.sh` |
| `dev-setup.sh` | Development environment setup | `./scripts/dev-setup.sh` |
| `run_tests.sh` | Run test suite | `./scripts/run_tests.sh` |

### SQL Files

| File | Purpose |
|------|---------|
| `alert_dashboard.sql` | Create alert dashboard views |
| `enable_snapshot_isolation.sql` | Enable snapshot isolation |
| `sql_agent_jobs/` | SQL Server Agent job scripts |

---

## Common Usage Examples

### Generate Full Documentation

```bash
# Generate all documentation
python scripts/refresh_documentation.py

# Or run individually:
python scripts/generate_data_dictionary.py
python scripts/generate_summary_report.py
python scripts/generate_sp_dependencies.py
```

### Analyze Database Performance

```bash
# Capture baseline metrics
python scripts/capture_performance_baseline.py

# Investigate a blocking event
python scripts/investigate_blocking_event.py --date 2026-01-06

# Generate performance recommendations
python scripts/generate_final_performance_report.py
```

### Index Management

```bash
# Find missing indexes
python scripts/extract_missing_indexes.py

# Test index deployment (dry run)
python scripts/deploy_indexes_test.py

# Deploy to production (careful!)
python scripts/deploy_indexes_production.py --confirm
```

### Interactive Schema Explorer

```bash
# Launch interactive browser
python scripts/schema_explorer.py

# Commands in explorer:
#   tables          - List all tables
#   table <name>    - Show table details
#   sp <name>       - Show stored procedure
#   search <term>   - Search across objects
#   quit            - Exit
```

---

## Configuration

### Environment Variables

Scripts use `.env` file in project root:

```env
DB_SERVER=eds-sqlserver.eastus2.cloudapp.azure.com
DB_DATABASE=EDS
DB_USERNAME=your_username
DB_PASSWORD=your_password
```

### Config Files

- `scripts/config.py` - Shared settings (timeouts, paths)
- `config.yaml` - Application-wide configuration
- `agent_config.yaml` - AI agent configuration

---

## Dependencies

Scripts require:
```
pyodbc          # SQL Server connectivity
pandas          # Data manipulation
openpyxl        # Excel export
python-dotenv   # Environment loading
rich            # Console formatting (optional)
```

Install with:
```bash
pip install -e ".[scripts]"
# or
pip install pyodbc pandas openpyxl python-dotenv rich
```

---

## Output Locations

| Type | Location |
|------|----------|
| Markdown docs | `/docs/` |
| Excel exports | `/docs/` |
| HTML reports | `/docs/` |
| Performance data | `/output/` |
| Logs | `/logs/` |

---

## Troubleshooting

### Connection Errors
```bash
# Test database connection
python test_db.py
```

### Permission Denied
- Ensure database user has read access to system tables
- Some scripts require elevated permissions for writes

### Script Hangs
- Large tables may take time to document
- Add `--timeout 300` flag if supported
- Check `/logs/` for progress

---

## See Also

- [Database Architecture](../docs/wiki/architecture/database-architecture.md)
- [API Reference](../docs/API_REFERENCE.md)
- [Development Setup](../docs/DEVELOPMENT.md)
