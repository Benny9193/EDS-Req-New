"""SQL query validation and security enforcement.

Validates queries before they reach the database, blocking dangerous operations,
enforcing read-only mode, and flagging sensitive data access.
"""

import logging
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

logger = logging.getLogger(__name__)


class QueryType(str, Enum):
    SELECT = "select"
    INSERT = "insert"
    UPDATE = "update"
    DELETE = "delete"
    DDL = "ddl"
    EXEC = "exec"
    UNKNOWN = "unknown"


@dataclass
class ValidationResult:
    is_valid: bool
    query_type: QueryType
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    sanitized: Optional[str] = None
    risk_level: str = "low"  # "low", "medium", "high"


# Always blocked regardless of mode — these are dangerous server-level operations
DEFAULT_BLOCKED_PATTERNS = [
    re.compile(r'\bxp_cmdshell\b', re.IGNORECASE),
    re.compile(r'\bsp_executesql\b', re.IGNORECASE),
    re.compile(r'\bOPENROWSET\b', re.IGNORECASE),
    re.compile(r'\bOPENDATASOURCE\b', re.IGNORECASE),
    re.compile(r'\bBULK\s+INSERT\b', re.IGNORECASE),
    re.compile(r'\bWAITFOR\s+DELAY\b', re.IGNORECASE),
    re.compile(r'\bWAITFOR\s+TIME\b', re.IGNORECASE),
    re.compile(r'\bEXEC\s*\(', re.IGNORECASE),
    re.compile(r'\bEXECUTE\s*\(', re.IGNORECASE),
    re.compile(r'--.*?(\bDROP\b|\bDELETE\b|\bTRUNCATE\b)', re.IGNORECASE),
    re.compile(r'/\*.*?(\bDROP\b|\bDELETE\b|\bTRUNCATE\b).*?\*/', re.IGNORECASE | re.DOTALL),
    re.compile(r'\bSHUTDOWN\b', re.IGNORECASE),
]

# Write operations — blocked when allow_writes=False
WRITE_PATTERNS = [
    re.compile(r'^\s*INSERT\b', re.IGNORECASE | re.MULTILINE),
    re.compile(r'^\s*UPDATE\b', re.IGNORECASE | re.MULTILINE),
    re.compile(r'^\s*DELETE\b', re.IGNORECASE | re.MULTILINE),
    re.compile(r'^\s*TRUNCATE\b', re.IGNORECASE | re.MULTILINE),
    re.compile(r'^\s*DROP\b', re.IGNORECASE | re.MULTILINE),
    re.compile(r'^\s*CREATE\b', re.IGNORECASE | re.MULTILINE),
    re.compile(r'^\s*ALTER\b', re.IGNORECASE | re.MULTILINE),
    re.compile(r'^\s*MERGE\b', re.IGNORECASE | re.MULTILINE),
    re.compile(r'^\s*REPLACE\b', re.IGNORECASE | re.MULTILINE),
    re.compile(r'^\s*UPSERT\b', re.IGNORECASE | re.MULTILINE),
]

# Sensitive data access — generates warnings but doesn't block
SENSITIVE_PATTERNS = [
    re.compile(r'\bpassword\b', re.IGNORECASE),
    re.compile(r'\bsocial_security\b', re.IGNORECASE),
    re.compile(r'\bssn\b', re.IGNORECASE),
    re.compile(r'\bcredit_card\b', re.IGNORECASE),
    re.compile(r'\bpii\b', re.IGNORECASE),
]

# Patterns for classifying query type
_TYPE_PATTERNS = [
    (QueryType.SELECT, re.compile(r'^\s*SELECT\b', re.IGNORECASE | re.MULTILINE)),
    (QueryType.INSERT, re.compile(r'^\s*INSERT\b', re.IGNORECASE | re.MULTILINE)),
    (QueryType.UPDATE, re.compile(r'^\s*UPDATE\b', re.IGNORECASE | re.MULTILINE)),
    (QueryType.DELETE, re.compile(r'^\s*DELETE\b', re.IGNORECASE | re.MULTILINE)),
    (QueryType.EXEC, re.compile(r'^\s*EXEC(?:UTE)?\s', re.IGNORECASE | re.MULTILINE)),
    (QueryType.DDL, re.compile(
        r'^\s*(?:CREATE|ALTER|DROP|TRUNCATE)\b', re.IGNORECASE | re.MULTILINE
    )),
]


