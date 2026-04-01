FROM python:3.12-slim

# Install ODBC driver for SQL Server connectivity
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl gnupg2 unixodbc-dev \
    && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
    && curl -fsSL https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy project files
COPY pyproject.toml agent_config.yaml ./
COPY agent/ agent/

# Install with agent dependencies
RUN pip install --no-cache-dir -e ".[agent]"

# Create data directories
RUN mkdir -p data/sessions data/memory data/audit data/vectordb

# Default to CLI mode
ENTRYPOINT ["eds-agent"]
CMD ["status"]

# MCP server mode: docker run eds-agent mcp --sse
# Chat mode: docker run -it eds-agent chat
# GUI mode requires nicegui: docker run -p 8080:8080 eds-agent-gui
