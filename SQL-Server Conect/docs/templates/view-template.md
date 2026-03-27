# View Documentation Template

Use this template when documenting database views. Replace all placeholders with actual content.

---

## {ViewName}

**Schema:** `dbo` | **Created:** {date}

### Purpose

{One sentence explaining what this view presents and why it exists.}

### Business Context

{2-3 sentences explaining how this view is used. What reporting/application need does it serve?}

### Usage

- **Application Features:** {Which screens/features use this view}
- **Reports:** {Which reports use this view}
- **Ad-hoc Queries:** {Common analysis use cases}

### Source Tables

| Table | Join Type | Join Condition | Columns Used |
|-------|-----------|----------------|--------------|
| {Table1} | Base | - | {columns} |
| {Table2} | LEFT JOIN | {join condition} | {columns} |
| {Table3} | INNER JOIN | {join condition} | {columns} |

### Columns

| Column | Source | Type | Description |
|--------|--------|------|-------------|
| {Column1} | {Table.Column} | {type} | {What this represents} |
| {Column2} | {Table.Column} | {type} | {What this represents} |
| {CalculatedCol} | Expression | {type} | {Formula and meaning} |

### Filtering Logic

{Describe any WHERE clause filtering built into the view}

```sql
-- Built-in filters:
WHERE Active = 1           -- Only active records
  AND DistrictId IS NOT NULL  -- {reason for filter}
```

### Aggregations

{If the view includes GROUP BY or aggregations}

| Aggregation | Description |
|-------------|-------------|
| SUM({Column}) | {What is being summed} |
| COUNT(*) | {What is being counted} |

### Related Views

| View | Relationship |
|------|--------------|
| {View1} | {How they relate - subset? different filter?} |
| {View2} | {How they relate} |

### Common Query Patterns

```sql
-- Typical usage
SELECT *
FROM {ViewName}
WHERE DistrictId = @DistrictId
ORDER BY {Column};

-- With additional filtering
SELECT {columns}
FROM {ViewName}
WHERE {conditions}
  AND {date_range};
```

### Performance Notes

- **Complexity:** {Simple/Moderate/Complex}
- **Underlying Indexes:** {Are source tables properly indexed for this view?}
- **Materialization:** {Is this indexed/materialized or computed on-demand?}
- **Expected Row Count:** {Typical result set size}

### Variants

{If there are multiple versions of this view}

| View Name | Difference |
|-----------|------------|
| {ViewName} | Current version |
| {ViewName}1 | {How it differs} |
| {ViewName}Original | {Legacy version - still needed?} |

### Notes

- {Any quirks or gotchas}
- {Data quality considerations}
- {When data refreshes}

### Change History

| Date | Change | Reason |
|------|--------|--------|
| {date} | Initial documentation | Phase 1 documentation effort |

---

## Quick Reference

**Owner:** {Domain/Team}
**Active/Deprecated:** {Active/Deprecated/Legacy}
**Refresh Frequency:** {Real-time/Daily/On-demand}
