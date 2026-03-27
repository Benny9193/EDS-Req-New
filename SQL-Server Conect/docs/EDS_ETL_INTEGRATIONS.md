# EDS Database - ETL & Integration Points

Generated: 2026-01-15

This document provides technical specifications for data integration points, ETL processes, and external system connectivity.

---

## Overview

EDS integrates with multiple external systems for authentication, catalog management, financial synchronization, and vendor communication.

---

## Integration Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           INTEGRATION LAYER                                  │
└─────────────────────────────────────────────────────────────────────────────┘

  INBOUND                        EDS DATABASE                      OUTBOUND
  ───────                        ────────────                      ────────
                                      │
┌──────────────┐                      │                    ┌──────────────┐
│  SSO/IdP     │──SAML/OIDC──────────►│                    │  Financial   │
│  Providers   │                      │◄───GL Export──────►│   System     │
└──────────────┘                      │                    └──────────────┘
                                      │
┌──────────────┐                      │                    ┌──────────────┐
│   Vendor     │──Catalog Import─────►│                    │    SMTP      │
│   Catalogs   │                      │───Notifications───►│   (Email)    │
└──────────────┘                      │                    └──────────────┘
                                      │
┌──────────────┐                      │                    ┌──────────────┐
│   Vendor     │──Bid Results────────►│                    │  Reporting   │
│   Bids       │                      │───Report Data─────►│   (SSRS)     │
└──────────────┘                      │                    └──────────────┘
                                      │
┌──────────────┐                      │                    ┌──────────────┐
│   Punch-Out  │◄─cXML───────────────►│                    │   Document   │
│   Vendors    │                      │───Attachments────►│   Storage    │
└──────────────┘                      │                    └──────────────┘
                                      │
