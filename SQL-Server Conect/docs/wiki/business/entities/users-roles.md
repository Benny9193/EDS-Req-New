# Users & Roles

[Home](../../index.md) > [Business](../index.md) > [Entities](index.md) > Users & Roles

---

## Overview

Users are individuals who interact with the EDS system. Each user has roles that determine their permissions and capabilities within the procurement workflow.

---

## User Types

### By Function

| Type | Description | Typical Role |
|------|-------------|--------------|
| Requestor | Creates purchase requisitions | Teacher, Staff |
| Approver | Reviews and approves requests | Principal, Director |
| Buyer | Processes POs and vendor orders | Purchasing Agent |
| Receiver | Confirms receipt of goods | Warehouse Staff |
| Finance | Manages budgets and payments | Accountant |
| Admin | System configuration | IT, Super User |

### By Access Level

| Level | Access |
|-------|--------|
| District Admin | Full system access |
| School Admin | Full access to assigned schools |
| Department Head | Approve for department |
| Standard User | Create and view own requests |
| View Only | Read-only access |

---

## Key Tables

### Users Table

| Field | Description |
|-------|-------------|
| UserId | Primary key |
| Email | Login identifier (unique) |
| FirstName, LastName | Display name |
| DistrictId | Primary district |
| Active | Account status |
| SSOID | Single Sign-On identifier |
| SSOProvider | SSO provider name |
| LastLogin | Last activity timestamp |

### UserRoles Table

| Field | Description |
|-------|-------------|
| UserRoleId | Primary key |
| UserId | User reference |
| RoleId | Role reference |
| SchoolId | Scope (null = all schools) |

### UserSchools Table

| Field | Description |
|-------|-------------|
| UserId | User reference |
| SchoolId | School assignment |
| IsPrimary | Default school flag |

---

## Role Hierarchy

```
District Administrator
    │
    ├── Purchasing Director
    │       │
    │       └── Buyer
    │
    ├── Finance Director
    │       │
    │       └── Accountant
    │
    └── School Administrator (per school)
            │
            ├── Department Head
            │
            └── Requestor
```

---

## Application Users (System Accounts)

EDS uses several system accounts for application connectivity:

| Account | Purpose | Monthly Usage |
|---------|---------|---------------|
| EDSIQWebUser | Primary web application | 214+ hours |
| EDSAdmin | Administrative tasks | Variable |
| DPA Monitoring | Performance monitoring | Continuous |

**Note:** `EDSIQWebUser` is the main application account and represents all web traffic.

---

## Authentication

### SSO Integration
- SAML-based Single Sign-On
- Syncs user attributes from IdP
- Automatic provisioning/deprovisioning

### Known Issue: SSO Deadlocks
Parallel SSO updates can cause deadlocks. See [KI-005: SSO Deadlocks](../../performance/known-issues/sso-deadlocks.md).

```sql
-- SSO Update Pattern (causes deadlocks)
UPDATE dbo.Users
SET SSOID = @P0, SSOProvider = @P1
WHERE Email = @P2 AND Active = 1
```

---

## Permission Model

### Action-Based Permissions

| Permission | Description |
|------------|-------------|
| CREATE_REQUISITION | Can create new requests |
| APPROVE_REQUISITION | Can approve requests |
| CREATE_PO | Can generate purchase orders |
| RECEIVE_GOODS | Can mark items received |
| MANAGE_VENDORS | Can add/edit vendors |
| MANAGE_BUDGETS | Can modify account codes |
| ADMIN_USERS | Can manage user accounts |

### Scope-Based Permissions

| Scope | Access Level |
|-------|-------------|
| Own | User's own records only |
| School | All records for assigned schools |
| Department | Records for user's department |
| District | All district records |

---

## Common Queries

### Find User by Email
```sql
SELECT UserId, FirstName, LastName, Email, Active, LastLogin
FROM Users
WHERE Email = @Email
```

### Get User Roles
```sql
SELECT r.RoleName, ur.SchoolId, s.SchoolName
FROM UserRoles ur
JOIN Roles r ON ur.RoleId = r.RoleId
LEFT JOIN Schools s ON ur.SchoolId = s.SchoolId
WHERE ur.UserId = @UserId
```

### Active Users by School
```sql
SELECT s.SchoolName, COUNT(DISTINCT us.UserId) as ActiveUsers
FROM Schools s
JOIN UserSchools us ON s.SchoolId = us.SchoolId
JOIN Users u ON us.UserId = u.UserId
WHERE u.Active = 1
GROUP BY s.SchoolId, s.SchoolName
ORDER BY ActiveUsers DESC
```

---

## User Activity Monitoring

### Peak Usage Hours
- **Morning:** 8:00 AM - 10:00 AM
- **Afternoon:** 1:00 PM - 3:00 PM
- **Month-End:** Higher activity for budget reconciliation

### Activity Metrics
See [User Activity Documentation](../../user-activity/index.md) for detailed analysis.

---

## See Also

- [Districts & Schools](districts-schools.md) - Organizational structure
- [Schema: Users & Security](../../schema/by-domain/users-security.md)
- [SSO Deadlocks](../../performance/known-issues/sso-deadlocks.md)

