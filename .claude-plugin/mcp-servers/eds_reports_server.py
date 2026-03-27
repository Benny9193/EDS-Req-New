#!/usr/bin/env python3
"""
EDS Reports MCP Server
======================

Model Context Protocol server for generating Excel reports from the EDS database.
Provides tools to generate, validate, preview, and manage structured reports.

Uses FastMCP with stdio transport. All logging goes to stderr.

Tools:
  - generate_report    — Execute a report plan and create an Excel file
  - validate_plan      — Validate a report plan JSON without executing
  - preview_report     — Execute queries and preview data without creating a file
  - list_reports       — List previously generated reports
  - get_report_schema  — Get the JSON schema for creating report plans
  - delete_report      — Delete a generated report file
"""

import sys
import os
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional

# ── Ensure project root is importable ──────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# ── Load .env before anything else ─────────────────────────────────────
from dotenv import load_dotenv

load_dotenv(PROJECT_ROOT / ".env")

# ── Logging to stderr only (MCP uses stdout for protocol) ─────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger("eds-reports-mcp")

# ── FastMCP import ─────────────────────────────────────────────────────
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    logger.error(
        "MCP SDK not installed. Install with: pip install mcp\n"
        "  or: pip install 'mcp[cli]'"
    )
    sys.exit(1)

# ── EDS imports ────────────────────────────────────────────────────────
from agent.export import ReportPlan, ReportBuilder
from agent.export.models import REPORT_PLAN_JSON_SCHEMA

# ── Server setup ───────────────────────────────────────────────────────
mcp = FastMCP(
    "EDS Reports Server",
    instructions=(
        "Report generation tools for the EDS procurement system. "
        "Generate Excel reports from structured report plans with SQL queries. "
        "Use get_report_schema to see the expected JSON format for report plans."
    ),
)

# ── Configuration ──────────────────────────────────────────────────────
OUTPUT_DIR = PROJECT_ROOT / "output"
MAX_ROWS = 50000
QUERY_TIMEOUT = 120


# ═══════════════════════════════════════════════════════════════════════
# Helper Functions
# ═══════════════════════════════════════════════════════════════════════

def _serialize_value(value: Any) -> Any:
    """Convert a database value to JSON-safe format."""
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, bytes):
        return value.hex()
    if isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def _get_report_files() -> List[Dict[str, Any]]:
    """Get list of report files in the output directory."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    reports = []
    for file_path in OUTPUT_DIR.glob("*.xlsx"):
        stat = file_path.stat()
        reports.append({
            "filename": file_path.name,
            "path": str(file_path.resolve()),
            "size_bytes": stat.st_size,
            "size_kb": round(stat.st_size / 1024, 1),
            "created": datetime.fromtimestamp(stat.st_ctime).isoformat(),
            "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        })

    # Sort by modified time, newest first
    reports.sort(key=lambda x: x["modified"], reverse=True)
    return reports


def _format_preview_table(columns: List[str], rows: List[Dict], max_rows: int = 10) -> str:
    """Format query results as a markdown table preview."""
    if not rows:
        return "*No data returned*"

    display_rows = rows[:max_rows]

    lines = []
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join(["---"] * len(columns)) + " |")

    for row in display_rows:
        values = []
        for col in columns:
            v = str(row.get(col, ""))
            if len(v) > 40:
                v = v[:37] + "..."
            values.append(v)
        lines.append("| " + " | ".join(values) + " |")

    result = "\n".join(lines)
    if len(rows) > max_rows:
        result += f"\n\n*...and {len(rows) - max_rows} more rows*"

    return result


# ═══════════════════════════════════════════════════════════════════════
# MCP Tools
# ═══════════════════════════════════════════════════════════════════════

@mcp.tool()
def get_report_schema() -> str:
    """
    Get the JSON schema for creating report plans.

    Use this to understand the structure expected by generate_report.
    The schema shows all required and optional fields for defining
    queries and sheets in a report.

    Returns:
        JSON schema documentation with field descriptions
    """
    return f"""# Report Plan JSON Schema

