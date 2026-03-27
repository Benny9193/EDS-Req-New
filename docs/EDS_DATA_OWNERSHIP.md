# EDS Database - Data Ownership & Stewardship Guide

Generated: 2026-01-15

This document defines data ownership responsibilities, stewardship roles, and governance policies for the EDS database.

---

## Overview

The EDS database contains ~540 million rows across 438 tables, supporting purchasing operations for educational institutions. Clear data ownership ensures accountability, data quality, and compliance.

---

## Ownership Model

### RACI Matrix

| Role | Description |
|------|-------------|
| **R** - Responsible | Creates/modifies data |
| **A** - Accountable | Owns data quality and decisions |
| **C** - Consulted | Provides input on data standards |
| **I** - Informed | Needs visibility into data |

---

## Domain Ownership

### 1. Bidding Domain (~506M rows)

**Data Steward:** Purchasing/Procurement Director

| Table Group | Responsible | Accountable | Consulted | Informed |
|-------------|-------------|-------------|-----------|----------|
| BidHeaders | Bid Manager | Procurement Dir | Legal | Vendors |
| BidResults | Vendors | Bid Manager | Finance | Schools |
| Awards | Bid Manager | Procurement Dir | Board | All Users |
| BidRequestItems | Schools | Bid Manager | Category Mgr | Vendors |

**Key Decisions:**
- Bid award criteria
- Vendor qualification standards
- Pricing policies
- Contract terms

**Data Quality Metrics:**
- Award completion rate
- Bid response time
- Price variance tracking

---

### 2. Orders & Purchasing Domain (~395M rows)

**Data Steward:** Purchasing Manager

| Table Group | Responsible | Accountable | Consulted | Informed |
|-------------|-------------|-------------|-----------|----------|
| Requisitions | End Users | School Admin | Budget Mgr | Approvers |
| Detail | End Users | School Admin | Buyers | Finance |
| PO | Buyers | Purchasing Mgr | Vendors | Finance |
| Approvals | Approvers | Approval Admin | IT | End Users |

**Key Decisions:**
- Approval routing
- Purchase limits
- Vendor selection
- Budget allocation

**Data Quality Metrics:**
- Requisition-to-PO cycle time
- Approval turnaround
- Order accuracy rate

---

### 3. Vendors Domain (~24M rows)

**Data Steward:** Vendor Relations Manager

| Table Group | Responsible | Accountable | Consulted | Informed |
|-------------|-------------|-------------|-----------|----------|
| Vendors | Vendor Relations | Procurement Dir | Legal | Buyers |
| VendorContacts | Vendor Relations | Vendor Mgr | IT | Buyers |
| VendorDocuments | Vendors | Vendor Mgr | Compliance | Buyers |
| VendorAwards | Bid Manager | Procurement Dir | Finance | Vendors |

**Key Decisions:**
- Vendor approval/suspension
- Document requirements
- Performance ratings
- Diversity tracking

**Data Quality Metrics:**
- Active vendor count
- Document compliance rate
- Contact accuracy

---

### 4. Inventory & Catalog Domain (~199M rows)

**Data Steward:** Catalog Manager

| Table Group | Responsible | Accountable | Consulted | Informed |
|-------------|-------------|-------------|-----------|----------|
| Items | Catalog Team | Catalog Mgr | Category Mgr | Users |
| CrossRefs | Catalog Team | Catalog Mgr | Vendors | Buyers |
| Catalog | Vendors | Catalog Mgr | IT | Users |
| Category | Category Mgr | Procurement Dir | IT | All |

**Key Decisions:**
- Item standardization
- Category structure
- Pricing updates
- Catalog refresh cycles

**Data Quality Metrics:**
- Item accuracy rate
- Price currency
- Cross-reference coverage

---

### 5. Users & Security Domain (~28K users)

**Data Steward:** IT Administrator / Security Officer

| Table Group | Responsible | Accountable | Consulted | Informed |
|-------------|-------------|-------------|-----------|----------|
| Users | IT Admin | Security Officer | HR | Managers |
| Roles | Security Officer | IT Director | Business | Users |
| Permissions | Security Officer | IT Director | Business | Auditors |
| Sessions | System | IT Admin | Security | - |

**Key Decisions:**
- Access provisioning
- Role definitions
- Password policies
- SSO configuration

**Data Quality Metrics:**
- Inactive account rate
- Permission accuracy
- Login success rate

---

### 6. Finance & Budget Domain (~1.5M rows)

**Data Steward:** Finance Director

| Table Group | Responsible | Accountable | Consulted | Informed |
|-------------|-------------|-------------|-----------|----------|
| Budgets | Finance Team | Finance Dir | District Admin | Schools |
| BudgetAccounts | Finance Team | Finance Dir | School Admin | Users |
| Accounts | Finance Team | Finance Dir | IT | Auditors |

**Key Decisions:**
- Budget allocations
- Account structure
- Fiscal year setup
- Encumbrance rules

