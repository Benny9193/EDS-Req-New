# What is EDS?

[Home](../index.md) > [Business](index.md) > What is EDS?

---

## Overview

**EDS (Educational Data Systems)** is a comprehensive **e-procurement platform** designed specifically for **K-12 school districts**. It streamlines the entire purchasing lifecycle from requisition creation through purchase order fulfillment.

---

## Core Capabilities

### 1. Requisition Management
- School staff create purchase requests
- Multi-level approval workflows
- Budget validation and tracking
- Integration with district accounting systems

### 2. Vendor Management
- Vendor registration and onboarding
- Vendor contact management
- Performance tracking
- Electronic PO delivery

### 3. Competitive Bidding
- Bid solicitation and management
- Vendor bid submission portal
- Award processing
- Contract management

### 4. Purchase Orders
- Automated PO generation from approved requisitions
- Electronic PO transmission
- Receiving and invoicing
- Payment tracking

### 5. Product Catalogs
- Centralized item catalog
- Pricing management
- Cross-reference lookups
- Category organization

---

## Business Value

| Benefit | Description |
|---------|-------------|
| **Cost Savings** | Competitive bidding ensures best pricing |
| **Compliance** | Audit trail for all purchases |
| **Efficiency** | Automated workflows reduce manual effort |
| **Visibility** | Real-time budget and spending tracking |
| **Standardization** | Consistent purchasing across schools |

---

## Key Stakeholders

### School District Staff
- **Requesters** - Teachers, staff who create requisitions
- **Approvers** - Principals, department heads who approve purchases
- **Purchasing** - District purchasing department

### Vendors
- **Bid Contacts** - Submit competitive bids
- **Sales Contacts** - Manage orders and fulfillment

### Administrators
- **District Admins** - Configure system, manage users
- **DBA Team** - Database administration and monitoring

---

## System Statistics

| Entity | Count | Description |
|--------|-------|-------------|
| Districts | Multiple | School districts using the system |
| Schools | Hundreds | Individual schools within districts |
| Users | 17+ active | Database users/accounts |
| Vendors | Thousands | Registered vendors |
| Requisitions | 2M+ | Historical purchase requests |
| Line Items | 30M+ | Requisition detail records |
| Purchase Orders | Millions | Generated POs |

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| **Database** | SQL Server 2017 Developer Edition |
| **Web App** | Java (JDBC), IIS |
| **API/Services** | Node.js (node-mssql) |
| **Infrastructure** | Azure VM, Kubernetes |
| **Monitoring** | SolarWinds DPA |

---

## Related Documentation

- [Business Entities](entities/index.md) - Detailed entity documentation
- [Workflows](workflows/index.md) - Business process flows
- [Architecture](../architecture/system-overview.md) - Technical architecture

---

## See Also

| Topic | Description |
|-------|-------------|
| [Districts & Schools](entities/districts-schools.md) | Organization hierarchy |
| [Requisition Workflow](workflows/requisition-to-po.md) | End-to-end procurement |
| [User Roles](entities/users-roles.md) | User types and permissions |
