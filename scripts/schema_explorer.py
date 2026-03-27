#!/usr/bin/env python3
"""
MSSQL Schema Explorer
=====================
Interactive schema exploration tool for SQL Server databases.

Features:
- Browse databases, schemas, tables, views
- Explore columns with types, constraints, and descriptions
- View indexes and foreign key relationships
- Browse stored procedures, functions, and triggers
- Search across all database objects
- ERD/relationship diagram generation
- Export schema to Excel/CSV
- Schema comparison between databases
- Data preview for tables
- Visual dependency graphs (graphviz)
- Table size trending over time

Requirements:
    pip install streamlit pandas pyodbc python-dotenv openpyxl graphviz

    For visual dependency graphs, also install Graphviz system package:
    https://graphviz.org/download/

Usage:
    streamlit run schema_explorer.py

    # Custom port:
    streamlit run schema_explorer.py --server.port 8081

Environment Variables (.env):
    DB_SERVER=your_server
    DB_USERNAME=your_username
    DB_PASSWORD=your_password
"""

import streamlit as st
import pandas as pd
import pyodbc
import os
import io
import json
from typing import List, Dict, Optional, Any, Tuple
from dotenv import load_dotenv
from datetime import datetime, timedelta
from pathlib import Path

# Optional: graphviz for dependency visualization
try:
    import graphviz
    GRAPHVIZ_AVAILABLE = True
except ImportError:
    GRAPHVIZ_AVAILABLE = False

# Load environment variables
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(env_path)

