# EDS Database Documentation

> Comprehensive documentation for the EDS (Electronic Data Systems) database

**Generated:** January 9, 2026

---

## Quick Links

| Document | Description | Size |
|----------|-------------|------|
| [Data Dictionary](EDS_DATA_DICTIONARY.md) | Complete table and column reference | 438 KB |
| [Stored Procedures](EDS_STORED_PROCEDURES.md) | All 395 procedures with source code | 1.3 MB |
| [Views](EDS_VIEWS.md) | All 474 views with SQL definitions | 1.8 MB |
| [ERD Diagrams](EDS_ERD.md) | Entity relationship diagrams (Mermaid) | 16 KB |
| [Business Domains](EDS_BUSINESS_DOMAINS.md) | Tables organized by functional area | 37 KB |
| [Archive Analysis](EDS_ARCHIVE_ANALYSIS.md) | Archive vs active schema comparison | 8 KB |
| [Excel Data Dictionary](EDS_DATA_DICTIONARY.xlsx) | Searchable Excel workbook | 303 KB |

---

## Database Overview

### Schema Statistics

| Metric | Count |
|--------|-------|
| **Tables** | 438 |
| **Columns** | 4,638 |
| **Stored Procedures** | 395 |
| **Views** | 474 |
| **Indexes** | 815 |
| **Foreign Keys** | 31 |

### Business Domains

The EDS database supports the following functional areas:

| Domain | Tables | Description |
|--------|--------|-------------|
| **Bidding System** | 50+ | Bid management, vendor responses, awards |
| **Orders & Purchasing** | 30+ | Purchase orders, requisitions, contracts |
| **Vendor Management** | 25+ | Vendor profiles, certifications, contacts |
| **Inventory & Items** | 20+ | Product catalog, inventory tracking |
| **Users & Security** | 15+ | Authentication, authorization, audit |
| **Finance & Budgets** | 15+ | Budget tracking, accounts, transactions |
| **Documents** | 10+ | File attachments, templates |
| **Reporting** | 10+ | Report definitions, scheduling |

See [Business Domains Guide](EDS_BUSINESS_DOMAINS.md) for detailed breakdowns.

---

## Documentation Files

### Primary References

#### [EDS_DATA_DICTIONARY.md](EDS_DATA_DICTIONARY.md)
Complete reference of all tables and columns including:
- Table properties (rows, created/modified dates)
- Column definitions (types, nullability, defaults)
- Primary keys and foreign key relationships
- Index definitions

#### [EDS_STORED_PROCEDURES.md](EDS_STORED_PROCEDURES.md)
Documentation for all 395 stored procedures:
- Parameter definitions with types
- Full source code (truncated for large procedures)
- Creation and modification dates
- Organized by schema and naming convention

#### [EDS_VIEWS.md](EDS_VIEWS.md)
Documentation for all 474 views:
- Column definitions
- SQL source code
- Table dependencies
- Organized by schema

### Visual Documentation

#### [EDS_ERD.md](EDS_ERD.md)
Entity Relationship Diagrams using Mermaid syntax:
- **Core Tables ERD** - Top 30 tables by row count
- **Bidding System ERD** - Bid-related tables
- Relationship summary (defined FKs and implied relationships)

### Analysis Documents

#### [EDS_BUSINESS_DOMAINS.md](EDS_BUSINESS_DOMAINS.md)
Tables organized by business function:
- Domain classifications with table lists
- Row counts and relationships
- Key tables highlighted per domain

#### [EDS_ARCHIVE_ANALYSIS.md](EDS_ARCHIVE_ANALYSIS.md)
Comparison of archive vs dbo schemas:
- Tables in both schemas (49 tables)
- Tables without archive (333 tables)
- Orphaned archive tables (2 tables)
- Storage recommendations

### Spreadsheet Export

#### [EDS_DATA_DICTIONARY.xlsx](EDS_DATA_DICTIONARY.xlsx)
Excel workbook with 6 sheets for easy filtering:

