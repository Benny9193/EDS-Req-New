# Districts & Schools

[Home](../../index.md) > [Business](../index.md) > [Entities](index.md) > Districts & Schools

---

## Overview

Districts and Schools form the organizational hierarchy in EDS. A district represents a school district (e.g., "Springfield Unified School District"), and schools are individual campuses within that district.

---

## Districts

### Purpose
- Top-level organizational unit
- Controls system-wide settings and policies
- Manages vendor relationships and contracts
- Owns budgets and account codes

### Key Fields

| Field | Description |
|-------|-------------|
| DistrictId | Primary key |
| DistrictName | Display name |
| DistrictCode | Short identifier |
| State | State abbreviation |
| FiscalYearStart | Budget cycle start month |
| Active | Is district active |

### Business Rules

1. **One District = One Database Instance** - Typically each district has its own EDS instance
2. **District Admins** - Have full control over their district's configuration
3. **Shared Services** - Some states use cooperative purchasing across districts

---

## Schools

### Purpose
- Individual campus or facility
- Delivery location for purchases
- User assignment location
- Budget allocation unit

### Key Fields

| Field | Description |
|-------|-------------|
| SchoolId | Primary key |
| DistrictId | Parent district (FK) |
| SchoolName | Campus name |
| SchoolCode | Short identifier |
| Address, City, State, Zip | Delivery address |
| Active | Is school active |

### School Types

| Type | Description |
|------|-------------|
| Elementary | K-5 schools |
| Middle | 6-8 schools |
| High School | 9-12 schools |
| District Office | Central administration |
| Warehouse | Distribution center |
| Other | Special programs, alternative schools |

---

## Organizational Hierarchy

```
District: Springfield USD
    │
    ├── School: District Office (Admin)
    │
    ├── School: Springfield Elementary
    │       └── Users: Teachers, Office Staff
    │
    ├── School: Springfield Middle
    │       └── Users: Teachers, Office Staff
    │
    ├── School: Springfield High
    │       └── Users: Teachers, Office Staff
    │
    └── School: Central Warehouse
            └── Users: Receiving Staff
```

---

## Common Queries

### List All Schools in a District
```sql
SELECT s.SchoolId, s.SchoolName, s.SchoolCode,
       s.Address, s.City, s.State, s.Zip
FROM Schools s
WHERE s.DistrictId = @DistrictId
  AND s.Active = 1
ORDER BY s.SchoolName
```

### Count Users per School
```sql
SELECT s.SchoolName, COUNT(us.UserId) as UserCount
FROM Schools s
LEFT JOIN UserSchools us ON s.SchoolId = us.SchoolId
WHERE s.DistrictId = @DistrictId
  AND s.Active = 1
GROUP BY s.SchoolId, s.SchoolName
ORDER BY UserCount DESC
```

---

## Related Tables

| Table | Relationship | Purpose |
|-------|--------------|---------|
| Users | District → Users | District-level users |
| UserSchools | School ↔ Users | School assignments |
| Budgets | District → Budgets | Account codes |
| Vendors | District → Vendors | Approved vendors |
| Requisitions | School → Requisitions | Purchase requests |

---

## Business Processes

### Adding a New School
1. Create school record with district assignment
2. Set up delivery address
3. Assign budget codes
4. Add users with school access
5. Configure approval routing

### Deactivating a School
1. Transfer pending requisitions
2. Reassign users to other schools
3. Archive budget allocations
4. Set Active = 0

---

## See Also

- [Users & Roles](users-roles.md) - People assigned to schools
- [Requisitions](requisitions.md) - Purchases by school
- [Schema: Users & Security](../../schema/by-domain/users-security.md)

