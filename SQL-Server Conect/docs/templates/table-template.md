# Table Documentation Template

Use this template when documenting database tables. Replace all placeholders with actual content.

---

## {TableName}

**Schema:** `dbo` | **Rows:** {row_count} | **Created:** {date}

### Purpose

{One sentence explaining what this table stores and why it exists.}

### Business Context

{2-3 sentences explaining how this table fits into business processes. What business problem does it solve? When is data written/read?}

### Usage

- **Application:** {Which application features use this table}
- **Reports:** {Which reports query this table}
- **Integrations:** {External systems that read/write this table}

### Key Relationships

```
Parent Tables (this table references):
├── {ParentTable1} via {ForeignKeyColumn} - {relationship description}
└── {ParentTable2} via {ForeignKeyColumn} - {relationship description}

Child Tables (reference this table):
├── {ChildTable1} - {relationship description}
└── {ChildTable2} - {relationship description}
```

### Columns

| Column | Type | Nullable | Description | Business Rules |
|--------|------|----------|-------------|----------------|
| {PrimaryKey} | int IDENTITY | No | Primary key | Auto-generated |
| {Column1} | {type} | {Yes/No} | {What this column represents} | {Validation rules, constraints} |
| {Column2} | {type} | {Yes/No} | {What this column represents} | {Validation rules, constraints} |
| {ForeignKey} | int | {Yes/No} | FK to {Table} - {what it links} | Must exist in {Table} |

### Status/State Values

{Include if the table has status columns}

| Column | Value | Meaning | Valid Transitions |
|--------|-------|---------|-------------------|
| {StatusColumn} | 0 | {Meaning} | Can transition to: 1, 2 |
| {StatusColumn} | 1 | {Meaning} | Can transition to: 2, 3 |

### Indexes

| Index Name | Columns | Type | Purpose |
|------------|---------|------|---------|
| PK_{TableName} | {PK Column} | Clustered | Primary key |
| IX_{TableName}_{Column} | {Column(s)} | Non-clustered | {Query optimization purpose} |

### Common Query Patterns

```sql
-- Get active records for a district
SELECT * FROM {TableName}
WHERE DistrictId = @DistrictId AND Active = 1;

-- Join pattern for related data
SELECT t.*, r.Name
FROM {TableName} t
JOIN {RelatedTable} r ON t.{FK} = r.{PK};
```

### Data Quality Notes

- {Known data quality issues}
- {Duplicate handling rules}
- {Orphaned record handling}

### Performance Considerations

- {Table size and growth rate}
- {Partition strategy if applicable}
- {Archive policy}

### Change History

| Date | Change | Reason |
|------|--------|--------|
| {date} | Initial documentation | Phase 1 documentation effort |

---

## Quick Reference

**Owner:** {Domain/Team}
**Retention:** {How long data is kept}
**Backup Priority:** {Critical/High/Medium/Low}
**PII/Sensitive:** {Yes/No - what fields}
