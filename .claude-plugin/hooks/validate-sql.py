#!/usr/bin/env python3
"""
PreToolUse hook — Validates Bash commands that contain SQL for safety.

Checks for dangerous SQL operations that could modify or destroy data.
Blocks: DROP, DELETE, TRUNCATE, ALTER, UPDATE (unless user explicitly approved).
Allows: SELECT, WITH, EXEC (read-safe stored procedures).

Runs before any Bash tool execution. Only inspects commands that contain
SQL-related keywords (python -m agent ... sql --execute).

Exit codes:
  0 = allow (no issues found)
  2 = block (dangerous operation detected)
"""

import json
import sys
import re


# SQL operations that are always blocked
BLOCKED_OPERATIONS = [
    r'\bDROP\s+(TABLE|DATABASE|INDEX|VIEW|PROCEDURE)',
    r'\bDELETE\s+FROM\b',
    r'\bTRUNCATE\s+TABLE\b',
    r'\bALTER\s+(TABLE|DATABASE)\b',
    r'\bUPDATE\s+\w+\s+SET\b',
    r'\bINSERT\s+INTO\b',
    r'\bxp_cmdshell\b',
    r'\bsp_configure\b',
    r'\bOPENROWSET\b',
    r'\bBULK\s+INSERT\b',
    r'\bEXEC\s+sp_executesql\b',
    r'\bGRANT\b',
    r'\bREVOKE\b',
    r'\bDENY\b',
]

# Commands we care about (SQL execution via the agent)
SQL_PATTERNS = [
    'sql --execute',
    'sql -e',
    '--execute',
]


def main():
    """Check Bash commands for dangerous SQL operations."""
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        # Can't parse input, allow by default
        sys.exit(0)

    tool_name = hook_input.get("tool_name", "")
    tool_input = hook_input.get("tool_input", {})

    # Only check Bash commands
    if tool_name != "Bash":
        sys.exit(0)

    command = tool_input.get("command", "")

    # Only inspect commands that look like SQL execution
    is_sql_command = any(pattern in command for pattern in SQL_PATTERNS)
    if not is_sql_command:
        sys.exit(0)

    # Check for dangerous operations
    command_upper = command.upper()
    for pattern in BLOCKED_OPERATIONS:
        match = re.search(pattern, command_upper)
        if match:
            matched_text = match.group(0)
            # Output denial
            output = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": (
                        f"BLOCKED: Dangerous SQL operation detected: '{matched_text}'. "
                        f"This operation could modify or destroy data. "
                        f"The EDS agent is configured for read-only access. "
                        f"If you need to run write operations, execute them directly "
                        f"in SQL Server Management Studio."
                    )
                }
            }
            print(json.dumps(output))
            sys.exit(0)

    # Command is safe, allow it
    sys.exit(0)


if __name__ == "__main__":
    main()
