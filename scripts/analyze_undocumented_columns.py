#!/usr/bin/env python3
"""
Analyze remaining undocumented columns and generate descriptions.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection

db = DatabaseConnection(database='EDS')
db.connect()

# Get undocumented table columns
print("=== Undocumented Table Columns ===\n")
table_cols = db.execute_query('''
    SELECT
        s.name AS SchemaName,
        t.name AS TableName,
        c.name AS ColumnName,
        ty.name AS DataType
    FROM sys.columns c
    INNER JOIN sys.tables t ON c.object_id = t.object_id
    INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
    INNER JOIN sys.types ty ON c.user_type_id = ty.user_type_id
    LEFT JOIN sys.extended_properties ep ON c.object_id = ep.major_id
        AND c.column_id = ep.minor_id AND ep.name = 'MS_Description'
    WHERE ep.value IS NULL
    ORDER BY s.name, t.name, c.column_id
''')

print(f"Total: {len(table_cols)}\n")
for schema, table, col, dtype in table_cols:
    print(f"{schema}.{table}.{col} ({dtype})")

print("\n\n=== Undocumented View Columns ===\n")
view_cols = db.execute_query('''
    SELECT
        s.name AS SchemaName,
        v.name AS ViewName,
        c.name AS ColumnName,
        ty.name AS DataType
    FROM sys.columns c
    INNER JOIN sys.views v ON c.object_id = v.object_id
    INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
    INNER JOIN sys.types ty ON c.user_type_id = ty.user_type_id
    LEFT JOIN sys.extended_properties ep ON c.object_id = ep.major_id
        AND c.column_id = ep.minor_id AND ep.name = 'MS_Description'
    WHERE ep.value IS NULL
    ORDER BY s.name, v.name, c.column_id
''')

print(f"Total: {len(view_cols)}\n")
for schema, view, col, dtype in view_cols:
    print(f"{schema}.{view}.{col} ({dtype})")

db.disconnect()
