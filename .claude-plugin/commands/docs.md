---
allowed-tools: Bash(cd C?EDS && python:*), Bash(cd /c/EDS && python:*), Bash(ls:*), Bash(dir:*)
description: Search EDS database documentation — tables, stored procedures, views, indexes, and business domains.
argument-hint: <search term>
---

## Context

- Working directory: C:\EDS
- Documentation index: C:\EDS\data\vectordb (ChromaDB vector store)
- Doc types: tables, procedures, views, indexes, all
- Source docs in C:\EDS\docs\: EDS_DATA_DICTIONARY.md, EDS_STORED_PROCEDURES.md, EDS_VIEWS.md, EDS_INDEXES.md, EDS_BUSINESS_DOMAINS.md, EDS_ERD.md, EDS_PROCEDURE_DEPENDENCIES.md

## Your Task

The user wants to search EDS database documentation. Their search term is the argument passed to this command.

Run this command:

```
cd C:\EDS && python -m agent --provider claude docs "<SEARCH_TERM>"
```

Replace `<SEARCH_TERM>` with the user's exact search term from the slash command argument.

### Doc Type Filtering

If the user's query clearly targets a specific type, add the `-t` flag:

- Tables/columns: `-t tables`
- Stored procedures: `-t procedures`
- Views: `-t views`
- Indexes: `-t indexes`

Examples:
```
cd C:\EDS && python -m agent --provider claude docs -t tables "vendor columns"
cd C:\EDS && python -m agent --provider claude docs -t procedures "approval workflow"
```

### Adjusting Results

Default is 5 results. For broader searches, increase with `--limit`:

```
cd C:\EDS && python -m agent --provider claude docs --limit 10 "<SEARCH_TERM>"
```

### After Results

Summarize the key findings from the documentation search. If the user needs more detail, suggest:
- `/sql` to query the actual data
- `/schema <table_name>` for live table structure from the database
- `/report` to generate an Excel report from the data

### Error Handling

- If no results found, suggest the user check that the vector DB is built: `cd C:\EDS && python -m agent.rag.indexer`
- If the command fails, try a broader search term or different doc type filter
