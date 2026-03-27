# EDS Database - Archive Strategy & Data Retention

Generated: 2026-01-15

This document defines the data archival strategy, retention policies, and procedures for managing historical data in the EDS database.

---

## Overview

The EDS database contains ~540 million rows of operational data. Without proper archival, database size, performance, and maintenance costs grow unsustainably. This archive strategy balances:

- **Performance**: Keep operational tables small for fast queries
- **Compliance**: Retain data for regulatory requirements
- **Cost**: Minimize storage costs for old data
- **Accessibility**: Maintain access to historical data when needed

---

## Archive Architecture

### Schema Design

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           ARCHIVE ARCHITECTURE                               │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│                              EDS DATABASE                                     │
│                                                                              │
│  ┌─────────────────────┐        ┌─────────────────────┐                     │
│  │     dbo schema      │        │   archive schema    │                     │
│  │   (operational)     │  ───►  │   (historical)      │                     │
│  │                     │        │                     │                     │
│  │  Requisitions       │        │  Requisitions       │                     │
│  │  Detail             │        │  Detail             │                     │
│  │  PO                 │        │  PO                 │                     │
│  │  BidHeaders         │        │  BidHeaders         │                     │
│  │  BidResults         │        │  BidResults         │                     │
│  │  ...                │        │  ...                │                     │
│  └─────────────────────┘        └─────────────────────┘                     │
│                                          │                                   │
│                                          ▼                                   │
│                                 ┌─────────────────────┐                     │
│                                 │   Offsite Backup    │                     │
│                                 │   (Cold Storage)    │                     │
│                                 └─────────────────────┘                     │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Archive Schema Tables

The `archive` schema mirrors the `dbo` schema for historical data:

| Archive Table | Source Table | Est. Rows | Retention |
|---------------|--------------|-----------|-----------|
| archive.Requisitions | dbo.Requisitions | ~10M | 7 years |
| archive.Detail | dbo.Detail | ~25M | 7 years |
| archive.PO | dbo.PO | ~2M | 7 years |
| archive.PODetailItems | dbo.PODetailItems | ~4M | 7 years |
| archive.Approvals | dbo.Approvals | ~3M | 7 years |
| archive.BidHeaders | dbo.BidHeaders | ~3M | 10 years |
| archive.BidHeaderDetail | dbo.BidHeaderDetail | ~100M | 10 years |
| archive.BidResults | dbo.BidResults | ~15M | 10 years |
| archive.BidResultsDetail | dbo.BidResultsDetail | ~15M | 10 years |
| archive.Awards | dbo.Awards | ~1.5M | 10 years |
| archive.Catalog | dbo.Catalog | ~5K | 5 years |
| archive.CrossRefs | dbo.CrossRefs | ~100M | 5 years |
| archive.UserAccounts | dbo.UserAccounts | ~500K | 3 years |
| archive.ReportSession | dbo.ReportSession | ~4M | 1 year |
| archive.ReportSessionLinks | dbo.ReportSessionLinks | ~50M | 1 year |

---

## Retention Policies

### By Data Category

| Category | Operational | Archive | Total Retention | Justification |
|----------|-------------|---------|-----------------|---------------|
| **Transactions** | 2 years | 5 years | 7 years | Financial audit |
| **Bids/Awards** | 3 years | 7 years | 10 years | Procurement compliance |
| **Catalog/Pricing** | Current + 2 years | 3 years | 5 years | Price history |
| **Users/Sessions** | 1 year | 2 years | 3 years | Security audit |
| **Reports** | 90 days | 9 months | 1 year | Storage optimization |
| **Audit Logs** | 1 year | 6 years | 7 years | Compliance |

### By Table

| Table | Operational Retention | Archive Retention | Notes |
|-------|----------------------|-------------------|-------|
| Requisitions | 2 fiscal years | 5 years | Based on fiscal close |
| Detail | 2 fiscal years | 5 years | With requisition |
| PO | 2 fiscal years | 5 years | With requisition |
| Approvals | 2 fiscal years | 5 years | Audit trail |
| BidHeaders | 3 years from close | 7 years | Procurement regulation |
| BidResults | 3 years from close | 7 years | With bid |
| Awards | Contract term + 3 years | 7 years | Contract compliance |
| Catalog | Current effective | 5 years | Price history |
| CrossRefs | Current effective | 5 years | Product history |
| SessionTable | 30 days | - | Cleanup only |
| ReportSession | 90 days | 9 months | Storage intensive |
| EmailBlastLog | 1 year | 2 years | Communication audit |

---

## Archive Procedures

### Automated Archive Jobs

| Job | Schedule | Procedure | Description |
|-----|----------|-----------|-------------|
| Nightly Cleanup | Daily 4 AM | sp_NightlyGarbageCollection | Session/temp cleanup |
| Monthly Archive | 1st of month | sp_ArchiveOldData | Move old data to archive |
| Quarterly Purge | Quarterly | sp_PurgeArchive | Remove expired archive data |
| Annual Review | January | sp_ArchiveReview | Validation and reporting |

