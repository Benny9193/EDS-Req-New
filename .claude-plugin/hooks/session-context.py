#!/usr/bin/env python3
"""
SessionStart hook — Injects EDS database context into Claude's session.

Runs on startup and resume. Provides Claude with awareness of available
slash commands and key schema information so it can proactively suggest
the right command for the user's task.

Output on stdout is added to Claude's context as a system message.
"""

import json
import sys
import os


def main():
    """Inject EDS context on session start."""
    # Read hook input from stdin
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        hook_input = {}

    # Check if we're in the EDS project directory
    cwd = hook_input.get("cwd", os.getcwd())
    if "EDS" not in cwd.upper():
        # Not in EDS project, skip silently
        sys.exit(0)

    # Provide context about available commands
    context = """EDS DBA Tools plugin is active. Available slash commands:

Commands:
  /report <desc>          — Generate formatted Excel report (preview → approve → execute)
  /report-preview <desc>  — Preview report plan only (no SQL execution)
  /sql <question>         — Generate SQL from natural language (shows query → approve → execute)
  /docs <search>          — Search database documentation (tables, procs, views, indexes)
  /schema <object>        — Inspect table/view/procedure structure from live database
  /ask <question>         — Ask about EDS database concepts, workflows, relationships
  /run [script]           — Run monitoring/analysis scripts (no args = list available)
  /status                 — Show agent config, providers, DB connection status

Key EDS tables: BidHeaders, BidTrades, BidImports, Awards, Vendors, Counties, Requisitions, PO, Items, Category, District, School, Users
Databases: EDS (catalog), dpa_EDSAdmin (monitoring)

When the user asks about data, suggest the appropriate command."""

    # Output as JSON with additionalContext for Claude
    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context
        }
    }
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
