---
allowed-tools: Bash(cd C?EDS && python:*), Bash(cd /c/EDS && python:*), Bash(ls:*), Bash(dir:*)
description: Run an EDS monitoring or analysis script. Use without arguments to list available scripts.
argument-hint: [script_name] [--args ...]
---

## Context

- Working directory: C:\EDS
- Scripts directory: C:\EDS\scripts\
- 47+ available Python scripts for monitoring, analysis, and documentation

## Your Task

The user wants to run a monitoring or analysis script, or see what's available.

### If no argument provided — List available scripts

Show the user the organized script catalog:

**Performance Monitoring:**
- `capture_performance_baseline` — Capture current performance metrics
- `analyze_performance_issues` — Analyze issues (use `--args --days 30`)
- `investigate_blocking_event` — Investigate blocking (use `--args --date 2025-01-09`)
- `validate_index_performance` — Validate index performance

**Index Management:**
- `extract_missing_indexes` — Find missing indexes (use `--args --min-saving 80`)
- `generate_index_scripts` — Generate CREATE INDEX scripts
- `deploy_indexes_test` — Deploy indexes to test
- `deploy_indexes_production` — Deploy indexes to production

**Reports & Dashboards:**
- `generate_final_performance_report` — Comprehensive performance report
- `generate_alert_dashboard` — Alert dashboard
- `generate_summary_report` — Executive summary
- `generate_html_report` — HTML report

**Documentation Generation:**
- `refresh_documentation` — Rebuild all documentation
- `generate_data_dictionary` — Complete data dictionary
- `generate_sproc_docs` — Stored procedure documentation
- `generate_erd` — Entity relationship diagram
- `check_coverage` — Documentation coverage check

**Analysis:**
- `analyze_business_domains` — Business domain analysis
- `analyze_circular_deps` — Find circular dependencies
- `analyze_root_procedures` — Find entry point procedures
- `investigate_infinite_loops` — Find infinite loops

### If script name provided — Execute it

First do a dry run to show what will execute:

```
cd C:\EDS && python -m agent --provider claude run --dry-run <SCRIPT_NAME>
```

Then ask the user to confirm before executing:

```
cd C:\EDS && python -m agent --provider claude run <SCRIPT_NAME>
```

If the user provided additional arguments (like `--days 30`), pass them with `--args`:

```
cd C:\EDS && python -m agent --provider claude run <SCRIPT_NAME> --args <ARG1> --args <ARG2>
```

### Error Handling

- If the script doesn't exist, show the available scripts list
- If the script fails with a DB error, check `.env` configuration
- If the script takes too long, mention it may be running a heavy query and to wait
