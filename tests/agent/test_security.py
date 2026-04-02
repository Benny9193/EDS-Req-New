"""Tests for the SQL query security validator."""

import pytest

from agent.security.validator import (
    QueryType,
    QueryValidator,
    ValidationResult,
)


@pytest.fixture
def validator():
    """Default read-only validator."""
    return QueryValidator()


@pytest.fixture
def write_validator():
    """Validator with writes allowed."""
    return QueryValidator(allow_writes=True)


class TestQueryTypeClassification:
    def test_select(self, validator):
        result = validator.validate("SELECT * FROM Vendors")
        assert result.query_type == QueryType.SELECT

    def test_select_with_leading_whitespace(self, validator):
        result = validator.validate("  SELECT TOP 10 * FROM Vendors")
        assert result.query_type == QueryType.SELECT

    def test_insert_classified(self, write_validator):
        result = write_validator.validate("INSERT INTO Foo (Col) VALUES (1)")
        assert result.query_type == QueryType.INSERT

    def test_update_classified(self, write_validator):
        result = write_validator.validate("UPDATE Foo SET Col = 1")
        assert result.query_type == QueryType.UPDATE

    def test_delete_classified(self, write_validator):
        result = write_validator.validate("DELETE FROM Foo WHERE Id = 1")
        assert result.query_type == QueryType.DELETE

    def test_exec_classified(self, validator):
        result = validator.validate("EXEC sp_GetVendors @Id = 1")
        assert result.query_type == QueryType.EXEC

    def test_execute_classified(self, validator):
        result = validator.validate("EXECUTE sp_GetVendors")
        assert result.query_type == QueryType.EXEC

    def test_ddl_create(self, write_validator):
        result = write_validator.validate("CREATE INDEX IX_Test ON Foo(Col)")
        assert result.query_type == QueryType.DDL

    def test_ddl_alter(self, write_validator):
        result = write_validator.validate("ALTER TABLE Foo ADD Col INT")
        assert result.query_type == QueryType.DDL

    def test_unknown(self, validator):
        result = validator.validate("WITH cte AS (SELECT 1) SELECT * FROM cte")
        assert result.query_type == QueryType.UNKNOWN


class TestBlockedPatterns:
    """Blocked patterns should always be rejected, even with allow_writes=True."""

    @pytest.mark.parametrize("query", [
        "EXEC xp_cmdshell 'dir'",
        "SELECT * FROM OPENROWSET('SQLOLEDB', ...)",
        "SELECT * FROM OPENDATASOURCE('SQLOLEDB', ...)",
        "BULK INSERT Foo FROM 'file.csv'",
        "WAITFOR DELAY '00:00:10'",
        "WAITFOR TIME '23:00:00'",
        "EXEC('DROP TABLE Foo')",
        "EXECUTE('SELECT 1')",
        "SHUTDOWN",
        "SELECT 1 -- DROP TABLE Foo",
        "/* DELETE everything */ SELECT 1",
        "sp_executesql N'SELECT 1'",
    ])
    def test_blocked_always_rejected(self, write_validator, query):
        result = write_validator.validate(query)
        assert not result.is_valid
        assert result.risk_level == "high"
        assert len(result.errors) > 0

    def test_blocked_case_insensitive(self, validator):
        result = validator.validate("exec XP_CMDSHELL 'whoami'")
        assert not result.is_valid

    def test_safe_exec_sp_not_blocked(self, validator):
        """EXEC sp_name (without parens) should not be blocked."""
        result = validator.validate("EXEC sp_GetVendors @VendorId = 9")
        assert result.is_valid