class QueryValidator:
    """Validates SQL queries before execution.

    Args:
        allow_writes: If False (default), block INSERT/UPDATE/DELETE/DDL operations.
        allowed_databases: List of database names queries may target.
            Defaults to ["EDS", "dpa_EDSAdmin"].
        max_query_length: Maximum allowed query string length.
    """

    def __init__(
        self,
        allow_writes: bool = False,
        allowed_databases: Optional[List[str]] = None,
        max_query_length: int = 10_000,
    ):
        self.allow_writes = allow_writes
        self.allowed_databases = allowed_databases or ["EDS", "dpa_EDSAdmin"]
        self.max_query_length = max_query_length

    def validate(
        self,
        query: str,
        target_database: Optional[str] = None,
    ) -> ValidationResult:
        """Validate a SQL query for safety.

        Validation sequence:
        1. Length check
        2. Database allowlist check
        3. Blocked pattern scan (always rejected)
        4. Write pattern scan (rejected if allow_writes=False)
        5. Sensitive pattern scan (warnings only)
        6. Query type classification

        Args:
            query: The SQL query string to validate.
            target_database: Optional database name the query targets.

        Returns:
            ValidationResult with is_valid, query_type, errors, warnings, risk_level.
        """
        errors: List[str] = []
        warnings: List[str] = []
        risk_level = "low"

        # 1. Length check
        if len(query) > self.max_query_length:
            return ValidationResult(
                is_valid=False,
                query_type=QueryType.UNKNOWN,
                errors=[
                    f"Query exceeds maximum length "
                    f"({len(query):,} > {self.max_query_length:,} chars)"
                ],
                risk_level="medium",
            )

        # 2. Database allowlist
        if target_database and target_database not in self.allowed_databases:
            return ValidationResult(
                is_valid=False,
                query_type=QueryType.UNKNOWN,
                errors=[
                    f"Database '{target_database}' is not in the allowed list: "
                    f"{self.allowed_databases}"
                ],
                risk_level="high",
            )

        # 3. Blocked patterns — always rejected
        for pattern in DEFAULT_BLOCKED_PATTERNS:
            match = pattern.search(query)
            if match:
                errors.append(
                    f"Blocked operation detected: {match.group()}"
                )
                risk_level = "high"

        if errors:
            return ValidationResult(
                is_valid=False,
                query_type=self._classify_query(query),
                errors=errors,
                risk_level=risk_level,
            )

        # 4. Write patterns — rejected when allow_writes=False
        if not self.allow_writes:
            for pattern in WRITE_PATTERNS:
                match = pattern.search(query)
                if match:
                    errors.append(
                        f"Write operation not allowed in read-only mode: "
                        f"{match.group().strip()}"
                    )
                    risk_level = "medium"

        if errors:
            return ValidationResult(
                is_valid=False,
                query_type=self._classify_query(query),
                errors=errors,
                risk_level=risk_level,
            )

        # 5. Sensitive patterns — warnings only
        for pattern in SENSITIVE_PATTERNS:
            match = pattern.search(query)
            if match:
                warnings.append(
                    f"Query accesses potentially sensitive data: {match.group()}"
                )
                if risk_level == "low":
                    risk_level = "medium"

        # 6. Classify and return
        query_type = self._classify_query(query)
        sanitized = query.strip()

        return ValidationResult(
            is_valid=True,
            query_type=query_type,
            warnings=warnings,
            sanitized=sanitized,
            risk_level=risk_level,
        )

    def _classify_query(self, query: str) -> QueryType:
        """Classify a query into a QueryType based on its leading keyword."""
        for qtype, pattern in _TYPE_PATTERNS:
            if pattern.search(query):
                return qtype
        return QueryType.UNKNOWN