┌──────────────┐                      │                    ┌──────────────┐
│   EDI        │──832 Catalog────────►│                    │    PO        │
│   Partners   │◄─850 PO─────────────►│───PO Transmission─►│  Transmission│
└──────────────┘                      │                    └──────────────┘
```

---

## Inbound Integrations

### 1. SSO/Identity Provider Sync

**Purpose:** Synchronize user accounts from identity providers

| Attribute | Specification |
|-----------|---------------|
| Protocol | SAML 2.0, OIDC |
| Direction | Inbound (just-in-time provisioning) |
| Frequency | Real-time (on login) |
| Tables Affected | Users, SSOAttributes, SSOLog |

**Data Flow:**
```
IdP → SAML Assertion → EDS Web Server → sp_FA_AttemptLogin → Users table
```

**Field Mapping:**
| IdP Attribute | EDS Column | Notes |
|---------------|------------|-------|
| email | Users.Email | Primary identifier |
| firstName | Users.FirstName | Display name |
| lastName | Users.LastName | Display name |
| sub/nameId | Users.SSOID | SSO unique ID |
| groups | UserRoles | Role assignment |

**Known Issues:**
- Parallel SSO updates can cause deadlocks (KI-005)
- Solution: Serialize updates via sp_SSOUpdateUser

---

### 2. Vendor Catalog Import

**Purpose:** Load vendor product catalogs into EDS

| Attribute | Specification |
|-----------|---------------|
| Formats | CSV, Excel, XML, EDI 832 |
| Direction | Inbound |
| Frequency | Weekly to monthly |
| Tables Affected | Items, CrossRefs, Catalog, CatalogText |

**Import Process:**
```
Vendor File → sp_CatalogImport → Staging Tables → Validation → Production Tables
```

**Staging Tables:**
| Table | Purpose |
|-------|---------|
| CatalogImportStaging | Raw imported data |
| CatalogImportErrors | Validation failures |
| CatalogImportLog | Import audit trail |

**Field Mapping (Standard):**
| Source Column | Target Table.Column | Validation |
|---------------|---------------------|------------|
| VendorSKU | CrossRefs.VendorItemCode | Required, unique per vendor |
| Description | Items.Description | Required, max 1024 chars |
| UnitPrice | CrossRefs.CatalogPrice | Numeric, > 0 |
| UOM | Units.Code | Must exist in Units table |
| UPC | CrossRefs.UPC_ISBN | Optional, 12-14 digits |
| ManufacturerName | Manufacturers.Name | Lookup or create |

**Procedures:**
| Procedure | Purpose |
|-----------|---------|
| sp_CatalogImport | Main import orchestrator |
| sp_CatalogImporterXML | XML format parser |
| sp_ValidateCatalogImport | Data validation |
| sp_MergeCatalogItems | Merge staging to production |

---

### 3. Vendor Bid Import

**Purpose:** Load vendor bid responses

| Attribute | Specification |
|-----------|---------------|
| Formats | CSV, Excel, XML |
| Direction | Inbound |
| Frequency | During bid periods |
| Tables Affected | BidResults, BidResultsDetail, BidImports |

**Import Process:**
```
Vendor Bid File → sp_ImportVendorsBid → Validation → BidResults/Detail
```

**Field Mapping:**
| Source Column | Target Table.Column |
|---------------|---------------------|
| BidHeaderId | BidResults.BidHeaderId |
| VendorId | BidResults.VendorId |
| ItemId | BidResultsDetail.ItemId |
| UnitPrice | BidResultsDetail.Price |
| Quantity | BidResultsDetail.Quantity |
| Comments | BidResultsDetail.Comments |

---

### 4. Punch-Out Integration (cXML)

**Purpose:** Real-time shopping cart integration with external vendor sites

| Attribute | Specification |
|-----------|---------------|
| Protocol | cXML 1.2.x |
| Direction | Bidirectional |
| Frequency | Real-time |
| Tables Affected | cxmlSession, Detail, Requisitions |

**Message Flow:**
```
1. PunchOutSetupRequest (EDS → Vendor)
2. PunchOutSetupResponse (Vendor → EDS)
3. User shops on vendor site
4. PunchOutOrderMessage (Vendor → EDS)
5. Cart items → Requisition detail
```

**Session Table:**
| Column | Purpose |
|--------|---------|
| cxmlSessionId | Session identifier |
| BuyerCookie | EDS session reference |
| VendorId | Punch-out vendor |
| CartXML | Returned cart contents |
| Status | Session state |
| Created | Timestamp |

**Supported Vendors:**
- Amazon Business
- Staples
- Office Depot
- Dell
- CDW

---

### 5. EDI Integration

**Purpose:** Electronic Data Interchange for catalogs and orders

| Transaction | Direction | Description |
|-------------|-----------|-------------|
| EDI 832 | Inbound | Price/Sales Catalog |
| EDI 850 | Outbound | Purchase Order |
| EDI 855 | Inbound | Purchase Order Acknowledgment |
| EDI 856 | Inbound | Advance Ship Notice |
| EDI 810 | Inbound | Invoice |

**EDI Processing:**
```
EDI File → EDI Translator → sp_ProcessEDI[Type] → EDS Tables
```

---

## Outbound Integrations

### 1. Financial System Export (GL)

**Purpose:** Export encumbrances, expenses, and payments to GL

| Attribute | Specification |
|-----------|---------------|
| Formats | CSV, XML, REST API |
| Direction | Outbound |
| Frequency | Daily batch or real-time |
| Tables Source | PO, PODetailItems, Requisitions, BudgetAccounts |

**Export Types:**
| Export | Trigger | Data |
|--------|---------|------|
| Encumbrance | PO creation | PO amount by account |
| Liquidation | PO receipt | Encumbrance release |
| Expense | Invoice | Actual cost by account |
| Budget Transfer | User request | Account adjustments |

**Field Mapping:**
| EDS Field | GL Field | Notes |
|-----------|----------|-------|
| BudgetAccounts.AccountCode | GL Account | May require translation |
| PO.TotalAmount | Amount | Currency precision |
| PO.PONumber | Reference | External reference |
| PO.CreatedDate | Transaction Date | |

**Procedures:**
| Procedure | Purpose |
|-----------|---------|
| sp_ExportToGL | Generate GL export file |
| sp_CreateGLTransaction | Real-time API call |
| usp_ReconcileGL | Reconciliation report |

---

### 2. PO Transmission

**Purpose:** Send purchase orders to vendors

| Attribute | Specification |
|-----------|---------------|
| Methods | Email, Fax, EDI, Punch-out |
| Direction | Outbound |
| Frequency | On-demand |
| Tables Source | PO, PODetailItems, Vendors |

**Transmission Flow:**
```
sp_CreatePO → usp_QueuePOsToSend → POSendQueue → usp_StartPOSend → Vendor
                                                       │
                                                       ▼
                                              usp_EndPOSend (status update)