class TestWritePatterns:
    def test_insert_blocked_readonly(self, validator):
        result = validator.validate("INSERT INTO Foo (Col) VALUES (1)")
        assert not result.is_valid
        assert result.risk_level == "medium"

    def test_update_blocked_readonly(self, validator):
        result = validator.validate("UPDATE Foo SET Col = 1")
        assert not result.is_valid

    def test_delete_blocked_readonly(self, validator):
        result = validator.validate("DELETE FROM Foo WHERE Id = 1")
        assert not result.is_valid

    def test_truncate_blocked_readonly(self, validator):
        result = validator.validate("TRUNCATE TABLE Foo")
        assert not result.is_valid

    def test_drop_blocked_readonly(self, validator):
        result = validator.validate("DROP TABLE Foo")
        assert not result.is_valid

    def test_create_blocked_readonly(self, validator):
        result = validator.validate("CREATE TABLE Foo (Id INT)")
        assert not result.is_valid

    def test_alter_blocked_readonly(self, validator):
        result = validator.validate("ALTER TABLE Foo ADD Col INT")
        assert not result.is_valid

    def test_merge_blocked_readonly(self, validator):
        result = validator.validate("MERGE INTO Foo USING Bar ON Foo.Id = Bar.Id")
        assert not result.is_valid

    def test_insert_allowed_with_writes(self, write_validator):
        result = write_validator.validate("INSERT INTO Foo (Col) VALUES (1)")
        assert result.is_valid

    def test_update_allowed_with_writes(self, write_validator):
        result = write_validator.validate("UPDATE Foo SET Col = 1 WHERE Id = 1")
        assert result.is_valid

    def test_delete_allowed_with_writes(self, write_validator):
        result = write_validator.validate("DELETE FROM Foo WHERE Id = 1")
        assert result.is_valid


class TestSensitivePatterns:
    def test_password_warning(self, validator):
        result = validator.validate("SELECT password FROM Users")
        assert result.is_valid
        assert len(result.warnings) == 1
        assert "password" in result.warnings[0]
        assert result.risk_level == "medium"

    def test_ssn_warning(self, validator):
        result = validator.validate("SELECT ssn FROM Employees")
        assert result.is_valid
        assert len(result.warnings) == 1

    def test_credit_card_warning(self, validator):
        result = validator.validate("SELECT credit_card FROM Payments")
        assert result.is_valid
        assert any("credit_card" in w for w in result.warnings)

    def test_no_warning_for_safe_query(self, validator):
        result = validator.validate("SELECT VendorName FROM Vendors")
        assert result.is_valid
        assert len(result.warnings) == 0
        assert result.risk_level == "low"


class TestDatabaseAllowlist:
    def test_allowed_database(self, validator):
        result = validator.validate("SELECT 1", target_database="EDS")
        assert result.is_valid

    def test_allowed_dpa(self, validator):
        result = validator.validate("SELECT 1", target_database="dpa_EDSAdmin")
        assert result.is_valid

    def test_disallowed_database(self, validator):
        result = validator.validate("SELECT 1", target_database="master")
        assert not result.is_valid
        assert result.risk_level == "high"
        assert "master" in result.errors[0]

    def test_no_database_specified(self, validator):
        result = validator.validate("SELECT 1")
        assert result.is_valid

    def test_custom_allowlist(self):
        v = QueryValidator(allowed_databases=["TestDB"])
        result = v.validate("SELECT 1", target_database="EDS")
        assert not result.is_valid


class TestQueryLength:
    def test_within_limit(self, validator):
        result = validator.validate("SELECT 1")
        assert result.is_valid

    def test_exceeds_limit(self):
        v = QueryValidator(max_query_length=50)
        result = v.validate("SELECT " + "a" * 100)
        assert not result.is_valid
        assert result.risk_level == "medium"
        assert "length" in result.errors[0].lower()

    def test_default_limit_allows_large_queries(self, validator):
        query = "SELECT " + ", ".join(f"col{i}" for i in range(500)) + " FROM Foo"
        result = validator.validate(query)
        assert result.is_valid


class TestSanitization:
    def test_sanitized_strips_whitespace(self, validator):
        result = validator.validate("  SELECT 1  ")
        assert result.sanitized == "SELECT 1"

    def test_sanitized_none_on_failure(self, validator):
        result = validator.validate("DROP TABLE Foo")
        assert result.sanitized is None


class TestValidationResult:
    def test_dataclass_defaults(self):
        r = ValidationResult(is_valid=True, query_type=QueryType.SELECT)
        assert r.warnings == []
        assert r.errors == []
        assert r.sanitized is None
        assert r.risk_level == "low"
