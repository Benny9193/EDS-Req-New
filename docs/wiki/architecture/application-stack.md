# Application Stack

[Home](../index.md) > [Architecture](index.md) > Application Stack

---

## Overview

The EDS application stack consists of multiple services running on Kubernetes, connecting to a SQL Server database hosted on Azure.

---

## Application Components

### EDSIQ Web Application

| Property | Value |
|----------|-------|
| Language | CFML (ColdFusion Markup Language) |
| Framework | CFWheels (MVC) on Lucee CFML engine |
| Database Access | CFQUERY / ORM |
| Web Server | NGINX → Lucee/Tomcat |
| Sessions | Redis |

**Key Features:**
- Main user interface
- Requisition entry
- Approval workflows
- PO generation
- Reporting

### API Layer

| Property | Value |
|----------|-------|
| Language | Node.js |
| Framework | Express |
| Database Access | mssql package |
| Authentication | JWT |

**Key Features:**
- REST API endpoints
- Mobile application support
- Third-party integrations
- Webhook handlers

### Job Service

| Property | Value |
|----------|-------|
| Language | Java |
| Framework | Spring Batch |
| Scheduling | Quartz |
| Database Access | JDBC |

**Key Jobs:**
- Vendor synchronization
- Notification sending
- Report generation
- Data cleanup

---

## Infrastructure

### Kubernetes (Azure AKS)

```
Azure AKS Cluster
│
├── Namespace: eds-production
│   │
│   ├── Deployment: edsiq-web
│   │   └── Pods: eds-edsiq-2-* (3 replicas)
│   │
│   ├── Deployment: edsiq-api
│   │   └── Pods: eds-api-* (2 replicas)
│   │
│   ├── Deployment: edsiq-jobs
│   │   └── Pods: eds-jobs-* (1 replica)
│   │
│   └── Services, Ingress, ConfigMaps
│
└── Namespace: eds-staging
    └── (Similar structure)
```

### Pod Configuration

**Web Application Pods:**
```yaml
resources:
  requests:
    memory: "2Gi"
    cpu: "1000m"
  limits:
    memory: "4Gi"
    cpu: "2000m"
replicas: 3
```

---

## Database Connectivity

### Connection Pool Settings

| Setting | Value | Purpose |
|---------|-------|---------|
| Min Pool Size | 10 | Always available connections |
| Max Pool Size | 100 | Maximum concurrent connections |
| Connection Timeout | 30s | Time to acquire connection |
| Idle Timeout | 600s | Close idle connections |
| Max Lifetime | 1800s | Prevent stale connections |

### Connection String Pattern
```
jdbc:sqlserver://eds-sqlserver.eastus2.cloudapp.azure.com:1433;
  database=EDS;
  encrypt=true;
  trustServerCertificate=false;
  loginTimeout=30;
  applicationName=EDSIQ
```

### User Accounts

| Account | Application | Purpose |
|---------|-------------|---------|
| EDSIQWebUser | Web App | Primary application account |
| EDSJobUser | Jobs | Background job processing |
| EDSAPIUser | API | API layer access |

---

## Application Flow

### Request Processing

```
User Request
    │
    ▼
Azure Load Balancer
    │
    ▼
Kubernetes Ingress
    │
    ▼
┌─────────────────────────────────────┐
│         EDSIQ Web Pod               │
│                                     │
│  1. Authentication check            │
│  2. Authorization validation        │
│  3. Request processing              │
│  4. Database query (CFQUERY/JDBC)   │
│  5. Response formatting             │
│                                     │
└─────────────────────────────────────┘
    │
    ▼
SQL Server (via connection pool)
```

### Background Job Flow

```
Scheduler (Quartz)
    │
    ▼
┌─────────────────────────────────────┐
│         Job Service Pod             │
│                                     │
│  1. Job triggered by schedule       │
│  2. Acquire database connection     │
│  3. Execute job logic               │
│  4. Update status                   │
│  5. Release connection              │
│                                     │
└─────────────────────────────────────┘
    │
    ▼
SQL Server
```

---

## Monitoring Integration

### Health Checks

| Endpoint | Type | Frequency |
|----------|------|-----------|
| /health | Liveness | 10s |
| /ready | Readiness | 5s |
| /actuator/health | Spring Actuator | On demand |

### Logging

| Component | Log Destination |
|-----------|-----------------|
| Application | Azure Log Analytics |
| Database | SQL Server logs |
| Kubernetes | Azure Monitor |

### Metrics

| Metric | Source | Alert Threshold |
|--------|--------|-----------------|
| Response Time | Application | > 2s |
| Error Rate | Application | > 1% |
| Connection Pool | Lucee JDBC pool | > 80% used |
| Pod Memory | Kubernetes | > 80% |

---

## Known Application-Level Issues

### SSO Sync (KI-005)

The application's SSO synchronization runs parallel updates that cause database deadlocks.

**Location:** `eds-edsiq-2-868b8bf5f-t74zq` (same pod)

**Recommendation:** Serialize SSO updates in application layer.

### Vendor Sync Job (KI-002)

The vendor sync job runs every hour regardless of changes.

**Location:** Job Service

**Recommendation:** Implement delta sync logic.

---

## See Also

- [Database Architecture](database-architecture.md) - Database configuration
- [Integrations](integrations.md) - External system connections
- [User Activity](../user-activity/application-users.md) - Application user accounts