# Page configuration
st.set_page_config(
    page_title="MSSQL Schema Explorer",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .schema-card {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
        margin: 8px 0;
        border-left: 4px solid #1f77b4;
    }
    .object-count {
        font-size: 24px;
        font-weight: bold;
        color: #1f77b4;
    }
    .info-label {
        color: #666;
        font-size: 12px;
    }
    .column-pk { color: #ff9900; font-weight: bold; }
    .column-fk { color: #0066cc; font-weight: bold; }
    .column-nullable { color: #999; }
    .column-required { color: #333; font-weight: bold; }
    code { background-color: #f4f4f4; padding: 2px 6px; border-radius: 4px; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { padding: 8px 16px; }
    .diff-added { background-color: #d4edda; }
    .diff-removed { background-color: #f8d7da; }
    .diff-modified { background-color: #fff3cd; }
</style>
""", unsafe_allow_html=True)


class SchemaExplorer:
    """Database schema exploration class."""

    def __init__(self):
        self.conn = None
        self.current_database = None
        self._server = None
        self._username = None
        self._password = None

    def connect(self, server: str, username: str, password: str,
                database: str = "master") -> bool:
        """Establish database connection."""
        try:
            drivers = [d for d in pyodbc.drivers() if 'SQL Server' in d]
            if not drivers:
                st.error("No SQL Server ODBC driver found")
                return False

            # Prefer newer drivers
            preferred = ['ODBC Driver 18 for SQL Server',
                        'ODBC Driver 17 for SQL Server']
            driver = next((d for d in preferred if d in drivers), drivers[0])

            conn_str = (
                f"DRIVER={{{driver}}};"
                f"SERVER={server};"
                f"DATABASE={database};"
                f"UID={username};"
                f"PWD={password};"
                f"Encrypt=yes;"
                f"TrustServerCertificate=yes;"
                f"Connection Timeout=30"
            )

            self.conn = pyodbc.connect(conn_str, timeout=30)
            self.current_database = database
            self._server = server
            self._username = username
            self._password = password
            return True
        except pyodbc.Error as e:
            st.error(f"Connection failed: {e}")
            return False

    def disconnect(self):
        """Close connection."""
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute_query(self, query: str, params: tuple = None) -> pd.DataFrame:
        """Execute query and return DataFrame."""
        try:
            if params:
                return pd.read_sql(query, self.conn, params=params)
            return pd.read_sql(query, self.conn)
        except Exception as e:
            st.error(f"Query error: {e}")
            return pd.DataFrame()

    def execute_query_raw(self, query: str, params: tuple = None) -> List[Tuple]:
        """Execute query and return raw results."""
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            st.error(f"Query error: {e}")
            return []

    def switch_database(self, database: str) -> bool:
        """Switch to a different database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(f"USE [{database}]")
            cursor.close()
            self.current_database = database
            return True
        except Exception as e:
            st.error(f"Failed to switch database: {e}")
            return False

    def get_databases(self) -> pd.DataFrame:
        """Get list of all databases."""
        query = """
        SELECT
            name AS database_name,
            database_id,
            create_date,
            state_desc AS state,
            recovery_model_desc AS recovery_model,
            CAST(SUM(size) * 8.0 / 1024 AS DECIMAL(10,2)) AS size_mb
        FROM sys.databases d
        LEFT JOIN sys.master_files f ON d.database_id = f.database_id
        WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb')
        GROUP BY name, d.database_id, create_date, state_desc, recovery_model_desc
        ORDER BY name
        """
        return self.execute_query(query)

    def get_schemas(self) -> pd.DataFrame:
        """Get list of schemas in current database."""
        query = """
        SELECT
            s.schema_id,
            s.name AS schema_name,
            p.name AS owner,
            (SELECT COUNT(*) FROM sys.tables t WHERE t.schema_id = s.schema_id) AS table_count,
            (SELECT COUNT(*) FROM sys.views v WHERE v.schema_id = s.schema_id) AS view_count,
            (SELECT COUNT(*) FROM sys.procedures pr WHERE pr.schema_id = s.schema_id) AS procedure_count
        FROM sys.schemas s
        INNER JOIN sys.database_principals p ON s.principal_id = p.principal_id
        WHERE s.name NOT IN ('sys', 'INFORMATION_SCHEMA', 'guest')
        ORDER BY s.name
        """
        return self.execute_query(query)

    def get_tables(self, schema: str = None) -> pd.DataFrame:
        """Get list of tables, optionally filtered by schema."""
        query = """
        SELECT
            s.name AS schema_name,
            t.name AS table_name,
            t.object_id,
            t.create_date,
            t.modify_date,
            p.rows AS row_count,
            CAST(SUM(a.total_pages) * 8.0 / 1024 AS DECIMAL(10,2)) AS size_mb,
            (SELECT COUNT(*) FROM sys.columns c WHERE c.object_id = t.object_id) AS column_count,
            (SELECT COUNT(*) FROM sys.indexes i WHERE i.object_id = t.object_id AND i.type > 0) AS index_count,
            ISNULL(ep.value, '') AS description
        FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.partitions p ON t.object_id = p.object_id AND p.index_id IN (0,1)
        LEFT JOIN sys.allocation_units a ON p.partition_id = a.container_id
        LEFT JOIN sys.extended_properties ep ON ep.major_id = t.object_id
            AND ep.minor_id = 0 AND ep.name = 'MS_Description'
        """
        if schema:
            query += " WHERE s.name = ?"
        query += """
        GROUP BY s.name, t.name, t.object_id, t.create_date, t.modify_date, p.rows, ep.value
        ORDER BY s.name, t.name
        """
        return self.execute_query(query, (schema,) if schema else None)

    def get_columns(self, schema: str, table: str) -> pd.DataFrame:
        """Get columns for a specific table."""
        query = """
        SELECT
            c.column_id,
            c.name AS column_name,
            TYPE_NAME(c.user_type_id) AS data_type,
            CASE
                WHEN TYPE_NAME(c.user_type_id) IN ('varchar', 'nvarchar', 'char', 'nchar')
                    THEN CASE WHEN c.max_length = -1 THEN 'MAX'
                         ELSE CAST(CASE WHEN TYPE_NAME(c.user_type_id) LIKE 'n%'
                              THEN c.max_length/2 ELSE c.max_length END AS VARCHAR) END
                WHEN TYPE_NAME(c.user_type_id) IN ('decimal', 'numeric')
                    THEN CAST(c.precision AS VARCHAR) + ',' + CAST(c.scale AS VARCHAR)
                ELSE NULL
            END AS type_detail,
            c.is_nullable,
            c.is_identity,
            ISNULL(dc.definition, '') AS default_value,
            CASE WHEN pk.column_id IS NOT NULL THEN 1 ELSE 0 END AS is_primary_key,
            CASE WHEN fk.parent_column_id IS NOT NULL THEN 1 ELSE 0 END AS is_foreign_key,
            ISNULL(fk_ref.ref_table, '') AS references_table,
            ISNULL(ep.value, '') AS description
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.default_constraints dc ON c.default_object_id = dc.object_id
        LEFT JOIN (
            SELECT ic.object_id, ic.column_id
            FROM sys.index_columns ic
            INNER JOIN sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
            WHERE i.is_primary_key = 1
        ) pk ON c.object_id = pk.object_id AND c.column_id = pk.column_id
        LEFT JOIN sys.foreign_key_columns fk ON c.object_id = fk.parent_object_id
            AND c.column_id = fk.parent_column_id
        LEFT JOIN (
            SELECT
                fkc.parent_object_id,
                fkc.parent_column_id,
                SCHEMA_NAME(rt.schema_id) + '.' + rt.name AS ref_table
            FROM sys.foreign_key_columns fkc
            INNER JOIN sys.tables rt ON fkc.referenced_object_id = rt.object_id
        ) fk_ref ON c.object_id = fk_ref.parent_object_id AND c.column_id = fk_ref.parent_column_id
        LEFT JOIN sys.extended_properties ep ON ep.major_id = c.object_id
            AND ep.minor_id = c.column_id AND ep.name = 'MS_Description'
        WHERE s.name = ? AND t.name = ?
        ORDER BY c.column_id
        """
        return self.execute_query(query, (schema, table))

    def get_indexes(self, schema: str, table: str) -> pd.DataFrame:
        """Get indexes for a specific table."""
        query = """
        SELECT
            i.name AS index_name,
            i.type_desc AS index_type,
            i.is_unique,
            i.is_primary_key,
            i.fill_factor,
            STUFF((
                SELECT ', ' + c.name + CASE WHEN ic.is_descending_key = 1 THEN ' DESC' ELSE '' END
                FROM sys.index_columns ic
                INNER JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
                WHERE ic.object_id = i.object_id AND ic.index_id = i.index_id AND ic.is_included_column = 0
                ORDER BY ic.key_ordinal
                FOR XML PATH('')
            ), 1, 2, '') AS key_columns,
            STUFF((
                SELECT ', ' + c.name
                FROM sys.index_columns ic
                INNER JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
                WHERE ic.object_id = i.object_id AND ic.index_id = i.index_id AND ic.is_included_column = 1
                ORDER BY ic.index_column_id
                FOR XML PATH('')
            ), 1, 2, '') AS included_columns,
            ps.row_count,
            CAST(ps.used_page_count * 8.0 / 1024 AS DECIMAL(10,2)) AS size_mb
        FROM sys.indexes i
        INNER JOIN sys.tables t ON i.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.dm_db_partition_stats ps ON i.object_id = ps.object_id AND i.index_id = ps.index_id
        WHERE s.name = ? AND t.name = ? AND i.type > 0
        ORDER BY i.is_primary_key DESC, i.name
        """
        return self.execute_query(query, (schema, table))

    def get_foreign_keys(self, schema: str, table: str) -> pd.DataFrame:
        """Get foreign keys for a specific table."""
        query = """
        SELECT
            fk.name AS constraint_name,
            COL_NAME(fkc.parent_object_id, fkc.parent_column_id) AS column_name,
            SCHEMA_NAME(rt.schema_id) + '.' + rt.name AS referenced_table,
            COL_NAME(fkc.referenced_object_id, fkc.referenced_column_id) AS referenced_column,
            fk.delete_referential_action_desc AS on_delete,
            fk.update_referential_action_desc AS on_update,
            fk.is_disabled
        FROM sys.foreign_keys fk
        INNER JOIN sys.foreign_key_columns fkc ON fk.object_id = fkc.constraint_object_id
        INNER JOIN sys.tables t ON fk.parent_object_id = t.object_id
        INNER JOIN sys.tables rt ON fk.referenced_object_id = rt.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE s.name = ? AND t.name = ?
        ORDER BY fk.name, fkc.constraint_column_id
        """
        return self.execute_query(query, (schema, table))

    def get_all_foreign_keys(self, schema: str = None) -> pd.DataFrame:
        """Get all foreign keys in the database for ERD generation."""
        query = """
        SELECT
            SCHEMA_NAME(pt.schema_id) AS parent_schema,
            pt.name AS parent_table,
            COL_NAME(fkc.parent_object_id, fkc.parent_column_id) AS parent_column,
            SCHEMA_NAME(rt.schema_id) AS referenced_schema,
            rt.name AS referenced_table,
            COL_NAME(fkc.referenced_object_id, fkc.referenced_column_id) AS referenced_column,
            fk.name AS constraint_name
        FROM sys.foreign_keys fk
        INNER JOIN sys.foreign_key_columns fkc ON fk.object_id = fkc.constraint_object_id
        INNER JOIN sys.tables pt ON fk.parent_object_id = pt.object_id
        INNER JOIN sys.tables rt ON fk.referenced_object_id = rt.object_id
        """
        if schema:
            query += " WHERE SCHEMA_NAME(pt.schema_id) = ? OR SCHEMA_NAME(rt.schema_id) = ?"
            return self.execute_query(query, (schema, schema))
        return self.execute_query(query)

    def get_table_primary_keys(self, schema: str = None) -> pd.DataFrame:
        """Get primary key columns for all tables."""
        query = """
        SELECT
            s.name AS schema_name,
            t.name AS table_name,
            c.name AS column_name
        FROM sys.index_columns ic
        INNER JOIN sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
        INNER JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
        INNER JOIN sys.tables t ON i.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE i.is_primary_key = 1
        """
        if schema:
            query += " AND s.name = ?"
            return self.execute_query(query, (schema,))
        return self.execute_query(query)

    def get_views(self, schema: str = None) -> pd.DataFrame:
        """Get list of views."""
        query = """
        SELECT
            s.name AS schema_name,
            v.name AS view_name,
            v.object_id,
            v.create_date,
            v.modify_date,
            OBJECTPROPERTYEX(v.object_id, 'IsSchemaBound') AS is_schema_bound,
            (SELECT COUNT(*) FROM sys.columns c WHERE c.object_id = v.object_id) AS column_count,
            ISNULL(ep.value, '') AS description
        FROM sys.views v
        INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON ep.major_id = v.object_id
            AND ep.minor_id = 0 AND ep.name = 'MS_Description'
        """
        if schema:
            query += " WHERE s.name = ?"
        query += " ORDER BY s.name, v.name"
        return self.execute_query(query, (schema,) if schema else None)

    def get_view_definition(self, schema: str, view: str) -> str:
        """Get view definition."""
        query = "SELECT OBJECT_DEFINITION(OBJECT_ID(?))"
        result = self.execute_query(query, (f"{schema}.{view}",))
        if not result.empty:
            return result.iloc[0, 0] or ""
        return ""

    def get_stored_procedures(self, schema: str = None) -> pd.DataFrame:
        """Get list of stored procedures."""
        query = """
        SELECT
            s.name AS schema_name,
            p.name AS procedure_name,
            p.object_id,
            p.create_date,
            p.modify_date,
            (SELECT COUNT(*) FROM sys.parameters pa WHERE pa.object_id = p.object_id) AS param_count,
            ISNULL(ep.value, '') AS description
        FROM sys.procedures p
        INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON ep.major_id = p.object_id
            AND ep.minor_id = 0 AND ep.name = 'MS_Description'
        WHERE p.is_ms_shipped = 0
        """
        if schema:
            query += " AND s.name = ?"
        query += " ORDER BY s.name, p.name"
        return self.execute_query(query, (schema,) if schema else None)

    def get_procedure_parameters(self, schema: str, procedure: str) -> pd.DataFrame:
        """Get parameters for a stored procedure."""
        query = """
        SELECT
            p.parameter_id,
            CASE WHEN p.name = '' THEN '@return_value' ELSE p.name END AS parameter_name,
            TYPE_NAME(p.user_type_id) AS data_type,
            p.max_length,
            p.precision,
            p.scale,
            p.is_output,
            p.has_default_value,
            p.default_value
        FROM sys.parameters p
        INNER JOIN sys.procedures pr ON p.object_id = pr.object_id
        INNER JOIN sys.schemas s ON pr.schema_id = s.schema_id
        WHERE s.name = ? AND pr.name = ?
        ORDER BY p.parameter_id
        """
        return self.execute_query(query, (schema, procedure))

    def get_procedure_definition(self, schema: str, procedure: str) -> str:
        """Get procedure definition."""
        query = "SELECT OBJECT_DEFINITION(OBJECT_ID(?))"
        result = self.execute_query(query, (f"{schema}.{procedure}",))
        if not result.empty:
            return result.iloc[0, 0] or ""
        return ""

    def get_functions(self, schema: str = None) -> pd.DataFrame:
        """Get list of functions."""
        query = """
        SELECT
            s.name AS schema_name,
            o.name AS function_name,
            o.object_id,
            o.type_desc AS function_type,
            o.create_date,
            o.modify_date,
            (SELECT COUNT(*) FROM sys.parameters pa WHERE pa.object_id = o.object_id) AS param_count,
            ISNULL(ep.value, '') AS description
        FROM sys.objects o
        INNER JOIN sys.schemas s ON o.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON ep.major_id = o.object_id
            AND ep.minor_id = 0 AND ep.name = 'MS_Description'
        WHERE o.type IN ('FN', 'IF', 'TF', 'AF')
        """
        if schema:
            query += " AND s.name = ?"
        query += " ORDER BY s.name, o.name"
        return self.execute_query(query, (schema,) if schema else None)

    def get_triggers(self, schema: str = None) -> pd.DataFrame:
        """Get list of triggers."""
        query = """
        SELECT
            s.name AS schema_name,
            t.name AS table_name,
            tr.name AS trigger_name,
            tr.object_id,
            CASE WHEN tr.is_instead_of_trigger = 1 THEN 'INSTEAD OF' ELSE 'AFTER' END AS trigger_type,
            CASE WHEN OBJECTPROPERTY(tr.object_id, 'ExecIsInsertTrigger') = 1 THEN 'INSERT ' ELSE '' END +
            CASE WHEN OBJECTPROPERTY(tr.object_id, 'ExecIsUpdateTrigger') = 1 THEN 'UPDATE ' ELSE '' END +
            CASE WHEN OBJECTPROPERTY(tr.object_id, 'ExecIsDeleteTrigger') = 1 THEN 'DELETE' ELSE '' END AS events,
            tr.is_disabled,
            tr.create_date,
            tr.modify_date
        FROM sys.triggers tr
        INNER JOIN sys.tables t ON tr.parent_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        """
        if schema:
            query += " WHERE s.name = ?"
        query += " ORDER BY s.name, t.name, tr.name"
        return self.execute_query(query, (schema,) if schema else None)

    def search_objects(self, search_term: str) -> pd.DataFrame:
        """Search for objects across the database."""
        query = """
        SELECT
            s.name AS schema_name,
            o.name AS object_name,
            o.type_desc AS object_type,
            o.create_date,
            o.modify_date
        FROM sys.objects o
        INNER JOIN sys.schemas s ON o.schema_id = s.schema_id
        WHERE o.name LIKE ?
            AND o.type IN ('U', 'V', 'P', 'FN', 'IF', 'TF', 'TR')
        ORDER BY o.type_desc, s.name, o.name
        """
        return self.execute_query(query, (f"%{search_term}%",))

    def search_columns(self, search_term: str) -> pd.DataFrame:
        """Search for columns across all tables."""
        query = """
        SELECT
            s.name AS schema_name,
            t.name AS table_name,
            c.name AS column_name,
            TYPE_NAME(c.user_type_id) AS data_type,
            c.is_nullable,
            ISNULL(ep.value, '') AS description
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON ep.major_id = c.object_id
            AND ep.minor_id = c.column_id AND ep.name = 'MS_Description'
        WHERE c.name LIKE ?
        ORDER BY s.name, t.name, c.name
        """
        return self.execute_query(query, (f"%{search_term}%",))

    def preview_table_data(self, schema: str, table: str, limit: int = 100) -> pd.DataFrame:
        """Preview data from a table with a row limit."""
        # Use parameterized limit isn't directly supported, so we validate
        limit = min(max(1, limit), 1000)  # Clamp between 1 and 1000
        query = f"SELECT TOP {limit} * FROM [{schema}].[{table}]"
        return self.execute_query(query)

    def get_schema_for_comparison(self, database: str = None) -> Dict[str, Any]:
        """Get complete schema information for comparison."""
        original_db = self.current_database
        if database and database != self.current_database:
            self.switch_database(database)

        schema_info = {
            'database': self.current_database,
            'tables': {},
            'views': {},
            'procedures': {},
            'functions': {}
        }

        # Get all tables with columns
        tables = self.get_tables()
        for _, table_row in tables.iterrows():
            schema_name = table_row['schema_name']
            table_name = table_row['table_name']
            full_name = f"{schema_name}.{table_name}"

            columns = self.get_columns(schema_name, table_name)
            schema_info['tables'][full_name] = {
                'row_count': table_row['row_count'],
                'columns': {
                    row['column_name']: {
                        'data_type': row['data_type'],
                        'type_detail': row['type_detail'],
                        'is_nullable': row['is_nullable'],
                        'is_primary_key': row['is_primary_key'],
                        'is_foreign_key': row['is_foreign_key']
                    }
                    for _, row in columns.iterrows()
                }
            }

        # Get views
        views = self.get_views()
        for _, view_row in views.iterrows():
            full_name = f"{view_row['schema_name']}.{view_row['view_name']}"
            schema_info['views'][full_name] = {
                'column_count': view_row['column_count']
            }

        # Get procedures
        procs = self.get_stored_procedures()
        for _, proc_row in procs.iterrows():
            full_name = f"{proc_row['schema_name']}.{proc_row['procedure_name']}"
            schema_info['procedures'][full_name] = {
                'param_count': proc_row['param_count']
            }

        # Get functions
        funcs = self.get_functions()
        for _, func_row in funcs.iterrows():
            full_name = f"{func_row['schema_name']}.{func_row['function_name']}"
            schema_info['functions'][full_name] = {
                'function_type': func_row['function_type'],
                'param_count': func_row['param_count']
            }

        # Restore original database
        if database and database != original_db:
            self.switch_database(original_db)

        return schema_info

    def get_all_columns_for_export(self, schema: str = None) -> pd.DataFrame:
        """Get all columns for export functionality."""
        query = """
        SELECT
            s.name AS schema_name,
            t.name AS table_name,
            c.name AS column_name,
            c.column_id,
            TYPE_NAME(c.user_type_id) AS data_type,
            CASE
                WHEN TYPE_NAME(c.user_type_id) IN ('varchar', 'nvarchar', 'char', 'nchar')
                    THEN CASE WHEN c.max_length = -1 THEN 'MAX'
                         ELSE CAST(CASE WHEN TYPE_NAME(c.user_type_id) LIKE 'n%'
                              THEN c.max_length/2 ELSE c.max_length END AS VARCHAR) END
                WHEN TYPE_NAME(c.user_type_id) IN ('decimal', 'numeric')
                    THEN CAST(c.precision AS VARCHAR) + ',' + CAST(c.scale AS VARCHAR)
                ELSE NULL
            END AS type_detail,
            c.is_nullable,
            c.is_identity,
            CASE WHEN pk.column_id IS NOT NULL THEN 1 ELSE 0 END AS is_primary_key,
            CASE WHEN fk.parent_column_id IS NOT NULL THEN 1 ELSE 0 END AS is_foreign_key,
            ISNULL(ep.value, '') AS description
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN (
            SELECT ic.object_id, ic.column_id
            FROM sys.index_columns ic
            INNER JOIN sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
            WHERE i.is_primary_key = 1
        ) pk ON c.object_id = pk.object_id AND c.column_id = pk.column_id
        LEFT JOIN sys.foreign_key_columns fk ON c.object_id = fk.parent_object_id
            AND c.column_id = fk.parent_column_id
        LEFT JOIN sys.extended_properties ep ON ep.major_id = c.object_id
            AND ep.minor_id = c.column_id AND ep.name = 'MS_Description'
        """
        if schema:
            query += " WHERE s.name = ?"
        query += " ORDER BY s.name, t.name, c.column_id"
        return self.execute_query(query, (schema,) if schema else None)

    # ===== NEW FEATURES =====

    def get_index_usage_stats(self, schema: str = None) -> pd.DataFrame:
        """Get index usage statistics to identify unused or underused indexes."""
        query = """
        SELECT
            SCHEMA_NAME(t.schema_id) AS schema_name,
            t.name AS table_name,
            i.name AS index_name,
            i.type_desc AS index_type,
            i.is_primary_key,
            i.is_unique,
            ISNULL(ius.user_seeks, 0) AS user_seeks,
            ISNULL(ius.user_scans, 0) AS user_scans,
            ISNULL(ius.user_lookups, 0) AS user_lookups,
            ISNULL(ius.user_seeks, 0) + ISNULL(ius.user_scans, 0) + ISNULL(ius.user_lookups, 0) AS total_reads,
            ISNULL(ius.user_updates, 0) AS user_updates,
            ISNULL(ius.last_user_seek, '1900-01-01') AS last_user_seek,
            ISNULL(ius.last_user_scan, '1900-01-01') AS last_user_scan,
            ISNULL(ius.last_user_lookup, '1900-01-01') AS last_user_lookup,
            ISNULL(ius.last_user_update, '1900-01-01') AS last_user_update,
            CAST(ps.used_page_count * 8.0 / 1024 AS DECIMAL(10,2)) AS size_mb,
            CASE
                WHEN i.is_primary_key = 1 THEN 'Primary Key'
                WHEN i.is_unique = 1 THEN 'Unique Constraint'
                WHEN ISNULL(ius.user_seeks, 0) + ISNULL(ius.user_scans, 0) + ISNULL(ius.user_lookups, 0) = 0
                    AND ISNULL(ius.user_updates, 0) > 0 THEN 'UNUSED - Consider Dropping'
                WHEN ISNULL(ius.user_seeks, 0) + ISNULL(ius.user_scans, 0) + ISNULL(ius.user_lookups, 0) < 10
                    THEN 'Low Usage'
                ELSE 'Active'
            END AS status
        FROM sys.indexes i
        INNER JOIN sys.tables t ON i.object_id = t.object_id
        LEFT JOIN sys.dm_db_index_usage_stats ius ON i.object_id = ius.object_id
            AND i.index_id = ius.index_id AND ius.database_id = DB_ID()
        LEFT JOIN sys.dm_db_partition_stats ps ON i.object_id = ps.object_id AND i.index_id = ps.index_id
        WHERE i.type > 0 AND i.is_hypothetical = 0
        """
        if schema:
            query += " AND SCHEMA_NAME(t.schema_id) = ?"
        query += " ORDER BY total_reads ASC, user_updates DESC"
        return self.execute_query(query, (schema,) if schema else None)

    def get_missing_index_suggestions(self) -> pd.DataFrame:
        """Get missing index suggestions from SQL Server."""
        query = """
        SELECT TOP 50
            SCHEMA_NAME(t.schema_id) AS schema_name,
            t.name AS table_name,
            mid.equality_columns,
            mid.inequality_columns,
            mid.included_columns,
            migs.unique_compiles,
            migs.user_seeks,
            migs.user_scans,
            migs.avg_total_user_cost,
            migs.avg_user_impact,
            CAST(migs.avg_total_user_cost * migs.avg_user_impact * (migs.user_seeks + migs.user_scans) AS DECIMAL(18,2)) AS improvement_measure,
            'CREATE NONCLUSTERED INDEX [IX_' + t.name + '_' + REPLACE(REPLACE(REPLACE(ISNULL(mid.equality_columns,''), ', ', '_'), '[', ''), ']', '') + '] ON ' +
            mid.statement + ' (' + ISNULL(mid.equality_columns, '') +
            CASE WHEN mid.equality_columns IS NOT NULL AND mid.inequality_columns IS NOT NULL THEN ', ' ELSE '' END +
            ISNULL(mid.inequality_columns, '') + ')' +
            ISNULL(' INCLUDE (' + mid.included_columns + ')', '') AS suggested_index_script
        FROM sys.dm_db_missing_index_details mid
        INNER JOIN sys.dm_db_missing_index_groups mig ON mid.index_handle = mig.index_handle
        INNER JOIN sys.dm_db_missing_index_group_stats migs ON mig.index_group_handle = migs.group_handle
        INNER JOIN sys.tables t ON mid.object_id = t.object_id
        WHERE mid.database_id = DB_ID()
        ORDER BY improvement_measure DESC
        """
        return self.execute_query(query)

    def get_object_dependencies(self, schema: str, object_name: str) -> pd.DataFrame:
        """Get objects that the specified object depends on (references)."""
        query = """
        SELECT
            SCHEMA_NAME(ref_obj.schema_id) AS referenced_schema,
            ref_obj.name AS referenced_object,
            ref_obj.type_desc AS referenced_type,
            sed.referenced_minor_name AS referenced_column,
            sed.is_caller_dependent,
            sed.is_ambiguous
        FROM sys.sql_expression_dependencies sed
        INNER JOIN sys.objects obj ON sed.referencing_id = obj.object_id
        INNER JOIN sys.schemas s ON obj.schema_id = s.schema_id
        LEFT JOIN sys.objects ref_obj ON sed.referenced_id = ref_obj.object_id
        WHERE s.name = ? AND obj.name = ?
        ORDER BY referenced_schema, referenced_object
        """
        return self.execute_query(query, (schema, object_name))

    def get_object_dependents(self, schema: str, object_name: str) -> pd.DataFrame:
        """Get objects that depend on (reference) the specified object."""
        query = """
        SELECT
            SCHEMA_NAME(obj.schema_id) AS dependent_schema,
            obj.name AS dependent_object,
            obj.type_desc AS dependent_type,
            sed.referencing_minor_name AS referencing_column
        FROM sys.sql_expression_dependencies sed
        INNER JOIN sys.objects obj ON sed.referencing_id = obj.object_id
        INNER JOIN sys.objects ref_obj ON sed.referenced_id = ref_obj.object_id
        INNER JOIN sys.schemas s ON ref_obj.schema_id = s.schema_id
        WHERE s.name = ? AND ref_obj.name = ?
        ORDER BY dependent_schema, dependent_object
        """
        return self.execute_query(query, (schema, object_name))

    def get_all_dependencies(self, schema: str = None) -> pd.DataFrame:
        """Get all object dependencies in the database."""
        query = """
        SELECT
            SCHEMA_NAME(obj.schema_id) AS referencing_schema,
            obj.name AS referencing_object,
            obj.type_desc AS referencing_type,
            SCHEMA_NAME(ref_obj.schema_id) AS referenced_schema,
            ref_obj.name AS referenced_object,
            ref_obj.type_desc AS referenced_type
        FROM sys.sql_expression_dependencies sed
        INNER JOIN sys.objects obj ON sed.referencing_id = obj.object_id
        LEFT JOIN sys.objects ref_obj ON sed.referenced_id = ref_obj.object_id
        WHERE ref_obj.object_id IS NOT NULL
        """
        if schema:
            query += " AND (SCHEMA_NAME(obj.schema_id) = ? OR SCHEMA_NAME(ref_obj.schema_id) = ?)"
            return self.execute_query(query, (schema, schema))
        query += " ORDER BY referencing_schema, referencing_object"
        return self.execute_query(query)

    def get_schema_change_history(self, days: int = 30) -> pd.DataFrame:
        """Get recent schema changes based on object create/modify dates."""
        query = """
        SELECT
            SCHEMA_NAME(o.schema_id) AS schema_name,
            o.name AS object_name,
            o.type_desc AS object_type,
            o.create_date,
            o.modify_date,
            CASE
                WHEN o.create_date = o.modify_date THEN 'Created'
                WHEN o.modify_date > o.create_date THEN 'Modified'
                ELSE 'Unknown'
            END AS change_type,
            DATEDIFF(day, o.modify_date, GETDATE()) AS days_since_change
        FROM sys.objects o
        WHERE o.type IN ('U', 'V', 'P', 'FN', 'IF', 'TF', 'TR')
            AND o.is_ms_shipped = 0
            AND o.modify_date >= DATEADD(day, -?, GETDATE())
        ORDER BY o.modify_date DESC
        """
        return self.execute_query(query, (days,))

    def get_recent_ddl_events(self) -> pd.DataFrame:
        """Get recent DDL events from default trace (if available)."""
        query = """
        DECLARE @trace_path NVARCHAR(260)
        SELECT @trace_path = path FROM sys.traces WHERE is_default = 1

        IF @trace_path IS NOT NULL
        BEGIN
            SELECT TOP 100
                te.name AS event_name,
                t.DatabaseName AS database_name,
                t.ObjectName AS object_name,
                t.ObjectType AS object_type,
                t.LoginName AS login_name,
                t.StartTime AS event_time,
                t.TextData AS ddl_text
            FROM fn_trace_gettable(@trace_path, DEFAULT) t
            INNER JOIN sys.trace_events te ON t.EventClass = te.trace_event_id
            WHERE te.name IN ('Object:Created', 'Object:Altered', 'Object:Deleted')
                AND t.DatabaseName = DB_NAME()
            ORDER BY t.StartTime DESC
        END
        ELSE
        BEGIN
            SELECT
                'Default trace not available' AS event_name,
                NULL AS database_name,
                NULL AS object_name,
                NULL AS object_type,
                NULL AS login_name,
                NULL AS event_time,
                NULL AS ddl_text
            WHERE 1=0
        END
        """
        return self.execute_query(query)

    def get_column_profile(self, schema: str, table: str, column: str) -> Dict[str, Any]:
        """Get detailed statistics for a specific column."""
        # First get column info
        col_info_query = """
        SELECT
            TYPE_NAME(c.user_type_id) AS data_type,
            c.max_length,
            c.precision,
            c.scale,
            c.is_nullable
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE s.name = ? AND t.name = ? AND c.name = ?
        """
        col_info = self.execute_query(col_info_query, (schema, table, column))

        if col_info.empty:
            return {}

        data_type = col_info.iloc[0]['data_type']
        profile = {'data_type': data_type}

        # Build profile query based on data type
        numeric_types = ['int', 'bigint', 'smallint', 'tinyint', 'decimal', 'numeric', 'float', 'real', 'money', 'smallmoney']
        string_types = ['varchar', 'nvarchar', 'char', 'nchar', 'text', 'ntext']
        date_types = ['date', 'datetime', 'datetime2', 'smalldatetime', 'time', 'datetimeoffset']

        try:
            # Base stats for all types
            base_query = f"""
            SELECT
                COUNT(*) AS total_rows,
                COUNT([{column}]) AS non_null_count,
                COUNT(*) - COUNT([{column}]) AS null_count,
                CAST(COUNT(DISTINCT [{column}]) AS BIGINT) AS distinct_count
            FROM [{schema}].[{table}]
            """
            base_stats = self.execute_query(base_query)
            if not base_stats.empty:
                profile.update(base_stats.iloc[0].to_dict())

            # Type-specific stats
            if data_type.lower() in numeric_types:
                num_query = f"""
                SELECT
                    MIN([{column}]) AS min_value,
                    MAX([{column}]) AS max_value,
                    AVG(CAST([{column}] AS FLOAT)) AS avg_value,
                    STDEV(CAST([{column}] AS FLOAT)) AS std_dev
                FROM [{schema}].[{table}]
                WHERE [{column}] IS NOT NULL
                """
                num_stats = self.execute_query(num_query)
                if not num_stats.empty:
                    profile.update(num_stats.iloc[0].to_dict())

            elif data_type.lower() in string_types:
                str_query = f"""
                SELECT
                    MIN(LEN([{column}])) AS min_length,
                    MAX(LEN([{column}])) AS max_length,
                    AVG(CAST(LEN([{column}]) AS FLOAT)) AS avg_length
                FROM [{schema}].[{table}]
                WHERE [{column}] IS NOT NULL
                """
                str_stats = self.execute_query(str_query)
                if not str_stats.empty:
                    profile.update(str_stats.iloc[0].to_dict())

                # Get top values
                top_query = f"""
                SELECT TOP 10 [{column}] AS value, COUNT(*) AS frequency
                FROM [{schema}].[{table}]
                WHERE [{column}] IS NOT NULL
                GROUP BY [{column}]
                ORDER BY COUNT(*) DESC
                """
                top_values = self.execute_query(top_query)
                if not top_values.empty:
                    profile['top_values'] = top_values.to_dict('records')

            elif data_type.lower() in date_types:
                date_query = f"""
                SELECT
                    MIN([{column}]) AS min_date,
                    MAX([{column}]) AS max_date
                FROM [{schema}].[{table}]
                WHERE [{column}] IS NOT NULL
                """
                date_stats = self.execute_query(date_query)
                if not date_stats.empty:
                    profile.update(date_stats.iloc[0].to_dict())

        except Exception as e:
            profile['error'] = str(e)

        return profile

    def get_table_profile_summary(self, schema: str, table: str) -> pd.DataFrame:
        """Get a summary profile of all columns in a table."""
        query = f"""
        SELECT
            c.name AS column_name,
            TYPE_NAME(c.user_type_id) AS data_type,
            c.is_nullable,
            (SELECT COUNT(*) FROM [{schema}].[{table}]) AS total_rows
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE s.name = ? AND t.name = ?
        ORDER BY c.column_id
        """
        columns_df = self.execute_query(query, (schema, table))

        if columns_df.empty:
            return pd.DataFrame()

        # Build dynamic query for null counts and distinct counts
        col_stats = []
        for _, row in columns_df.iterrows():
            col_name = row['column_name']
            try:
                stats_query = f"""
                SELECT
                    '{col_name}' AS column_name,
                    COUNT([{col_name}]) AS non_null_count,
                    COUNT(*) - COUNT([{col_name}]) AS null_count,
                    COUNT(DISTINCT [{col_name}]) AS distinct_count
                FROM [{schema}].[{table}]
                """
                stats = self.execute_query(stats_query)
                if not stats.empty:
                    col_stats.append(stats.iloc[0].to_dict())
            except Exception:
                col_stats.append({
                    'column_name': col_name,
                    'non_null_count': None,
                    'null_count': None,
                    'distinct_count': None
                })

        stats_df = pd.DataFrame(col_stats)
        result = columns_df.merge(stats_df, on='column_name', how='left')

        # Calculate null percentage
        if 'total_rows' in result.columns and 'null_count' in result.columns:
            result['null_pct'] = (result['null_count'] / result['total_rows'] * 100).round(2)
            result['unique_pct'] = (result['distinct_count'] / result['total_rows'] * 100).round(2)

        return result

    def generate_dependency_graph(self, schema: str = None,
                                   object_name: str = None,
                                   depth: int = 2) -> Optional['graphviz.Digraph']:
        """
        Generate a visual dependency graph using graphviz.

        Args:
            schema: Filter to specific schema
            object_name: Center graph around specific object
            depth: How many levels of dependencies to show (1-3)

        Returns:
            graphviz.Digraph object or None if graphviz not available
        """
        if not GRAPHVIZ_AVAILABLE:
            return None

        # Get all dependencies
        deps = self.get_all_dependencies(schema)
        if deps.empty:
            return None

        # Create directed graph
        dot = graphviz.Digraph(
            comment='Object Dependencies',
            engine='dot'
        )
        dot.attr(rankdir='LR', splines='ortho')
        dot.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='10')

        # Color scheme by object type
        type_colors = {
            'USER_TABLE': '#E3F2FD',
            'VIEW': '#E8F5E9',
            'SQL_STORED_PROCEDURE': '#FFF3E0',
            'SQL_SCALAR_FUNCTION': '#F3E5F5',
            'SQL_TABLE_VALUED_FUNCTION': '#F3E5F5',
            'SQL_INLINE_TABLE_VALUED_FUNCTION': '#F3E5F5',
            'SQL_TRIGGER': '#FFEBEE',
            'DEFAULT': '#F5F5F5'
        }

        # If specific object, filter to related dependencies
        if object_name:
            related_objects = set([object_name])
            for _ in range(depth):
                new_related = set()
                for obj in related_objects:
                    # Find objects this one references
                    refs = deps[deps['referencing_name'].str.contains(obj, case=False, na=False)]
                    new_related.update(refs['referenced_name'].tolist())
                    # Find objects that reference this one
                    refs_by = deps[deps['referenced_name'].str.contains(obj, case=False, na=False)]
                    new_related.update(refs_by['referencing_name'].tolist())
                related_objects.update(new_related)

            # Filter dependencies to only related objects
            deps = deps[
                deps['referencing_name'].isin(related_objects) |
                deps['referenced_name'].isin(related_objects)
            ]

        # Add nodes and edges
        nodes_added = set()
        for _, row in deps.iterrows():
            ref_name = row['referencing_name']
            ref_type = row['referencing_type']
            referenced_name = row['referenced_name']
            referenced_type = row.get('referenced_type', 'DEFAULT')

            # Add referencing node
            if ref_name not in nodes_added:
                color = type_colors.get(ref_type, type_colors['DEFAULT'])
                label = f"{ref_name}\\n({ref_type.replace('SQL_', '').replace('_', ' ').title()})"
                dot.node(ref_name, label, fillcolor=color)
                nodes_added.add(ref_name)

            # Add referenced node
            if referenced_name not in nodes_added:
                color = type_colors.get(referenced_type, type_colors['DEFAULT'])
                ref_type_label = referenced_type.replace('SQL_', '').replace('_', ' ').title() if referenced_type else 'Object'
                label = f"{referenced_name}\\n({ref_type_label})"
                dot.node(referenced_name, label, fillcolor=color)
                nodes_added.add(referenced_name)

            # Add edge
            dot.edge(ref_name, referenced_name, color='#666666')

        return dot

    def get_table_sizes(self, schema: str = None) -> pd.DataFrame:
        """Get current table sizes including row count, data size, and index size."""
        query = """
        SELECT
            s.name AS schema_name,
            t.name AS table_name,
            p.rows AS row_count,
            CAST(SUM(a.total_pages) * 8 / 1024.0 AS DECIMAL(18,2)) AS total_size_mb,
            CAST(SUM(a.used_pages) * 8 / 1024.0 AS DECIMAL(18,2)) AS used_size_mb,
            CAST(SUM(CASE WHEN i.type <= 1 THEN a.data_pages ELSE 0 END) * 8 / 1024.0 AS DECIMAL(18,2)) AS data_size_mb,
            CAST(SUM(CASE WHEN i.type > 1 THEN a.used_pages ELSE 0 END) * 8 / 1024.0 AS DECIMAL(18,2)) AS index_size_mb,
            GETDATE() AS snapshot_time
        FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        INNER JOIN sys.indexes i ON t.object_id = i.object_id
        INNER JOIN sys.partitions p ON i.object_id = p.object_id AND i.index_id = p.index_id
        INNER JOIN sys.allocation_units a ON p.partition_id = a.container_id
        WHERE t.is_ms_shipped = 0
        """
        if schema:
            query += " AND s.name = ?"
            query += " GROUP BY s.name, t.name, p.rows ORDER BY SUM(a.total_pages) DESC"
            return self.execute_query(query, (schema,))
        else:
            query += " GROUP BY s.name, t.name, p.rows ORDER BY SUM(a.total_pages) DESC"
            return self.execute_query(query)

    def get_table_size_history_path(self) -> Path:
        """Get path to table size history file."""
        data_dir = Path(os.path.dirname(os.path.dirname(__file__))) / 'data' / 'schema_explorer'
        data_dir.mkdir(parents=True, exist_ok=True)
        return data_dir / f'{self.current_database}_table_sizes.json'

    def save_table_size_snapshot(self) -> bool:
        """Save current table sizes to history file."""
        try:
            sizes = self.get_table_sizes()
            if sizes.empty:
                return False

            history_path = self.get_table_size_history_path()

            # Load existing history
            history = []
            if history_path.exists():
                with open(history_path, 'r') as f:
                    history = json.load(f)

            # Add current snapshot
            snapshot = {
                'timestamp': datetime.now().isoformat(),
                'database': self.current_database,
                'tables': sizes.to_dict('records')
            }
            history.append(snapshot)

            # Keep only last 365 days of snapshots
            cutoff = datetime.now() - timedelta(days=365)
            history = [h for h in history if datetime.fromisoformat(h['timestamp']) > cutoff]

            # Save
            with open(history_path, 'w') as f:
                json.dump(history, f, indent=2, default=str)

            return True
        except Exception as e:
            st.error(f"Failed to save snapshot: {e}")
            return False

    def load_table_size_history(self) -> List[Dict]:
        """Load table size history from file."""
        history_path = self.get_table_size_history_path()
        if history_path.exists():
            with open(history_path, 'r') as f:
                return json.load(f)
        return []

    def get_table_size_trend(self, schema: str, table: str,
                             days: int = 30) -> pd.DataFrame:
        """Get size trend for a specific table over time."""
        history = self.load_table_size_history()

        if not history:
            return pd.DataFrame()

        cutoff = datetime.now() - timedelta(days=days)

        trend_data = []
        for snapshot in history:
            snapshot_time = datetime.fromisoformat(snapshot['timestamp'])
            if snapshot_time < cutoff:
                continue

            for table_data in snapshot['tables']:
                if table_data['schema_name'] == schema and table_data['table_name'] == table:
                    trend_data.append({
                        'timestamp': snapshot_time,
                        'row_count': table_data['row_count'],
                        'total_size_mb': table_data['total_size_mb'],
                        'data_size_mb': table_data['data_size_mb'],
                        'index_size_mb': table_data['index_size_mb']
                    })
                    break

        if not trend_data:
            return pd.DataFrame()

        return pd.DataFrame(trend_data).sort_values('timestamp')

    def get_database_size_trend(self, days: int = 30) -> pd.DataFrame:
        """Get total database size trend over time."""
        history = self.load_table_size_history()

        if not history:
            return pd.DataFrame()

        cutoff = datetime.now() - timedelta(days=days)

        trend_data = []
        for snapshot in history:
            snapshot_time = datetime.fromisoformat(snapshot['timestamp'])
            if snapshot_time < cutoff:
                continue

            total_rows = sum(t['row_count'] for t in snapshot['tables'])
            total_size = sum(t['total_size_mb'] for t in snapshot['tables'])
            total_data = sum(t['data_size_mb'] for t in snapshot['tables'])
            total_index = sum(t['index_size_mb'] for t in snapshot['tables'])

            trend_data.append({
                'timestamp': snapshot_time,
                'total_rows': total_rows,
                'total_size_mb': total_size,
                'data_size_mb': total_data,
                'index_size_mb': total_index,
                'table_count': len(snapshot['tables'])
            })

        if not trend_data:
            return pd.DataFrame()

        return pd.DataFrame(trend_data).sort_values('timestamp')


def generate_mermaid_erd(explorer: SchemaExplorer, schema: str = None,
                         selected_tables: List[str] = None) -> str:
    """Generate Mermaid ERD diagram from foreign key relationships."""
    tables = explorer.get_tables(schema)
    fks = explorer.get_all_foreign_keys(schema)
    pks = explorer.get_table_primary_keys(schema)

    if tables.empty:
        return "erDiagram\n    %% No tables found"

    # Filter tables if selection provided
    if selected_tables:
        tables = tables[tables.apply(
            lambda r: f"{r['schema_name']}.{r['table_name']}" in selected_tables, axis=1)]

    # Build table definitions with PK columns
    pk_by_table = {}
    for _, row in pks.iterrows():
        table_key = f"{row['schema_name']}.{row['table_name']}"
        if table_key not in pk_by_table:
            pk_by_table[table_key] = []
        pk_by_table[table_key].append(row['column_name'])

    mermaid = "erDiagram\n"

    # Add tables
    table_names = set()
    for _, row in tables.iterrows():
        table_key = f"{row['schema_name']}__{row['table_name']}"
        table_names.add(table_key)
        pk_cols = pk_by_table.get(f"{row['schema_name']}.{row['table_name']}", [])
        if pk_cols:
            mermaid += f"    {table_key} {{\n"
            for pk in pk_cols:
                mermaid += f"        PK {pk}\n"
            mermaid += "    }\n"

    # Add relationships
    for _, row in fks.iterrows():
        parent_key = f"{row['parent_schema']}__{row['parent_table']}"
        ref_key = f"{row['referenced_schema']}__{row['referenced_table']}"

        # Only include if both tables are in our set
        if selected_tables:
            parent_full = f"{row['parent_schema']}.{row['parent_table']}"
            ref_full = f"{row['referenced_schema']}.{row['referenced_table']}"
            if parent_full not in selected_tables or ref_full not in selected_tables:
                continue

        mermaid += f"    {ref_key} ||--o{{ {parent_key} : \"{row['parent_column']}\"\n"

    return mermaid


def compare_schemas(schema1: Dict, schema2: Dict) -> Dict[str, Any]:
    """Compare two database schemas and return differences."""
    differences = {
        'tables': {'added': [], 'removed': [], 'modified': []},
        'views': {'added': [], 'removed': []},
        'procedures': {'added': [], 'removed': []},
        'functions': {'added': [], 'removed': []}
    }

    # Compare tables
    tables1 = set(schema1['tables'].keys())
    tables2 = set(schema2['tables'].keys())

    differences['tables']['added'] = list(tables2 - tables1)
    differences['tables']['removed'] = list(tables1 - tables2)

    # Check for modified tables (column changes)
    common_tables = tables1 & tables2
    for table in common_tables:
        cols1 = set(schema1['tables'][table]['columns'].keys())
        cols2 = set(schema2['tables'][table]['columns'].keys())

        if cols1 != cols2:
            added_cols = cols2 - cols1
            removed_cols = cols1 - cols2
            differences['tables']['modified'].append({
                'table': table,
                'added_columns': list(added_cols),
                'removed_columns': list(removed_cols)
            })
        else:
            # Check for type changes in common columns
            for col in cols1:
                if schema1['tables'][table]['columns'][col] != schema2['tables'][table]['columns'][col]:
                    differences['tables']['modified'].append({
                        'table': table,
                        'column': col,
                        'old': schema1['tables'][table]['columns'][col],
                        'new': schema2['tables'][table]['columns'][col]
                    })

    # Compare views
    views1 = set(schema1['views'].keys())
    views2 = set(schema2['views'].keys())
    differences['views']['added'] = list(views2 - views1)
    differences['views']['removed'] = list(views1 - views2)

    # Compare procedures
    procs1 = set(schema1['procedures'].keys())
    procs2 = set(schema2['procedures'].keys())
    differences['procedures']['added'] = list(procs2 - procs1)
    differences['procedures']['removed'] = list(procs1 - procs2)

    # Compare functions
    funcs1 = set(schema1['functions'].keys())
    funcs2 = set(schema2['functions'].keys())
    differences['functions']['added'] = list(funcs2 - funcs1)
    differences['functions']['removed'] = list(funcs1 - funcs2)

    return differences


def export_to_excel(explorer: SchemaExplorer, schema: str = None) -> bytes:
    """Export schema documentation to Excel."""
    output = io.BytesIO()

    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        # Tables sheet
        tables = explorer.get_tables(schema)
        if not tables.empty:
            tables.to_excel(writer, sheet_name='Tables', index=False)

        # Columns sheet
        columns = explorer.get_all_columns_for_export(schema)
        if not columns.empty:
            columns.to_excel(writer, sheet_name='Columns', index=False)

        # Views sheet
        views = explorer.get_views(schema)
        if not views.empty:
            views.to_excel(writer, sheet_name='Views', index=False)

        # Procedures sheet
        procs = explorer.get_stored_procedures(schema)
        if not procs.empty:
            procs.to_excel(writer, sheet_name='Procedures', index=False)

        # Functions sheet
        funcs = explorer.get_functions(schema)
        if not funcs.empty:
            funcs.to_excel(writer, sheet_name='Functions', index=False)

        # Triggers sheet
        triggers = explorer.get_triggers(schema)
        if not triggers.empty:
            triggers.to_excel(writer, sheet_name='Triggers', index=False)

        # Foreign Keys sheet
        fks = explorer.get_all_foreign_keys(schema)
        if not fks.empty:
            fks.to_excel(writer, sheet_name='Foreign Keys', index=False)

    output.seek(0)
    return output.getvalue()


def export_to_csv(explorer: SchemaExplorer, export_type: str, schema: str = None) -> str:
    """Export specific schema data to CSV."""
    if export_type == 'tables':
        df = explorer.get_tables(schema)
    elif export_type == 'columns':
        df = explorer.get_all_columns_for_export(schema)
    elif export_type == 'views':
        df = explorer.get_views(schema)
    elif export_type == 'procedures':
        df = explorer.get_stored_procedures(schema)
    elif export_type == 'functions':
        df = explorer.get_functions(schema)
    elif export_type == 'foreign_keys':
        df = explorer.get_all_foreign_keys(schema)
    else:
        return ""

    return df.to_csv(index=False)


# Initialize session state
if 'explorer' not in st.session_state:
    st.session_state.explorer = SchemaExplorer()
if 'connected' not in st.session_state:
    st.session_state.connected = False
if 'comparison_schema1' not in st.session_state:
    st.session_state.comparison_schema1 = None
if 'comparison_schema2' not in st.session_state:
    st.session_state.comparison_schema2 = None


def main():
    st.title("🔍 MSSQL Schema Explorer")

    # Sidebar - Connection
    with st.sidebar:
        st.header("Connection")

        if not st.session_state.connected:
            server = st.text_input("Server", value=os.getenv('DB_SERVER', ''))
            username = st.text_input("Username", value=os.getenv('DB_USERNAME', ''))
            password = st.text_input("Password", type="password", value=os.getenv('DB_PASSWORD', ''))
            database = st.text_input("Database", value=os.getenv('DB_DATABASE', 'master'))

            if st.button("Connect", type="primary"):
                if st.session_state.explorer.connect(server, username, password, database):
                    st.session_state.connected = True
                    st.rerun()
        else:
            st.success(f"Connected to: {st.session_state.explorer.current_database}")

            # Database selector
            databases = st.session_state.explorer.get_databases()
            if not databases.empty:
                db_list = ['master'] + databases['database_name'].tolist()
                current_idx = db_list.index(st.session_state.explorer.current_database) if st.session_state.explorer.current_database in db_list else 0
                selected_db = st.selectbox("Switch Database", db_list, index=current_idx)
                if selected_db != st.session_state.explorer.current_database:
                    if st.session_state.explorer.switch_database(selected_db):
                        st.rerun()

            if st.button("Disconnect"):
                st.session_state.explorer.disconnect()
                st.session_state.connected = False
                st.rerun()

    # Main content
    if not st.session_state.connected:
        st.info("Please connect to a database using the sidebar.")
        st.markdown("""
        ### Getting Started
        1. Enter your SQL Server connection details in the sidebar
        2. Click **Connect** to establish connection
        3. Use the tabs to explore your database schema

        ### Features
        - **Schema Browser**: Explore tables, views, procedures, functions, triggers
        - **ERD Diagrams**: Generate relationship diagrams from foreign keys
        - **Data Preview**: Sample rows from any table
        - **Schema Export**: Export to Excel or CSV
        - **Schema Compare**: Compare schemas between databases
        - **Index Usage**: Identify unused indexes and get optimization suggestions
        - **Dependencies**: Track object relationships and references
        - **Change History**: View recent schema modifications
        - **Data Profiling**: Analyze column statistics and data quality

        ### Environment Variables
        You can also set these in your `.env` file:
        ```
        DB_SERVER=your_server
        DB_USERNAME=your_username
        DB_PASSWORD=your_password
        DB_DATABASE=your_database
        ```
        """)
        return

    explorer = st.session_state.explorer

    # Main tabs
    tabs = st.tabs([
        "📊 Overview", "📋 Tables", "👁️ Views", "⚙️ Procedures",
        "🔧 Functions", "⚡ Triggers", "🔎 Search",
        "🔗 ERD", "📤 Export", "🔄 Compare", "👀 Data Preview",
        "📈 Index Usage", "🔀 Dependencies", "📜 History", "📊 Profiling",
        "📉 Size Trends"
    ])

    # Overview Tab
    with tabs[0]:
        st.subheader(f"Database: {explorer.current_database}")

        # Schema summary
        schemas = explorer.get_schemas()
        if not schemas.empty:
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Schemas", len(schemas))
            col2.metric("Tables", schemas['table_count'].sum())
            col3.metric("Views", schemas['view_count'].sum())
            col4.metric("Procedures", schemas['procedure_count'].sum())

            st.markdown("---")
            st.subheader("Schemas")
            st.dataframe(
                schemas,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "schema_id": st.column_config.NumberColumn("ID", width="small"),
                    "schema_name": st.column_config.TextColumn("Schema", width="medium"),
                    "owner": st.column_config.TextColumn("Owner", width="medium"),
                    "table_count": st.column_config.NumberColumn("Tables", width="small"),
                    "view_count": st.column_config.NumberColumn("Views", width="small"),
                    "procedure_count": st.column_config.NumberColumn("Procedures", width="small"),
                }
            )

    # Tables Tab
    with tabs[1]:
        schemas = explorer.get_schemas()
        schema_list = ['All'] + schemas['schema_name'].tolist() if not schemas.empty else ['All']
        selected_schema = st.selectbox("Filter by Schema", schema_list, key="table_schema")

        tables = explorer.get_tables(None if selected_schema == 'All' else selected_schema)

        if not tables.empty:
            st.subheader(f"Tables ({len(tables)})")

            table_options = [f"{row['schema_name']}.{row['table_name']}" for _, row in tables.iterrows()]
            selected_table = st.selectbox("Select Table", table_options, key="selected_table")

            if selected_table:
                schema, table = selected_table.split('.', 1)

                table_info = tables[tables['table_name'] == table].iloc[0]
                with st.expander("Table Info", expanded=True):
                    col1, col2, col3, col4 = st.columns(4)
                    col1.metric("Rows", f"{table_info['row_count']:,}" if pd.notna(table_info['row_count']) else "N/A")
                    col2.metric("Size (MB)", f"{table_info['size_mb']:.2f}" if pd.notna(table_info['size_mb']) else "N/A")
                    col3.metric("Columns", table_info['column_count'])
                    col4.metric("Indexes", table_info['index_count'])
                    if table_info['description']:
                        st.info(f"**Description:** {table_info['description']}")

                col_tab, idx_tab, fk_tab = st.tabs(["Columns", "Indexes", "Foreign Keys"])

                with col_tab:
                    columns = explorer.get_columns(schema, table)
                    if not columns.empty:
                        st.dataframe(
                            columns,
                            use_container_width=True,
                            hide_index=True,
                            column_config={
                                "column_id": st.column_config.NumberColumn("#", width="small"),
                                "column_name": st.column_config.TextColumn("Column", width="medium"),
                                "data_type": st.column_config.TextColumn("Type", width="small"),
                                "type_detail": st.column_config.TextColumn("Detail", width="small"),
                                "is_nullable": st.column_config.CheckboxColumn("Nullable", width="small"),
                                "is_identity": st.column_config.CheckboxColumn("Identity", width="small"),
                                "is_primary_key": st.column_config.CheckboxColumn("PK", width="small"),
                                "is_foreign_key": st.column_config.CheckboxColumn("FK", width="small"),
                                "references_table": st.column_config.TextColumn("References", width="medium"),
                                "description": st.column_config.TextColumn("Description", width="large"),
                            }
                        )

                with idx_tab:
                    indexes = explorer.get_indexes(schema, table)
                    if not indexes.empty:
                        st.dataframe(indexes, use_container_width=True, hide_index=True)
                    else:
                        st.info("No indexes found for this table.")

                with fk_tab:
                    fks = explorer.get_foreign_keys(schema, table)
                    if not fks.empty:
                        st.dataframe(fks, use_container_width=True, hide_index=True)
                    else:
                        st.info("No foreign keys found for this table.")

    # Views Tab
    with tabs[2]:
        schemas = explorer.get_schemas()
        schema_list = ['All'] + schemas['schema_name'].tolist() if not schemas.empty else ['All']
        selected_schema = st.selectbox("Filter by Schema", schema_list, key="view_schema")

        views = explorer.get_views(None if selected_schema == 'All' else selected_schema)

        if not views.empty:
            st.subheader(f"Views ({len(views)})")

            view_options = [f"{row['schema_name']}.{row['view_name']}" for _, row in views.iterrows()]
            selected_view = st.selectbox("Select View", view_options, key="selected_view")

            if selected_view:
                schema, view = selected_view.split('.', 1)
                view_info = views[views['view_name'] == view].iloc[0]

                col1, col2, col3 = st.columns(3)
                col1.metric("Columns", view_info['column_count'])
                col2.metric("Schema Bound", "Yes" if view_info['is_schema_bound'] else "No")
                col3.metric("Created", view_info['create_date'].strftime("%Y-%m-%d") if pd.notna(view_info['create_date']) else "N/A")

                if view_info['description']:
                    st.info(f"**Description:** {view_info['description']}")

                with st.expander("View Definition"):
                    definition = explorer.get_view_definition(schema, view)
                    st.code(definition, language="sql")
        else:
            st.info("No views found.")

    # Procedures Tab
    with tabs[3]:
        schemas = explorer.get_schemas()
        schema_list = ['All'] + schemas['schema_name'].tolist() if not schemas.empty else ['All']
        selected_schema = st.selectbox("Filter by Schema", schema_list, key="proc_schema")

        procs = explorer.get_stored_procedures(None if selected_schema == 'All' else selected_schema)

        if not procs.empty:
            st.subheader(f"Stored Procedures ({len(procs)})")

            proc_options = [f"{row['schema_name']}.{row['procedure_name']}" for _, row in procs.iterrows()]
            selected_proc = st.selectbox("Select Procedure", proc_options, key="selected_proc")

            if selected_proc:
                schema, proc = selected_proc.split('.', 1)
                proc_info = procs[procs['procedure_name'] == proc].iloc[0]

                col1, col2, col3 = st.columns(3)
                col1.metric("Parameters", proc_info['param_count'])
                col2.metric("Created", proc_info['create_date'].strftime("%Y-%m-%d") if pd.notna(proc_info['create_date']) else "N/A")
                col3.metric("Modified", proc_info['modify_date'].strftime("%Y-%m-%d") if pd.notna(proc_info['modify_date']) else "N/A")

                if proc_info['description']:
                    st.info(f"**Description:** {proc_info['description']}")

                params = explorer.get_procedure_parameters(schema, proc)
                if not params.empty:
                    st.markdown("**Parameters:**")
                    st.dataframe(params, use_container_width=True, hide_index=True)

                with st.expander("Procedure Definition"):
                    definition = explorer.get_procedure_definition(schema, proc)
                    st.code(definition, language="sql")
        else:
            st.info("No stored procedures found.")

    # Functions Tab
    with tabs[4]:
        schemas = explorer.get_schemas()
        schema_list = ['All'] + schemas['schema_name'].tolist() if not schemas.empty else ['All']
        selected_schema = st.selectbox("Filter by Schema", schema_list, key="func_schema")

        functions = explorer.get_functions(None if selected_schema == 'All' else selected_schema)

        if not functions.empty:
            st.subheader(f"Functions ({len(functions)})")
            st.dataframe(functions, use_container_width=True, hide_index=True)
        else:
            st.info("No functions found.")

    # Triggers Tab
    with tabs[5]:
        schemas = explorer.get_schemas()
        schema_list = ['All'] + schemas['schema_name'].tolist() if not schemas.empty else ['All']
        selected_schema = st.selectbox("Filter by Schema", schema_list, key="trigger_schema")

        triggers = explorer.get_triggers(None if selected_schema == 'All' else selected_schema)

        if not triggers.empty:
            st.subheader(f"Triggers ({len(triggers)})")
            st.dataframe(triggers, use_container_width=True, hide_index=True)
        else:
            st.info("No triggers found.")

    # Search Tab
    with tabs[6]:
        st.subheader("Search Database Objects")

        col1, col2 = st.columns([3, 1])
        with col1:
            search_term = st.text_input("Search term", placeholder="Enter object or column name...")
        with col2:
            search_type = st.selectbox("Search in", ["Objects", "Columns"])

        if search_term:
            if search_type == "Objects":
                results = explorer.search_objects(search_term)
                if not results.empty:
                    st.success(f"Found {len(results)} objects matching '{search_term}'")
                    st.dataframe(results, use_container_width=True, hide_index=True)
                else:
                    st.warning(f"No objects found matching '{search_term}'")
            else:
                results = explorer.search_columns(search_term)
                if not results.empty:
                    st.success(f"Found {len(results)} columns matching '{search_term}'")
                    st.dataframe(results, use_container_width=True, hide_index=True)
                else:
                    st.warning(f"No columns found matching '{search_term}'")

    # ERD Tab
    with tabs[7]:
        st.subheader("Entity Relationship Diagram")
        st.markdown("Generate ERD diagrams from foreign key relationships using Mermaid syntax.")

        schemas = explorer.get_schemas()
        schema_list = ['All'] + schemas['schema_name'].tolist() if not schemas.empty else ['All']

        col1, col2 = st.columns([1, 2])
        with col1:
            erd_schema = st.selectbox("Schema", schema_list, key="erd_schema")

        # Get tables for selection
        tables = explorer.get_tables(None if erd_schema == 'All' else erd_schema)
        if not tables.empty:
            table_options = [f"{row['schema_name']}.{row['table_name']}" for _, row in tables.iterrows()]

            with col2:
                selected_tables = st.multiselect(
                    "Select Tables (leave empty for all)",
                    table_options,
                    key="erd_tables",
                    help="Select specific tables to include in the ERD, or leave empty to include all tables with relationships"
                )

            if st.button("Generate ERD", type="primary"):
                with st.spinner("Generating ERD..."):
                    mermaid_code = generate_mermaid_erd(
                        explorer,
                        None if erd_schema == 'All' else erd_schema,
                        selected_tables if selected_tables else None
                    )

                    st.markdown("### ERD Diagram")
                    st.markdown(f"```mermaid\n{mermaid_code}\n```")

                    with st.expander("View Mermaid Code"):
                        st.code(mermaid_code, language="text")

                    st.download_button(
                        "Download Mermaid Code",
                        mermaid_code,
                        file_name=f"erd_{explorer.current_database}.mmd",
                        mime="text/plain"
                    )

            # Show foreign keys table
            with st.expander("View All Foreign Key Relationships"):
                fks = explorer.get_all_foreign_keys(None if erd_schema == 'All' else erd_schema)
                if not fks.empty:
                    st.dataframe(fks, use_container_width=True, hide_index=True)
                else:
                    st.info("No foreign key relationships found.")
        else:
            st.info("No tables found in the selected schema.")

    # Export Tab
    with tabs[8]:
        st.subheader("Export Schema Documentation")

        schemas = explorer.get_schemas()
        schema_list = ['All'] + schemas['schema_name'].tolist() if not schemas.empty else ['All']
        export_schema = st.selectbox("Schema to Export", schema_list, key="export_schema")

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Excel Export")
            st.markdown("Export complete schema documentation to Excel with multiple sheets.")

            if st.button("Generate Excel", type="primary"):
                with st.spinner("Generating Excel file..."):
                    try:
                        excel_data = export_to_excel(
                            explorer,
                            None if export_schema == 'All' else export_schema
                        )
                        st.download_button(
                            "Download Excel File",
                            excel_data,
                            file_name=f"schema_{explorer.current_database}_{datetime.now().strftime('%Y%m%d')}.xlsx",
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
                        st.success("Excel file generated successfully!")
                    except ImportError:
                        st.error("openpyxl is required for Excel export. Install with: pip install openpyxl")

        with col2:
            st.markdown("### CSV Export")
            st.markdown("Export individual schema components to CSV.")

            csv_type = st.selectbox("Export Type", [
                "tables", "columns", "views", "procedures", "functions", "foreign_keys"
            ])

            if st.button("Generate CSV"):
                with st.spinner("Generating CSV..."):
                    csv_data = export_to_csv(
                        explorer,
                        csv_type,
                        None if export_schema == 'All' else export_schema
                    )
                    if csv_data:
                        st.download_button(
                            "Download CSV File",
                            csv_data,
                            file_name=f"{csv_type}_{explorer.current_database}_{datetime.now().strftime('%Y%m%d')}.csv",
                            mime="text/csv"
                        )
                        st.success("CSV file generated successfully!")
                    else:
                        st.warning("No data to export.")

    # Compare Tab
    with tabs[9]:
        st.subheader("Schema Comparison")
        st.markdown("Compare schemas between two databases to identify differences.")

        databases = explorer.get_databases()
        if not databases.empty:
            db_list = databases['database_name'].tolist()

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### Source Database")
                db1 = st.selectbox("Database 1", db_list, key="compare_db1")
                if st.button("Capture Schema 1"):
                    with st.spinner(f"Capturing schema from {db1}..."):
                        st.session_state.comparison_schema1 = explorer.get_schema_for_comparison(db1)
                        st.success(f"Captured schema from {db1}")

                if st.session_state.comparison_schema1:
                    schema1 = st.session_state.comparison_schema1
                    st.info(f"**{schema1['database']}**: {len(schema1['tables'])} tables, "
                           f"{len(schema1['views'])} views, {len(schema1['procedures'])} procedures")

            with col2:
                st.markdown("### Target Database")
                db2 = st.selectbox("Database 2", db_list, key="compare_db2")
                if st.button("Capture Schema 2"):
                    with st.spinner(f"Capturing schema from {db2}..."):
                        st.session_state.comparison_schema2 = explorer.get_schema_for_comparison(db2)
                        st.success(f"Captured schema from {db2}")

                if st.session_state.comparison_schema2:
                    schema2 = st.session_state.comparison_schema2
                    st.info(f"**{schema2['database']}**: {len(schema2['tables'])} tables, "
                           f"{len(schema2['views'])} views, {len(schema2['procedures'])} procedures")

            st.markdown("---")

            if st.session_state.comparison_schema1 and st.session_state.comparison_schema2:
                if st.button("Compare Schemas", type="primary"):
                    with st.spinner("Comparing schemas..."):
                        diff = compare_schemas(
                            st.session_state.comparison_schema1,
                            st.session_state.comparison_schema2
                        )

                        # Display results
                        st.markdown("### Comparison Results")

                        # Tables
                        st.markdown("#### Tables")
                        tcol1, tcol2, tcol3 = st.columns(3)

                        with tcol1:
                            st.markdown("**Added** (in target only)")
                            if diff['tables']['added']:
                                for t in diff['tables']['added']:
                                    st.markdown(f"- `{t}`")
                            else:
                                st.markdown("*None*")

                        with tcol2:
                            st.markdown("**Removed** (in source only)")
                            if diff['tables']['removed']:
                                for t in diff['tables']['removed']:
                                    st.markdown(f"- `{t}`")
                            else:
                                st.markdown("*None*")

                        with tcol3:
                            st.markdown("**Modified**")
                            if diff['tables']['modified']:
                                for mod in diff['tables']['modified']:
                                    if 'added_columns' in mod:
                                        st.markdown(f"- `{mod['table']}`: +{len(mod['added_columns'])} cols, -{len(mod['removed_columns'])} cols")
                                    else:
                                        st.markdown(f"- `{mod['table']}.{mod['column']}`: type changed")
                            else:
                                st.markdown("*None*")

                        # Views
                        st.markdown("#### Views")
                        vcol1, vcol2 = st.columns(2)
                        with vcol1:
                            st.markdown("**Added**")
                            for v in diff['views']['added'] or ["*None*"]:
                                st.markdown(f"- `{v}`" if v != "*None*" else v)
                        with vcol2:
                            st.markdown("**Removed**")
                            for v in diff['views']['removed'] or ["*None*"]:
                                st.markdown(f"- `{v}`" if v != "*None*" else v)

                        # Procedures
                        st.markdown("#### Stored Procedures")
                        pcol1, pcol2 = st.columns(2)
                        with pcol1:
                            st.markdown("**Added**")
                            for p in diff['procedures']['added'] or ["*None*"]:
                                st.markdown(f"- `{p}`" if p != "*None*" else p)
                        with pcol2:
                            st.markdown("**Removed**")
                            for p in diff['procedures']['removed'] or ["*None*"]:
                                st.markdown(f"- `{p}`" if p != "*None*" else p)

                        # Summary
                        st.markdown("---")
                        total_changes = (
                            len(diff['tables']['added']) + len(diff['tables']['removed']) + len(diff['tables']['modified']) +
                            len(diff['views']['added']) + len(diff['views']['removed']) +
                            len(diff['procedures']['added']) + len(diff['procedures']['removed']) +
                            len(diff['functions']['added']) + len(diff['functions']['removed'])
                        )
                        if total_changes == 0:
                            st.success("Schemas are identical!")
                        else:
                            st.warning(f"Found {total_changes} difference(s) between schemas.")
            else:
                st.info("Capture both schemas to compare them.")
        else:
            st.warning("No databases found.")

    # Data Preview Tab
    with tabs[10]:
        st.subheader("Data Preview")
        st.markdown("Preview sample data from tables (read-only).")

        schemas = explorer.get_schemas()
        schema_list = ['All'] + schemas['schema_name'].tolist() if not schemas.empty else ['All']
        preview_schema = st.selectbox("Filter by Schema", schema_list, key="preview_schema")

        tables = explorer.get_tables(None if preview_schema == 'All' else preview_schema)

        if not tables.empty:
            table_options = [f"{row['schema_name']}.{row['table_name']}" for _, row in tables.iterrows()]
            selected_table = st.selectbox("Select Table", table_options, key="preview_table")

            col1, col2 = st.columns([1, 3])
            with col1:
                row_limit = st.number_input("Row Limit", min_value=10, max_value=1000, value=100, step=10)

            if selected_table:
                schema, table = selected_table.split('.', 1)

                # Show table info
                table_info = tables[tables['table_name'] == table].iloc[0]
                st.info(f"**{selected_table}** - {table_info['row_count']:,} total rows, {table_info['column_count']} columns")

                if st.button("Load Data Preview", type="primary"):
                    with st.spinner(f"Loading {row_limit} rows from {selected_table}..."):
                        preview_data = explorer.preview_table_data(schema, table, row_limit)

                        if not preview_data.empty:
                            st.success(f"Showing {len(preview_data)} rows")
                            st.dataframe(
                                preview_data,
                                use_container_width=True,
                                hide_index=True
                            )

                            # Download option
                            csv = preview_data.to_csv(index=False)
                            st.download_button(
                                "Download Preview as CSV",
                                csv,
                                file_name=f"{selected_table}_preview.csv",
                                mime="text/csv"
                            )
                        else:
                            st.info("Table is empty or an error occurred.")
        else:
            st.info("No tables found.")

    # Index Usage Tab
    with tabs[11]:
        st.subheader("Index Usage Statistics")
        st.markdown("Analyze index usage to identify unused or underused indexes.")

        idx_tab1, idx_tab2 = st.tabs(["📊 Index Usage Stats", "💡 Missing Index Suggestions"])

        with idx_tab1:
            schemas = explorer.get_schemas()
            schema_list = ['All'] + schemas['schema_name'].tolist() if not schemas.empty else ['All']
            idx_schema = st.selectbox("Filter by Schema", schema_list, key="idx_usage_schema")

            if st.button("Analyze Index Usage", type="primary", key="analyze_idx"):
                with st.spinner("Analyzing index usage statistics..."):
                    idx_stats = explorer.get_index_usage_stats(
                        None if idx_schema == 'All' else idx_schema
                    )

                    if not idx_stats.empty:
                        # Summary metrics
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            total_indexes = len(idx_stats)
                            st.metric("Total Indexes", total_indexes)
                        with col2:
                            unused = len(idx_stats[idx_stats['usage_status'] == 'Unused'])
                            st.metric("Unused Indexes", unused)
                        with col3:
                            rarely_used = len(idx_stats[idx_stats['usage_status'] == 'Rarely Used'])
                            st.metric("Rarely Used", rarely_used)
                        with col4:
                            active = len(idx_stats[idx_stats['usage_status'] == 'Active'])
                            st.metric("Active Indexes", active)

                        # Filter by status
                        status_filter = st.multiselect(
                            "Filter by Status",
                            options=['Active', 'Rarely Used', 'Unused'],
                            default=['Unused', 'Rarely Used'],
                            key="idx_status_filter"
                        )

                        filtered_stats = idx_stats[idx_stats['usage_status'].isin(status_filter)] if status_filter else idx_stats

                        if not filtered_stats.empty:
                            st.dataframe(
                                filtered_stats,
                                use_container_width=True,
                                hide_index=True
                            )

                            # Recommendations
                            st.markdown("### Recommendations")
                            unused_indexes = idx_stats[idx_stats['usage_status'] == 'Unused']
                            if not unused_indexes.empty:
                                st.warning(f"⚠️ Found {len(unused_indexes)} unused indexes that may be candidates for removal:")
                                for _, idx in unused_indexes.head(10).iterrows():
                                    st.code(f"-- Consider dropping: [{idx['schema_name']}].[{idx['table_name']}].[{idx['index_name']}]")
                            else:
                                st.success("✅ No completely unused indexes found.")
                        else:
                            st.info("No indexes match the selected filters.")
                    else:
                        st.info("No index usage statistics available.")

        with idx_tab2:
            st.markdown("SQL Server's missing index suggestions based on query execution plans.")

            if st.button("Get Missing Index Suggestions", type="primary", key="get_missing_idx"):
                with st.spinner("Querying missing index suggestions..."):
                    missing_idx = explorer.get_missing_index_suggestions()

                    if not missing_idx.empty:
                        st.success(f"Found {len(missing_idx)} missing index suggestion(s)")

                        for _, idx in missing_idx.iterrows():
                            with st.expander(f"📋 {idx['schema_name']}.{idx['table_name']} (Impact: {idx['avg_user_impact']:.1f}%)"):
                                st.markdown(f"**Equality Columns:** {idx['equality_columns'] or 'None'}")
                                st.markdown(f"**Inequality Columns:** {idx['inequality_columns'] or 'None'}")
                                st.markdown(f"**Include Columns:** {idx['included_columns'] or 'None'}")
                                st.markdown(f"**User Seeks:** {idx['user_seeks']:,}")
                                st.markdown(f"**User Scans:** {idx['user_scans']:,}")

                                # Generate CREATE INDEX statement
                                cols = []
                                if idx['equality_columns']:
                                    cols.extend(idx['equality_columns'].split(', '))
                                if idx['inequality_columns']:
                                    cols.extend(idx['inequality_columns'].split(', '))

                                idx_name = f"IX_{idx['table_name']}_{'_'.join(c.strip('[]') for c in cols[:3])}"
                                include_clause = f" INCLUDE ({idx['included_columns']})" if idx['included_columns'] else ""

                                create_stmt = f"""CREATE NONCLUSTERED INDEX [{idx_name}]
ON [{idx['schema_name']}].[{idx['table_name']}] ({', '.join(cols)}){include_clause};"""

                                st.code(create_stmt, language="sql")
                    else:
                        st.info("No missing index suggestions available. This could mean your indexes are well-optimized!")

    # Dependencies Tab
    with tabs[12]:
        st.subheader("Object Dependencies")
        st.markdown("Track which objects reference each other in the database.")

        dep_tab1, dep_tab2, dep_tab3 = st.tabs(["🔍 Object Lookup", "🌐 All Dependencies", "📊 Visual Graph"])

        with dep_tab1:
            col1, col2 = st.columns(2)

            with col1:
                schemas = explorer.get_schemas()
                dep_schema = st.selectbox(
                    "Schema",
                    schemas['schema_name'].tolist() if not schemas.empty else [],
                    key="dep_schema"
                )

            with col2:
                # Get all objects in selected schema
                if dep_schema:
                    all_objects = []

                    tables = explorer.get_tables(dep_schema)
                    if not tables.empty:
                        all_objects.extend([f"Table: {t}" for t in tables['table_name'].tolist()])

                    views = explorer.get_views(dep_schema)
                    if not views.empty:
                        all_objects.extend([f"View: {v}" for v in views['view_name'].tolist()])

                    procs = explorer.get_procedures(dep_schema)
                    if not procs.empty:
                        all_objects.extend([f"Procedure: {p}" for p in procs['procedure_name'].tolist()])

                    funcs = explorer.get_functions(dep_schema)
                    if not funcs.empty:
                        all_objects.extend([f"Function: {f}" for f in funcs['function_name'].tolist()])

                    dep_object = st.selectbox("Select Object", all_objects, key="dep_object")
                else:
                    dep_object = None

            if dep_object and dep_schema:
                object_name = dep_object.split(': ', 1)[1]

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### 📤 Dependencies (References)")
                    st.caption("Objects that this object depends on")

                    deps = explorer.get_object_dependencies(dep_schema, object_name)
                    if not deps.empty:
                        st.dataframe(deps, use_container_width=True, hide_index=True)
                    else:
                        st.info("No dependencies found.")

                with col2:
                    st.markdown("### 📥 Dependents (Referenced By)")
                    st.caption("Objects that depend on this object")

                    dependents = explorer.get_object_dependents(dep_schema, object_name)
                    if not dependents.empty:
                        st.dataframe(dependents, use_container_width=True, hide_index=True)
                    else:
                        st.info("No dependents found.")

        with dep_tab2:
            schemas = explorer.get_schemas()
            schema_list = ['All'] + schemas['schema_name'].tolist() if not schemas.empty else ['All']
            all_dep_schema = st.selectbox("Filter by Schema", schema_list, key="all_dep_schema")

            if st.button("Load All Dependencies", type="primary", key="load_all_deps"):
                with st.spinner("Loading all dependencies..."):
                    all_deps = explorer.get_all_dependencies(
                        None if all_dep_schema == 'All' else all_dep_schema
                    )

                    if not all_deps.empty:
                        st.success(f"Found {len(all_deps)} dependency relationship(s)")

                        # Group by referencing object type
                        st.markdown("### Dependencies by Object Type")
                        type_counts = all_deps['referencing_type'].value_counts()
                        for obj_type, count in type_counts.items():
                            st.markdown(f"- **{obj_type}**: {count} dependencies")

                        st.markdown("### Full Dependency List")
                        st.dataframe(all_deps, use_container_width=True, hide_index=True)

                        # Download option
                        csv = all_deps.to_csv(index=False)
                        st.download_button(
                            "Download Dependencies CSV",
                            csv,
                            file_name="dependencies.csv",
                            mime="text/csv"
                        )
                    else:
                        st.info("No dependencies found.")

        with dep_tab3:
            if not GRAPHVIZ_AVAILABLE:
                st.warning("Graphviz is not installed. Install it with: `pip install graphviz`")
                st.info("You also need to install Graphviz system package: https://graphviz.org/download/")
            else:
                st.markdown("Generate visual dependency graphs showing object relationships.")

                col1, col2 = st.columns([2, 1])

                with col1:
                    schemas = explorer.get_schemas()
                    schema_list = ['All'] + schemas['schema_name'].tolist() if not schemas.empty else ['All']
                    graph_schema = st.selectbox("Filter by Schema", schema_list, key="graph_schema")

                with col2:
                    graph_depth = st.slider("Graph Depth", 1, 3, 2, key="graph_depth",
                                           help="How many levels of dependencies to show")

                # Optional: focus on specific object
                focus_on_object = st.checkbox("Focus on specific object", key="focus_object")

                focus_object_name = None
                if focus_on_object:
                    if graph_schema and graph_schema != 'All':
                        all_objects = []
                        tables = explorer.get_tables(graph_schema)
                        if not tables.empty:
                            all_objects.extend(tables['table_name'].tolist())
                        views = explorer.get_views(graph_schema)
                        if not views.empty:
                            all_objects.extend(views['view_name'].tolist())
                        procs = explorer.get_procedures(graph_schema)
                        if not procs.empty:
                            all_objects.extend(procs['procedure_name'].tolist())
                        funcs = explorer.get_functions(graph_schema)
                        if not funcs.empty:
                            all_objects.extend(funcs['function_name'].tolist())

                        if all_objects:
                            focus_object_name = st.selectbox("Center graph on", all_objects, key="focus_obj_select")
                    else:
                        focus_object_name = st.text_input("Object name to focus on", key="focus_obj_text")

                if st.button("Generate Dependency Graph", type="primary", key="gen_dep_graph"):
                    with st.spinner("Generating dependency graph..."):
                        graph = explorer.generate_dependency_graph(
                            schema=None if graph_schema == 'All' else graph_schema,
                            object_name=focus_object_name if focus_on_object else None,
                            depth=graph_depth
                        )

                        if graph:
                            st.success("Graph generated successfully!")

                            # Display the graph
                            st.graphviz_chart(graph, use_container_width=True)

                            # Legend
                            st.markdown("### Legend")
                            legend_cols = st.columns(6)
                            with legend_cols[0]:
                                st.markdown("🔵 **Table**")
                            with legend_cols[1]:
                                st.markdown("🟢 **View**")
                            with legend_cols[2]:
                                st.markdown("🟠 **Procedure**")
                            with legend_cols[3]:
                                st.markdown("🟣 **Function**")
                            with legend_cols[4]:
                                st.markdown("🔴 **Trigger**")
                            with legend_cols[5]:
                                st.markdown("⬜ **Other**")

                            # Download options
                            col1, col2 = st.columns(2)
                            with col1:
                                st.download_button(
                                    "Download as DOT",
                                    graph.source,
                                    file_name="dependencies.dot",
                                    mime="text/plain"
                                )
                            with col2:
                                try:
                                    svg_data = graph.pipe(format='svg').decode('utf-8')
                                    st.download_button(
                                        "Download as SVG",
                                        svg_data,
                                        file_name="dependencies.svg",
                                        mime="image/svg+xml"
                                    )
                                except Exception:
                                    st.caption("SVG export requires Graphviz system installation")
                        else:
                            st.info("No dependencies found to visualize.")

    # History Tab
    with tabs[13]:
        st.subheader("Schema Change History")
        st.markdown("Track recent schema modifications and DDL events.")

        hist_tab1, hist_tab2 = st.tabs(["📅 Recent Changes", "📋 DDL Events"])

        with hist_tab1:
            days = st.slider("Show changes from last N days", 1, 365, 30, key="history_days")

            if st.button("Load Change History", type="primary", key="load_history"):
                with st.spinner(f"Loading changes from last {days} days..."):
                    history = explorer.get_schema_change_history(days)

                    if not history.empty:
                        # Summary
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            created = len(history[history['change_type'] == 'Created'])
                            st.metric("Objects Created", created)
                        with col2:
                            modified = len(history[history['change_type'] == 'Modified'])
                            st.metric("Objects Modified", modified)
                        with col3:
                            total = len(history)
                            st.metric("Total Changes", total)

                        # Filter by change type
                        change_filter = st.multiselect(
                            "Filter by Change Type",
                            options=['Created', 'Modified'],
                            default=['Created', 'Modified'],
                            key="change_type_filter"
                        )

                        filtered_history = history[history['change_type'].isin(change_filter)] if change_filter else history

                        # Group by object type
                        st.markdown("### Changes by Object Type")
                        type_summary = filtered_history.groupby('object_type').size().reset_index(name='count')
                        for _, row in type_summary.iterrows():
                            st.markdown(f"- **{row['object_type']}**: {row['count']} change(s)")

                        st.markdown("### Change Details")
                        st.dataframe(
                            filtered_history,
                            use_container_width=True,
                            hide_index=True
                        )
                    else:
                        st.info(f"No schema changes found in the last {days} days.")

        with hist_tab2:
            st.markdown("DDL events from SQL Server's default trace (if available).")
            st.caption("Note: DDL event capture requires specific SQL Server configuration.")

            if st.button("Load DDL Events", type="primary", key="load_ddl"):
                with st.spinner("Querying DDL events from default trace..."):
                    ddl_events = explorer.get_recent_ddl_events()

                    if not ddl_events.empty:
                        st.success(f"Found {len(ddl_events)} DDL event(s)")

                        # Summary by event type
                        st.markdown("### Events by Type")
                        event_summary = ddl_events['event_type'].value_counts()
                        for event_type, count in event_summary.items():
                            st.markdown(f"- **{event_type}**: {count}")

                        st.markdown("### Event Details")
                        st.dataframe(ddl_events, use_container_width=True, hide_index=True)
                    else:
                        st.info("No DDL events found or default trace is not enabled.")

    # Profiling Tab
    with tabs[14]:
        st.subheader("Data Profiling")
        st.markdown("Analyze column statistics including min, max, distinct counts, and null percentages.")

        schemas = explorer.get_schemas()
        schema_list = schemas['schema_name'].tolist() if not schemas.empty else []
        profile_schema = st.selectbox("Select Schema", schema_list, key="profile_schema")

        if profile_schema:
            tables = explorer.get_tables(profile_schema)

            if not tables.empty:
                table_list = tables['table_name'].tolist()
                profile_table = st.selectbox("Select Table", table_list, key="profile_table")

                if profile_table:
                    table_info = tables[tables['table_name'] == profile_table].iloc[0]
                    st.info(f"**{profile_schema}.{profile_table}** - {table_info['row_count']:,} rows, {table_info['column_count']} columns")

                    prof_tab1, prof_tab2 = st.tabs(["📊 Table Summary", "🔬 Column Detail"])

                    with prof_tab1:
                        if st.button("Generate Table Profile", type="primary", key="gen_table_profile"):
                            with st.spinner(f"Profiling {profile_schema}.{profile_table}..."):
                                profile_summary = explorer.get_table_profile_summary(profile_schema, profile_table)

                                if not profile_summary.empty:
                                    st.success("Profile generated successfully!")

                                    # Highlight columns with issues
                                    st.markdown("### Data Quality Indicators")

                                    high_null_cols = profile_summary[profile_summary['null_percent'] > 50]
                                    if not high_null_cols.empty:
                                        st.warning(f"⚠️ {len(high_null_cols)} column(s) with >50% null values")

                                    low_cardinality = profile_summary[
                                        (profile_summary['distinct_count'] < 10) &
                                        (profile_summary['distinct_count'] > 0)
                                    ]
                                    if not low_cardinality.empty:
                                        st.info(f"📋 {len(low_cardinality)} column(s) with low cardinality (<10 distinct values)")

                                    st.markdown("### Column Statistics")
                                    st.dataframe(
                                        profile_summary,
                                        use_container_width=True,
                                        hide_index=True
                                    )

                                    # Download option
                                    csv = profile_summary.to_csv(index=False)
                                    st.download_button(
                                        "Download Profile CSV",
                                        csv,
                                        file_name=f"{profile_schema}_{profile_table}_profile.csv",
                                        mime="text/csv"
                                    )
                                else:
                                    st.error("Failed to generate profile. Table may be empty or inaccessible.")

                    with prof_tab2:
                        columns = explorer.get_columns(profile_schema, profile_table)

                        if not columns.empty:
                            col_list = columns['column_name'].tolist()
                            detail_column = st.selectbox("Select Column", col_list, key="detail_column")

                            if detail_column and st.button("Profile Column", type="primary", key="profile_col"):
                                with st.spinner(f"Profiling column {detail_column}..."):
                                    col_profile = explorer.get_column_profile(profile_schema, profile_table, detail_column)

                                    if col_profile:
                                        col1, col2 = st.columns(2)

                                        with col1:
                                            st.markdown("### Basic Statistics")
                                            st.metric("Total Count", f"{col_profile.get('total_count', 0):,}")
                                            st.metric("Distinct Count", f"{col_profile.get('distinct_count', 0):,}")
                                            st.metric("Null Count", f"{col_profile.get('null_count', 0):,}")
                                            st.metric("Null Percentage", f"{col_profile.get('null_percent', 0):.2f}%")

                                        with col2:
                                            st.markdown("### Value Statistics")
                                            st.metric("Min Value", str(col_profile.get('min_value', 'N/A'))[:50])
                                            st.metric("Max Value", str(col_profile.get('max_value', 'N/A'))[:50])

                                            if col_profile.get('avg_value') is not None:
                                                st.metric("Average", f"{col_profile['avg_value']:.2f}")

                                            if col_profile.get('avg_length') is not None:
                                                st.metric("Avg Length", f"{col_profile['avg_length']:.1f}")

                                        # Top values
                                        if col_profile.get('top_values'):
                                            st.markdown("### Top 10 Values")
                                            top_df = pd.DataFrame(
                                                col_profile['top_values'],
                                                columns=['Value', 'Count']
                                            )
                                            st.dataframe(top_df, use_container_width=True, hide_index=True)
                                    else:
                                        st.error("Failed to profile column.")
                        else:
                            st.info("No columns found.")
            else:
                st.info("No tables found in selected schema.")

    # Size Trends Tab
    with tabs[15]:
        st.subheader("Table Size Trends")
        st.markdown("Track table and database size changes over time.")

        trend_tab1, trend_tab2, trend_tab3 = st.tabs(["📊 Current Sizes", "📈 Table Trends", "🗄️ Database Trends"])

        with trend_tab1:
            st.markdown("### Current Table Sizes")

            schemas = explorer.get_schemas()
            schema_list = ['All'] + schemas['schema_name'].tolist() if not schemas.empty else ['All']
            size_schema = st.selectbox("Filter by Schema", schema_list, key="size_schema")

            col1, col2 = st.columns([3, 1])
            with col2:
                if st.button("Take Snapshot", type="secondary", key="take_snapshot",
                            help="Save current sizes for trend tracking"):
                    with st.spinner("Saving snapshot..."):
                        if explorer.save_table_size_snapshot():
                            st.success("Snapshot saved!")
                        else:
                            st.error("Failed to save snapshot")

            with col1:
                if st.button("Load Current Sizes", type="primary", key="load_sizes"):
                    with st.spinner("Loading table sizes..."):
                        sizes = explorer.get_table_sizes(
                            None if size_schema == 'All' else size_schema
                        )

                        if not sizes.empty:
                            # Summary metrics
                            col1, col2, col3, col4 = st.columns(4)
                            with col1:
                                st.metric("Total Tables", len(sizes))
                            with col2:
                                total_size = sizes['total_size_mb'].sum()
                                if total_size > 1024:
                                    st.metric("Total Size", f"{total_size/1024:.2f} GB")
                                else:
                                    st.metric("Total Size", f"{total_size:.2f} MB")
                            with col3:
                                total_rows = sizes['row_count'].sum()
                                st.metric("Total Rows", f"{total_rows:,}")
                            with col4:
                                data_ratio = (sizes['data_size_mb'].sum() / sizes['total_size_mb'].sum() * 100) if sizes['total_size_mb'].sum() > 0 else 0
                                st.metric("Data vs Index", f"{data_ratio:.1f}% data")

                            # Display table
                            st.dataframe(
                                sizes.drop(columns=['snapshot_time'], errors='ignore'),
                                use_container_width=True,
                                hide_index=True
                            )

                            # Top 10 largest tables chart
                            st.markdown("### Top 10 Largest Tables")
                            top_10 = sizes.nlargest(10, 'total_size_mb')
                            chart_data = top_10[['table_name', 'data_size_mb', 'index_size_mb']].set_index('table_name')
                            st.bar_chart(chart_data)

                            # Download
                            csv = sizes.to_csv(index=False)
                            st.download_button(
                                "Download Sizes CSV",
                                csv,
                                file_name="table_sizes.csv",
                                mime="text/csv"
                            )
                        else:
                            st.info("No tables found.")

        with trend_tab2:
            st.markdown("### Individual Table Trends")
            st.caption("View size changes for a specific table over time.")

            # Check for history
            history = explorer.load_table_size_history()
            if not history:
                st.warning("No historical data available. Take snapshots regularly to track trends.")
                st.info("Click 'Take Snapshot' in the Current Sizes tab to start tracking.")
            else:
                st.success(f"Found {len(history)} snapshot(s) in history")

                col1, col2 = st.columns(2)
                with col1:
                    schemas = explorer.get_schemas()
                    trend_schema = st.selectbox("Schema", schemas['schema_name'].tolist() if not schemas.empty else [], key="trend_schema")

                with col2:
                    if trend_schema:
                        tables = explorer.get_tables(trend_schema)
                        trend_table = st.selectbox("Table", tables['table_name'].tolist() if not tables.empty else [], key="trend_table")
                    else:
                        trend_table = None

                trend_days = st.slider("Days to show", 7, 365, 30, key="trend_days")

                if trend_schema and trend_table:
                    if st.button("Show Trend", type="primary", key="show_trend"):
                        trend_data = explorer.get_table_size_trend(trend_schema, trend_table, trend_days)

                        if not trend_data.empty:
                            st.markdown(f"### Size Trend for {trend_schema}.{trend_table}")

                            # Calculate changes
                            if len(trend_data) >= 2:
                                first = trend_data.iloc[0]
                                last = trend_data.iloc[-1]
                                row_change = last['row_count'] - first['row_count']
                                size_change = last['total_size_mb'] - first['total_size_mb']

                                col1, col2, col3, col4 = st.columns(4)
                                with col1:
                                    st.metric("Current Rows", f"{last['row_count']:,}",
                                             delta=f"{row_change:+,}")
                                with col2:
                                    st.metric("Current Size", f"{last['total_size_mb']:.2f} MB",
                                             delta=f"{size_change:+.2f} MB")
                                with col3:
                                    st.metric("Data Points", len(trend_data))
                                with col4:
                                    pct_change = ((last['total_size_mb'] / first['total_size_mb']) - 1) * 100 if first['total_size_mb'] > 0 else 0
                                    st.metric("Size Change", f"{pct_change:+.1f}%")

                            # Row count chart
                            st.markdown("#### Row Count Over Time")
                            row_chart = trend_data[['timestamp', 'row_count']].set_index('timestamp')
                            st.line_chart(row_chart)

                            # Size chart
                            st.markdown("#### Size Over Time (MB)")
                            size_chart = trend_data[['timestamp', 'total_size_mb', 'data_size_mb', 'index_size_mb']].set_index('timestamp')
                            st.line_chart(size_chart)

                            # Data table
                            st.markdown("#### Raw Data")
                            st.dataframe(trend_data, use_container_width=True, hide_index=True)
                        else:
                            st.info(f"No trend data found for {trend_schema}.{trend_table}")

        with trend_tab3:
            st.markdown("### Database-Wide Trends")
            st.caption("View overall database size changes over time.")

            history = explorer.load_table_size_history()
            if not history:
                st.warning("No historical data available. Take snapshots regularly to track trends.")
            else:
                db_trend_days = st.slider("Days to show", 7, 365, 30, key="db_trend_days")

                if st.button("Show Database Trends", type="primary", key="show_db_trend"):
                    db_trend = explorer.get_database_size_trend(db_trend_days)

                    if not db_trend.empty:
                        st.markdown(f"### Database Size Trend ({explorer.current_database})")

                        # Calculate changes
                        if len(db_trend) >= 2:
                            first = db_trend.iloc[0]
                            last = db_trend.iloc[-1]

                            col1, col2, col3, col4 = st.columns(4)
                            with col1:
                                row_change = last['total_rows'] - first['total_rows']
                                st.metric("Total Rows", f"{last['total_rows']:,}",
                                         delta=f"{row_change:+,}")
                            with col2:
                                size = last['total_size_mb']
                                size_change = last['total_size_mb'] - first['total_size_mb']
                                if size > 1024:
                                    st.metric("Total Size", f"{size/1024:.2f} GB",
                                             delta=f"{size_change:+.2f} MB")
                                else:
                                    st.metric("Total Size", f"{size:.2f} MB",
                                             delta=f"{size_change:+.2f} MB")
                            with col3:
                                table_change = last['table_count'] - first['table_count']
                                st.metric("Table Count", last['table_count'],
                                         delta=f"{table_change:+d}" if table_change != 0 else None)
                            with col4:
                                pct_change = ((last['total_size_mb'] / first['total_size_mb']) - 1) * 100 if first['total_size_mb'] > 0 else 0
                                st.metric("Growth", f"{pct_change:+.1f}%")

                        # Total size chart
                        st.markdown("#### Database Size Over Time")
                        size_chart = db_trend[['timestamp', 'total_size_mb', 'data_size_mb', 'index_size_mb']].set_index('timestamp')
                        st.area_chart(size_chart)

                        # Row count chart
                        st.markdown("#### Total Rows Over Time")
                        row_chart = db_trend[['timestamp', 'total_rows']].set_index('timestamp')
                        st.line_chart(row_chart)

                        # Data table
                        st.markdown("#### Snapshot History")
                        st.dataframe(db_trend, use_container_width=True, hide_index=True)
                    else:
                        st.info("No database trend data found for the selected period.")


if __name__ == "__main__":
    main()