```

**Queue Table:**
| Column | Purpose |
|--------|---------|
| POSendQueueId | Queue entry ID |
| POId | PO to send |
| VendorId | Receiving vendor |
| Method | Transmission method |
| Status | Pending/Sent/Failed |
| AttemptCount | Retry tracking |
| SentDate | Transmission timestamp |

---

### 3. Email Notifications (SMTP)

**Purpose:** Send workflow notifications

| Attribute | Specification |
|-----------|---------------|
| Provider | SMTP / SendGrid |
| Direction | Outbound |
| Frequency | Event-driven |
| Tables Source | Users, Requisitions, Approvals |

**Notification Types:**
| Event | Recipients | Template |
|-------|------------|----------|
| Requisition Submitted | Approver | ApprovalRequest.html |
| Requisition Approved | Requestor | ApprovalComplete.html |
| Requisition Rejected | Requestor | ApprovalRejected.html |
| PO Generated | Requestor, Vendor | POCreated.html |
| Approval Reminder | Approver | ApprovalReminder.html |
| Bid Due Reminder | Vendors | BidReminder.html |

**Tables:**
| Table | Purpose |
|-------|---------|
| EmailBlast | Email campaigns |
| EmailBlastLog | Delivery tracking |
| EmailTemplates | HTML templates |

---

### 4. Reporting Services (SSRS)

**Purpose:** Generate reports from EDS data

| Attribute | Specification |
|-----------|---------------|
| Platform | SQL Server Reporting Services |
| Direction | Outbound (data) |
| Frequency | On-demand, scheduled |
| Tables Source | All (read-only views) |

**Report Categories:**
| Category | Examples |
|----------|----------|
| Budget | Account balance, encumbrance |
| Purchasing | PO summary, requisition status |
| Vendor | Performance, spend analysis |
| Bidding | Award summary, bid comparison |

**Data Access:**
- Reports use read-only views
- Dedicated reporting database user
- Views prefixed with `rs_` or `vw_Rpt`

---

### 5. Document Storage

**Purpose:** Store and retrieve document attachments

| Attribute | Specification |
|-----------|---------------|
| Storage | Azure Blob / SharePoint / Database |
| Direction | Bidirectional |
| Frequency | On-demand |
| Tables | Documents, DocumentTypes, VendorDocuments |

**Document Types:**
| Type | Storage | Retention |
|------|---------|-----------|
| Requisition Attachments | Blob | 7 years |
| Bid Documents | Blob | 10 years |
| Vendor Documents (W-9) | Blob | 7 years |
| Contract Files | SharePoint | Contract term + 7 years |

---

## Batch Jobs & Scheduling

### Daily Jobs

| Job | Time | Procedure | Purpose |
|-----|------|-----------|---------|
| GL Export | 2:00 AM | sp_ExportToGL | Send daily transactions |
| Price Sync | 3:00 AM | sp_SyncPrices | Update from vendor feeds |
| Garbage Collection | 4:00 AM | sp_NightlyGarbageCollection | Cleanup temp data |
| Session Cleanup | 5:00 AM | sp_CleanupSessions | Remove old sessions |

### Weekly Jobs

| Job | Day | Time | Procedure | Purpose |
|-----|-----|------|-----------|---------|
| Catalog Refresh | Sunday | 1:00 AM | sp_RefreshCatalogs | Full catalog sync |
| Index Defrag | Sunday | 2:00 AM | sp_DefragAll | Index maintenance |
| Reporting Sync | Sunday | 6:00 AM | sp_SyncReportingDB | Reporting DB refresh |

### Monthly Jobs

| Job | Day | Time | Procedure | Purpose |
|-----|-----|------|-----------|---------|
| Archive Old Data | 1st | 12:00 AM | sp_ArchiveOldData | Move to archive schema |
| Reindex | 1st | 1:00 AM | sp_ReindexAll | Full index rebuild |
| Statistics Update | 1st | 4:00 AM | sp_UpdateStatistics | Update query stats |

---

## Error Handling & Retry Logic

### Retry Configuration

| Integration | Max Retries | Retry Interval | Escalation |
|-------------|-------------|----------------|------------|
| SSO Sync | 3 | Immediate | Alert IT |
| Catalog Import | 2 | 1 hour | Alert Catalog Mgr |
| PO Transmission | 5 | 15 min exponential | Alert Purchasing |
| GL Export | 3 | 30 min | Alert Finance |
| Email | 3 | 5 min | Log only |

### Error Logging

| Table | Purpose |
|-------|---------|
| IntegrationLog | All integration activity |
| IntegrationErrors | Failed operations |
| POSendErrors | PO transmission failures |
| CatalogImportErrors | Catalog import issues |

---

## Monitoring & Alerting

### Health Checks

| Integration | Check | Frequency | Alert Threshold |
|-------------|-------|-----------|-----------------|
| SSO | Login test | 5 min | 2 failures |
| GL API | Ping | 1 min | 3 failures |
| Email | Send test | 15 min | 2 failures |
| Catalog Job | Status check | Hourly | Job failure |

### Key Metrics

| Metric | Target | Alert |
|--------|--------|-------|
| Catalog import success rate | 99% | < 95% |
| PO transmission success rate | 99.5% | < 98% |
| GL export success rate | 99.9% | < 99% |
| Email delivery rate | 98% | < 95% |

---

## Security Considerations

### Authentication

| Integration | Method | Credential Storage |
|-------------|--------|-------------------|
| SSO | SAML/OIDC tokens | IdP managed |
| GL API | API Key + TLS | Azure Key Vault |
| Punch-out | cXML shared secret | Encrypted config |
| Email | SMTP auth | Encrypted config |
| Blob Storage | Azure AD | Managed identity |

### Data Protection

| Measure | Application |
|---------|-------------|
| TLS 1.2+ | All external connections |
| Encryption at rest | Sensitive data columns |
| IP whitelisting | Critical integrations |
| Audit logging | All data exchange |

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-01-15 | Initial ETL & integration documentation | Phase 4 Documentation |

