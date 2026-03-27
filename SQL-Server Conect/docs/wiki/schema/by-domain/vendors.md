# Schema: Vendors Domain

[Home](../../index.md) > [Schema](../index.md) > [By Domain](index.md) > Vendors

---

## Overview

The vendors domain contains 32 tables managing supplier information, contacts, performance, and compliance.

---

## Table Count: 32

### Core Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| Vendors | Vendor master | VendorId, VendorName, VendorCode, Active |
| VendorContacts | Contact people | ContactId, VendorId, Name, Email, Phone |
| VendorAddresses | Multiple addresses | AddressId, VendorId, AddressType |
| VendorCategories | Classification | CategoryId, VendorId, Category |
| VendorCertifications | Diversity/compliance | CertId, VendorId, CertType, ExpirationDate |

### Performance Tables

| Table | Purpose |
|-------|---------|
| VendorPerformance | Delivery/quality metrics |
| VendorScores | Quarterly ratings |
| VendorComplaints | Issue tracking |
| VendorReviews | Annual reviews |

### Financial Tables

| Table | Purpose |
|-------|---------|
| VendorBanking | Payment info |
| VendorTaxInfo | W-9 / Tax ID |
| VendorInsurance | Liability coverage |
| VendorBonds | Bonding info |

---

## Key Relationships

```
Vendors (1) ──────► (N) VendorContacts
     │
     ├──────► (N) VendorAddresses
     │
     ├──────► (N) VendorCategories
     │
     ├──────► (N) CrossRefs (Catalog Items)
     │
     ├──────► (N) BidResponses
     │
     └──────► (N) PurchaseOrders
```

---

## Critical Table: Vendors

### Schema
| Column | Type | Description |
|--------|------|-------------|
| VendorId | INT | Primary key |
| VendorCode | VARCHAR(50) | Short identifier |
| VendorName | VARCHAR(200) | Business name |
| Address | VARCHAR(200) | Primary address |
| City | VARCHAR(100) | City |
| State | VARCHAR(2) | State code |
| Zip | VARCHAR(10) | Postal code |
| Phone | VARCHAR(20) | Main phone |
| Fax | VARCHAR(20) | Fax number |
| Email | VARCHAR(200) | Primary email |
| Website | VARCHAR(200) | Web URL |
| TaxId | VARCHAR(20) | Federal EIN |
| Active | BIT | Is active |
| MinimumOrder | DECIMAL | Min order amount |
| PaymentTerms | VARCHAR(50) | Net 30, etc. |
| Created | DATETIME | Create date |
| Modified | DATETIME | Last modified |

---

## Vendor Sync Job

A scheduled job synchronizes vendor data with external systems:

```sql
-- Typical sync query pattern
SELECT v.VendorId, v.VendorCode, v.VendorName,
       v.Address, v.City, v.State, v.Zip,
       v.Phone, v.Email, v.TaxId,
       vc.ContactName, vc.ContactEmail
FROM Vendors v
LEFT JOIN VendorContacts vc ON v.VendorId = vc.VendorId
WHERE v.Modified > @LastSyncTime
   OR vc.Modified > @LastSyncTime
```

**Known Issue:** This job runs hourly 24/7, wasting ~59 hours/month. See [KI-002](../../performance/known-issues/vendor-sync-job.md).

---

## Common Queries

### Search Vendors
```sql
SELECT VendorId, VendorCode, VendorName,
       City, State, Phone, Email, Active
FROM Vendors
WHERE VendorName LIKE '%' + @SearchTerm + '%'
   OR VendorCode LIKE '%' + @SearchTerm + '%'
ORDER BY VendorName
```

### Vendors with Contacts
```sql
SELECT v.VendorName, v.Phone, v.Email,
       vc.ContactName, vc.Title, vc.DirectPhone, vc.Email as ContactEmail
FROM Vendors v
LEFT JOIN VendorContacts vc ON v.VendorId = vc.VendorId
WHERE v.Active = 1
ORDER BY v.VendorName, vc.IsPrimary DESC
```

### Vendor Order History
```sql
SELECT v.VendorName,
       COUNT(po.POId) as POCount,
       SUM(po.TotalAmount) as TotalSpend,
       MAX(po.PODate) as LastOrderDate
FROM Vendors v
LEFT JOIN PurchaseOrders po ON v.VendorId = po.VendorId
    AND po.PODate > DATEADD(year, -1, GETDATE())
WHERE v.Active = 1
GROUP BY v.VendorId, v.VendorName
ORDER BY TotalSpend DESC
```

### Expiring Certifications
```sql
SELECT v.VendorName, vc.CertificationType,
       vc.CertificationNumber, vc.ExpirationDate,
       DATEDIFF(day, GETDATE(), vc.ExpirationDate) as DaysRemaining
FROM VendorCertifications vc
JOIN Vendors v ON vc.VendorId = v.VendorId
WHERE vc.ExpirationDate BETWEEN GETDATE() AND DATEADD(day, 90, GETDATE())
ORDER BY vc.ExpirationDate
```

---

## Index Recommendations

### Vendors Table
```sql
-- For name searches
CREATE INDEX IX_Vendors_Name
ON Vendors (VendorName)
INCLUDE (VendorCode, City, State, Active)

-- For code lookups
CREATE UNIQUE INDEX IX_Vendors_Code
ON Vendors (VendorCode)

-- For active vendor lists
CREATE INDEX IX_Vendors_Active
ON Vendors (Active)
INCLUDE (VendorName, City, State)
```

### VendorContacts Table
```sql
-- For vendor contact lookups
CREATE INDEX IX_VendorContacts_VendorId
ON VendorContacts (VendorId)
INCLUDE (ContactName, Email, Phone, IsPrimary)
```

---

## Diversity Certifications

| Certification | Code | Description |
|---------------|------|-------------|
| MBE | Minority Business | Minority-owned |
| WBE | Women Business | Women-owned |
| DBE | Disadvantaged | Economically disadvantaged |
| SBE | Small Business | Small business |
| SDVOB | Service-Disabled Veteran | Veteran-owned |
| HUB | Historically Underutilized | State-specific |

---

## Vendor Portal Integration

Some vendors access a self-service portal:

| Feature | Description |
|---------|-------------|
| Profile Update | Maintain contact info |
| Catalog Upload | Submit pricing |
| Bid Response | Submit bids online |
| PO Acknowledgment | Confirm orders |
| Invoice Submission | Submit invoices |

---

## Performance Considerations

### High-Impact Operations
| Operation | Impact | Mitigation |
|-----------|--------|------------|
| Vendor sync | Runs too frequently | Schedule smart |
| Bulk catalog update | Many CrossRef changes | Batch process |
| Vendor deactivation | Cascading updates | Careful planning |

---

## See Also

- [Business: Vendors](../../business/entities/vendors.md)
- [Inventory & Catalog](inventory-catalog.md) - CrossRefs
- [Vendor Sync Job Issue](../../performance/known-issues/vendor-sync-job.md)