| Sheet | Contents |
|-------|----------|
| Tables | 438 tables with row counts |
| Columns | 4,638 columns with types |
| Indexes | 815 indexes with columns |
| StoredProcedures | 395 procedures |
| Views | 474 views |
| ForeignKeys | 31 FK relationships |

---

## SQL Server Documentation

### [EDS_EXTENDED_PROPERTIES.sql](EDS_EXTENDED_PROPERTIES.sql)
SQL script to add inline documentation to SQL Server:
- 381 table descriptions
- 1,596 column descriptions
- Uses `MS_Description` extended properties
- Appears in SSMS Object Explorer and documentation tools

**To apply:**
```sql
-- Run in SSMS connected to EDS database
-- Review script first, then execute
```

---

## API Reference

### [API_REFERENCE.md](API_REFERENCE.md)
Documentation for the Python monitoring tools:
- `db_utils` module - Database connectivity
- `config` module - Configuration management
- `logging_config` module - Structured logging

---

## Performance Analysis

Performance analysis outputs are stored in `output/performance/`:

| File | Description |
|------|-------------|
| `performance_report.txt` | Executive summary |
| `missing_indexes.csv` | Index recommendations |
| `slow_queries.csv` | High I/O queries |
| `blocking_events.csv` | Lock contention events |
| `io_latency.csv` | Disk latency metrics |

---

## Scripts Reference

Documentation generation scripts in `scripts/`:

| Script | Output |
|--------|--------|
| `generate_data_dictionary.py` | `EDS_DATA_DICTIONARY.md` |
| `generate_sproc_docs.py` | `EDS_STORED_PROCEDURES.md` |
| `generate_views_docs.py` | `EDS_VIEWS.md` |
| `generate_erd.py` | `EDS_ERD.md` |
| `analyze_business_domains.py` | `EDS_BUSINESS_DOMAINS.md` |
| `analyze_archive_schema.py` | `EDS_ARCHIVE_ANALYSIS.md` |
| `export_to_excel.py` | `EDS_DATA_DICTIONARY.xlsx` |
| `generate_extended_properties.py` | `EDS_EXTENDED_PROPERTIES.sql` |

### Regenerating Documentation

```bash
# Regenerate all documentation
python scripts/generate_data_dictionary.py -d EDS
python scripts/generate_sproc_docs.py -d EDS
python scripts/generate_views_docs.py -d EDS
python scripts/generate_erd.py -d EDS
python scripts/analyze_business_domains.py -d EDS
python scripts/analyze_archive_schema.py -d EDS
python scripts/export_to_excel.py -d EDS
python scripts/generate_extended_properties.py -d EDS
```

---

## Key Findings

### Database Health

1. **Low Referential Integrity**: Only 31 foreign keys for 438 tables
   - Many relationships are enforced by application logic
   - 219 implicit relationships detected by naming convention

2. **Missing Primary Keys**: 94 tables lack primary keys
   - Most are in the archive schema
   - Consider adding PKs for data integrity

3. **Archive Schema**: 49 tables have archived copies
   - Archive holds historical data for retention
   - 2 orphaned archive tables should be reviewed

### Performance Concerns

From performance analysis:
- 50 missing index recommendations
- 50 slow queries identified (up to 27.5B buffer reads)
- 44 blocking events detected
- 100 I/O latency issues

See `output/performance/` for detailed reports.

---

## Maintenance

### Keeping Documentation Current

Run documentation scripts after schema changes:
```bash
# Quick refresh of key docs
python scripts/generate_data_dictionary.py -d EDS
python scripts/export_to_excel.py -d EDS
```

### Adding Table Descriptions

1. Edit `TABLE_DESCRIPTIONS` dict in `generate_extended_properties.py`
2. Regenerate: `python scripts/generate_extended_properties.py -d EDS`
3. Execute SQL script in SSMS

---

*Documentation generated by SQL Server Monitoring Tools*
