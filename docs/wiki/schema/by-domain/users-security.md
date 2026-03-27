# Schema: Users & Security Domain

[Home](../../index.md) > [Schema](../index.md) > [By Domain](index.md) > Users & Security

---

## Overview

The users domain contains 24 tables managing authentication, authorization, roles, and permissions.

---

## Table Count: 24

### Core Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| Users | User accounts | UserId, Email, FirstName, LastName, Active |
| Roles | Role definitions | RoleId, RoleName, Description |
| UserRoles | User-role assignments | UserRoleId, UserId, RoleId, SchoolId |
| Permissions | Permission definitions | PermissionId, PermissionCode, Description |
| RolePermissions | Role-permission mapping | RoleId, PermissionId |

### School Assignment Tables

| Table | Purpose |
|-------|---------|
| UserSchools | User's school assignments |
| UserDepartments | Department assignments |
| SchoolAccess | School-level access rules |

### SSO Tables

| Table | Purpose |
|-------|---------|
| SSOProviders | Identity provider config |
| SSOAttributes | Attribute mapping |
| SSOLog | Authentication log |

### Session Tables

| Table | Purpose |
|-------|---------|
| Sessions | Active sessions |
| SessionHistory | Past sessions |
| LoginAttempts | Failed login tracking |

---

## Key Relationships

```
Users (1) ──────► (N) UserRoles ──────► (1) Roles
     │                                       │
     │                                       └──► RolePermissions
     │
     ├──────► (N) UserSchools ──────► (1) Schools
     │
     ├──────► (N) Requisitions (as creator)
     │
     └──────► SSOProviders (via SSOID)
```

---

## Critical Table: Users

### Schema
| Column | Type | Description |
|--------|------|-------------|
| UserId | INT | Primary key |
| Email | VARCHAR(200) | Login identifier (unique) |
| PasswordHash | VARCHAR(256) | Hashed password |
| FirstName | VARCHAR(100) | First name |
| LastName | VARCHAR(100) | Last name |
| DistrictId | INT | Primary district |
| Title | VARCHAR(100) | Job title |
| Phone | VARCHAR(20) | Phone number |
| Active | BIT | Account enabled |
| SSOID | VARCHAR(200) | SSO identifier |
| SSOProvider | VARCHAR(100) | SSO provider name |
| LastLogin | DATETIME | Last successful login |
| FailedAttempts | INT | Consecutive failed logins |
| LockoutEnd | DATETIME | Account lockout expiry |
| Created | DATETIME | Account created |
| Modified | DATETIME | Last modified |

### SSO Update Issue

Parallel SSO updates cause deadlocks:

```sql
-- This query causes deadlocks when run in parallel
UPDATE dbo.Users
SET SSOID = @P0, SSOProvider = @P1
WHERE Email = @P2
  AND Active = 1
```

**Known Issue:** 20 deadlocks/month involving 8-12 sessions. See [KI-005](../../performance/known-issues/sso-deadlocks.md).

---

## Common Queries

### Find User by Email
```sql
SELECT UserId, Email, FirstName, LastName,
       Active, LastLogin, SSOID, SSOProvider
FROM Users
WHERE Email = @Email
```

### User with Roles
```sql
SELECT u.UserId, u.Email, u.FirstName, u.LastName,
       r.RoleName, s.SchoolName
FROM Users u
JOIN UserRoles ur ON u.UserId = ur.UserId
JOIN Roles r ON ur.RoleId = r.RoleId
LEFT JOIN Schools s ON ur.SchoolId = s.SchoolId
WHERE u.UserId = @UserId
ORDER BY r.RoleName, s.SchoolName
```

### Users by School
```sql
SELECT u.UserId, u.Email, u.FirstName, u.LastName,
       u.Title, u.LastLogin
FROM Users u
JOIN UserSchools us ON u.UserId = us.UserId
WHERE us.SchoolId = @SchoolId
  AND u.Active = 1
ORDER BY u.LastName, u.FirstName
```

### Check Permission
```sql
SELECT 1
FROM Users u
JOIN UserRoles ur ON u.UserId = ur.UserId
JOIN RolePermissions rp ON ur.RoleId = rp.RoleId
JOIN Permissions p ON rp.PermissionId = p.PermissionId
WHERE u.UserId = @UserId
  AND p.PermissionCode = @PermissionCode
  AND (ur.SchoolId IS NULL OR ur.SchoolId = @SchoolId)
```

---

## Role Hierarchy

| Level | Role | Typical Permissions |
|-------|------|---------------------|
| 1 | District Admin | All permissions |
| 2 | Purchasing Director | Vendor, Bid, PO management |
| 3 | Finance Director | Budget, Payment management |
| 4 | School Admin | School-level everything |
| 5 | Principal | Approve for school |
| 6 | Department Head | Approve for department |
| 7 | Buyer | Create/manage POs |
| 8 | Requestor | Create requisitions |
| 9 | View Only | Read access only |

---

## Index Recommendations

### Users Table
```sql
-- For email lookups (most common)
CREATE UNIQUE INDEX IX_Users_Email
ON Users (Email)
INCLUDE (UserId, FirstName, LastName, Active, SSOID)

-- For SSO updates (prevent deadlocks)
CREATE INDEX IX_Users_Email_Active
ON Users (Email, Active)
INCLUDE (SSOID, SSOProvider)

-- For district queries
CREATE INDEX IX_Users_DistrictId
ON Users (DistrictId, Active)
INCLUDE (Email, FirstName, LastName)
```

### UserRoles Table
```sql
-- For user permission checks
CREATE INDEX IX_UserRoles_UserId
ON UserRoles (UserId)
INCLUDE (RoleId, SchoolId)

-- For role membership queries
CREATE INDEX IX_UserRoles_RoleId
ON UserRoles (RoleId)
```

---

## Application Users

EDS uses system accounts for application connectivity:

| Account | Usage | Monthly Hours |
|---------|-------|---------------|
| EDSIQWebUser | Primary web app | 214+ |
| EDSAdmin | Admin operations | Variable |
| DPAMonitor | Performance monitoring | Continuous |

---

## Security Features

### Password Policy
| Setting | Value |
|---------|-------|
| Minimum Length | 8 characters |
| Complexity | Upper, lower, number, special |
| Expiration | 90 days |
| History | 12 passwords |
| Lockout | 5 failed attempts |
| Lockout Duration | 30 minutes |

### SSO Integration
| Provider | Protocol | Status |
|----------|----------|--------|
| Azure AD | SAML 2.0 | Supported |
| Okta | SAML 2.0 | Supported |
| Google | OIDC | Supported |
| ADFS | SAML 2.0 | Supported |

---

## Performance Considerations

### High-Impact Operations
| Operation | Impact | Mitigation |
|-----------|--------|------------|
| SSO bulk sync | Deadlocks | Serialize updates |
| Permission check | Called frequently | Cache results |
| Login query | Every auth | Optimize indexes |

### Known Issues
- [KI-005: SSO Deadlocks](../../performance/known-issues/sso-deadlocks.md)

---

## See Also

- [Business: Users & Roles](../../business/entities/users-roles.md)
- [Districts & Schools](../../business/entities/districts-schools.md)
- [SSO Deadlock Issue](../../performance/known-issues/sso-deadlocks.md)

