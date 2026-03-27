#!/usr/bin/env python3
"""
UserPromptSubmit hook — Detects when the user's prompt could benefit
from a specific slash command and adds a hint to Claude's context.

Analyzes the user's message for keywords that map to EDS commands,
helping Claude suggest the right tool proactively.

Exit 0 with JSON stdout = additionalContext added to Claude's processing.
"""

import json
import sys
import re


# Keyword → command mapping
COMMAND_HINTS = [
    {
        "keywords": [r"\breport\b", r"\bexcel\b", r"\bspreadsheet\b", r"\bworkbook\b", r"\bexport to excel\b"],
        "command": "/report",
        "hint": "The user may want an Excel report. Consider suggesting /report <description>."
    },
    {
        "keywords": [r"\bquery\b", r"\bselect\b", r"\bhow many\b", r"\bcount of\b", r"\blist all\b", r"\btop \d+\b", r"\bshow me\b"],
        "command": "/sql",
        "hint": "The user may want to query data. Consider suggesting /sql <question>."
    },
    {
        "keywords": [r"\bschema\b", r"\bcolumns?\b", r"\bdata type\b", r"\bprimary key\b", r"\bforeign key\b", r"\btable structure\b"],
        "command": "/schema",
        "hint": "The user may want schema details. Consider suggesting /schema <table_name>."
    },
    {
        "keywords": [r"\bperformance\b", r"\bblocking\b", r"\bslow\b", r"\bindex(es)?\b", r"\bbaseline\b", r"\bmonitor\b"],
        "command": "/run",
        "hint": "The user may want to run a monitoring script. Consider suggesting /run to see available scripts."
    },
    {
        "keywords": [r"\bdocumentation\b", r"\bstored proc\b", r"\bsproc\b", r"\bwhat does .+ do\b", r"\bwhere is .+ defined\b"],
        "command": "/docs",
        "hint": "The user may want documentation. Consider suggesting /docs <search_term>."
    },
]


def main():
    """Analyze user prompt and suggest appropriate commands."""
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    # Get the user's prompt
    user_prompt = hook_input.get("user_prompt", "")
    if not user_prompt:
        # Try alternate field names
        user_prompt = hook_input.get("prompt", hook_input.get("content", ""))

    if not user_prompt:
        sys.exit(0)

    prompt_lower = user_prompt.lower()

    # Skip if the user is already using a slash command
    if prompt_lower.startswith("/"):
        sys.exit(0)

    # Check for keyword matches
    hints = []
    for mapping in COMMAND_HINTS:
        for pattern in mapping["keywords"]:
            if re.search(pattern, prompt_lower):
                hints.append(mapping["hint"])
                break  # One match per command is enough

    if hints:
        context = "EDS command suggestions based on user's message:\n" + "\n".join(f"- {h}" for h in hints)
        output = {
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": context
            }
        }
        print(json.dumps(output))

    sys.exit(0)


if __name__ == "__main__":
    main()
