#!/usr/bin/env python3
"""
Generate Summary Report

Creates an executive overview of the database schema including
statistics, documentation coverage, and key findings.
"""

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


def generate_summary_report(database='EDS', output_dir='docs'):
    """Generate comprehensive database summary report."""

    logger = setup_logging('generate_summary_report')
    logger.info(f"Generating summary report for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Database size and info
    db_info = db.fetch_one('''
        SELECT
            DB_NAME() AS DatabaseName,
            SUSER_SNAME(owner_sid) AS Owner,
            create_date AS Created,
            collation_name AS Collation
        FROM sys.databases WHERE name = DB_NAME()
    ''')

    # Database size
    db_size = db.fetch_one('''
        SELECT
            SUM(CASE WHEN type = 0 THEN size END) * 8.0 / 1024 AS DataMB,
            SUM(CASE WHEN type = 1 THEN size END) * 8.0 / 1024 AS LogMB
        FROM sys.database_files
    ''')

    # Object counts
    table_count = db.fetch_one('SELECT COUNT(*) FROM sys.tables')[0]
    view_count = db.fetch_one('SELECT COUNT(*) FROM sys.views')[0]
    sp_count = db.fetch_one('SELECT COUNT(*) FROM sys.procedures')[0]
    fn_count = db.fetch_one("SELECT COUNT(*) FROM sys.objects WHERE type IN ('FN', 'IF', 'TF')")[0]
    trigger_count = db.fetch_one('SELECT COUNT(*) FROM sys.triggers WHERE parent_class = 1')[0]
    index_count = db.fetch_one('SELECT COUNT(*) FROM sys.indexes WHERE name IS NOT NULL')[0]

    # Column counts
    table_cols = db.fetch_one('''
        SELECT COUNT(*) FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
    ''')[0]

    view_cols = db.fetch_one('''
        SELECT COUNT(*) FROM sys.columns c
        INNER JOIN sys.views v ON c.object_id = v.object_id
    ''')[0]

    sp_params = db.fetch_one('''
        SELECT COUNT(*) FROM sys.parameters pm
        INNER JOIN sys.procedures p ON pm.object_id = p.object_id
        WHERE pm.parameter_id > 0
    ''')[0]

    # Documentation coverage
    tables_doc = db.fetch_one('''
        SELECT COUNT(*) FROM sys.tables t
        INNER JOIN sys.extended_properties ep ON t.object_id = ep.major_id
        AND ep.minor_id = 0 AND ep.name = 'MS_Description'
    ''')[0]

    table_cols_doc = db.fetch_one('''
        SELECT COUNT(*) FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.extended_properties ep ON c.object_id = ep.major_id
        AND c.column_id = ep.minor_id AND ep.name = 'MS_Description'
    ''')[0]

    views_doc = db.fetch_one('''
        SELECT COUNT(*) FROM sys.views v
        INNER JOIN sys.extended_properties ep ON v.object_id = ep.major_id
        AND ep.minor_id = 0 AND ep.name = 'MS_Description'
    ''')[0]

    view_cols_doc = db.fetch_one('''
        SELECT COUNT(*) FROM sys.columns c
        INNER JOIN sys.views v ON c.object_id = v.object_id
        INNER JOIN sys.extended_properties ep ON c.object_id = ep.major_id
        AND c.column_id = ep.minor_id AND ep.name = 'MS_Description'
    ''')[0]

    sp_doc = db.fetch_one('''
        SELECT COUNT(*) FROM sys.procedures p
        INNER JOIN sys.extended_properties ep ON p.object_id = ep.major_id
        AND ep.minor_id = 0 AND ep.name = 'MS_Description'
    ''')[0]

    sp_params_doc = db.fetch_one('''
        SELECT COUNT(*) FROM sys.parameters pm
        INNER JOIN sys.procedures p ON pm.object_id = p.object_id
        INNER JOIN sys.extended_properties ep ON pm.object_id = ep.major_id
        AND pm.parameter_id = ep.minor_id AND ep.name = 'MS_Description'
        WHERE pm.parameter_id > 0
    ''')[0]

    # Top tables by size
    top_tables = db.execute_query('''
        SELECT TOP 20
            s.name AS SchemaName,
            t.name AS TableName,
            ISNULL(p.row_count, 0) AS [Rows],
            CAST(ISNULL(p.used_page_count * 8.0 / 1024, 0) AS DECIMAL(10,2)) AS SizeMB
        FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.dm_db_partition_stats p ON t.object_id = p.object_id AND p.index_id < 2
        ORDER BY p.row_count DESC
    ''')

    # Schema breakdown
    schemas = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            COUNT(DISTINCT t.object_id) AS Tables,
            COUNT(DISTINCT v.object_id) AS Views,
            COUNT(DISTINCT p.object_id) AS Procedures
        FROM sys.schemas s
        LEFT JOIN sys.tables t ON s.schema_id = t.schema_id
        LEFT JOIN sys.views v ON s.schema_id = v.schema_id
        LEFT JOIN sys.procedures p ON s.schema_id = p.schema_id
        GROUP BY s.name
        HAVING COUNT(DISTINCT t.object_id) > 0 OR COUNT(DISTINCT v.object_id) > 0 OR COUNT(DISTINCT p.object_id) > 0
        ORDER BY s.name
    ''')

    # Foreign key count
    fk_count = db.fetch_one('SELECT COUNT(*) FROM sys.foreign_keys')[0]

    # Check constraint count
    check_count = db.fetch_one('SELECT COUNT(*) FROM sys.check_constraints')[0]

    # Default constraint count
    default_count = db.fetch_one('SELECT COUNT(*) FROM sys.default_constraints')[0]

    db.disconnect()

    # Generate report
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_SUMMARY.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Executive Summary\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('---\n\n')

        # Database overview
        f.write('## Database Overview\n\n')
        f.write('| Property | Value |\n')
        f.write('|----------|-------|\n')
        f.write(f'| Database Name | {db_info[0]} |\n')
        f.write(f'| Owner | {db_info[1]} |\n')
        f.write(f'| Created | {db_info[2]} |\n')
        f.write(f'| Collation | {db_info[3]} |\n')
        f.write(f'| Data Size | {db_size[0]:,.1f} MB |\n')
        f.write(f'| Log Size | {db_size[1]:,.1f} MB |\n')
        f.write('\n---\n\n')

        # Object counts
        f.write('## Object Inventory\n\n')
        f.write('| Object Type | Count |\n')
        f.write('|-------------|-------|\n')
        f.write(f'| Tables | {table_count:,} |\n')
        f.write(f'| Table Columns | {table_cols:,} |\n')
        f.write(f'| Views | {view_count:,} |\n')
        f.write(f'| View Columns | {view_cols:,} |\n')
        f.write(f'| Stored Procedures | {sp_count:,} |\n')
        f.write(f'| SP Parameters | {sp_params:,} |\n')
        f.write(f'| Functions | {fn_count:,} |\n')
        f.write(f'| Triggers | {trigger_count:,} |\n')
        f.write(f'| Indexes | {index_count:,} |\n')
        f.write(f'| Foreign Keys | {fk_count:,} |\n')
        f.write(f'| Check Constraints | {check_count:,} |\n')
        f.write(f'| Default Constraints | {default_count:,} |\n')
        f.write('\n---\n\n')

        # Documentation coverage
        f.write('## Documentation Coverage\n\n')

        def pct(a, b):
            return f'{100*a/b:.1f}%' if b > 0 else 'N/A'

        f.write('| Object Type | Documented | Total | Coverage |\n')
        f.write('|-------------|------------|-------|----------|\n')
        f.write(f'| Tables | {tables_doc:,} | {table_count:,} | {pct(tables_doc, table_count)} |\n')
        f.write(f'| Table Columns | {table_cols_doc:,} | {table_cols:,} | {pct(table_cols_doc, table_cols)} |\n')
        f.write(f'| Views | {views_doc:,} | {view_count:,} | {pct(views_doc, view_count)} |\n')
        f.write(f'| View Columns | {view_cols_doc:,} | {view_cols:,} | {pct(view_cols_doc, view_cols)} |\n')
        f.write(f'| Stored Procedures | {sp_doc:,} | {sp_count:,} | {pct(sp_doc, sp_count)} |\n')
        f.write(f'| SP Parameters | {sp_params_doc:,} | {sp_params:,} | {pct(sp_params_doc, sp_params)} |\n')

        total_doc = tables_doc + table_cols_doc + views_doc + view_cols_doc + sp_doc + sp_params_doc
        total_all = table_count + table_cols + view_count + view_cols + sp_count + sp_params
        f.write(f'| **TOTAL** | **{total_doc:,}** | **{total_all:,}** | **{pct(total_doc, total_all)}** |\n')
        f.write('\n---\n\n')

        # Schema breakdown
        f.write('## Schema Breakdown\n\n')
        f.write('| Schema | Tables | Views | Procedures |\n')
        f.write('|--------|--------|-------|------------|\n')
        for schema in schemas:
            f.write(f'| {schema[0]} | {schema[1]} | {schema[2]} | {schema[3]} |\n')
        f.write('\n---\n\n')

        # Top tables
        f.write('## Largest Tables (Top 20)\n\n')
        f.write('| Schema | Table | Rows | Size (MB) |\n')
        f.write('|--------|-------|------|----------|\n')
        for t in top_tables:
            f.write(f'| {t[0]} | {t[1]} | {t[2]:,} | {t[3]:,} |\n')
        f.write('\n---\n\n')

        # Key metrics
        f.write('## Key Metrics\n\n')

        avg_cols = table_cols / table_count if table_count > 0 else 0
        avg_params = sp_params / sp_count if sp_count > 0 else 0

        f.write(f'- **Average columns per table:** {avg_cols:.1f}\n')
        f.write(f'- **Average parameters per stored procedure:** {avg_params:.1f}\n')
        f.write(f'- **Views to tables ratio:** {view_count/table_count:.2f}:1\n')
        f.write(f'- **Indexes per table:** {index_count/table_count:.1f}\n')
        f.write(f'- **Foreign keys per table:** {fk_count/table_count:.2f}\n')
        f.write('\n---\n\n')

        # Footer
        f.write('## Documentation Files\n\n')
        f.write('- `EDS_TABLES.md` - Complete table documentation\n')
        f.write('- `EDS_VIEWS.md` - View documentation\n')
        f.write('- `EDS_STORED_PROCEDURES.md` - Stored procedure documentation\n')
        f.write('- `EDS_INDEXES.md` - Index documentation\n')
        f.write('- `EDS_ERD.md` - Entity relationship diagram\n')

    logger.info(f"[OK] Summary report saved to {output_file}")
    print(f"\nSummary report saved to: {output_file}")
    print(f"  Total objects: {total_all:,}")
    print(f"  Documentation coverage: {100*total_doc/total_all:.1f}%")

    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate summary report')
    parser.add_argument('--database', '-d', default='EDS', help='Database name')
    parser.add_argument('--output', '-o', default='docs', help='Output directory')

    args = parser.parse_args()

    try:
        generate_summary_report(database=args.database, output_dir=args.output)
    except DatabaseConnectionError as e:
        print(f"Connection failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
