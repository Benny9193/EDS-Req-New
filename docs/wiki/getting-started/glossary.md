# Glossary

[Home](../index.md) > [Getting Started](index.md) > Glossary

---

## EDS Terminology

### A

**Account Code**
A structured code representing a budget account in the general ledger. Format: Fund-School-Program-Object-Function-Project.

**Active Flag**
A boolean field indicating whether a record is current. Used for soft deletion.

**Approval Routing**
The workflow that determines which approvers must review a requisition based on amount, school, and other factors.

**Award**
A formal contract granted to a vendor as a result of a competitive bidding process.

---

### B

**BidHeader**
The master record for a bid/solicitation containing title, dates, and type.

**BidMappedItems**
A table that links items to their awarded vendors and contract prices.

**Blocking**
A condition where one database session holds locks that another session needs, causing the second session to wait.

**Budget**
An allocation of funds to a specific account code for a fiscal year.

---

### C

**Catalog**
A collection of items available for purchase from vendors.

**CrossRef**
A record linking an internal item to a vendor-specific product with pricing. Short for "Cross Reference."

**cXML**
Commerce XML - a standard protocol for punch-out catalog integration.

---

### D

**Deadlock**
A circular dependency where two or more sessions are waiting for each other, requiring SQL Server to kill one session.

**Detail**
A line item on a requisition specifying an item, quantity, and price.

**DPA**
Database Performance Analyzer - SolarWinds monitoring tool used to track SQL Server performance.

**District**
The top-level organizational unit (e.g., a school district).

---

### E

**EDI**
Electronic Data Interchange - a standard for electronic document exchange between organizations.

**EDS**
Educational Data Systems - the K-12 procurement software system.

**EDSIQ**
The web application component of EDS.

**Encumbrance**
Budget that is reserved/committed when a purchase order is created, but not yet spent.

**Expenditure**
Actual money spent when an invoice is paid.

---

### F

**Fiscal Year**
The 12-month accounting period used for budgeting. Often July 1 - June 30 for schools.

---

### G-H

**GL**
General Ledger - the master accounting record.

**Head Blocker**
The session at the root of a blocking chain, causing all other blocked sessions.

---

### I

**IFB**
Invitation for Bid - a formal request for vendors to submit prices for specified goods/services.

**Item**
An internal product record representing something that can be purchased.

---

### J-K

**JDBC**
Java Database Connectivity - the database driver layer used by the Lucee CFML engine to connect to SQL Server.

**Job**
A scheduled background task that runs automatically.

---

### L-M

**Lock**
A mechanism SQL Server uses to control concurrent access to data.

**Lock Escalation**
When SQL Server converts many row-level locks to a single page or table lock.

---

### N-O

**NOLOCK**
A SQL Server hint that allows reading data without acquiring shared locks, potentially returning uncommitted data.

---

### P

**Parameter Sniffing**
When SQL Server creates an execution plan based on the first parameter values it sees, which may not be optimal for other values.

**PO / Purchase Order**
An official document authorizing a vendor to supply goods or services.

**Punch-Out**
A catalog integration where users shop on a vendor's website and transfer cart contents back to EDS.

---

### Q-R

**Requisition**
A formal request to purchase goods or services, pending approval.

**RFP**
Request for Proposal - a solicitation for vendors to propose solutions, evaluated on multiple criteria.

**RFQ**
Request for Quote - an informal request for pricing.

**Rollover**
The process of carrying forward budget or encumbrances from one fiscal year to the next.

---

### S

**School**
A physical location within a district (campus, building).

**Session**
A connection to the database with a unique session ID (SPID).

**SPID**
Server Process ID - the unique identifier for a database session.

**SQL Hash**
A unique identifier for a SQL statement, used to track query performance across executions.

**SSO**
Single Sign-On - authentication that allows users to access EDS using their organization's identity provider.

---

### T

**Three-Way Match**
The process of matching a PO, receiving document, and invoice before payment.

**Trigger**
A special stored procedure that automatically executes when data is modified.

**trig_DetailUpdate**
The trigger on the Detail table that updates pricing and vendor information when requisition lines change.

---

### U

**UDF / User-Defined Function**
A custom SQL Server function. Example: uf_RequisitionIsVisible.

**UOM / Unit of Measure**
How items are counted (Each, Case, Pack, Box, etc.).

---

### V

**Vendor**
A supplier who provides goods or services.

**VendorSKU**
The vendor's product code for an item.

---

### W-Z

**Wait Type**
The category of resource a SQL Server session is waiting for (e.g., LCK_M_X, PAGEIOLATCH_SH).

**Workflow**
The sequence of steps required to complete a business process.

---

## Database Terms

### DPA Tables

| Table | Purpose |
|-------|---------|
| CON_SQL_SUM_1 | SQL statement execution statistics |
| CON_BLOCKING_SUM_1 | Blocking session history |
| CON_DEADLOCK_1 | Deadlock event records |
| CON_DEADLOCK_DETAIL_1 | Deadlock graph details |
| CONU_1 | Database user information |
| CONPR_1 | Program/application information |
| CONST_1 | SQL text storage |

### Common Wait Types

| Wait Type | Meaning |
|-----------|---------|
| LCK_M_X | Waiting for exclusive lock |
| LCK_M_S | Waiting for shared lock |
| LCK_M_U | Waiting for update lock |
| PAGEIOLATCH_* | Waiting for page I/O |
| CXPACKET | Parallelism coordination |
| SOS_SCHEDULER_YIELD | CPU pressure |

---

## Acronyms

| Acronym | Meaning |
|---------|---------|
| AKS | Azure Kubernetes Service |
| AP | Accounts Payable |
| BAFO | Best and Final Offer |
| CI | Clustered Index |
| DBE | Disadvantaged Business Enterprise |
| DMV | Dynamic Management View |
| FK | Foreign Key |
| GL | General Ledger |
| HUB | Historically Underutilized Business |
| IIS | Internet Information Services |
| MBE | Minority Business Enterprise |
| NC | Non-Clustered |
| OIDC | OpenID Connect |
| PK | Primary Key |
| REST | Representational State Transfer |
| SAML | Security Assertion Markup Language |
| SBE | Small Business Enterprise |
| SP | Stored Procedure |
| SSRS | SQL Server Reporting Services |
| TLS | Transport Layer Security |
| UDF | User-Defined Function |
| WBE | Women Business Enterprise |

---

## See Also

- [Quick Reference](quick-reference.md) - System overview
- [What is EDS](../business/what-is-eds.md) - System description

