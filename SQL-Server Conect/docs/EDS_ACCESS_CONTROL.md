# EDS Database - Access Control Requirements

Generated: 2026-01-15

This document defines access control requirements, role-based permissions, and security policies for the EDS database.

---

## Overview

EDS implements a multi-layered access control model combining:
- Database-level authentication
- Application-level authorization (RBAC)
- Row-level security (district/school filtering)
- Column-level restrictions (sensitive data)

---

## Database Access Model

### Authentication Tiers

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           DATABASE ACCESS LAYERS                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────────┐
│   SQL Logins     │ ─── Direct database access (DBAs, Service Accounts)
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Database Users  │ ─── Schema-level permissions
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Database Roles  │ ─── Permission grouping
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Object Perms    │ ─── Table/View/Procedure access
└──────────────────┘
```

---

## SQL Server Principals

### System Accounts

| Login | Purpose | Access Level | Monthly Hours |
|-------|---------|--------------|---------------|
| EDSIQWebUser | Primary web application | Execute stored procedures | 214+ |
| EDSAdmin | Administrative operations | db_owner | Variable |
| EDSReadOnly | Reporting/BI queries | db_datareader | Continuous |
| DPAMonitor | Performance monitoring | VIEW SERVER STATE | Continuous |
| SQLAgent | Job execution | db_owner | Scheduled |
| BackupService | Backup operations | db_backupoperator | Nightly |

### Application Connection

```
Web Application ──► Connection Pool ──► EDSIQWebUser ──► Stored Procedures
                                              │
                                              ▼
                                        No direct table access
                                        (procedure-only model)
```

---

## Database Roles

### Built-in Roles Used

| Role | Members | Purpose |
|------|---------|---------|
| db_owner | EDSAdmin, SQLAgent | Full control |
| db_datareader | EDSReadOnly, ReportUser | Read all tables/views |
| db_datawriter | (none) | Not used directly |
| db_executor | EDSIQWebUser | Execute procedures |

### Custom Roles

| Role | Purpose | Permissions |
|------|---------|-------------|
| EDS_AppExecute | Application execution | EXECUTE on all sp_FA_* procedures |
| EDS_ReportReader | Report data access | SELECT on rs_* and vw_Rpt* views |
| EDS_CatalogAdmin | Catalog management | EXECUTE on sp_Catalog* procedures |
| EDS_BidManager | Bid administration | EXECUTE on sp_Bid*, sp_Award* procedures |

---

## Schema Permissions

### Schema Access Matrix

| Schema | EDSIQWebUser | EDSAdmin | EDSReadOnly | ReportUser |
|--------|--------------|----------|-------------|------------|
| dbo | EXECUTE | ALL | SELECT | SELECT (views) |
| archive | - | ALL | SELECT | - |
| staging | - | ALL | - | - |
| audit | - | SELECT | - | - |
| EDSIQWebUser | EXECUTE | ALL | - | - |
| VMS | EXECUTE | ALL | - | - |

---

## Application-Level Authorization (RBAC)

### Role Hierarchy

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         APPLICATION ROLE HIERARCHY                           │
└─────────────────────────────────────────────────────────────────────────────┘

Level 1: ┌──────────────────┐
         │  System Admin    │ ──── All permissions, all districts
         └────────┬─────────┘
                  │
Level 2: ┌────────┴─────────┐
         │  District Admin  │ ──── All permissions within district
         └────────┬─────────┘
                  │
Level 3: ┌────────┴─────────┬───────────────────┬───────────────────┐
         │ Procurement Dir  │   Finance Dir     │   IT Admin        │
         └────────┬─────────┴─────────┬─────────┴─────────┬─────────┘
                  │                   │                   │
Level 4: ┌────────┴─────────┐ ┌───────┴───────┐ ┌────────┴────────┐
         │  Purchasing Mgr  │ │  Budget Mgr   │ │  Security Admin │
         └────────┬─────────┘ └───────┬───────┘ └─────────────────┘
                  │                   │
Level 5: ┌────────┴─────────┐ ┌───────┴───────┐
         │  Buyer           │ │  Accountant   │
         └────────┬─────────┘ └───────────────┘
                  │
Level 6: ┌────────┴─────────┐
         │  School Admin    │ ──── All permissions within school
         └────────┬─────────┘
                  │
Level 7: ┌────────┴─────────┬───────────────────┐
         │   Principal      │   Department Head │
         └────────┬─────────┴─────────┬─────────┘
                  │                   │
Level 8: ┌────────┴───────────────────┴─────────┐
         │           Requestor                   │ ──── Create requisitions
         └──────────────────────────────────────┘
                          │
Level 9: ┌────────────────┴─────────────────────┐
         │           View Only                   │ ──── Read-only access
         └──────────────────────────────────────┘
```

