---
allowed-tools: Bash(cd C?EDS && python:*), Bash(cd /c/EDS && python:*), Bash(ls:*), Bash(dir:*)
description: Ask the EDS DBA agent a question about the database, schema, or system.
argument-hint: <question>
---

## Context

- Working directory: C:\EDS
- The agent uses RAG (vector search) over EDS documentation to answer questions
- Documentation covers: tables, stored procedures, views, indexes, business domains, ERD, dependencies

## Your Task

The user wants to ask a question about the EDS database system. Their question is the argument passed to this command.

Run this command:

```
cd C:\EDS && python -m agent --provider claude ask "<USER_QUESTION>"
```

Replace `<USER_QUESTION>` with the user's exact question.

### When to use this vs other commands

- `/ask` — Best for conceptual questions: "What tables store vendor info?", "How does the approval workflow work?", "What's the relationship between bids and awards?"
- `/sql` — Best when the user needs actual data or a SQL query
- `/docs` — Best for searching documentation by keyword
- `/schema` — Best for inspecting a specific table or object

### After the response

Based on the answer, suggest next steps:
- If the answer references specific tables → "Use `/schema <table>` to inspect its structure"
- If the answer suggests querying data → "Use `/sql <question>` to generate and run the query"
- If the answer could become a report → "Use `/report <description>` to create an Excel report"

### Error Handling

- If the command fails with an API key error, retry with `--provider ollama`
- If results seem incomplete, suggest rebuilding the doc index: `cd C:\EDS && python -m agent.rag.indexer`
