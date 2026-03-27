# EDS Quick Reference

[Home](../index.md) > [Getting Started](index.md) > Quick Reference

---

## One-Page Overview

### What is EDS?
**Educational Data Systems** - E-procurement platform for K-12 school districts handling requisitions, bidding, and purchase orders.

---

## Key Numbers

| Metric | Value |
|--------|-------|
| Database Size | ~1.4 TB |
| Tables | 439 |
| Stored Procedures | 396 |
| Views | 475 |
| Daily Users | 200+ |
| Monthly Transactions | Millions |

---

## Core Entities

| Entity | Table | Rows | Purpose |
|--------|-------|------|---------|
| **Requisitions** | Requisitions | 2M | Purchase requests |
| **Line Items** | Detail | 30M | Requisition items |
| **Vendors** | Vendors | 10K+ | Suppliers |
| **Items** | Items | 1.5M | Product catalog |
| **Bids** | BidHeaders/Bids | 10K+ | Competitive bids |
| **POs** | PO | 1M+ | Purchase orders |

---

## Business Workflow

```
Requisition → Approval → PO → Vendor → Fulfillment
     │            │       │
     └─ Budget ───┘       └─ Bid Awards
```

---

## Key Stored Procedures

| Procedure | Purpose |
|-----------|---------|
| sp_CreateNewRequisition | Create new req |
| sp_SubmitRequisition | Submit for approval |
| sp_ApproveReq | Approve requisition |
| sp_ConvertReqs | Convert to PO |
| usp_GetIndexData | Bid pricing lookup |

---

## Application Stack

| Layer | Technology |
|-------|------------|
| Web App | Java (JDBC) |
| API | Node.js |
| Database | SQL Server 2017 |
| Infrastructure | Azure / Kubernetes |
| Monitoring | SolarWinds DPA |

---

## Peak Times

| Time | Activity |
|------|----------|
| 7-9 AM | Business peak |
| 10 PM | Batch jobs |
| 2-4 AM | Maintenance |

---

## Active Performance Issues

| Issue | Impact |
|-------|--------|
| usp_GetIndexData | 24+ hr executions |
| Vendor Sync | Runs hourly (wasteful) |
| trig_DetailUpdate | Blocking cascades |
| SSO Updates | Deadlocks |

---

## Quick Commands

### Check Blocking
```sql
SELECT * FROM CON_BLOCKING_SUM_1
WHERE DATEHOUR > DATEADD(hour, -1, GETDATE())
```

### Check Deadlocks
```sql
SELECT * FROM CON_DEADLOCK_1
WHERE D > DATEADD(day, -1, GETDATE())
```

### Check Slow Queries
```sql
SELECT TOP 10 SQLHASH, SUM(TIMESECS) as TotalSecs
FROM CON_SQL_SUM_1
WHERE DATEHOUR > DATEADD(hour, -1, GETDATE())
GROUP BY SQLHASH ORDER BY 2 DESC
```

---

## Contacts

| Role | Contact |
|------|---------|
| DBA Team | dba-team@company.com |
| On-Call | David Harrison |

---

## Key Documentation

- [Full Wiki](../index.md)
- [Schema Reference](../schema/index.md)
- [Performance Issues](../performance/known-issues/index.md)
- [Daily Monitoring](../operations/daily-monitoring.md)
