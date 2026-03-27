# Stored Procedure Documentation Template

Use this template when documenting stored procedures. Replace all placeholders with actual content.

---

## {ProcedureName}

**Schema:** `dbo` | **Created:** {date} | **Last Modified:** {date}

### Purpose

{One sentence explaining what this procedure does and why it exists.}

### Business Context

{2-3 sentences explaining when/why this procedure is called. What business process does it support?}

### Parameters

| Parameter | Type | Direction | Required | Description | Valid Values |
|-----------|------|-----------|----------|-------------|--------------|
| @{Param1} | int | IN | Yes | {What this parameter represents} | {Range or valid values} |
| @{Param2} | varchar(50) | IN | No | {What this parameter represents} | Default: {value} |
| @{ReturnParam} | int | OUT | - | {What is returned} | {Meaning of values} |

### Return Values

| Value | Meaning |
|-------|---------|
| 0 | Success |
| -1 | {Error condition} |
| -2 | {Error condition} |

### Tables Affected

| Table | Operation | Description |
|-------|-----------|-------------|
| {Table1} | SELECT | {What data is read} |
| {Table2} | INSERT | {What records are created} |
| {Table3} | UPDATE | {What fields are modified} |
| {Table4} | DELETE | {What records are removed} |

### Side Effects

- {Transaction behavior - does it commit/rollback?}
- {Triggers that may fire}
- {Audit records created}
- {Emails/notifications sent}

### Dependencies

**Calls These Procedures:**
- `sp_{OtherProc1}` - {why}
- `sp_{OtherProc2}` - {why}

**Called By:**
- `sp_{CallingProc1}` - {context}
- Application: {feature name}

### Example Usage

```sql
-- Basic usage
EXEC dbo.{ProcedureName}
    @{Param1} = 123,
    @{Param2} = 'value';

-- With output parameter
DECLARE @Result int;
EXEC dbo.{ProcedureName}
    @{Param1} = 123,
    @{ReturnParam} = @Result OUTPUT;
SELECT @Result;
```

### Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| {Error message} | {What causes it} | {How to fix} |

### Performance Notes

- **Typical Execution Time:** {ms/seconds}
- **Resource Impact:** {Low/Medium/High}
- **Blocking Potential:** {Yes/No - explain}
- **Recommended Scheduling:** {Real-time/Off-hours/Batch}

### Security

- **Required Permissions:** {EXECUTE on procedure, SELECT on tables, etc.}
- **Row-Level Security:** {Does it respect RLS?}

### Business Rules Implemented

1. {Rule 1 - what validation/logic is enforced}
2. {Rule 2 - what validation/logic is enforced}

### Change History

| Date | Change | Reason | Author |
|------|--------|--------|--------|
| {date} | Initial documentation | Phase 1 documentation effort | {name} |

---

## Quick Reference

**Owner:** {Domain/Team}
**Criticality:** {Critical/High/Medium/Low}
**Active/Deprecated:** {Active/Deprecated/Legacy}
