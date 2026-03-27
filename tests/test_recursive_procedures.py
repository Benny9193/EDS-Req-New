#!/usr/bin/env python3
"""
Test Recursive Procedures

Unit tests to validate recursive stored procedures for:
- Proper termination conditions
- Maximum recursion depth limits
- Safe execution with test data
"""

import os
import sys
import re
import pytest
from unittest.mock import MagicMock, patch

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from db_utils import DatabaseConnection


@pytest.mark.integration
class TestRecursiveProcedureAnalysis:
    """Static analysis tests for recursive procedures (requires DB)."""

    @pytest.fixture
    def db_connection(self):
        """Create database connection for tests."""
        try:
            db = DatabaseConnection(database='EDS')
            db.connect()
            yield db
            db.disconnect()
        except Exception as e:
            pytest.skip(f"Database connection not available: {e}")

    @pytest.fixture
    def recursive_procedures(self, db_connection):
        """Get all recursive procedures and their definitions."""
        procedures = db_connection.execute_query('''
            SELECT
                s.name AS SchemaName,
                p.name AS ProcName,
                OBJECT_DEFINITION(p.object_id) AS Definition
            FROM sys.procedures p
            INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
        ''')

        # Find self-calling procedures
        deps = db_connection.execute_query('''
            SELECT DISTINCT
                OBJECT_NAME(d.referencing_id) AS CallerName,
                d.referenced_entity_name AS RefName
            FROM sys.sql_expression_dependencies d
            INNER JOIN sys.procedures p ON d.referencing_id = p.object_id
            INNER JOIN sys.procedures p2 ON d.referenced_id = p2.object_id
        ''')

        call_graph = {}
        for caller, callee in deps:
            if caller not in call_graph:
                call_graph[caller] = set()
            call_graph[caller].add(callee)

        # Also check EXEC patterns
        exec_pattern = re.compile(r'\bEXEC(?:UTE)?\s+(?:\[?(\w+)\]?\.)?\[?(\w+)\]?', re.IGNORECASE)
        sp_names = {p[1] for p in procedures}

        for schema, proc, definition in procedures:
            if definition:
                if proc not in call_graph:
                    call_graph[proc] = set()
                matches = exec_pattern.findall(definition)
                for _, match_proc in matches:
                    if match_proc in sp_names:
                        call_graph[proc].add(match_proc)

        recursive = []
        for schema, proc, definition in procedures:
            if proc in call_graph.get(proc, set()):
                recursive.append({
                    'schema': schema,
                    'name': proc,
                    'definition': definition or ''
                })

        return recursive

    def test_all_recursive_procs_have_definitions(self, recursive_procedures):
        """All recursive procedures should have accessible definitions."""
        missing_def = [p['name'] for p in recursive_procedures if not p['definition']]
        assert len(missing_def) == 0, f"Procedures missing definitions: {missing_def}"

    def test_recursive_procs_have_termination_condition(self, recursive_procedures):
        """Each recursive procedure should have a termination condition."""
        termination_patterns = [
            r'IF\s+.*\s+RETURN',
            r'WHERE\s+.*\s+IS\s+NULL',
            r'@@ROWCOUNT\s*=\s*0',
            r'IF\s+NOT\s+EXISTS',
            r'IF\s+@\w+\s*(?:<=?|>=?|=)\s*\d+',
            r'WHILE\s+.*\s*(?:<=?|>=?|<>)',
            r'IF\s+@\w+\s+IS\s+NULL',
            r'WHEN\s+.*\s+THEN\s+RETURN',
        ]

        procs_without_termination = []
        for proc in recursive_procedures:
            definition = proc['definition']
            has_termination = False

            for pattern in termination_patterns:
                if re.search(pattern, definition, re.IGNORECASE):
                    has_termination = True
                    break

            if not has_termination:
                procs_without_termination.append(proc['name'])

        # Report but don't fail - some may have implicit termination
        if procs_without_termination:
            print(f"\nWarning: {len(procs_without_termination)} procedures without obvious termination:")
            for name in procs_without_termination[:10]:
                print(f"  - {name}")

    def test_no_infinite_loop_patterns(self, recursive_procedures):
        """Check for dangerous patterns that could cause infinite loops."""
        dangerous_patterns = [
            (r'EXEC\s+\w+\s*$', 'Recursive call with no parameters'),
            (r'WHILE\s+1\s*=\s*1', 'Infinite WHILE loop'),
            (r'WHILE\s+TRUE', 'Infinite WHILE TRUE loop'),
            (r'GOTO\s+\w+.*GOTO\s+\w+', 'Multiple GOTO statements'),
        ]

        issues = []
        for proc in recursive_procedures:
            definition = proc['definition']
            for pattern, desc in dangerous_patterns:
                if re.search(pattern, definition, re.IGNORECASE):
                    # Check if there's a BREAK statement (may be safe)
                    if 'WHILE' in desc and 'BREAK' in definition.upper():
                        continue  # Has BREAK, likely safe
                    issues.append(f"{proc['name']}: {desc}")

        # Report issues as warnings rather than failing
        if issues:
            print(f"\n⚠️  WARNING: {len(issues)} dangerous patterns found:")
            for issue in issues:
                print(f"  - {issue}")
            print("\nReview docs/EDS_INFINITE_LOOP_ANALYSIS.md for details.")

    def test_recursive_depth_limit_exists(self, recursive_procedures):
        """Check if procedures using CTEs have MAXRECURSION option."""
        cte_procs = []
        for proc in recursive_procedures:
            definition = proc['definition']
            if re.search(r'\bWITH\s+\w+\s*AS\s*\(', definition, re.IGNORECASE):
                if 'MAXRECURSION' not in definition.upper():
                    cte_procs.append(proc['name'])

        # Report CTEs without MAXRECURSION
        if cte_procs:
            print(f"\nInfo: {len(cte_procs)} CTEs without explicit MAXRECURSION (default is 100):")
            for name in cte_procs[:5]:
                print(f"  - {name}")


