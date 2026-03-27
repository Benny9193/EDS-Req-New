---
allowed-tools: Bash(cd C?EDS && python:*), Bash(cd /c/EDS && python:*), Bash(ls:*), Bash(dir:*)
description: Preview a report plan without executing SQL. Shows what queries and sheets would be generated.
argument-hint: <report description>
---

## Context

- Working directory: C:\EDS
- Available databases: EDS (product catalog, requisitions, bids, vendors), dpa_EDSAdmin (DPA monitoring)
- Key EDS tables: BidHeaders, BidTrades, BidImports, Awards, Vendors, Counties, Requisitions, PO, Items, Category, District, School, Users

## Your Task

The user wants to preview a report plan WITHOUT running any SQL or generating an Excel file.

Run this command:

```
cd C:\EDS && python -m agent --provider claude report --preview "<USER_REQUEST>"
```

Replace `<USER_REQUEST>` with the user's exact report description from the slash command argument. Preserve their wording.

After the command completes, summarize the plan:
- Report title and description
- Number of queries and which databases they target
- Sheet names, types (summary/detail/pivot/drilldown), and column counts
- Whether the plan looks reasonable for the user's request

Then tell the user: "To generate the actual Excel file, use `/report` with the same description."

### Error Handling

- If the command fails with an Anthropic API key error, retry with `--provider ollama` as fallback
- If it fails with a database connection error, tell the user to check their `.env` file at `C:\EDS\.env` for DB_SERVER, DB_USERNAME, DB_PASSWORD
- If the LLM produces invalid JSON, suggest the user rephrase with more specific terms (mention table names like BidHeaders, Vendors, Requisitions)

### Provider Notes

- Default provider is `claude` (uses ANTHROPIC_API_KEY from environment)
- If the user says "use ollama" or "use local model", switch to `--provider ollama`
- If the user says "use openai" or "use gpt", switch to `--provider openai`
