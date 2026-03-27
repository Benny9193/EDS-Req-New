# System Integrations

[Home](../index.md) > [Architecture](index.md) > Integrations

---

## Overview

EDS integrates with several external systems for authentication, financial synchronization, vendor catalogs, and notifications.

---

## Integration Map

```
                          ┌─────────────────┐
                          │    SSO/IdP      │
                          │  (Azure AD,     │
                          │   Okta, etc.)   │
                          └────────┬────────┘
                                   │ SAML/OIDC
                                   ▼
┌─────────────┐          ┌─────────────────┐          ┌─────────────┐
│   Vendor    │ ◄────────│                 │──────────► │  Financial  │
│   Systems   │   EDI    │       EDS       │   REST    │   System    │
│  (Catalogs) │          │                 │           │    (GL)     │
└─────────────┘          └────────┬────────┘          └─────────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
                    ▼              ▼              ▼
             ┌───────────┐ ┌───────────┐ ┌───────────┐
             │   Email   │ │ Reporting │ │  Document │
             │  (SMTP)   │ │  (SSRS)   │ │  Storage  │
             └───────────┘ └───────────┘ └───────────┘
```

---

## Authentication (SSO)

### Supported Providers

| Provider | Protocol | Status |
|----------|----------|--------|
| Azure AD | SAML 2.0 | Active |
| Okta | SAML 2.0 | Active |
| Google Workspace | OIDC | Active |
| ADFS | SAML 2.0 | Supported |
| OneLogin | SAML 2.0 | Supported |

### SSO Flow

```
User                IdP                 EDS
  │                  │                   │
  │──Login Request──►│                   │
  │                  │                   │
  │◄──Auth Challenge─│                   │
  │                  │                   │
  │──Credentials────►│                   │
  │                  │                   │
  │◄──SAML Assertion─│                   │
  │                  │                   │
  │───SAML Assertion────────────────────►│
  │                  │                   │
  │◄─────────Session Token───────────────│
```

### Known Issue: SSO Updates

Parallel SSO attribute updates cause deadlocks. See [KI-005](../performance/known-issues/sso-deadlocks.md).

---

## Financial System Integration

### Purpose
- GL account code validation
- Budget transfer synchronization
- Payment information exchange
- Journal entry creation

### Integration Methods

| Method | Use Case |
|--------|----------|
| REST API | Real-time account lookup |
| Batch File | Daily GL posting |
| Database Link | Direct query (if supported) |

### Data Exchange

```
EDS                          Financial System
 │                                  │
 ├──Account Validation────────────►│
 │◄─────Valid/Invalid──────────────┤
 │                                  │
 ├──Budget Transfer Request───────►│
 │◄─────Confirmation───────────────┤
 │                                  │
 ├──PO Encumbrance────────────────►│
 │                                  │
 ├──Invoice/Payment───────────────►│
 │◄─────Payment Confirmation───────┤
```

---

## Vendor Integrations

### Catalog Updates

| Method | Description |
|--------|-------------|
| EDI (Electronic Data Interchange) | Standard 832 Price/Sales Catalog |
| File Upload | CSV/Excel manual upload |
| Punch-Out | cXML round-trip shopping |
| API | REST-based catalog sync |

### Punch-Out Vendors

| Vendor | Protocol | Status |
|--------|----------|--------|
| Amazon Business | cXML | Active |
| Staples | cXML | Active |
| Office Depot | cXML | Active |
| Dell | cXML | Active |
| CDW | cXML | Supported |

### Punch-Out Flow

```
User (EDS)           EDS Server          Vendor Site
    │                    │                    │
    │──Shop Request─────►│                    │
    │                    │                    │
    │◄───────────────────│──Setup Request────►│
    │                    │◄──Setup Response───│
    │                    │                    │
    │──────────────Redirect to Vendor────────►│
    │                    │                    │
    │◄─────────────Shopping Session───────────│
    │                    │                    │
    │──────────────Cart Checkout─────────────►│
    │                    │                    │
    │◄──────────────────│◄──Cart Contents────│
    │                    │                    │
    │◄──Requisition Created──│                │
```

### Vendor Sync Job

A scheduled job synchronizes vendor data. See [KI-002](../performance/known-issues/vendor-sync-job.md) for known issues.

---

## Notification Services

### Email (SMTP)

| Setting | Value |
|---------|-------|
| Provider | Azure SendGrid / SMTP |
| Templates | HTML email templates |
| Triggers | Workflow events |

### Email Triggers

| Event | Recipients |
|-------|------------|
| Requisition submitted | Approver |
| Requisition approved | Requestor |
| Requisition rejected | Requestor |
| PO generated | Buyer, Vendor |
| Approval reminder | Approver |

---

## Reporting Services

### SQL Server Reporting Services (SSRS)

| Feature | Usage |
|---------|-------|
| Standard Reports | Budget, PO, Vendor reports |
| Ad-Hoc Reports | Report Builder |
| Subscriptions | Scheduled delivery |
| Export | PDF, Excel, Word |

### Report Data Source

```
Report Server
    │
    └──► EDSProd Database (Read-only replica)
             │
             └──► Report-specific views
```

---

## Document Storage

### Storage Options

| Option | Usage |
|--------|-------|
| Azure Blob Storage | Primary document storage |
| Database BLOB | Small documents |
| SharePoint | Document collaboration |

### Document Types

| Type | Integration |
|------|-------------|
| Requisition Attachments | Direct upload |
| Bid Documents | Vendor submission |
| Contract Files | Managed storage |
| Vendor Documents | W-9, Insurance |

---

## Integration Security

### Authentication Methods

| Integration | Auth Method |
|-------------|-------------|
| SSO | SAML/OIDC tokens |
| Financial | API Key + TLS |
| Vendors | cXML credentials |
| Email | SMTP auth |
| Storage | Azure AD |

### Data Protection

| Measure | Application |
|---------|-------------|
| TLS 1.2+ | All connections |
| API Keys | Secret management |
| IP Whitelisting | Critical integrations |
| Audit Logging | All data exchange |

---

## Monitoring & Troubleshooting

### Health Checks

| Integration | Check Method | Frequency |
|-------------|--------------|-----------|
| SSO | Login test | 5 min |
| Financial API | Ping endpoint | 1 min |
| Vendor Catalogs | Job status | Hourly |
| Email | Send test | 15 min |

### Common Issues

| Issue | Symptom | Resolution |
|-------|---------|------------|
| SSO timeout | Login fails | Check IdP status |
| Catalog sync failure | Missing products | Review job logs |
| Email delivery | Missing notifications | Check SMTP config |
| Financial API error | Account validation fails | Verify credentials |

---

## See Also

- [Application Stack](application-stack.md) - Application layer
- [Database Architecture](database-architecture.md) - Database configuration
- [SSO Deadlock Issue](../performance/known-issues/sso-deadlocks.md)