---

## Permission Definitions

### Core Permissions

| Permission Code | Description | Typical Roles |
|-----------------|-------------|---------------|
| REQ_CREATE | Create requisitions | Requestor+ |
| REQ_EDIT | Edit own requisitions | Requestor+ |
| REQ_DELETE | Delete requisitions | School Admin+ |
| REQ_APPROVE | Approve requisitions | Approver roles |
| REQ_VIEW_ALL | View all requisitions | School Admin+ |

### PO Permissions

| Permission Code | Description | Typical Roles |
|-----------------|-------------|---------------|
| PO_CREATE | Create purchase orders | Buyer+ |
| PO_EDIT | Edit purchase orders | Buyer+ |
| PO_CANCEL | Cancel purchase orders | Purchasing Mgr+ |
| PO_TRANSMIT | Transmit POs to vendors | Buyer+ |
| PO_VIEW_ALL | View all POs | Purchasing Mgr+ |

### Bid Permissions

| Permission Code | Description | Typical Roles |
|-----------------|-------------|---------------|
| BID_CREATE | Create bids | Bid Manager |
| BID_EDIT | Edit bids | Bid Manager |
| BID_AWARD | Award bids | Procurement Dir |
| BID_VIEW | View bid results | Bid Manager+ |
| BID_IMPORT | Import bid responses | Bid Manager |

### Vendor Permissions

| Permission Code | Description | Typical Roles |
|-----------------|-------------|---------------|
| VENDOR_CREATE | Create vendors | Vendor Relations |
| VENDOR_EDIT | Edit vendors | Vendor Relations |
| VENDOR_APPROVE | Approve vendors | Procurement Dir |
| VENDOR_SUSPEND | Suspend vendors | Procurement Dir |
| VENDOR_VIEW | View vendor info | Buyer+ |

### Budget Permissions

| Permission Code | Description | Typical Roles |
|-----------------|-------------|---------------|
| BUDGET_VIEW | View budget balances | Requestor+ |
| BUDGET_EDIT | Edit budgets | Finance Dir |
| BUDGET_TRANSFER | Transfer funds | Finance Dir |
| ACCOUNT_CREATE | Create accounts | Finance Dir |
| ACCOUNT_EDIT | Edit accounts | Finance Dir |

### Admin Permissions

| Permission Code | Description | Typical Roles |
|-----------------|-------------|---------------|
| USER_CREATE | Create users | IT Admin |
| USER_EDIT | Edit users | IT Admin |
| USER_DELETE | Delete users | IT Admin |
| ROLE_ASSIGN | Assign roles | IT Admin |
| SYSTEM_CONFIG | System configuration | System Admin |

---

## Row-Level Security

### District Filtering

All user queries are filtered by district context:

```sql
-- Example: Requisition access filtered by user's district
SELECT r.*
FROM Requisitions r
INNER JOIN UserSchools us ON r.SchoolId = us.SchoolId
WHERE us.UserId = @CurrentUserId
  AND r.Active = 1
```

### School Filtering

School-level users see only their assigned schools:

```sql
-- Example: School-restricted access
SELECT r.*
FROM Requisitions r
WHERE r.SchoolId IN (
    SELECT SchoolId
    FROM UserSchools
    WHERE UserId = @CurrentUserId
)
```

### Approval Chain Visibility

Approvers see only requisitions in their approval scope:

```sql
-- Example: Approval queue
SELECT r.*
FROM Requisitions r
INNER JOIN Approvals a ON r.RequisitionId = a.RequisitionId
WHERE a.ApproverId = @CurrentUserId
  AND a.Status = 'P'  -- Pending
```

---

## Sensitive Data Controls

### Column-Level Restrictions

| Table | Column | Sensitivity | Access |
|-------|--------|-------------|--------|
| Users | PasswordHash | Critical | System only |
| Users | SSN | PII | HR Admin only |
| Vendors | TaxId | Sensitive | Finance only |
| Vendors | BankAccount | Critical | Finance Dir only |
| VendorContacts | Email | PII | Vendor Relations+ |
| VendorContacts | Phone | PII | Vendor Relations+ |

### Data Masking

