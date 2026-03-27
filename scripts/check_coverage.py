#!/usr/bin/env python3
"""Check final documentation coverage."""

import sys
sys.path.insert(0, 'scripts')
from db_utils import DatabaseConnection

db = DatabaseConnection(database='EDS')
db.connect()

print('=== FINAL DOCUMENTATION COVERAGE ===')
print()

# Tables
total = db.fetch_one('SELECT COUNT(*) FROM sys.tables')[0]
documented = db.fetch_one('''
    SELECT COUNT(*) FROM sys.tables t
    INNER JOIN sys.extended_properties ep ON t.object_id = ep.major_id
    AND ep.minor_id = 0 AND ep.name = 'MS_Description'
''')[0]
print(f'Tables:           {documented:,}/{total:,} ({100*documented/total:.1f}%)')

# Table Columns
total = db.fetch_one('''
    SELECT COUNT(*) FROM sys.columns c
    INNER JOIN sys.tables t ON c.object_id = t.object_id
''')[0]
documented = db.fetch_one('''
    SELECT COUNT(*) FROM sys.columns c
    INNER JOIN sys.tables t ON c.object_id = t.object_id
    INNER JOIN sys.extended_properties ep ON c.object_id = ep.major_id
    AND c.column_id = ep.minor_id AND ep.name = 'MS_Description'
''')[0]
print(f'Table Columns:    {documented:,}/{total:,} ({100*documented/total:.1f}%)')

# Views
total = db.fetch_one('SELECT COUNT(*) FROM sys.views')[0]
documented = db.fetch_one('''
    SELECT COUNT(*) FROM sys.views v
    INNER JOIN sys.extended_properties ep ON v.object_id = ep.major_id
    AND ep.minor_id = 0 AND ep.name = 'MS_Description'
''')[0]
print(f'Views:            {documented:,}/{total:,} ({100*documented/total:.1f}%)')

# View Columns
total = db.fetch_one('''
    SELECT COUNT(*) FROM sys.columns c
    INNER JOIN sys.views v ON c.object_id = v.object_id
''')[0]
documented = db.fetch_one('''
    SELECT COUNT(*) FROM sys.columns c
    INNER JOIN sys.views v ON c.object_id = v.object_id
    INNER JOIN sys.extended_properties ep ON c.object_id = ep.major_id
    AND c.column_id = ep.minor_id AND ep.name = 'MS_Description'
''')[0]
print(f'View Columns:     {documented:,}/{total:,} ({100*documented/total:.1f}%)')

# Stored Procedures
total = db.fetch_one('SELECT COUNT(*) FROM sys.procedures')[0]
documented = db.fetch_one('''
    SELECT COUNT(*) FROM sys.procedures p
    INNER JOIN sys.extended_properties ep ON p.object_id = ep.major_id
    AND ep.minor_id = 0 AND ep.name = 'MS_Description'
''')[0]
print(f'Stored Procs:     {documented:,}/{total:,} ({100*documented/total:.1f}%)')

# SP Parameters
total = db.fetch_one('''
    SELECT COUNT(*) FROM sys.parameters pm
    INNER JOIN sys.procedures p ON pm.object_id = p.object_id
    WHERE pm.parameter_id > 0
''')[0]
documented = db.fetch_one('''
    SELECT COUNT(*) FROM sys.parameters pm
    INNER JOIN sys.procedures p ON pm.object_id = p.object_id
    INNER JOIN sys.extended_properties ep ON pm.object_id = ep.major_id
    AND pm.parameter_id = ep.minor_id AND ep.name = 'MS_Description'
    WHERE pm.parameter_id > 0
''')[0]
print(f'SP Parameters:    {documented:,}/{total:,} ({100*documented/total:.1f}%)')

db.disconnect()