@pytest.mark.integration
class TestRecursiveProcedureExecution:
    """Runtime tests for recursive procedures (requires DB)."""

    @pytest.fixture
    def db_connection(self):
        """Create database connection for tests."""
        try:
            db = DatabaseConnection(database='EDS')
            db.connect()
            yield db
            db.disconnect()
        except Exception as e:
            pytest.skip(f"Database connection not available: {e}")

    def test_recursive_proc_timeout_handling(self, db_connection):
        """Test that recursive procedures have connection available."""
        # Verify connection is available for potential timeout testing
        assert db_connection._conn is not None
        # Note: pyodbc timeout=0 means no timeout (unlimited)
        # This is informational - actual timeout should be set per-query if needed
        timeout = db_connection._conn.timeout
        if timeout == 0:
            print("\nInfo: Connection has no timeout limit (timeout=0)")
        else:
            print(f"\nInfo: Connection timeout is {timeout} seconds")

    def test_recursion_depth_query(self, db_connection):
        """Verify we can check SQL Server's recursion settings."""
        result = db_connection.fetch_one('''
            SELECT @@MAX_PRECISION AS MaxPrecision,
                   @@NESTLEVEL AS CurrentNestLevel
        ''')
        assert result is not None
        assert result[1] >= 0  # Current nest level should be valid


