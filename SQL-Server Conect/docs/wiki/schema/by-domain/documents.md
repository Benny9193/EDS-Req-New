# Schema: Documents Domain

[Home](../../index.md) > [Schema](../index.md) > [By Domain](index.md) > Documents

---

## Overview

The documents domain contains 15 tables managing file attachments, document storage, and file metadata across the system.

---

## Table Count: 15

### Core Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| Documents | Document master | DocumentId, FileName, FileType, FilePath |
| Attachments | Entity-document links | AttachmentId, EntityType, EntityId, DocumentId |
| FileStorage | Blob storage | FileId, Content, ContentType |
| DocumentTypes | Type definitions | TypeId, TypeName, AllowedExtensions |

### Entity-Specific Tables

| Table | Purpose |
|-------|---------|
| RequisitionAttachments | Requisition files |
| POAttachments | PO files |
| BidAttachments | Bid documents |
| VendorDocuments | Vendor files (W-9, insurance) |
| ContractDocuments | Contract files |

### Version Control

| Table | Purpose |
|-------|---------|
| DocumentVersions | Version history |
| DocumentCheckins | Check in/out tracking |

---

## Key Relationships

```
Documents (1) ──────► (N) Attachments ──────► Various Entities
     │                                              │
     │                                              ├── Requisitions
     │                                              ├── PurchaseOrders
     │                                              ├── BidHeaders
     │                                              ├── Vendors
     │                                              └── Contracts
     │
     └──────► (N) DocumentVersions
                    │
                    └──────► FileStorage (blob)
```

---

## Critical Table: Documents

### Schema
| Column | Type | Description |
|--------|------|-------------|
| DocumentId | INT | Primary key |
| FileName | VARCHAR(255) | Original file name |
| FileType | VARCHAR(10) | Extension (.pdf, .xlsx) |
| FilePath | VARCHAR(500) | Storage path |
| FileSize | BIGINT | Size in bytes |
| ContentType | VARCHAR(100) | MIME type |
| Description | VARCHAR(500) | User description |
| UploadedBy | INT | User FK |
| UploadedDate | DATETIME | Upload timestamp |
| IsPublic | BIT | Public access flag |
| Active | BIT | Soft delete flag |

---

## Attachment Patterns

### Generic Attachments Table
```sql
-- Polymorphic attachment linking
SELECT *
FROM Attachments
WHERE EntityType = 'Requisition'  -- or 'PO', 'Bid', etc.
  AND EntityId = @RequisitionId
```

### Entity-Specific Tables
Each major entity has its own attachment table for performance:
```sql
SELECT d.*
FROM RequisitionAttachments ra
JOIN Documents d ON ra.DocumentId = d.DocumentId
WHERE ra.RequisitionId = @RequisitionId
```

---

## Common Queries

### Documents for Entity
```sql
SELECT d.DocumentId, d.FileName, d.FileType,
       d.FileSize, d.UploadedDate,
       u.FirstName + ' ' + u.LastName as UploadedBy
FROM Documents d
JOIN Attachments a ON d.DocumentId = a.DocumentId
JOIN Users u ON d.UploadedBy = u.UserId
WHERE a.EntityType = @EntityType
  AND a.EntityId = @EntityId
ORDER BY d.UploadedDate DESC
```

### Recent Uploads
```sql
SELECT d.FileName, d.FileType, d.FileSize,
       d.UploadedDate,
       u.FirstName + ' ' + u.LastName as UploadedBy,
       a.EntityType, a.EntityId
FROM Documents d
JOIN Users u ON d.UploadedBy = u.UserId
LEFT JOIN Attachments a ON d.DocumentId = a.DocumentId
WHERE d.UploadedDate > DATEADD(day, -7, GETDATE())
ORDER BY d.UploadedDate DESC
```

