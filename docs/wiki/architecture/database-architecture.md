# Database Architecture

[Home](../index.md) > [Architecture](index.md) > Database Architecture

---

## Overview

The EDS database runs on SQL Server 2017 hosted on an Azure Virtual Machine, with performance monitoring provided by SolarWinds DPA.

---

## Server Configuration

### Hardware

| Component | Specification |
|-----------|---------------|
| Platform | Azure Virtual Machine |
| Instance Type | Standard_D16s_v3 |
| vCPUs | 16 |
| Memory | 64 GB |
| Storage | Premium SSD |
| Region | East US 2 |

### SQL Server

| Setting | Value |
|---------|-------|
| Version | SQL Server 2017 |
| Edition | Enterprise |
| Collation | SQL_Latin1_General_CP1_CI_AS |
| Max Memory | 52 GB |
| Max DOP | 4 |
| Cost Threshold | 50 |

---

## Database Layout

### Production Databases

| Database | Purpose | Size (Est) |
|----------|---------|------------|
| EDS | Primary production | 200+ GB |
| EDSProd | Reporting replica | 200+ GB |
| tempdb | Temp operations | 50+ GB |

### Monitoring Database

| Database | Purpose | Retention |
|----------|---------|-----------|
| dpa_EDSAdmin | DPA monitoring data | 30 days |

---

## Database Objects

### EDS Production Database

| Object Type | Count |
|-------------|-------|
| Tables | 439 |
| Views | 475 |
| Stored Procedures | 396 |
| Functions | 200+ |
| Triggers | 52 |
| Indexes | 1500+ |

### Table Distribution by Domain

| Domain | Tables |
|--------|--------|
| Bidding | 76 |
| Orders | 45 |
| Vendors | 32 |
| Inventory | 28 |
| Users | 24 |
| Finance | 18 |
| Documents | 15 |
| Other | 200 |

---

## Storage Architecture

### File Groups

```
PRIMARY
    └── EDS.mdf (Primary data file)

SECONDARY
    └── EDS_Secondary.ndf (Secondary data file)

LOG
    └── EDS_log.ldf (Transaction log)
```

### TempDB Configuration

```
tempdb
    ├── tempdev1.mdf (8 GB)
    ├── tempdev2.ndf (8 GB)
    ├── tempdev3.ndf (8 GB)
    ├── tempdev4.ndf (8 GB)
    └── templog.ldf (4 GB)
```

**Note:** TempDB files = number of CPU cores (up to 8)

---

## Connection Configuration

### Network Settings

| Setting | Value |
|---------|-------|
| Server | eds-sqlserver.eastus2.cloudapp.azure.com |
| Port | 1433 |
| Protocol | TCP/IP |
| Encryption | Required (TLS 1.2) |

### Authentication

| Method | Usage |
|--------|-------|
| SQL Authentication | Application accounts |
| Windows Authentication | DBA access |
| Azure AD | Optional integration |

---

## Memory Configuration

### Buffer Pool

```
Total Server Memory: 64 GB
    │
    ├── Max Server Memory: 52 GB (SQL Server)
    │   │
    │   ├── Buffer Pool: ~48 GB
    │   ├── Plan Cache: ~2 GB
    │   └── Other: ~2 GB
    │
    └── OS Reserved: 12 GB
```

### Key Settings

| Setting | Value | Purpose |
|---------|-------|---------|
| min server memory | 8 GB | Minimum allocation |
| max server memory | 52 GB | Maximum allocation |
| optimize for ad hoc | 1 | Reduce plan cache bloat |
| lock pages in memory | Enabled | Prevent paging |

---

## Query Store

### Configuration

| Setting | Value |
|---------|-------|
| Operation Mode | READ_WRITE |
| Max Size | 1000 MB |
| Statistics Collection | AUTO |
| Stale Query Threshold | 30 days |
| Capture Mode | AUTO |

### Benefits
- Query plan history
- Force good plans
- Performance regression detection

---

## Monitoring (DPA)

### SolarWinds DPA

| Feature | Usage |
|---------|-------|
| Wait Analysis | Real-time wait monitoring |
| Blocking | Block chain visualization |
| Deadlocks | Deadlock graph capture |
| Query History | Historical query analysis |
| Alerting | Threshold-based alerts |

### Key DPA Tables

| Table | Content |
|-------|---------|
| CON_SQL_SUM_1 | Query execution statistics |
| CON_BLOCKING_SUM_1 | Blocking history |
| CON_DEADLOCK_1 | Deadlock events |
| CONU_1 | Database users |
| CONPR_1 | Program/application info |
| CONST_1 | SQL text storage |

---

## Backup Strategy

### Backup Schedule

| Type | Schedule | Retention |
|------|----------|-----------|
| Full | Daily 4 AM | 7 days |
| Differential | Every 4 hours | 2 days |
| Transaction Log | Every 15 minutes | 2 days |

### Backup Location
- Primary: Azure Blob Storage
- Secondary: Geo-redundant storage

### Recovery Model
- **Production:** FULL
- **Reporting:** SIMPLE

---

## High Availability

### Current Configuration

| Feature | Status |
|---------|--------|
| Always On AG | Not configured |
| Log Shipping | Not configured |
| Database Mirroring | Not configured |
| Azure Backup | Configured |

### Recommended Improvements
1. Configure Always On Availability Group
2. Add read replica for reporting
3. Implement automatic failover

---

## Maintenance Plan

### Index Maintenance

| Task | Schedule | Method |
|------|----------|--------|
| Reorganize | Daily | Fragmentation 10-30% |
| Rebuild | Weekly | Fragmentation > 30% |
| Update Statistics | Daily | All tables |

### Integrity Checks

| Check | Schedule |
|-------|----------|
| CHECKDB | Weekly (Sunday) |
| CHECKCATALOG | Monthly |
| Physical Only | Daily |

---

## Performance Configuration

### Key Settings

```sql
-- Verify settings
SELECT name, value_in_use
FROM sys.configurations
WHERE name IN (
    'max degree of parallelism',
    'cost threshold for parallelism',
    'optimize for ad hoc workloads',
    'max server memory (MB)'
)
```

| Setting | Current | Recommended |
|---------|---------|-------------|
| MAXDOP | 4 | 4 (appropriate for 16 cores) |
| Cost Threshold | 50 | 50 |
| Ad Hoc Optimization | ON | ON |
| Max Memory | 52 GB | 52 GB |

---

## See Also

- [Schema Overview](../schema/index.md) - Database objects
- [Performance Overview](../performance/index.md) - Performance metrics
- [Application Stack](application-stack.md) - Application connectivity