### Archive Process Flow

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           ARCHIVE PROCESS FLOW                                │
└──────────────────────────────────────────────────────────────────────────────┘

1. IDENTIFY CANDIDATES
   │
   ├── sp_IdentifyArchiveCandidates
   │   └── Based on: fiscal year, status, last activity
   │
   ▼
2. VALIDATE INTEGRITY
   │
   ├── sp_ValidateArchiveCandidates
   │   └── Check: referential integrity, business rules
   │
   ▼
3. ARCHIVE DATA
   │
   ├── sp_ArchiveRequisitions
   │   ├── INSERT INTO archive.Requisitions SELECT FROM dbo.Requisitions
   │   ├── INSERT INTO archive.Detail SELECT FROM dbo.Detail
   │   ├── INSERT INTO archive.Approvals SELECT FROM dbo.Approvals
   │   └── Related tables...
   │
   ▼
4. VERIFY ARCHIVE
   │
   ├── sp_VerifyArchive
   │   └── Compare counts, checksums
   │
   ▼
5. REMOVE FROM OPERATIONAL
   │
   ├── sp_RemoveArchivedData
   │   └── DELETE from dbo tables (cascading)
   │
   ▼
6. LOG COMPLETION
   │
   └── ArchiveLog table updated
```

---

## Archive Criteria

### Requisitions Archive Criteria

Archive requisitions when ALL conditions are met:

```sql
-- Archive criteria for requisitions
WHERE r.FiscalYear < (YEAR(GETDATE()) - 2)  -- Older than 2 fiscal years
  AND r.Status IN ('C', 'X', 'V')            -- Closed, Cancelled, Voided
  AND NOT EXISTS (                           -- No active POs
      SELECT 1 FROM PO p
      WHERE p.RequisitionId = r.RequisitionId
        AND p.Status NOT IN ('C', 'X')
  )
  AND r.ModifiedDate < DATEADD(YEAR, -2, GETDATE())  -- No recent changes
```

### PO Archive Criteria

```sql
-- Archive criteria for purchase orders
WHERE p.FiscalYear < (YEAR(GETDATE()) - 2)
  AND p.Status IN ('C', 'R', 'X')  -- Closed, Received, Cancelled
  AND p.InvoiceStatus = 'P'         -- Paid
  AND p.ModifiedDate < DATEADD(YEAR, -2, GETDATE())
```

### Bid Archive Criteria

```sql
-- Archive criteria for bids
WHERE b.CloseDate < DATEADD(YEAR, -3, GETDATE())  -- Closed 3+ years ago
  AND b.Status IN ('A', 'C', 'E')                  -- Awarded, Closed, Expired
  AND NOT EXISTS (                                 -- No active awards
      SELECT 1 FROM Awards a
      WHERE a.BidHeaderId = b.BidHeaderId
        AND a.ExpirationDate > GETDATE()
  )
```

---

## Archive Table Specifications

### Archived Requisitions

| Column | Type | Notes |
|--------|------|-------|
| RequisitionId | INT PK | Matches source |
| DistrictId | INT | For filtering |
| SchoolId | INT | For filtering |
| FiscalYear | INT | Archive key |
| Status | CHAR(1) | Final status |
| TotalAmount | MONEY | Final amount |
| CreatedDate | DATETIME | Original create |
| ArchivedDate | DATETIME | Archive timestamp |
| OriginalData | NVARCHAR(MAX) | JSON of original |

### Archived Bid Headers

| Column | Type | Notes |
|--------|------|-------|
| BidHeaderId | INT PK | Matches source |
| CategoryId | INT | Category reference |
| BidNumber | VARCHAR(50) | Bid identifier |
| CloseDate | DATETIME | Bid close date |
| AwardDate | DATETIME | Award date |
| Status | VARCHAR(10) | Final status |
| TotalAwarded | MONEY | Award value |
| ArchivedDate | DATETIME | Archive timestamp |
| OriginalData | NVARCHAR(MAX) | JSON of original |

---

## Purge Procedures

### Expired Archive Data

Data that exceeds total retention is permanently purged:

```sql
-- Purge expired archive data
DELETE FROM archive.Requisitions
WHERE ArchivedDate < DATEADD(YEAR, -5, GETDATE());