### Storage Usage
```sql
SELECT dt.TypeName,
       COUNT(*) as DocumentCount,
       SUM(d.FileSize) / 1024.0 / 1024.0 as TotalSizeMB
FROM Documents d
JOIN DocumentTypes dt ON d.FileType = dt.Extension
WHERE d.Active = 1
GROUP BY dt.TypeName
ORDER BY TotalSizeMB DESC
```

---

## File Types

### Allowed Types
| Extension | MIME Type | Max Size |
|-----------|-----------|----------|
| .pdf | application/pdf | 25 MB |
| .doc/.docx | application/msword | 25 MB |
| .xls/.xlsx | application/vnd.ms-excel | 25 MB |
| .jpg/.png | image/* | 10 MB |
| .txt | text/plain | 5 MB |
| .csv | text/csv | 50 MB |

### Blocked Types
| Extension | Reason |
|-----------|--------|
| .exe | Executable |
| .bat | Script |
| .dll | Library |
| .zip | Archive (scan first) |

---

## Storage Options

### File System Storage
```
/var/eds/documents/
    ├── 2026/
    │   ├── 01/
    │   │   ├── req/
    │   │   ├── po/
    │   │   └── bid/
    │   └── 02/
    └── archive/
```

### Database BLOB Storage
```sql
SELECT fs.Content
FROM FileStorage fs
JOIN Documents d ON fs.FileId = d.FileStorageId
WHERE d.DocumentId = @DocumentId
```

### Cloud Storage (Azure/S3)
- Files stored in cloud blob storage
- Database stores reference URL
- CDN for public documents

---

## Index Recommendations

### Documents Table
```sql
-- For recent uploads
CREATE INDEX IX_Documents_UploadedDate
ON Documents (UploadedDate DESC)
INCLUDE (FileName, FileType, FileSize, UploadedBy)

-- For user's documents
CREATE INDEX IX_Documents_UploadedBy
ON Documents (UploadedBy)
```

### Attachments Table
```sql
-- For entity lookups
CREATE INDEX IX_Attachments_Entity
ON Attachments (EntityType, EntityId)
INCLUDE (DocumentId)
```

---

## Document Versioning

### Version Table
| Column | Type | Description |
|--------|------|-------------|
| VersionId | INT | Primary key |
| DocumentId | INT | Parent document |
| VersionNumber | INT | Version sequence |
| FileStorageId | INT | Blob reference |
| ModifiedBy | INT | User FK |
| ModifiedDate | DATETIME | Version timestamp |
| Comments | VARCHAR(500) | Change notes |

### Check In/Out
```sql
-- Check out document
UPDATE Documents
SET CheckedOutBy = @UserId,
    CheckedOutDate = GETDATE()
WHERE DocumentId = @DocumentId
  AND CheckedOutBy IS NULL

-- Check in with new version
INSERT INTO DocumentVersions (DocumentId, VersionNumber, ...)
SELECT @DocumentId, MAX(VersionNumber) + 1, ...
FROM DocumentVersions
WHERE DocumentId = @DocumentId
```

---

## Cleanup & Archival

### Orphaned Documents
```sql
-- Find documents not attached to anything
SELECT d.DocumentId, d.FileName, d.UploadedDate
FROM Documents d
LEFT JOIN Attachments a ON d.DocumentId = a.DocumentId
WHERE a.AttachmentId IS NULL
  AND d.UploadedDate < DATEADD(day, -30, GETDATE())
```

### Archive Old Documents
```sql
-- Move to archive storage
UPDATE Documents
SET FilePath = REPLACE(FilePath, '/documents/', '/archive/'),
    IsArchived = 1,
    ArchivedDate = GETDATE()
WHERE UploadedDate < DATEADD(year, -7, GETDATE())
  AND IsArchived = 0
```

---

## See Also

- [Orders & Purchasing](orders-purchasing.md) - Requisition/PO attachments
- [Bidding](bidding.md) - Bid documents
- [Vendors](vendors.md) - Vendor documents

