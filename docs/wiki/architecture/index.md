# Architecture

[Home](../index.md) > Architecture

---

## Overview

This section documents the technical architecture of the EDS system, including the application stack, database architecture, and system integrations.

---

## Contents

| Document | Description |
|----------|-------------|
| [System Overview](system-overview.md) | High-level architecture diagram |
| [Application Stack](application-stack.md) | Application layer technologies |
| [Database Architecture](database-architecture.md) | SQL Server configuration |
| [Integrations](integrations.md) | External system connections |

---

## Architecture Summary

### High-Level View

```
┌─────────────────────────────────────────────────────────────────────┐
│                         USERS                                        │
│   School Staff │ Administrators │ Vendors │ Finance                  │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     PRESENTATION LAYER                               │
│        Web Application │ Mobile │ Vendor Portal                      │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     APPLICATION LAYER                                │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │
│   │ EDSIQ Web   │  │  API Layer  │  │ Job Service │                │
│   │   (Java)    │  │  (Node.js)  │  │   (Java)    │                │
│   └─────────────┘  └─────────────┘  └─────────────┘                │
│                                                                      │
│              Running on Kubernetes (Azure AKS)                       │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       DATA LAYER                                     │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │              SQL Server 2017 (Azure VM)                      │   │
│   │                                                              │   │
│   │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │   │
│   │  │   EDS   │  │ EDSProd │  │  DPA    │  │ Archive │        │   │
│   │  │ (Main)  │  │(Reports)│  │(Monitor)│  │         │        │   │
│   │  └─────────┘  └─────────┘  └─────────┘  └─────────┘        │   │
│   └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Technology Stack

### Application Layer

| Component | Technology | Purpose |
|-----------|------------|---------|
| Web App | Java (Spring Boot) | Main application |
| API | Node.js | REST API services |
| Jobs | Java | Background processing |
| Hosting | Kubernetes (AKS) | Container orchestration |

### Data Layer

| Component | Technology | Purpose |
|-----------|------------|---------|
| Database | SQL Server 2017 | Primary data store |
| Hosting | Azure VM | Database server |
| Monitoring | SolarWinds DPA | Performance monitoring |

### Integration Layer

| System | Protocol | Purpose |
|--------|----------|---------|
| SSO Providers | SAML/OIDC | Authentication |
| Financial Systems | REST/SOAP | GL integration |
| Vendor Catalogs | EDI/REST | Catalog updates |

---

## Key Characteristics

### Scalability
- Kubernetes auto-scaling for application tier
- Database scaling via Azure VM sizing
- Connection pooling for efficient resource use

### Reliability
- Kubernetes pod redundancy
- Database backups to Azure Blob
- Health checks and auto-restart

### Security
- SSL/TLS for all connections
- Azure Key Vault for secrets
- Role-based access control

---

## See Also

- [Schema Overview](../schema/index.md) - Database schema
- [Performance Overview](../performance/index.md) - Performance metrics
- [Troubleshooting](../troubleshooting/index.md) - Problem resolution

