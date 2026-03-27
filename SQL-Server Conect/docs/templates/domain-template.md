# Business Domain Documentation Template

Use this template when documenting a business domain (logical grouping of related tables). Replace all placeholders with actual content.

---

## {Domain Name} Domain

**Tables:** {count} | **Total Rows:** {count} | **Primary Owner:** {team/role}

### Overview

{2-3 paragraphs describing what this domain covers, its business purpose, and how it fits into the overall system.}

### Business Processes

#### Process 1: {Process Name}

{Description of the business process}

**Workflow:**
```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Step 1    │───►│   Step 2    │───►│   Step 3    │───►│   Step 4    │
│  {Action}   │    │  {Action}   │    │  {Action}   │    │  {Action}   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
     │                   │                   │                   │
     ▼                   ▼                   ▼                   ▼
 {Table1}            {Table2}            {Table3}            {Table4}
```

**Tables Involved:**
| Step | Table | Action | Description |
|------|-------|--------|-------------|
| 1 | {Table1} | INSERT | {What happens} |
| 2 | {Table2} | UPDATE | {What happens} |
| 3 | {Table3} | INSERT | {What happens} |

**Business Rules:**
1. {Rule 1}
2. {Rule 2}
3. {Rule 3}

**Status Transitions:**
```
{Status1} ──► {Status2} ──► {Status3}
    │              │
    ▼              ▼
{Status4}     {Status5}
```

---

#### Process 2: {Process Name}

{Repeat structure for each major process}

---

### Entity Relationship Diagram

```mermaid
erDiagram
    {Table1} ||--o{ {Table2} : "has many"
    {Table1} ||--|| {Table3} : "has one"
    {Table2} }|--|| {Table4} : "belongs to"

    {Table1} {
        int {PK} PK
        int {FK} FK
        varchar Name
    }
```

### Core Tables

| Table | Rows | Purpose | Key Relationships |
|-------|------|---------|-------------------|
| {Table1} | {count} | {Main purpose} | Parent of {Table2} |
| {Table2} | {count} | {Main purpose} | Child of {Table1} |
| {Table3} | {count} | {Main purpose} | Lookup table |

### Supporting Tables

| Table | Rows | Purpose |
|-------|------|---------|
| {SupportTable1} | {count} | {Purpose} |
| {SupportTable2} | {count} | {Purpose} |

### Lookup/Reference Tables

| Table | Values | Used By |
|-------|--------|---------|
| {LookupTable1} | {count} values | {Tables that reference it} |
| {LookupTable2} | {count} values | {Tables that reference it} |

### Key Stored Procedures

| Procedure | Purpose | Called By |
|-----------|---------|-----------|
| sp_{Proc1} | {What it does} | {Application/other procs} |
| sp_{Proc2} | {What it does} | {Application/other procs} |

### Key Views

| View | Purpose | Source Tables |
|------|---------|---------------|
| {View1} | {What it presents} | {Tables} |
| {View2} | {What it presents} | {Tables} |

### Integration Points

#### Inbound Data

| Source | Method | Frequency | Tables Affected |
|--------|--------|-----------|-----------------|
| {System1} | {API/File/Manual} | {Daily/Real-time} | {Tables} |

#### Outbound Data

| Destination | Method | Frequency | Source Tables |
|-------------|--------|-----------|---------------|
| {System1} | {API/File/Report} | {Daily/Real-time} | {Tables} |

### Data Quality Considerations

- **Common Issues:** {Known data quality problems}
- **Validation Rules:** {Key validations enforced}
- **Cleanup Processes:** {How bad data is handled}

### Security & Access

- **Data Sensitivity:** {PII, financial, etc.}
- **Access Control:** {Row-level security, district scoping}
- **Audit Requirements:** {What needs to be logged}

### Archive Strategy

| Table | Retention | Archive Method | Archive Table |
|-------|-----------|----------------|---------------|
| {Table1} | {X years} | {Move/Delete/Flag} | {ArchiveTable} |

### Performance Considerations

- **High-Volume Tables:** {Tables with most activity}
- **Slow Queries:** {Known performance issues}
- **Index Strategy:** {Key indexes for this domain}

### Related Domains

| Domain | Relationship |
|--------|--------------|
| {Domain1} | {How they interact} |
| {Domain2} | {How they interact} |

### Glossary

| Term | Definition |
|------|------------|
| {Term1} | {What it means in this context} |
| {Term2} | {What it means in this context} |

### Change History

| Date | Change | Reason |
|------|--------|--------|
| {date} | Initial documentation | Phase 1 documentation effort |

---

## Quick Reference

**Domain Owner:** {Team/Person}
**Primary Application:** {Application name}
**Support Contact:** {Email/Team}