Use this schema when creating report plans for generate_report.

```json
{REPORT_PLAN_JSON_SCHEMA}
```

## Sheet Types

- **summary**: High-level aggregated data with totals
- **detail**: Raw data rows with all columns
- **pivot**: Cross-tabulation with row/column grouping
- **drilldown**: Grouped data with subtotals by category

## Column Formats

- **number**: Integer formatting with thousands separator
- **currency**: Dollar formatting ($1,234.56)
- **date**: Date formatting (MM/DD/YYYY)
- **percent**: Percentage formatting (12.34%)
- **text**: Plain text (default)

## Example Report Plan

```json
{{
  "title": "Vendor Bid Analysis",
  "description": "Summary of vendor bids for Q1 2024",
  "queries": [
    {{
      "name": "bid_summary",
      "sql": "SELECT VendorName, COUNT(*) as BidCount, SUM(TotalAmount) as TotalValue FROM BidImports bi JOIN Vendors v ON bi.VendorID = v.VendorID GROUP BY VendorName ORDER BY TotalValue DESC",
      "database": "EDS",
      "description": "Vendor bid totals"
    }}
  ],
  "sheets": [
    {{
      "name": "Vendor Summary",
      "type": "summary",
      "query_ref": "bid_summary",
      "columns": [
        {{"name": "Vendor", "source": "VendorName"}},
        {{"name": "Bids", "source": "BidCount", "format": "number"}},
        {{"name": "Total Value", "source": "TotalValue", "format": "currency"}}
      ],
      "include_totals": true
    }}
  ]
}}
```
"""


@mcp.tool()
def validate_plan(report_plan_json: str) -> str:
    """
    Validate a report plan JSON without executing queries.

    Use this before generate_report to check for errors in the plan structure,
    query definitions, and sheet configurations.

    Args:
        report_plan_json: JSON string containing the report plan

    Returns:
        Validation result with any errors found
    """
    try:
        # Parse JSON
        try:
            data = json.loads(report_plan_json)
        except json.JSONDecodeError as e:
            return f"**Invalid JSON**\n\nParse error at position {e.pos}: {e.msg}"

        # Attempt to create ReportPlan (runs validation)
        try:
            plan = ReportPlan.from_dict(data)
        except ValueError as e:
            return f"**Validation Failed**\n\n{str(e)}"

        # Success - return summary
        query_list = "\n".join(
            f"  - **{q.name}** ({q.database}): {q.description or 'No description'}"
            for q in plan.queries
        )
        sheet_list = "\n".join(
            f"  - **{s.name}** ({s.type}): uses query '{s.query_ref}'"
            for s in plan.sheets
        )

        return f"""**Validation Passed** ✓

## Report: {plan.title}

{plan.description}

### Queries ({len(plan.queries)})
{query_list}

### Sheets ({len(plan.sheets)})
{sheet_list}

### Generated Filename
`{plan.get_generated_filename()}`
"""

    except Exception as e:
        logger.exception("validate_plan failed")
        return f"**Error**: {e}"


@mcp.tool()
def generate_report(
    report_plan_json: str,
    output_dir: Optional[str] = None,
) -> str:
    """
    Execute a report plan and generate an Excel file.

    Takes a complete report plan JSON, executes all SQL queries against
    the database, and creates a formatted Excel workbook with multiple sheets.

    Args:
        report_plan_json: JSON string containing the complete report plan.
                          Use get_report_schema to see the expected format.
        output_dir: Optional output directory (default: project output folder)

    Returns:
        Result summary with file path and statistics

    Example:
        generate_report('{"title": "Sales Report", "queries": [...], "sheets": [...]}')
    """
    try:
        # Parse and validate
        try:
            data = json.loads(report_plan_json)
        except json.JSONDecodeError as e:
            return f"**Error**: Invalid JSON at position {e.pos}: {e.msg}"

        try:
            plan = ReportPlan.from_dict(data)
        except ValueError as e:
            return f"**Validation Error**\n\n{str(e)}"

        # Build report
        config = {
            "output_dir": output_dir or str(OUTPUT_DIR),
            "max_rows": MAX_ROWS,
            "timeout": QUERY_TIMEOUT,
        }

        builder = ReportBuilder(config=config)
        result = builder.build(plan)

        # Format response
        query_results = "\n".join(
            f"  - {name}: {count:,} rows"
            for name, count in result["query_results"].items()
        )

        sheet_results = "\n".join(
            f"  - **{s['name']}** ({s['type']}): {s['rows']:,} rows"
            + (f" — Error: {s.get('error')}" if s.get('error') else "")
            for s in result["sheet_results"]
        )

        error_section = ""
        if result["errors"]:
            error_section = "\n### Warnings\n" + "\n".join(
                f"  - {e}" for e in result["errors"]
            )

        return f"""**Report Generated Successfully**

