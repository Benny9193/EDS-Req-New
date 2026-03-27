#!/usr/bin/env python3
"""
Document View Columns

Adds MS_Description extended properties to view columns by:
1. Copying descriptions from corresponding table columns
2. Using pattern-based descriptions for remaining columns
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection
from logging_config import setup_logging

# Import column descriptions from other scripts
from add_column_descriptions_v2 import get_description


def document_view_columns(database='EDS'):
    """Add MS_Description to view columns."""

    logger = setup_logging('document_view_columns')
    logger.info(f"Documenting view columns for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get total view columns
    total = db.fetch_one('''
        SELECT COUNT(*)
        FROM sys.columns c
        INNER JOIN sys.views v ON c.object_id = v.object_id
    ''')
    logger.info(f"Total view columns: {total[0]}")

    # Get undocumented view columns
    undoc_cols = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            v.name AS ViewName,
            c.name AS ColumnName
        FROM sys.columns c
        INNER JOIN sys.views v ON c.object_id = v.object_id
        INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON c.object_id = ep.major_id
            AND c.column_id = ep.minor_id AND ep.name = 'MS_Description'
        WHERE ep.value IS NULL
        ORDER BY v.name, c.column_id
    ''')

    logger.info(f"Undocumented view columns: {len(undoc_cols)}")

    # Get existing table column descriptions to copy
    table_descs = db.execute_query('''
        SELECT
            c.name AS ColumnName,
            CAST(ep.value AS NVARCHAR(MAX)) AS Description
        FROM sys.extended_properties ep
        INNER JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        WHERE ep.name = 'MS_Description'
    ''')

    # Build lookup (column name -> description)
    col_lookup = {}
    for col, desc in table_descs:
        if col not in col_lookup:
            col_lookup[col] = desc

    logger.info(f"Found {len(col_lookup)} unique column descriptions to reference")

    success = 0
    from_table = 0
    from_pattern = 0
    skipped = 0

    for schema, view, column in undoc_cols:
        # Try to get description from table columns first
        desc = col_lookup.get(column)
        if desc:
            from_table += 1
        else:
            # Fall back to pattern-based description
            desc = get_description(column)
            if desc:
                from_pattern += 1
            else:
                skipped += 1
                continue

        # Add "(View)" prefix to distinguish from table columns
        desc = f'(View) {desc}'

        try:
            db.execute_non_query('''
                EXEC sp_addextendedproperty
                    @name = N'MS_Description',
                    @value = ?,
                    @level0type = N'SCHEMA', @level0name = ?,
                    @level1type = N'VIEW', @level1name = ?,
                    @level2type = N'COLUMN', @level2name = ?
            ''', (desc, schema, view, column))
            success += 1
            if success % 200 == 0:
                logger.info(f"  Applied {success} column descriptions...")
        except Exception as e:
            pass  # Skip errors silently

    db.disconnect()

    logger.info(f"[OK] View column descriptions added: {success}")
    logger.info(f"  From table columns: {from_table}")
    logger.info(f"  From patterns: {from_pattern}")
    logger.info(f"  Skipped (no match): {skipped}")

    print(f"\nView column descriptions added: {success}")
    print(f"  From table columns: {from_table}")
    print(f"  From patterns: {from_pattern}")
    print(f"  Skipped (no match): {skipped}")

    return success


if __name__ == '__main__':
    document_view_columns()
