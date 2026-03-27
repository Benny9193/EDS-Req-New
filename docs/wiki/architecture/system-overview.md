# System Architecture Overview

[Home](../index.md) > [Architecture](index.md) > System Overview

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              USERS                                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│  │ School Staff │  │   Vendors    │  │  Approvers   │  │    Admin     │    │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘    │
└─────────┼─────────────────┼─────────────────┼─────────────────┼────────────┘
          │                 │                 │                 │
          ▼                 ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         APPLICATION LAYER                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                    Kubernetes Cluster (Azure)                        │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌────────────┐  │    │
│  │  │ eds-edsiq-* │  │eds-edsiq-2-*│  │eds-nodeindex│  │eds-report- │  │    │
│  │  │(CFML/Lucee) │  │(CFML/Lucee) │  │   (Node.js) │  │  handler   │  │    │
│  │  │  170 hrs/mo │  │             │  │  62 hrs/mo  │  │            │  │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └────────────┘  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                    IIS / Legacy Services                             │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                  │    │
│  │  │     IIS     │  │   jTDS      │  │   Python    │                  │    │
│  │  │  2.7 hrs/mo │  │  2.6 hrs/mo │  │  8.6 hrs/mo │                  │    │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DATABASE LAYER                                       │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │              SQL Server 2017 (Developer Edition)                     │    │
│  │              eds-sqlserver.eastus2.cloudapp.azure.com               │    │
│  │              Windows Server 2022 Datacenter (Azure VM)               │    │
│  │  ┌─────────────────────────────┐  ┌─────────────────────────────┐   │    │
│  │  │           EDS               │  │      dpa_EDSAdmin           │   │    │
│  │  │    (Production Database)    │  │   (DPA Monitoring DB)       │   │    │
│  │  │    439 tables, ~1.4 TB      │  │    207 tables               │   │    │
│  │  └─────────────────────────────┘  └─────────────────────────────┘   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MONITORING LAYER                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │              SolarWinds Database Performance Analyzer (DPA)          │    │
│  │  • Real-time query monitoring                                        │    │
│  │  • Blocking detection                                                │    │
│  │  • Wait event analysis                                               │    │
│  │  • Index recommendations                                             │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Component Summary

### Application Tier

| Component | Technology | Purpose | Activity |
|-----------|------------|---------|----------|
| **eds-edsiq-*** | CFML (Lucee/CFWheels on JVM) | Main web application | 170 hrs/month |
| **eds-nodeindexer** | Node.js | Search indexing | 62 hrs/month |
| **eds-report-handler** | Node.js | Report generation | 7.7 hrs/month |
| **IIS** | .NET | Legacy services | 2.7 hrs/month |

### Database Tier

| Database | Purpose | Size |
|----------|---------|------|
| **EDS** | Production data | ~1.4 TB |
| **dpa_EDSAdmin** | Performance monitoring | ~50 GB |
| **SearchData** | Search indexes | Variable |

### Infrastructure

| Component | Details |
|-----------|---------|
| **Cloud** | Azure |
| **VM** | Windows Server 2022 Datacenter |
| **Container** | Kubernetes (multiple pods) |
| **Region** | East US 2 |

---

## Data Flow

### Requisition Flow
```
User → Web App (CFML/Lucee) → SQL Server → Stored Procedure → Tables
                                   ↓
                            Trigger fires
                                   ↓
                         Related tables updated
```

### Monitoring Flow
```
SQL Server → DPA Agent → dpa_EDSAdmin → Analysis
                                      ↓
                               Alerts/Reports
```

---

## Key Connections

| Source | Target | Protocol | Purpose |
|--------|--------|----------|---------|
| K8s Pods | SQL Server | TCP 1433 | Application queries |
| DPA Agent | SQL Server | TCP 1433 | Monitoring |
| SQL Agent | SQL Server | Internal | Scheduled jobs |

---

## Related Documentation

- [Application Stack](application-stack.md) - Detailed app components
- [Database Architecture](database-architecture.md) - SQL Server details
- [Integrations](integrations.md) - External system connections

---

## See Also

| Topic | Description |
|-------|-------------|
| [User Activity](../user-activity/index.md) | Who connects to EDS |
| [Performance](../performance/index.md) | Performance characteristics |
| [Schema](../schema/index.md) | Database structure |