### File
- **Path**: `{result['file_path']}`
- **Filename**: `{result['filename']}`

### Statistics
- **Sheets**: {result['sheet_count']}
- **Total Rows**: {result['total_rows']:,}
- **Build Time**: {result['elapsed_seconds']}s

### Query Results
{query_results}

### Sheet Results
{sheet_results}
{error_section}
"""

    except Exception as e:
        logger.exception("generate_report failed")
        return f"**Error**: Report generation failed: {e}"


@mcp.tool()
def preview_report(
    report_plan_json: str,
    preview_rows: int = 5,
) -> str:
    """
    Preview a report by executing queries without generating a file.

    Use this to verify queries return expected data before generating
    the full report. Shows a sample of rows from each query.

    Args:
        report_plan_json: JSON string containing the report plan
        preview_rows: Number of sample rows to show per query (default 5, max 20)

    Returns:
        Preview of each query's results as markdown tables
    """
    preview_rows = min(preview_rows, 20)

    try:
        # Parse and validate
        try:
            data = json.loads(report_plan_json)
        except json.JSONDecodeError as e:
            return f"**Error**: Invalid JSON at position {e.pos}: {e.msg}"

        try:
            plan = ReportPlan.from_dict(data)
        except ValueError as e:
            return f"**Validation Error**\n\n{str(e)}"

        # Import database utilities
        try:
            from scripts.db_utils import DatabaseConnection
        except ImportError:
            return "**Error**: Database connection module not available"

        # Execute each query with preview limit
        output_parts = [f"# Report Preview: {plan.title}\n"]

        for query_def in plan.queries:
            output_parts.append(f"\n## Query: {query_def.name}\n")
            output_parts.append(f"*Database: {query_def.database}*\n")

            if query_def.description:
                output_parts.append(f"{query_def.description}\n")

            try:
                # Add TOP to limit preview
                sql = query_def.sql.strip()
                sql_upper = sql.upper()
                if "TOP " not in sql_upper[:50]:
                    if sql_upper.startswith("SELECT DISTINCT"):
                        sql = f"SELECT DISTINCT TOP {preview_rows + 5} " + sql[len("SELECT DISTINCT "):]
                    elif sql_upper.startswith("SELECT"):
                        sql = f"SELECT TOP {preview_rows + 5} " + sql[len("SELECT "):]

                with DatabaseConnection(database=query_def.database, timeout=30) as db:
                    cursor = db._conn.cursor()
                    cursor.execute(sql)

                    columns = [desc[0] for desc in cursor.description]
                    raw_rows = cursor.fetchall()
                    cursor.close()

                    # Convert to list of dicts
                    rows = []
                    for row in raw_rows:
                        row_dict = {columns[i]: _serialize_value(row[i]) for i in range(len(columns))}
                        rows.append(row_dict)

                    output_parts.append(f"\n**Columns**: {', '.join(columns)}\n")
                    output_parts.append(f"**Sample Data** ({len(rows)} rows shown):\n\n")
                    output_parts.append(_format_preview_table(columns, rows, preview_rows))

            except Exception as e:
                output_parts.append(f"\n**Query Error**: {e}\n")

        # Show sheet mapping
        output_parts.append("\n\n## Sheet Mapping\n")
        for sheet_def in plan.sheets:
            output_parts.append(
                f"- **{sheet_def.name}** ({sheet_def.type}) ← query '{sheet_def.query_ref}'"
            )
            if sheet_def.columns:
                cols = ", ".join(c.name for c in sheet_def.columns[:5])
                if len(sheet_def.columns) > 5:
                    cols += f", ... ({len(sheet_def.columns)} total)"
                output_parts.append(f"  - Columns: {cols}")

        return "\n".join(output_parts)

    except Exception as e:
        logger.exception("preview_report failed")
        return f"**Error**: Preview failed: {e}"


@mcp.tool()
def list_reports(
    limit: int = 20,
    pattern: Optional[str] = None,
) -> str:
    """
    List previously generated report files.

    Shows Excel files in the output directory, sorted by modification date
    (newest first).

    Args:
        limit: Maximum number of reports to list (default 20)
        pattern: Optional filename pattern to filter (e.g., "Vendor*")

    Returns:
        List of reports with file info
    """
    try:
        reports = _get_report_files()

        if pattern:
            import fnmatch
            reports = [r for r in reports if fnmatch.fnmatch(r["filename"], pattern)]

        reports = reports[:limit]

        if not reports:
            if pattern:
                return f"No reports found matching pattern: {pattern}"
            return f"No reports found in output directory: {OUTPUT_DIR}"

        lines = ["# Generated Reports\n"]
        lines.append(f"*Output directory: `{OUTPUT_DIR}`*\n")
        lines.append("| Filename | Size | Modified |")
        lines.append("| --- | --- | --- |")

        for r in reports:
            modified = datetime.fromisoformat(r["modified"]).strftime("%Y-%m-%d %H:%M")
            size = f"{r['size_kb']} KB" if r["size_kb"] < 1024 else f"{r['size_kb']/1024:.1f} MB"
            lines.append(f"| {r['filename']} | {size} | {modified} |")

        lines.append(f"\n*{len(reports)} report(s) shown*")

        return "\n".join(lines)

    except Exception as e:
        logger.exception("list_reports failed")
        return f"**Error**: {e}"


@mcp.tool()
def delete_report(filename: str) -> str:
    """
    Delete a generated report file.

    Only deletes files from the output directory. Cannot delete files
    outside the designated output folder.

    Args:
        filename: Name of the report file to delete (e.g., "Vendor_Report_20240115.xlsx")

    Returns:
        Confirmation message
    """
    try:
        # Ensure filename doesn't contain path traversal
        if "/" in filename or "\\" in filename or ".." in filename:
            return "**Error**: Invalid filename. Provide just the filename, not a path."

        file_path = OUTPUT_DIR / filename

        # Verify it's actually in the output directory
        try:
            resolved = file_path.resolve()
            if not resolved.is_relative_to(OUTPUT_DIR.resolve()):
                return "**Error**: Cannot delete files outside the output directory."
        except ValueError:
            return "**Error**: Invalid file path."

        if not file_path.exists():
            return f"**Error**: File not found: {filename}"

        if not filename.endswith(".xlsx"):
            return "**Error**: Can only delete .xlsx report files."

        # Delete the file
        file_path.unlink()
        logger.info(f"Deleted report: {filename}")

        return f"**Deleted**: `{filename}`"

    except PermissionError:
        return f"**Error**: Cannot delete {filename} — file may be open in Excel."
    except Exception as e:
        logger.exception("delete_report failed")
        return f"**Error**: {e}"


@mcp.tool()
def get_report_templates() -> str:
    """
    Get example report plan templates for common report types.

    Returns ready-to-use JSON templates that can be customized
    for your specific reporting needs.

    Returns:
        Collection of report plan templates with descriptions
    """
    templates = {
        "Simple Detail Report": {
            "title": "Item Listing Report",
            "description": "List of items with vendor and pricing information",
            "queries": [
                {
                    "name": "items",
                    "sql": "SELECT i.ItemNumber, i.Description, v.VendorName, i.UnitPrice, i.UnitOfMeasure FROM Items i JOIN Vendors v ON i.VendorID = v.VendorID ORDER BY v.VendorName, i.ItemNumber",
                    "database": "EDS",
                    "description": "All items with vendor info"
                }
            ],
            "sheets": [
                {
                    "name": "Items",
                    "type": "detail",
                    "query_ref": "items",
                    "columns": [
                        {"name": "Item #", "source": "ItemNumber"},
                        {"name": "Description", "source": "Description", "width": 40},
                        {"name": "Vendor", "source": "VendorName", "width": 25},
                        {"name": "Price", "source": "UnitPrice", "format": "currency"},
                        {"name": "UOM", "source": "UnitOfMeasure"}
                    ],
                    "include_totals": False
                }
            ]
        },
        "Summary with Totals": {
            "title": "Vendor Summary Report",
            "description": "Aggregated vendor statistics with totals",
            "queries": [
                {
                    "name": "vendor_summary",
                    "sql": "SELECT v.VendorName, COUNT(DISTINCT i.ItemID) as ItemCount, SUM(i.UnitPrice) as TotalValue, AVG(i.UnitPrice) as AvgPrice FROM Vendors v JOIN Items i ON v.VendorID = i.VendorID GROUP BY v.VendorName ORDER BY TotalValue DESC",
                    "database": "EDS",
                    "description": "Vendor totals"
                }
            ],
            "sheets": [
                {
                    "name": "Vendor Summary",
                    "type": "summary",
                    "query_ref": "vendor_summary",
                    "columns": [
                        {"name": "Vendor", "source": "VendorName", "width": 30},
                        {"name": "Items", "source": "ItemCount", "format": "number"},
                        {"name": "Total Value", "source": "TotalValue", "format": "currency"},
                        {"name": "Avg Price", "source": "AvgPrice", "format": "currency"}
                    ],
                    "include_totals": True
                }
            ]
        },
        "Multi-Sheet Report": {
            "title": "Comprehensive Vendor Report",
            "description": "Summary and detail sheets in one workbook",
            "queries": [
                {
                    "name": "summary",
                    "sql": "SELECT v.VendorName, COUNT(*) as ItemCount FROM Vendors v JOIN Items i ON v.VendorID = i.VendorID GROUP BY v.VendorName ORDER BY ItemCount DESC",
                    "database": "EDS"
                },
                {
                    "name": "detail",
                    "sql": "SELECT v.VendorName, i.ItemNumber, i.Description, i.UnitPrice FROM Items i JOIN Vendors v ON i.VendorID = v.VendorID ORDER BY v.VendorName",
                    "database": "EDS"
                }
            ],
            "sheets": [
                {
                    "name": "Summary",
                    "type": "summary",
                    "query_ref": "summary",
                    "columns": [
                        {"name": "Vendor", "source": "VendorName"},
                        {"name": "Item Count", "source": "ItemCount", "format": "number"}
                    ]
                },
                {
                    "name": "All Items",
                    "type": "detail",
                    "query_ref": "detail",
                    "columns": [
                        {"name": "Vendor", "source": "VendorName"},
                        {"name": "Item #", "source": "ItemNumber"},
                        {"name": "Description", "source": "Description"},
                        {"name": "Price", "source": "UnitPrice", "format": "currency"}
                    ]
                }
            ]
        }
    }

    output = ["# Report Plan Templates\n"]
    output.append("Copy and customize these templates for generate_report.\n")

    for name, template in templates.items():
        output.append(f"\n## {name}\n")
        output.append(f"*{template['description']}*\n")
        output.append("```json")
        output.append(json.dumps(template, indent=2))
        output.append("```\n")

    return "\n".join(output)


# ═══════════════════════════════════════════════════════════════════════
# Entry point
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    logger.info("Starting EDS Reports MCP Server...")
    mcp.run()