| Table.Column | Masking Rule | Shown To |
|--------------|--------------|----------|
| Vendors.TaxId | XXX-XX-#### | Finance |
| Vendors.BankAccount | ****####  | Finance Dir |
| Users.Email | a***@domain | Non-admins |

---

## Session Management

### Session Controls

| Control | Setting | Purpose |
|---------|---------|---------|
| Session Timeout | 30 minutes | Inactivity logout |
| Concurrent Sessions | 3 max | Prevent sharing |
| Session Binding | IP + User Agent | Hijack prevention |
| Token Refresh | 5 minutes | Token rotation |

### Session Table

```sql
-- SessionTable stores active sessions
SessionId        INT PK
UserId           INT FK → Users
Token            VARCHAR(256)  -- Encrypted
IPAddress        VARCHAR(45)
UserAgent        VARCHAR(256)
Created          DATETIME
LastActivity     DATETIME
ExpiresAt        DATETIME
```

---

## Audit Requirements

### Audited Actions

| Category | Actions Logged |
|----------|----------------|
| Authentication | Login, Logout, Failed attempts |
| Authorization | Permission grants, Role changes |
| Data Access | Sensitive data views |
| Data Changes | Create, Update, Delete on key tables |
| Admin Actions | User management, Config changes |

### Audit Tables

| Table | Purpose |
|-------|---------|
| AuditLog | General audit trail |
| LoginAttempts | Authentication history |
| ChangeLog | Data modification history |
| AdminActions | Administrative activities |

### Audit Retention

| Audit Type | Retention | Archive |
|------------|-----------|---------|
| Login history | 2 years | Archive schema |
| Data changes | 7 years | Offsite backup |
| Admin actions | 7 years | Offsite backup |
| Access logs | 1 year | Delete |

---

## Access Request Process

### New User Access

```
1. Manager Request ─────► HR Approval
                              │
                              ▼
2. IT Creates Account ──► Role Assignment
                              │
                              ▼
3. School Assignment ───► Budget Account Assignment
                              │
                              ▼
4. User Training ───────► Access Enabled
```

### Role Change Request

```
1. User/Manager Request ─────► Data Owner Approval
                                     │
                                     ▼
2. IT Reviews ──────────────► Security Review (if elevated)
                                     │
                                     ▼
3. Role Updated ────────────► Audit Logged
```

### Access Removal

```
1. Termination Notice ─────► HR Notification
                                  │
                                  ▼
2. IT Disables Account ────► Session Terminated
                                  │
                                  ▼
3. Access Revoked ─────────► Audit Logged
```

---

## Periodic Access Review

### Review Schedule

| Review Type | Frequency | Reviewer |
|-------------|-----------|----------|
| User access | Quarterly | Manager |
| Role assignments | Quarterly | Data Owner |
| Privileged access | Monthly | Security Officer |
| Service accounts | Semi-annual | IT Director |
| Vendor access | Annual | Procurement Dir |

### Review Checklist

- [ ] Verify active status matches HR records
- [ ] Confirm role appropriateness for job function
- [ ] Check for segregation of duties violations
- [ ] Review privileged access justification
- [ ] Validate school/district assignments
- [ ] Remove unnecessary permissions

---

## Compliance Requirements

### Regulatory Mapping

| Regulation | Requirement | EDS Control |
|------------|-------------|-------------|
| FERPA | Student data protection | District/school filtering |
| PCI-DSS | Payment data security | Column-level encryption |
| SOX | Financial controls | Segregation of duties |
| State Procurement | Bid transparency | Audit trail |

### Segregation of Duties

| Conflicting Permissions | Control |
|-------------------------|---------|
| REQ_CREATE + REQ_APPROVE | Different users required |
| VENDOR_CREATE + BID_AWARD | Different users required |
| BUDGET_EDIT + PO_CREATE | Different users required |
| USER_CREATE + ROLE_ASSIGN | Dual approval required |

---

## Emergency Access

### Break-Glass Procedure

1. Emergency declared by IT Director or above
2. Break-glass account activated (pre-configured)
3. All actions logged with enhanced detail
4. Access reviewed within 24 hours
5. Formal incident report required

### Emergency Accounts

| Account | Purpose | Activation |
|---------|---------|------------|
| EDS_Emergency_Admin | Full admin access | IT Director approval |
| EDS_Emergency_Finance | Financial access | Finance Dir approval |
| EDS_Emergency_Proc | Procurement access | Procurement Dir approval |

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-01-15 | Initial access control documentation | Phase 4 Documentation |