**Data Quality Metrics:**
- Budget accuracy
- Encumbrance tracking
- Year-end reconciliation

---

### 7. Districts & Schools Domain (~16K records)

**Data Steward:** District Administrator

| Table Group | Responsible | Accountable | Consulted | Informed |
|-------------|-------------|-------------|-----------|----------|
| District | EDS Admin | District Admin | IT | All |
| School | District Admin | District Admin | Principals | Users |
| DistrictSettings | IT Admin | District Admin | EDS Support | - |

**Key Decisions:**
- District configuration
- School setup
- Approval hierarchies
- Shipping locations

**Data Quality Metrics:**
- Active school count
- Configuration completeness
- Address accuracy

---

### 8. Reporting Domain (~57M rows)

**Data Steward:** BI/Analytics Lead

| Table Group | Responsible | Accountable | Consulted | Informed |
|-------------|-------------|-------------|-----------|----------|
| ReportSession | System | IT Admin | Users | - |
| ReportSessionLinks | System | IT Admin | - | - |
| ReportDefinitions | BI Team | BI Lead | Business | Users |

**Key Decisions:**
- Report design
- Data retention
- Access controls
- Performance optimization

**Data Quality Metrics:**
- Report generation time
- Session cleanup rate
- Storage utilization

---

## Cross-Domain Ownership

### Shared Reference Tables

| Table | Primary Owner | Secondary Owner | Usage |
|-------|---------------|-----------------|-------|
| StatusTable | IT Admin | Business Analyst | All domains |
| Units | Catalog Mgr | Procurement | Orders, Catalog |
| ChargeTypes | Finance Dir | IT Admin | Billing |
| States | IT Admin | - | Addresses |

### Integration Touchpoints

| Integration | Data Source | Data Target | Owner |
|-------------|-------------|-------------|-------|
| SSO Sync | Identity Provider | Users | IT Admin |
| Catalog Import | Vendors | Items, CrossRefs | Catalog Mgr |
| GL Export | EDS | Financial System | Finance Dir |
| Bid Import | Vendors | BidResults | Bid Manager |

---

## Data Quality Responsibilities

### By Role

| Role | Responsibilities |
|------|------------------|
| **Data Steward** | Define standards, approve changes, resolve issues |
| **Data Owner** | Approve access, fund initiatives, escalate issues |
| **Data Custodian** | Implement controls, maintain systems, run jobs |
| **Data User** | Report issues, follow standards, validate entries |

### Quality Dimensions

| Dimension | Definition | Owner |
|-----------|------------|-------|
| **Accuracy** | Data correctly represents reality | Data Steward |
| **Completeness** | Required fields populated | Data Steward |
| **Consistency** | Same data in different places matches | IT Admin |
| **Timeliness** | Data available when needed | Data Custodian |
| **Validity** | Data conforms to format/range rules | Data Steward |
| **Uniqueness** | No unintended duplicates | Data Custodian |

---

## Governance Processes

### Data Change Management

```
Change Request
    ├── Impact Analysis (Data Steward)
    ├── Technical Review (IT Admin)
    ├── Approval (Data Owner)
    ├── Implementation (Data Custodian)
    └── Validation (Data Steward)
```

### Issue Resolution

| Severity | Response Time | Escalation Path |
|----------|---------------|-----------------|
| Critical | 1 hour | Steward → Owner → Director |
| High | 4 hours | Steward → Owner |
| Medium | 24 hours | Custodian → Steward |
| Low | 72 hours | Custodian |

### Access Request Process

```
User Request
    ├── Manager Approval
    ├── Data Owner Approval (if sensitive)
    ├── IT Implementation
    └── Periodic Review (Quarterly)
```

---

## Compliance & Audit

### Regulatory Requirements

| Regulation | Applicable Data | Owner |
|------------|-----------------|-------|
| FERPA | Student-related data | District Admin |
| PCI-DSS | Payment data | Finance Dir |
| State Procurement | Bid/Contract data | Procurement Dir |
| Records Retention | All operational data | Legal/Compliance |

### Audit Controls

| Control | Frequency | Owner |
|---------|-----------|-------|
| Access Review | Quarterly | Security Officer |
| Data Quality Audit | Monthly | Data Steward |
| Compliance Audit | Annual | Compliance |
| Penetration Test | Annual | IT Security |

---

## Contact Directory

| Domain | Steward Role | Contact Method |
|--------|--------------|----------------|
| Bidding | Procurement Director | procurement@district.edu |
| Orders | Purchasing Manager | purchasing@district.edu |
| Vendors | Vendor Relations | vendors@district.edu |
| Catalog | Catalog Manager | catalog@district.edu |
| Users/Security | IT Administrator | itadmin@district.edu |
| Finance | Finance Director | finance@district.edu |
| Districts | District Admin | admin@district.edu |
| Reporting | BI Lead | analytics@district.edu |

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-01-15 | Initial data ownership guide | Phase 4 Documentation |

