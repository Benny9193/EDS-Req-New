# Performance Overview

[Home](../index.md) > Performance

---

## Current State Summary

**Analysis Date:** January 12, 2026
**Data Source:** SolarWinds DPA (dpa_EDSAdmin database)
**Period:** Last 30 days

---

## Key Metrics

| Metric | Value | Status |
|--------|-------|--------|
| **Total DB Time** | 380 hours/month | Baseline |
| **Total Blocking Time** | 418 hours/month | High |
| **Deadlocks** | 20 (last 30 days) | Elevated |
| **Critical Incidents** | 1 (Jan 6, 2026) | Resolved |

---

## Top Performance Issues

| Priority | Issue | Impact | Status |
|----------|-------|--------|--------|
| **P1** | [usp_GetIndexData](known-issues/usp-getindexdata.md) | 24+ hrs execution | Active |
| **P2** | [Vendor Sync Job](known-issues/vendor-sync-job.md) | 59 hrs/month wasted | Active |
| **P3** | [trig_DetailUpdate](known-issues/trigger-blocking.md) | 82 min blocking cascades | Active |
| **P4** | [CrossRef Blocking](known-issues/crossref-blocking.md) | 12+ hrs blocked | Active |
| **P5** | [SSO Deadlocks](known-issues/sso-deadlocks.md) | 20 deadlocks/month | Active |

---

## Wait Event Analysis (Last 7 Days)

| Wait Event | Time (hrs) | Category |
|------------|------------|----------|
| Memory/CPU | 49.3 | CPU |
| LCK_M_IS | 39.9 | Locking |
| RESOURCE_SEMAPHORE | 28.8 | Memory |
| CXPACKET | 22.9 | Parallelism |
| PAGEIOLATCH_SH | 15.5 | I/O |
| CXCONSUMER | 11.5 | Parallelism |
| LCK_M_S | 9.6 | Locking |
| ASYNC_NETWORK_IO | 7.3 | Network |

---

## Usage Patterns

### Peak Hours
```
Hour    Activity
07:00   ████████████████████████████  High
08:00   ██████████████████  Medium
09:00   ████████████████████████  High
10:00   ████  Low
...
22:00   ████████████████████████████████████████  Batch Jobs
```

### Critical Times
- **7-9 AM:** Business hours peak
- **10 PM:** Batch job processing
- **2-4 AM:** Maintenance window

---

## In This Section

### Monitoring
- [Monitoring Guide](monitoring-guide.md) - How to use DPA
- Key Metrics - What to watch

### Known Issues
- [Issues Summary](known-issues/index.md) - All active issues
- [usp_GetIndexData](known-issues/usp-getindexdata.md) - P1 Critical
- [Vendor Sync Job](known-issues/vendor-sync-job.md) - P2 High
- [Trigger Blocking](known-issues/trigger-blocking.md) - P3 High
- [CrossRef Blocking](known-issues/crossref-blocking.md) - P4 Medium
- [SSO Deadlocks](known-issues/sso-deadlocks.md) - P5 Medium

### Incidents
- [Jan 6, 2026 Blocking](incidents/2026-01-06-blocking.md) - Major incident

### Optimization
- [Recommendations](recommendations.md) - Improvement actions

---

## Quick Actions

### If You See High Blocking
1. Check [blocking runbook](../troubleshooting/runbooks/blocking-emergency.md)
2. Identify blocker with DPA
3. Consider killing long-running blocker

### If You See Deadlocks
1. Check [deadlock guide](../troubleshooting/deadlocks.md)
2. Review deadlock graph in DPA
3. Identify conflicting queries

---

## Related Documentation

- [Operations](../operations/index.md) - Daily monitoring
- [Troubleshooting](../troubleshooting/index.md) - Problem resolution
- [Schema](../schema/index.md) - Database structure
