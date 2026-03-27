---
allowed-tools: Bash(cd C?EDS && python:*), Bash(cd /c/EDS && python:*), Bash(ls:*), Bash(dir:*)
description: Generate an Excel report from a natural language description. Creates formatted multi-sheet Excel workbooks with EDS brand styling.
argument-hint: <report description>
---

## Context

- Working directory: C:\EDS
- Output directory: C:\EDS\output\
- Available databases: EDS (product catalog, requisitions, bids, vendors), dpa_EDSAdmin (DPA monitoring)
- Report sheet types: summary (aggregated), detail (row-level), pivot (cross-tab heatmap), drilldown (grouped)
- Key EDS tables: BidHeaders, BidTrades, BidImports, Awards, Vendors, Counties, Requisitions, PO, Items, Category, District, School, Users

## Your Task

The user wants to generate an Excel report. Their request is the argument passed to this command.

Follow this two-phase workflow:

### Phase 1: Preview the Report Plan

Run this command to generate and preview the report plan WITHOUT executing any SQL:

```
cd C:\EDS && python -m agent --provider claude report --preview "<USER_REQUEST>"
```

Replace `<USER_REQUEST>` with the user's exact report description from the slash command argument. Preserve their wording.

After the command completes, summarize what the plan contains:
- Report title and description
- Number of queries and which databases they target
- Sheet names, types (summary/detail/pivot/drilldown), and column counts
- Whether the plan looks reasonable for the user's request

Then ask the user: "This is the report plan. Should I proceed with generating the Excel file, or would you like me to adjust the request?"

### Phase 2: Execute (only after user approval)

If the user approves, run the full report generation:

```
cd C:\EDS && python -m agent --provider claude report "<USER_REQUEST>"
```

After execution, report:
- The full path to the generated Excel file
- How many sheets were created and total row count
- Build time
- Any warnings or errors

If the user wants to open the file immediately, run with `--open`:
```
cd C:\EDS && python -m agent --provider claude report --open "<USER_REQUEST>"
```

### Error Handling

- If the command fails with an Anthropic API key error, retry with `--provider ollama` as fallback
- If it fails with a database connection error, tell the user to check their `.env` file at `C:\EDS\.env` for DB_SERVER, DB_USERNAME, DB_PASSWORD
- If the LLM produces invalid JSON, suggest the user rephrase with more specific terms (mention table names like BidHeaders, Vendors, Requisitions)

### Provider Notes

- Default provider is `claude` (uses ANTHROPIC_API_KEY from environment)
- If the user says "use ollama" or "use local model", switch to `--provider ollama`
- If the user says "use openai" or "use gpt", switch to `--provider openai`