DELETE FROM archive.BidHeaders
WHERE ArchivedDate < DATEADD(YEAR, -7, GETDATE());
```

### Purge Verification

Before purge, verify:
1. Backup exists
2. No regulatory hold
3. Approval from data owner
4. Audit log entry

### Purge Log

| Column | Type | Purpose |
|--------|------|---------|
| PurgeLogId | INT PK | Log entry ID |
| TableName | VARCHAR(100) | Purged table |
| RowCount | INT | Rows purged |
| PurgeDate | DATETIME | When purged |
| ApprovedBy | VARCHAR(100) | Approver |
| Reason | VARCHAR(500) | Purge reason |

---

## ReportSession Special Handling

ReportSessionLinks is the second largest table (~52M rows) and requires aggressive management:

### Retention Policy

| Age | Action |
|-----|--------|
| 0-30 days | Keep in operational |
| 30-90 days | Archive |
| 90+ days | Purge |

### Cleanup Procedure

```sql
-- Daily cleanup of old report sessions
EXEC sp_CleanupReportSessions
    @ArchiveOlderThanDays = 30,
    @PurgeOlderThanDays = 90,
    @BatchSize = 10000;
```

### Storage Impact

| Scenario | ReportSessionLinks Size | Savings |
|----------|------------------------|---------|
| No cleanup | 52M rows / 15GB | - |
| 90-day retention | 8M rows / 2.5GB | 83% |
| 30-day retention | 3M rows / 1GB | 93% |

---

## Cross-Reference Mapping

When data is archived, cross-reference mappings maintain integrity:

### Mapping Tables

| Table | Purpose |
|-------|---------|
| archive.RequisitionIdMapping | Old → Archive ID mapping |
| archive.POIdMapping | Old → Archive ID mapping |
| archive.BidHeaderIdMapping | Old → Archive ID mapping |

### Mapping Usage

```sql
-- Find archived requisition
SELECT a.*
FROM archive.Requisitions a
INNER JOIN archive.RequisitionIdMapping m
    ON a.RequisitionId = m.ArchiveRequisitionId
WHERE m.OriginalRequisitionId = @RequestedId;
```

---

## Recovery Procedures

### Restore from Archive

```sql
-- Restore single requisition from archive
EXEC sp_RestoreFromArchive
    @TableName = 'Requisitions',
    @RecordId = 12345,
    @Reason = 'Audit request',
    @RequestedBy = 'user@district.edu';
```

### Bulk Restore

```sql
-- Restore fiscal year for audit
EXEC sp_RestoreFiscalYear
    @FiscalYear = 2023,
    @DistrictId = 100,
    @Reason = 'State audit',
    @RequestedBy = 'auditor@state.gov';
```

### Restore Verification

| Check | Description |
|-------|-------------|
| Integrity | Foreign keys valid |
| Completeness | All related records |
| Uniqueness | No duplicate IDs |
| Status | Marked as restored |

---

## Monitoring & Reporting

### Archive Metrics

| Metric | Target | Alert Threshold |
|--------|--------|-----------------|
| Monthly archive volume | <1M rows | >2M rows |
| Archive job duration | <2 hours | >4 hours |
| Archive success rate | 100% | <99% |
| Storage growth (operational) | <5%/year | >10%/year |

### Monthly Archive Report

```sql
EXEC sp_ArchiveReport
    @ReportMonth = '2026-01',
    @IncludeDetails = 1;

-- Output:
-- Tables archived: 15
-- Rows archived: 250,000
-- Space reclaimed: 2.5 GB
-- Purged rows: 50,000
-- Errors: 0
```

### Annual Review Checklist

- [ ] Verify retention periods meet current regulations
- [ ] Review archive storage costs
- [ ] Validate restore procedures
- [ ] Test recovery from archive
- [ ] Update documentation
- [ ] Review and approve purge candidates

---

## Compliance Considerations

### Regulatory Holds

When litigation or audit pending:
1. Suspend archival for affected data
2. Suspend purge for affected data
3. Document hold scope
4. Resume when hold released

### Hold Table

| Column | Type | Purpose |
|--------|------|---------|
| HoldId | INT PK | Hold identifier |
| HoldName | VARCHAR(200) | Description |
| StartDate | DATE | Hold start |
| EndDate | DATE | Hold end (NULL = active) |
| Scope | NVARCHAR(MAX) | JSON criteria |
| RequestedBy | VARCHAR(100) | Legal/compliance |

### Audit Trail

All archive operations logged:

| Operation | Logged Data |
|-----------|-------------|
| Archive | Table, row count, date, operator |
| Purge | Table, row count, date, approver |
| Restore | Table, record ID, date, reason |
| Hold | Scope, start, requester |

---

## Disaster Recovery

### Archive Backup Schedule

| Backup Type | Frequency | Retention | Storage |
|-------------|-----------|-----------|---------|
| Full | Weekly | 4 weeks | Offsite |
| Differential | Daily | 7 days | Onsite |
| Transaction Log | Every 15 min | 24 hours | Onsite |

### Recovery Point Objective (RPO)

| Data Type | RPO |
|-----------|-----|
| Operational | 15 minutes |
| Archive | 24 hours |

### Recovery Time Objective (RTO)

| Scenario | RTO |
|----------|-----|
| Single table restore | 1 hour |
| Full archive restore | 8 hours |
| Complete database restore | 24 hours |

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-01-15 | Initial archive strategy documentation | Phase 4 Documentation |

