# EDS Documentation Wiki

> **EDS (Educational Data Systems)** - A comprehensive procurement platform for K-12 school districts

---

## Quick Stats

| Metric | Value |
|--------|-------|
| **Database** | SQL Server 2017 (dpa_EDSAdmin monitoring) |
| **Tables** | 439 |
| **Stored Procedures** | 396 |
| **Views** | 475 |
| **Database Size** | ~1.4 TB |
| **Daily Active Users** | ~200+ |

---

## Navigation

### Getting Started
- [Quick Reference](getting-started/quick-reference.md) - One-page overview
- [Glossary](getting-started/glossary.md) - EDS terminology

### Business
- [What is EDS?](business/what-is-eds.md) - System overview
- [Business Entities](business/entities/) - Districts, Schools, Vendors, etc.
- [Workflows](business/workflows/) - Requisitions, Bidding, POs

### Architecture
- [System Overview](architecture/system-overview.md) - High-level architecture
- [Application Stack](architecture/application-stack.md) - ColdFusion/Lucee, Node.js, Kubernetes
- [Database Architecture](architecture/database-architecture.md) - SQL Server configuration

### Schema Reference
- [Schema Overview](schema/index.md) - 439 tables summary
- [Tables by Domain](schema/by-domain/) - Bidding, Orders, Vendors, etc.
- [Stored Procedures](schema/stored-procedures.md) - 396 procedures
- [Views](schema/views.md) - 475 views
- [Triggers](schema/triggers.md) - 59 triggers

### Performance
- [Performance Overview](performance/index.md) - Current state
- [Known Issues](performance/known-issues/) - Active performance problems
- [Incidents](performance/incidents/) - Post-mortems
- [Recommendations](performance/recommendations.md) - Optimization guide

### Operations
- [Daily Monitoring](operations/daily-monitoring.md) - Morning checklist
- [SQL Agent Jobs](operations/sql-agent-jobs.md) - Scheduled jobs
- [Maintenance](operations/maintenance.md) - Index/stats maintenance

### Troubleshooting
- [Troubleshooting Guide](troubleshooting/index.md) - Problem resolution
- [Runbooks](troubleshooting/runbooks/) - Emergency procedures

### User Activity
- [Application Users](user-activity/application-users.md) - Who uses EDS
- [Usage Patterns](user-activity/usage-patterns.md) - Peak times, patterns

---

## Key Contacts

| Role | Contact |
|------|---------|
| DBA Team | dba-team@company.com |
| On-Call DBA | David Harrison |
| Manager | (See alert contacts) |

---

## Recent Updates

| Date | Change |
|------|--------|
| 2026-01-12 | Initial wiki creation with performance findings |
| 2026-01-12 | Added Jan 6 blocking incident post-mortem |
| 2026-01-12 | Documented 5 known performance issues |

---

## External Documentation

These detailed reference documents are maintained separately:

- [EDS_DATA_DICTIONARY.md](../EDS_DATA_DICTIONARY.md) - Complete table/column reference
- [EDS_STORED_PROCEDURES.md](../EDS_STORED_PROCEDURES.md) - Full SP documentation
- [EDS_VIEWS.md](../EDS_VIEWS.md) - Complete view documentation
- [EDS_ERD.md](../EDS_ERD.md) - Entity relationship diagrams
- [EDS_BUSINESS_DOMAINS.md](../EDS_BUSINESS_DOMAINS.md) - Domain organization
