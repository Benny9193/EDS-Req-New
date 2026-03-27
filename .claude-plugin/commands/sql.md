---
allowed-tools: Bash(cd C?EDS && python:*), Bash(cd /c/EDS && python:*), Bash(ls:*), Bash(dir:*)
description: Generate SQL from a natural language question. Shows the query and optionally executes it.
argument-hint: <question about the data>
---

## Context

- Working directory: C:\EDS
- Available databases: EDS (product catalog, requisitions, bids, vendors), dpa_EDSAdmin (DPA monitoring)
- Default database: EDS
- Key EDS tables: BidHeaders, BidTrades, BidImports, Awards, Vendors, Counties, Requisitions, PO, Items, Category, District, School, Users
- Key dpa_EDSAdmin tables: DPA monitoring views and tables

## Your Task

The user wants to generate a SQL query from a natural language question. Their question is the argument passed to this command.

### Phase 1: Generate SQL

Run this command to generate the SQL WITHOUT executing it:

```
cd C:\EDS && python -m agent --provider claude sql "<USER_QUESTION>"
```

Replace `<USER_QUESTION>` with the user's exact question from the slash command argument.

After the command completes, show:
- The generated SQL query (formatted for readability)
- Which database it targets
- A brief explanation of what the query does

Then ask the user: "Should I execute this query? I'll return the first 20 rows."

### Phase 2: Execute (only after user approval)

If the user approves, run with `--execute` and `--limit`:

```
cd C:\EDS && python -m agent --provider claude sql --execute --limit 20 "<USER_QUESTION>"
```

After execution, display the results in a readable table format.

If the user wants more rows, re-run with a higher `--limit` value (e.g., `--limit 100`).

### Database Selection

- By default, queries target the **EDS** database
- If the user mentions monitoring, performance, blocking, DPA, or wait stats, add `-d dpa_EDSAdmin`:

```
cd C:\EDS && python -m agent --provider claude sql -d dpa_EDSAdmin "<USER_QUESTION>"
```

### Error Handling

- If the command fails with an Anthropic API key error, retry with `--provider ollama` as fallback
- If it fails with a database connection error, tell the user to check their `.env` file at `C:\EDS\.env`
- If the generated SQL is clearly wrong, suggest the user rephrase using specific table or column names

### Provider Notes

- Default provider is `claude` (uses ANTHROPIC_API_KEY from environment)
- If the user says "use ollama" or "use local model", switch to `--provider ollama`
- If the user says "use openai" or "use gpt", switch to `--provider openai`
