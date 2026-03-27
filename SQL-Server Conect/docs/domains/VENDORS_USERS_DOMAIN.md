# EDS Database - Vendors & Users Domain

Generated: 2026-01-15

This document provides comprehensive documentation for all tables in the Vendors, Users, and Organization domain, which manages vendor relationships, user accounts, districts, schools, and security.

**Total Tables:** 51 | **Total Rows:** ~24 million

---

## Table of Contents

1. [Domain Overview](#domain-overview)
2. [Vendor Tables](#vendor-tables)
3. [User & Security Tables](#user--security-tables)
4. [Organization Tables](#organization-tables)
5. [Vendor Query Tables](#vendor-query-tables)
6. [Session & Activity Tables](#session--activity-tables)

---

## Domain Overview

This domain manages three interconnected areas:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ORGANIZATION & ACCESS HIERARCHY                           │
└─────────────────────────────────────────────────────────────────────────────┘

                         ┌──────────────┐
                         │   District   │
                         └──────────────┘
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
    ┌──────────┐         ┌──────────┐         ┌──────────┐
    │  School  │         │  Users   │         │ District │
    │          │         │          │         │ Vendor   │
    └──────────┘         └──────────┘         └──────────┘
          │                    │                    │
          │              ┌─────┴─────┐              │
          │              ▼           ▼              │
          │        ┌──────────┐ ┌──────────┐        │
          │        │ Security │ │  User    │        │
          │        │  Roles   │ │ Accounts │        │
          │        └──────────┘ └──────────┘        │
          │                                         │
          └─────────────────────────────────────────┘
                               │
                         ┌─────┴─────┐
                         ▼           ▼
                   ┌──────────┐ ┌──────────┐
                   │ Vendors  │ │ Sessions │
                   └──────────┘ └──────────┘
```

### Key Business Processes

| Process | Tables Involved | Description |
|---------|-----------------|-------------|
| Vendor Registration | Vendors, VendorContacts | Onboard new vendors |
| Vendor Qualification | DistrictVendor, VendorCategory | Approve for districts |
| User Management | Users, UserAccounts, SecurityRoleUsers | Create and manage users |
| Access Control | SecurityRoles, SecurityRoleKeys | Define permissions |
| Session Tracking | SessionTable, VendorSessions | Monitor active sessions |
| Vendor Communications | VendorQuery, VendorQueryStatus | Track vendor interactions |

---

## Vendor Tables

### Vendors

**Rows:** ~18,916 | **Purpose:** Master vendor/supplier records

The central vendor registry containing all suppliers in the system.

| Column | Type | Description |
|--------|------|-------------|
| VendorId | int PK | Unique vendor ID |
| Code | varchar | Short vendor code |
| Name | varchar | Company name |
| Address1-3 | varchar | Street address |
| City, State, ZipCode | varchar | Location |
| Phone, Fax | varchar | Contact numbers |
| EMail | varchar | Primary email |
| Active | tinyint | 1=Active vendor |
| UseGrossPrices | tinyint | Pricing method |
| ShippingPercentage | decimal | Default shipping % |
| AllowElectronicPOs | int | Can receive e-POs |

**cXML Integration Columns:**
| Column | Purpose |
|--------|---------|
| cXMLAddress | cXML endpoint URL |
| cXMLFromDomain | Sender domain |
| cXMLFromIdentity | Sender identity |
| cXMLToDomain | Recipient domain |
| cXMLToIdentity | Recipient identity |
| cXMLSenderSharedSecret | Auth secret (encrypted) |

**Relationships:**
- Child: VendorContacts, VendorCategory, VendorUploads, DistrictVendor
- Referenced by: Catalog, CrossRefs, Awards, BidResults, PO

---

### VendorContacts

**Rows:** ~23,307 | **Purpose:** Vendor contact persons

Individual contacts at vendor companies.

| Column | Type | Description |
|--------|------|-------------|
| VendorContactId | int PK | Unique contact ID |
| VendorId | int FK | Parent vendor |
| Name | varchar | Contact name |
| Title | varchar | Job title |
| Email | varchar | Email address |
| Phone | varchar | Phone number |
| IsPrimary | bit | Primary contact? |

---

### VendorCategory

**Rows:** ~6,798 | **Purpose:** Vendor product categories

What categories each vendor can supply.

| Column | Type | Description |
|--------|------|-------------|
| VCId | int PK | Unique ID |
| VendorId | int FK | Vendor |
| CategoryId | int FK | Category |
| Active | tinyint | Currently approved |

---

### VendorCategoryPP

**Rows:** ~17,681 | **Purpose:** Vendor category with pricing

Extended category assignments with pricing plans.

---

### DistrictVendor

**Rows:** ~315,736 | **Purpose:** District-vendor relationships

Links vendors to districts they can supply.

| Column | Type | Description |
|--------|------|-------------|
| DistrictVendorId | int PK | Unique ID |
| DistrictId | int FK | District |
| VendorId | int FK | Vendor |
| Active | tinyint | Currently approved |
| ApprovedDate | datetime | When approved |

---

### VendorUploads

**Rows:** ~1,533,361 | **Purpose:** Catalog upload tracking

Tracks vendor catalog/price uploads.

| Column | Type | Description |
|--------|------|-------------|
| UploadId | int PK | Unique upload ID |
| VendorId | int FK | Uploading vendor |
| UploadDate | datetime | When uploaded |
| FileName | varchar | Source file |
| Status | varchar | Upload status |
| RecordsProcessed | int | Items processed |

---

### VendorOrders

**Rows:** ~5,506 | **Purpose:** Vendor order tracking

Tracks orders sent to vendors.

---

### VendorSessions

**Rows:** ~10,794 | **Purpose:** Vendor portal sessions

Tracks vendor portal login sessions.

---

### VendorDeliveryRule

**Rows:** 1 | **Purpose:** Delivery rule configuration

Default delivery rules for vendors.

---

### VendorOverrideMessages

**Rows:** 5 | **Purpose:** Override message templates

System messages for vendor overrides.

---

### VendorCatalogNote

**Rows:** 11 | **Purpose:** Catalog notes

Notes attached to vendor catalogs.

---

### VendorDocRequest / VendorDocRequestDetail / VendorDocRequestStatus

**Rows:** 14 / 52 / 14 | **Purpose:** Document request workflow

Manages requests for vendor documentation.

---

## User & Security Tables

### Users

**Rows:** ~338,577 | **Purpose:** User accounts

All system users - district staff, school staff, EDS staff.

| Column | Type | Description |
|--------|------|-------------|
| UserId | int PK | Unique user ID |
| UserName | varchar | Login username |
| Email | varchar | Email address |
| FirstName, LastName | varchar | User name |
| SchoolId | int FK | Primary school |
| DistrictId | int FK | Primary district |
| ApprovalLevel | tinyint | Approval authority |
| Active | tinyint | 1=Active account |
| LastLogin | datetime | Last login time |
| Password | varbinary | Password hash |

**Relationships:**
- References: School, District
- Child: UserAccounts, SecurityRoleUsers, Requisitions, Approvals

---

### UserAccounts

**Rows:** ~6,036,974 | **Purpose:** User-to-budget account links

Links users to budget accounts they can charge to.

| Column | Type | Description |
|--------|------|-------------|
| UserAccountId | int PK | Unique ID |
| UserId | int FK | User |
| BudgetAccountId | int FK | Budget account |
| Active | tinyint | Currently authorized |

**Note:** This is a many-to-many relationship - users can have multiple accounts.

---

### SecurityRoles

**Rows:** 5 | **Purpose:** Role definitions

System security roles.

| SecurityRoleId | Name | Description |
|----------------|------|-------------|
| 1 | User | Basic user access |
| 2 | Approver | Can approve orders |
| 3 | Administrator | District admin |
| 4 | EDS Staff | EDS support |
| 5 | System Admin | Full access |

---

### SecurityRoleUsers

**Rows:** ~355,707 | **Purpose:** User role assignments

Links users to their security roles.

| Column | Type | Description |
|--------|------|-------------|
| SecurityRoleUserId | int PK | Unique ID |
| UserId | int FK | User |
| SecurityRoleId | int FK | Role |
| DistrictId | int FK | Scope (district) |

---

### SecurityRoleKeys

**Rows:** 65 | **Purpose:** Role permission keys

Specific permissions granted to roles.

---

### SecurityKeys

**Rows:** 14 | **Purpose:** Permission key definitions

Available permission keys.

---

### UserTrees

**Rows:** ~56,920 | **Purpose:** User hierarchy

Approval chain relationships.

---

### UserImports

**Rows:** ~328 | **Purpose:** User import tracking

Batch user import records.

---

### UserAdminLog

**Rows:** ~6,466 | **Purpose:** User admin activity

Audit log for user administration.

---

## Organization Tables

### District

**Rows:** ~969 | **Purpose:** School district records

School districts - the primary customer entity.

| Column | Type | Description |
|--------|------|-------------|
| DistrictId | int PK | Unique district ID |
| DistrictCode | varchar | Short code |
| Name | varchar | District name |
| Address1-2 | varchar | Address |
| City, State, ZipCode | varchar | Location |
| Phone, Fax | varchar | Contact |
| DistrictTypeId | int FK | District type |
| Active | tinyint | 1=Active customer |
| ContractDate | datetime | Contract start |
| ExpirationDate | datetime | Contract end |

**District Types:**
| TypeId | Description |
|--------|-------------|
| 1 | Booklet Only |
| 2 | Online Only |
| 3 | Booklet & Online |
| 4 | Online without Prior Year Reqs |
| 5 | Verify SBS Online |
| 6 | T&M Only |

---

### DistrictTypes

**Rows:** 6 | **Purpose:** District type definitions

(See table above)

---

### School

**Rows:** ~6,582 | **Purpose:** Individual schools

Schools, offices, and departments within districts.

| Column | Type | Description |
|--------|------|-------------|
| SchoolId | int PK | Unique school ID |
| DistrictId | int FK | Parent district |
| SchoolCode | varchar | School code |
| Name | varchar | School name |
| Address1-2 | varchar | Shipping address |
| City, State, ZipCode | varchar | Location |
| Active | tinyint | 1=Active |

---

### DistrictCategories

**Rows:** ~125,243 | **Purpose:** District category permissions

What categories each district can order from.

---

### DistrictContacts

**Rows:** ~3,818 | **Purpose:** District contact persons

Key contacts at each district.

| Column | Type | Description |
|--------|------|-------------|
| DistrictContactId | int PK | Unique ID |
| DistrictId | int FK | District |
| DistrictContactTypeId | int FK | Contact type |
| Name | varchar | Contact name |
| Email | varchar | Email |
| Phone | varchar | Phone |

**Contact Types:**
| TypeId | Description |
|--------|-------------|
| 1 | Business Administrator |
| 2 | Primary Contact |
| 3 | Athletic Director |
| 4 | Buildings and Grounds |
| 5 | Accounts Payable |
| 6 | RTK Contact |
| 8 | Additional Renewal Contact |

---

### DistrictContactTypes

**Rows:** 7 | **Purpose:** Contact type definitions

(See table above)

---

### DistrictCharges

**Rows:** ~22,477 | **Purpose:** District billing

Charges billed to districts.

---

### DistrictContinuances

**Rows:** ~14,436 | **Purpose:** Contract renewals

Tracks district contract continuances.

---

### DistrictProposedCharges

**Rows:** ~11,997 | **Purpose:** Pending charges

Proposed charges awaiting approval.

---

### DistrictNotifications

**Rows:** ~6,046 | **Purpose:** District notification settings

Notification preferences per district.

---

### DistrictNotes

**Rows:** 75 | **Purpose:** District notes

Notes attached to districts.

---

### DistrictReports

**Rows:** 11 | **Purpose:** District report config

Report configurations per district.

---

### DistrictPP

**Rows:** ~9,243 | **Purpose:** District pricing plans

Pricing plan assignments.

---

## Vendor Query Tables

### VendorQuery

**Rows:** ~15,610 | **Purpose:** Vendor inquiry tracking

Tracks communications/inquiries with vendors.

| Column | Type | Description |
|--------|------|-------------|
| VendorQueryId | int PK | Unique query ID |
| VendorId | int FK | Vendor |
| QueryType | varchar | Type of inquiry |
| QueryDate | datetime | When initiated |
| Status | varchar | Current status |

---

### VendorQueryDetail

**Rows:** ~169,433 | **Purpose:** Query line items

Details within vendor queries.

---

### VendorQueryStatus

**Rows:** ~30,222 | **Purpose:** Query status history

Status changes for vendor queries.

**Common Statuses Used:**

| StatusId | Name | Count |
|----------|------|-------|
| 1 | On Hold | 15,640 |
| 5 | At EDS | 7,589 |
| 4 | Rejected | 5,826 |
| 2 | Pending Approval | 905 |
| 3 | Approved | 172 |

---

### VendorQueryTandM / VendorQueryTandMDetail / VendorQueryTandMStatus

**Rows:** ~1,896 / ~1,142 / ~1,757 | **Purpose:** Time & Materials queries

T&M-specific vendor queries.

---

### VendorQueryMSRP / VendorQueryMSRPDetail / VendorQueryMSRPStatus

**Rows:** ~140 / ~2 / ~2 | **Purpose:** MSRP queries

MSRP-related vendor queries.

---

## Session & Activity Tables

### SessionTable

**Rows:** ~12,409,546 | **Purpose:** User session tracking

Tracks all user login sessions.

| Column | Type | Description |
|--------|------|-------------|
| SessionId | int PK | Unique session ID |
| UserId | int FK | User |
| LoginTime | datetime | Session start |
| LogoutTime | datetime | Session end |
| IPAddress | varchar | Client IP |
| UserAgent | varchar | Browser info |

**Note:** This is the largest table in this domain - consider archiving old sessions.

---

## Entity Relationship Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      VENDORS & USERS RELATIONSHIPS                           │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────┐          ┌──────────┐          ┌──────────┐
│ District │◄─────────│  School  │◄─────────│  Users   │
└──────────┘          └──────────┘          └──────────┘
     │                                            │
     ├───────────────────────────────────────────┤
     │                                            │
     ▼                                            ▼
┌──────────┐          ┌──────────┐          ┌──────────┐
│ District │          │ District │          │  User    │
│ Vendor   │          │Categories│          │ Accounts │
└──────────┘          └──────────┘          └──────────┘
     │                                            │
     ▼                                            ▼
┌──────────┐          ┌──────────┐          ┌──────────┐
│ Vendors  │◄─────────│ Vendor   │          │ Security │
│          │          │ Query    │          │RoleUsers │
└──────────┘          └──────────┘          └──────────┘
     │                      │                     │
     ▼                      ▼                     ▼
┌──────────┐          ┌──────────┐          ┌──────────┐
│ Vendor   │          │  Query   │          │ Security │
│ Contacts │          │  Status  │          │  Roles   │
└──────────┘          └──────────┘          └──────────┘
```

---

## Common Queries

### Get users for a district with roles
```sql
SELECT u.UserId, u.UserName, u.Email,
       s.Name AS SchoolName, sr.Name AS Role
FROM Users u
JOIN School s ON u.SchoolId = s.SchoolId
LEFT JOIN SecurityRoleUsers sru ON u.UserId = sru.UserId
LEFT JOIN SecurityRoles sr ON sru.SecurityRoleId = sr.SecurityRoleId
WHERE s.DistrictId = @DistrictId
  AND u.Active = 1;
```

### Get approved vendors for a district
```sql
SELECT v.VendorId, v.Code, v.Name,
       dv.ApprovedDate
FROM Vendors v
JOIN DistrictVendor dv ON v.VendorId = dv.VendorId
WHERE dv.DistrictId = @DistrictId
  AND dv.Active = 1
  AND v.Active = 1
ORDER BY v.Name;
```

### User's budget accounts
```sql
SELECT ba.AccountCode, ba.Description,
       ba.BudgetAmount, ba.AmountAvailable
FROM UserAccounts ua
JOIN BudgetAccounts ba ON ua.BudgetAccountId = ba.BudgetAccountId
WHERE ua.UserId = @UserId
  AND ua.Active = 1;
```

---

## Security Model

```
User authenticates
        │
        ▼
SessionTable record created
        │
        ▼
SecurityRoleUsers checked
        │
        ├── Role: User ──────► Basic ordering
        │
        ├── Role: Approver ──► Can approve requisitions
        │
        ├── Role: Admin ─────► District administration
        │
        └── Role: SysAdmin ──► Full system access

        │
        ▼
SecurityRoleKeys checked for specific permissions
```

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-01-15 | Initial Vendors/Users domain documentation | Phase 2 Documentation |