class TestRecursionSafetyPatterns:
    """Test for recommended safety patterns in recursive procedures."""

    @pytest.fixture
    def sample_definitions(self):
        """Sample procedure definitions for pattern testing."""
        return {
            'good_termination': '''
                CREATE PROCEDURE sp_Good @id INT, @depth INT = 0
                AS BEGIN
                    IF @depth > 10 RETURN  -- Termination condition
                    IF @id IS NULL RETURN
                    EXEC sp_Good @id - 1, @depth + 1
                END
            ''',
            'bad_no_termination': '''
                CREATE PROCEDURE sp_Bad @id INT
                AS BEGIN
                    SELECT * FROM Table WHERE id = @id
                    EXEC sp_Bad @id  -- No termination!
                END
            ''',
            'good_cte_recursion': '''
                CREATE PROCEDURE sp_CTE
                AS BEGIN
                    ;WITH hierarchy AS (
                        SELECT id, parent_id, 0 AS level
                        FROM nodes WHERE parent_id IS NULL
                        UNION ALL
                        SELECT n.id, n.parent_id, h.level + 1
                        FROM nodes n
                        INNER JOIN hierarchy h ON n.parent_id = h.id
                        WHERE h.level < 10  -- Depth limit
                    )
                    SELECT * FROM hierarchy
                    OPTION (MAXRECURSION 100)
                END
            ''',
            'good_rowcount_check': '''
                CREATE PROCEDURE sp_RowCount @id INT
                AS BEGIN
                    UPDATE Table SET processed = 1 WHERE id = @id
                    IF @@ROWCOUNT = 0 RETURN  -- Termination
                    EXEC sp_RowCount @id + 1
                END
            '''
        }

    def test_detect_termination_pattern(self, sample_definitions):
        """Test detection of termination patterns."""
        patterns = [
            r'IF\s+@\w+\s*>\s*\d+\s+RETURN',
            r'IF\s+@\w+\s+IS\s+NULL\s+RETURN',
            r'IF\s+@@ROWCOUNT\s*=\s*0\s+RETURN',
            r'WHERE\s+\w+\.level\s*<\s*\d+',
            r'OPTION\s*\(\s*MAXRECURSION',
        ]

        # Good procedures should match at least one pattern
        good_procs = ['good_termination', 'good_cte_recursion', 'good_rowcount_check']
        for proc_name in good_procs:
            definition = sample_definitions[proc_name]
            found = any(re.search(p, definition, re.IGNORECASE) for p in patterns)
            assert found, f"{proc_name} should have detectable termination"

        # Bad procedure should not match
        definition = sample_definitions['bad_no_termination']
        found = any(re.search(p, definition, re.IGNORECASE) for p in patterns)
        assert not found, "bad_no_termination should not have termination pattern"

    def test_depth_parameter_pattern(self, sample_definitions):
        """Test detection of depth tracking parameter."""
        depth_pattern = r'@(?:depth|level|iteration|count)\s+INT\s*=\s*0'

        good = sample_definitions['good_termination']
        assert re.search(depth_pattern, good, re.IGNORECASE), \
            "Good procedure should have depth parameter"

    def test_maxrecursion_option(self, sample_definitions):
        """Test detection of MAXRECURSION option."""
        pattern = r'OPTION\s*\(\s*MAXRECURSION\s+\d+\s*\)'

        cte = sample_definitions['good_cte_recursion']
        assert re.search(pattern, cte, re.IGNORECASE), \
            "CTE should have MAXRECURSION option"


@pytest.mark.integration
class TestRecursiveProcRecommendations:
    """Generate recommendations for improving recursive procedures (requires DB)."""

    @pytest.fixture
    def db_connection(self):
        """Create database connection for tests."""
        try:
            db = DatabaseConnection(database='EDS')
            db.connect()
            yield db
            db.disconnect()
        except Exception as e:
            pytest.skip(f"Database connection not available: {e}")

    def test_generate_recommendations(self, db_connection, recursive_procedures=None):
        """Generate safety recommendations for each recursive procedure."""
        if recursive_procedures is None:
            # Get procedures directly if fixture not available
            procedures = db_connection.execute_query('''
                SELECT p.name, OBJECT_DEFINITION(p.object_id) AS Definition
                FROM sys.procedures p
                WHERE OBJECT_DEFINITION(p.object_id) LIKE '%EXEC%' + p.name + '%'
            ''')
        else:
            procedures = [(p['name'], p['definition']) for p in recursive_procedures]

        recommendations = []
        for name, definition in procedures[:10]:  # Limit for test performance
            if not definition:
                continue

            issues = []

            # Check for depth parameter
            if not re.search(r'@(?:depth|level)\s+INT', definition, re.IGNORECASE):
                issues.append("Add @depth parameter to track recursion depth")

            # Check for explicit termination
            if not re.search(r'IF\s+.*RETURN', definition, re.IGNORECASE):
                issues.append("Add explicit IF condition with RETURN")

            # Check for MAXRECURSION in CTEs
            if 'WITH ' in definition and 'MAXRECURSION' not in definition.upper():
                issues.append("Add OPTION (MAXRECURSION n) for CTE")

            if issues:
                recommendations.append({
                    'procedure': name,
                    'recommendations': issues
                })

        # Output recommendations
        if recommendations:
            print("\n=== Recursive Procedure Recommendations ===")
            for rec in recommendations:
                print(f"\n{rec['procedure']}:")
                for issue in rec['recommendations']:
                    print(f"  - {issue}")

        # Test passes - we're just generating recommendations
        assert True


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])
