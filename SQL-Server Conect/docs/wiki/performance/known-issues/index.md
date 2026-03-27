# Known Performance Issues

[Home](../../index.md) > [Performance](../index.md) > Known Issues

---

## Active Issues Summary

**Last Updated:** January 12, 2026

| ID | Issue | Priority | Impact | Status |
|----|-------|----------|--------|--------|
| KI-001 | [usp_GetIndexData slow execution](usp-getindexdata.md) | P1 Critical | 24+ hrs/execution | Investigating |
| KI-002 | [Vendor Sync Job inefficiency](vendor-sync-job.md) | P2 High | 59 hrs/month wasted | Active |
| KI-003 | [trig_DetailUpdate blocking](trigger-blocking.md) | P3 High | 82 min cascades | Active |
| KI-004 | [CrossRef lookup blocking](crossref-blocking.md) | P4 Medium | 12+ hrs blocked | Active |
| KI-005 | [SSO User Update deadlocks](sso-deadlocks.md) | P5 Medium | 20 deadlocks/month | Active |

---

## Issue Details

### KI-001: usp_GetIndexData (P1 Critical)

**Summary:** Stored procedure for bid pricing lookups runs for 24+ hours
**Root Cause:** Parameter sniffing, 33M row BidResults scans, 19 different execution plans
**Impact:** 15.5% of total database time
**Affected:** Bid pricing, catalog lookups

[Full Details →](usp-getindexdata.md)

---

### KI-002: Vendor Sync Job (P2 High)

**Summary:** Vendor registration sync job runs hourly 24/7 with full table scans
**Root Cause:** No incremental sync logic, full comparison every hour
**Impact:** 59 hours/month (15.5% of DB time)
**Affected:** Background processing, resource consumption

[Full Details →](vendor-sync-job.md)

---

### KI-003: trig_DetailUpdate Blocking (P3 High)

**Summary:** Trigger on Detail table causes blocking cascades
**Root Cause:** Complex trigger logic holds locks during price calculations
**Impact:** Up to 82 minutes blocking per incident
**Affected:** Requisition entry, bulk operations

[Full Details →](trigger-blocking.md)

---

### KI-004: CrossRef Lookup Blocking (P4 Medium)

**Summary:** CrossRef lookups blocked by other operations
**Root Cause:** Victim of trig_DetailUpdate and bulk operations
**Impact:** 12+ hours blocked (accumulated)
**Affected:** Item lookups, pricing queries

[Full Details →](crossref-blocking.md)

---

### KI-005: SSO User Update Deadlocks (P5 Medium)

**Summary:** Concurrent SSO user updates cause deadlocks
**Root Cause:** Parallel updates from same pod, page-level locking
**Impact:** 20 deadlocks/month, 8-12 sessions involved per incident
**Affected:** User authentication, SSO sync

[Full Details →](sso-deadlocks.md)

---

## Recommendations Summary

### Quick Wins (Immediate)
1. Reduce vendor sync frequency to 4x daily
2. Add NOLOCK hints to read-only queries in triggers
3. Serialize SSO updates (process sequentially)

### Medium-Term
1. Rewrite usp_GetIndexData with plan stability
2. Implement change tracking for vendor sync
3. Refactor trig_DetailUpdate to async processing

### Long-Term
1. Add read replicas for reporting
2. Enable Query Store
3. Implement Resource Governor

---

## Related Documentation

- [Performance Overview](../index.md) - Current state
- [Incidents](../incidents/) - Post-mortems
- [Recommendations](../recommendations.md) - Full action plan
- [Troubleshooting](../../troubleshooting/index.md) - Problem resolution
