---
allowed-tools: Bash(cd C?EDS && python:*), Bash(cd /c/EDS && python:*), Bash(ls:*), Bash(dir:*)
description: Show EDS DBA agent status — configuration, providers, DB connection, and doc index status.
---

## Context

- Working directory: C:\EDS
- Config file: C:\EDS\agent_config.yaml
- Environment: C:\EDS\.env

## Your Task

The user wants to check the EDS DBA agent's status and configuration.

Run this command:

```
cd C:\EDS && python -m agent --provider claude status
```

After the output, provide a brief summary of the key information:
- Which LLM provider and model are active
- Whether the vector DB (documentation index) is built
- Number of saved sessions
- Any warnings about missing configuration

### Quick health checks

If the user mentions "connection" or "health", also test the database connection:

```
cd C:\EDS && python -m agent --provider claude sql --execute --limit 1 "SELECT 1 as connection_test"
```

If this succeeds, the database connection is working. If it fails, suggest checking `.env` credentials.

### Provider switching

If the user wants to switch providers, tell them about the `--provider` flag available on all commands:
- `--provider claude` (default in plugin, uses ANTHROPIC_API_KEY)
- `--provider ollama` (local, uses qwen2.5:14b at localhost:11434)
- `--provider openai` (uses OPENAI_API_KEY)
