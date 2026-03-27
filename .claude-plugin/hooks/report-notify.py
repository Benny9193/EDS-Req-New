#!/usr/bin/env python3
"""
PostToolUse hook — Detects when an Excel report has been generated and
provides helpful follow-up context.

Monitors Bash tool output for report generation completion signals
(file paths ending in .xlsx in the output directory).

Exit 0 with stdout = context message added to conversation.
"""

import json
import sys
import re
import os


def main():
    """Check if a report was just generated and provide follow-up context."""
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    tool_name = hook_input.get("tool_name", "")
    tool_response = hook_input.get("tool_response", "")

    # Only check Bash tool responses
    if tool_name != "Bash":
        sys.exit(0)

    # Convert tool_response to string if it's a dict
    if isinstance(tool_response, dict):
        response_text = json.dumps(tool_response)
    else:
        response_text = str(tool_response)

    # Look for Excel file generation patterns in the output
    xlsx_pattern = r'[A-Za-z]:\\[^\s]+\.xlsx|/[^\s]+\.xlsx'
    xlsx_matches = re.findall(xlsx_pattern, response_text)

    # Also check for report completion indicators
    report_completed = any(indicator in response_text for indicator in [
        "Report saved",
        "report saved",
        "Excel file",
        "sheets,",
        "total rows",
        "elapsed_seconds",
    ])

    if xlsx_matches and report_completed:
        file_path = xlsx_matches[0]
        filename = os.path.basename(file_path)

        # Provide helpful follow-up context
        context = (
            f"Report '{filename}' was generated successfully. "
            f"To open it, the user can run: "
            f"cd C:\\EDS && python -m agent --provider claude report --open "
            f"or open the file directly at: {file_path}"
        )
        print(context)

    sys.exit(0)


if __name__ == "__main__":
    main()
