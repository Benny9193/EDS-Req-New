---
allowed-tools: Bash(cd C?EDS && python:*), Bash(cd /c/EDS && python:*), Bash(ls:*), Bash(dir:*)
description: Inspect a database object (table, view, stored procedure) — shows columns, types, keys, and relationships.
argument-hint: <table or object name>
---

## Context

- Working directory: C:\EDS
- Databases: EDS, dpa_EDSAdmin
- This command queries the LIVE database to show current schema information

## Your Task

The user wants to inspect a database object. Their object name is the argument passed to this command.

### Step 1: Generate introspection SQL

Based on the object name, generate and run an appropriate query. Use `python -m agent --provider claude sql --execute --limit 50` with a natural language question that asks for schema details.

**For tables:**
```
cd C:\EDS && python -m agent --provider claude sql --execute --limit 100 "Show all columns for the <TABLE_NAME> table including data types, nullable, max length, and if it's a primary key or foreign key"
```

**For stored procedures:**
```
cd C:\EDS && python -m agent --provider claude sql --execute --limit 50 "Show the parameters for stored procedure <PROC_NAME> including data type and direction"
```

**For views:**
```
cd C:\EDS && python -m agent --provider claude sql --execute --limit 100 "Show the column definitions for the <VIEW_NAME> view"
```

### Step 2: Show relationships

If the object is a table, also run:
```
cd C:\EDS && python -m agent --provider claude sql --execute --limit 20 "Show all foreign key relationships for the <TABLE_NAME> table, both incoming and outgoing"
```

### Step 3: Show row count and sample

For tables, optionally show:
```
cd C:\EDS && python -m agent --provider claude sql --execute --limit 5 "Show the row count and 5 sample rows from <TABLE_NAME>"
```

### Database Selection

- Default: EDS database
- If the user mentions monitoring, DPA, performance, or wait stats, target dpa_EDSAdmin by adding `-d dpa_EDSAdmin`

### Output Format

Present the results as:
1. **Object type** (Table/View/Procedure)
2. **Column listing** with types and constraints
3. **Relationships** (foreign keys, references)
4. **Row count** and sample data (for tables)
5. **Suggestions** for related commands (`/sql`, `/report`, `/docs`)

### Error Handling

- If the object is not found, suggest checking the name or using `/docs` to search
- If the command fails with a DB error, check `.env` configuration
