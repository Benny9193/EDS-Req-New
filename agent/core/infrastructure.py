"""EDS infrastructure knowledge — Azure, SQL Server, Kubernetes, Elasticsearch.

Bakes production infrastructure awareness into the agent so it can answer
questions about the environment, diagnose issues in context, and generate
queries that respect the actual server topology.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


# ── SQL Server ───────────────────────────────────────────────────────

@dataclass
class SQLServerInfo:
    fqdn: str = "eds-sqlserver.eastus2.cloudapp.azure.com"
    port: int = 1433
    version: str = "SQL Server 2017 Enterprise (14.0.3520.4)"
    vm_size: str = "Standard_D16s_v3"
    vcpus: int = 16
    memory_gb: int = 64
    max_server_memory_gb: int = 52
    max_dop: int = 4
    cost_threshold: int = 50
    region: str = "East US 2"
    backup_full: str = "Daily 4 AM"
    backup_diff: str = "Every 4 hours"
    backup_log: str = "Every 15 minutes"
    recovery_model: str = "FULL"


@dataclass
class DatabaseInfo:
    name: str
    size: str
    tables: int = 0
    views: int = 0
    procs: int = 0
    purpose: str = ""


DATABASES: List[DatabaseInfo] = [
    DatabaseInfo("EDS", "1.48 TB", 439, 475, 396, "Primary production — products, vendors, categories, users, sessions, requisitions, orders, bids"),
    DatabaseInfo("dpa_EDSAdmin", "~50 GB", 207, 0, 0, "SolarWinds DPA monitoring — performance metrics, blocking events, wait stats"),
    DatabaseInfo("Catalogs", "224 GB", 25, 0, 45, "Production catalog data"),
    DatabaseInfo("VendorBids", "109 GB", 41, 23, 72, "Vendor bidding system"),
    DatabaseInfo("SearchData", "92 GB", 9, 0, 1, "Search index data"),
    DatabaseInfo("ContentCentral", "56 GB", 134, 7, 0, "Content/document management"),
    DatabaseInfo("WorkTables", "31 GB", 264, 0, 0, "Work/staging data"),
    DatabaseInfo("Documents", "6.8 GB", 39, 15, 12, "Document storage"),
    DatabaseInfo("EDS_Test", "1.22 TB", 0, 0, 0, "Full test copy"),
    DatabaseInfo("EDS_TEST_Old", "1.12 TB", 0, 0, 0, "Old test copy (cleanup candidate)"),
    DatabaseInfo("VendorBids_TEST", "99 GB", 0, 0, 0, "Test copy"),
    DatabaseInfo("NJ_RTK", "256 MB", 9, 6, 3, "NJ Right to Know"),
    DatabaseInfo("ProcurementAnalytics", "144 MB", 13, 0, 0, "Analytics DB"),
]


# ── Critical Tables ──────────────────────────────────────────────────

@dataclass
class CriticalTable:
    name: str
    rows: str
    domain: str
    notes: str = ""


CRITICAL_TABLES: List[CriticalTable] = [
    CriticalTable("CrossRefs", "150.6M", "Inventory", "Item→Vendor mapping. BLOCKING HOTSPOT — KI-004"),
    CriticalTable("Items", "30.1M", "Inventory", "Master product catalog"),
    CriticalTable("Detail", "30.8M", "Orders", "Line items on requisitions/POs. trig_DetailUpdate causes blocking — KI-003"),
    CriticalTable("Requisitions", "2.1M", "Orders", "Purchase request headers"),
    CriticalTable("Vendors", "18.9K", "Vendors", "Supplier database"),
    CriticalTable("Category", "12.9K", "Inventory", "Product classification"),
    CriticalTable("School", "12.9K", "Users", "Individual schools/departments"),
    CriticalTable("Users", "28.6K", "Security", "User accounts. SSO deadlocks — KI-005"),
    CriticalTable("District", "3.5K", "Org", "School districts"),
    CriticalTable("BidHeaders", "~50K", "Bidding", "Bid header records — use BidHeaderId not BidHeaderKey"),
    CriticalTable("PurchaseOrders", "~2M", "Orders", "PO headers"),
    CriticalTable("PurchaseOrderDetails", "~8M", "Orders", "PO line items"),
    CriticalTable("Approvals", "~3M", "Orders", "Approval decisions with Level field"),
    CriticalTable("SessionTable", "~100K", "Security", "Active login sessions with ApprovalLevel"),
]


# ── Known Issues ─────────────────────────────────────────────────────

@dataclass
class KnownIssue:
    id: str
    title: str
    severity: str  # "CRITICAL", "HIGH", "MEDIUM", "LOW"
    description: str
    root_cause: str
    mitigation: str


KNOWN_ISSUES: List[KnownIssue] = [
    KnownIssue(
        "KI-001", "usp_GetIndexData extreme execution time", "CRITICAL",
        "24+ hours execution time, 15.5% of total DB time. 33M row scans on BidResults.",
        "Parameter sniffing (19 different plans), expensive functions (String_Agg, ufn_RegExReplace), no covering indexes.",
        "Add OPTION (RECOMPILE), create covering indexes on BidResults and PricingConsolidated.",
    ),
    KnownIssue(
        "KI-002", "Vendor Sync Job wasting 59 hrs/month", "HIGH",
        "Full table scan comparison every hour, 24/7, regardless of changes.",
        "No change detection (no LastModified timestamp or CDC).",
        "Reduce frequency to 4x/day or implement Change Data Capture.",
    ),
    KnownIssue(
        "KI-003", "trig_DetailUpdate blocking (up to 82 min)", "HIGH",
        "Complex trigger holds locks during price lookups from CrossRefs, item remapping, vendor matching.",
        "Lock escalation (row→page→table), function calls while locks held.",
        "Add NOLOCK hints for reads in trigger, move non-critical logic to async.",
    ),
    KnownIssue(
        "KI-004", "CrossRef lookup blocking (12+ hours accumulated)", "MEDIUM",
        "Simple lookups <10ms becoming 737 minutes blocked due to upstream blockers.",
        "Victim of KI-003 and bulk operations. CrossRefs (150.6M rows) lacks covering index.",
        "Fix KI-003 first, then add covering index on CrossRefs.",
    ),
    KnownIssue(
        "KI-005", "SSO user update deadlocks (20/month)", "MEDIUM",
        "Parallel SSO updates from same K8s pod cause page-level deadlocks on Users table.",
        "No unique index on Email, parallel updates from eds-edsiq-2 pod.",
        "Serialize SSO updates in app layer. Create UNIQUE INDEX on Users(Email, Active) WHERE Active=1.",
    ),
]


# ── Azure / Kubernetes ───────────────────────────────────────────────

@dataclass
class KubernetesCluster:
    name: str
    resource_group: str
    k8s_version: str
    nodes: int
    purpose: str


K8S_CLUSTERS: List[KubernetesCluster] = [
    KubernetesCluster("eds-aks-prod", "eds-prod-rg", "1.32.11", 13, "Production (8 Linux + 5 Windows nodes)"),
    KubernetesCluster("eds-aks-uat", "eds-uat-rg", "1.32.11", 12, "UAT/Staging (7 Linux + 5 Windows nodes)"),
]


@dataclass
class ElasticsearchInfo:
    host: str = "20.122.81.233"
    port: int = 9200
    version: str = "7.15.2"
    active_alias: str = "pricing_consolidated_active"
    active_underlying_index: str = "pricing_consolidated_60"
    active_docs: str = "18.6M"
    active_size: str = "73.2 GB"
    total_indices: int = 44
    auth: str = "NONE (CRITICAL SECURITY ISSUE)"
    tls: str = "NONE"


@dataclass
class ServiceEndpoint:
    name: str
    namespace: str
    ip: str
    purpose: str


PROD_SERVICES: List[ServiceEndpoint] = [
    ServiceEndpoint("eds-edsiq", "eds-web-app", "52.251.10.10", "Main EDSIQ web app (CFML/Lucee)"),
    ServiceEndpoint("eds-edsiq-2", "eds-web-app", "4.153.197.31", "Secondary EDSIQ instance"),
    ServiceEndpoint("eds-dms", "eds-web-app", "20.10.230.104", "Document Management System"),
    ServiceEndpoint("eds-edsiq-asp", "eds-web-asp", "20.96.100.30", "Legacy ASP.NET endpoints"),
    ServiceEndpoint("eds-admin-portal", "eds-admin-portal", "4.153.107.44", "Admin portal"),
    ServiceEndpoint("eds-po", "eds-po", "52.177.80.178", "Purchase Order processing"),
    ServiceEndpoint("eds-querylite", "eds-querylite", "172.193.27.238", "Query Lite service"),
    ServiceEndpoint("eds-sds", "eds-sds", "4.153.101.19", "Safety Data Sheets"),
    ServiceEndpoint("eds-vendorbids", "eds-vendorbids", "4.152.73.254", "Vendor bidding system"),
    ServiceEndpoint("eds-nodeindexer", "eds-database", "172.175.208.125", "Search index builder"),
    ServiceEndpoint("eds-documentviewer", "eds-java-service", "20.186.83.121", "Document viewer"),
    ServiceEndpoint("eds-potransmitter", "eds-java-service", "4.152.239.185", "PO transmission to vendors"),
    ServiceEndpoint("eds-report-handler", "eds-java-service", "20.96.132.103", "Report generation"),
]


# ── Service Accounts ─────────────────────────────────────────────────

DB_ACCOUNTS: Dict[str, str] = {
    "EDSIQWebUser": "Web application (214+ hrs/month). db_datareader, db_datawriter, execute SPs.",
    "EDSAdmin": "Administrative. Full permissions + DDL.",
    "DPA Monitor": "SolarWinds monitoring (24/7). db_datareader only.",
    "Job Processor": "Background jobs (hourly/daily). db_datareader, db_datawriter, execute SPs.",
    "Integration Service Account": "SSO sync, HR sync. db_datareader, db_datawriter.",
}


# ── Usage Patterns ───────────────────────────────────────────────────

PEAK_HOURS = {
    "morning": "8:00-10:00 AM Eastern",
    "afternoon": "1:00-3:00 PM Eastern",
    "batch": "9:00-11:00 PM Eastern",
    "maintenance_window": "12:00-6:00 AM Eastern (lowest usage)",
}

ANNUAL_CYCLE = {
    "august": "Very High — back-to-school ordering",
    "september": "High — school start continuation",
    "october_may": "Normal operations",
    "june": "Very High — fiscal year-end close",
    "july": "Low — summer break",
}


# ── Monitoring Thresholds ────────────────────────────────────────────

HEALTH_THRESHOLDS = {
    "blocking_critical_minutes": 10,
    "blocking_warn_minutes": 5,
    "deadlock_investigate": 1,  # any deadlock warrants investigation
    "io_latency_warn_ms": 50,
    "io_latency_critical_ms": 100,
    "slow_query_buffer_gets": 10_000_000,
    "missing_index_impact_pct": 95,
    "disk_warn_pct": 20,
    "disk_critical_pct": 10,
    "connection_pool_warn_pct": 80,
}


# ── Context Generation ───────────────────────────────────────────────


def get_infrastructure_prompt() -> str:
    """Generate infrastructure context for the agent's system prompt."""
    sql = SQLServerInfo()
    es = ElasticsearchInfo()

    lines = [
        "=== EDS INFRASTRUCTURE CONTEXT ===",
        "",
        f"SQL Server: {sql.fqdn}:{sql.port}",
        f"  Version: {sql.version}",
        f"  VM: {sql.vm_size} ({sql.vcpus} vCPUs, {sql.memory_gb}GB RAM, {sql.max_server_memory_gb}GB for SQL)",
        f"  Max DOP: {sql.max_dop}, Cost Threshold: {sql.cost_threshold}",
        f"  Region: {sql.region}",
        "",
        "Databases (22 total, ~4.5 TB):",
    ]
    for db in DATABASES[:8]:  # Top 8 by importance
        lines.append(f"  - {db.name} ({db.size}): {db.purpose}")

    lines.extend([
        "",
        "Critical Tables:",
    ])
    for t in CRITICAL_TABLES[:8]:
        note = f" — {t.notes}" if t.notes else ""
        lines.append(f"  - {t.name} ({t.rows} rows, {t.domain}){note}")

    lines.extend([
        "",
        "Known Issues:",
    ])
    for ki in KNOWN_ISSUES:
        lines.append(f"  - [{ki.severity}] {ki.id}: {ki.title}")
        lines.append(f"    Mitigation: {ki.mitigation}")

    lines.extend([
        "",
        f"Elasticsearch: {es.host}:{es.port} (v{es.version})",
        f"  Active alias: {es.active_alias} → {es.active_underlying_index} ({es.active_docs} docs, {es.active_size})",
        f"  Always use the alias '{es.active_alias}' in queries, never the underlying index name.",
        f"  WARNING: {es.auth}",
        "",
        "Kubernetes: 2 AKS clusters (prod: 13 nodes, uat: 12 nodes) in East US 2",
        f"  {len(PROD_SERVICES)} production services across {len(set(s.namespace for s in PROD_SERVICES))} namespaces",
        "",
        f"Peak hours: {PEAK_HOURS['morning']}, {PEAK_HOURS['afternoon']}",
        f"Maintenance window: {PEAK_HOURS['maintenance_window']}",
        "",
        "When diagnosing performance issues, check known issues first (KI-001 through KI-005).",
        "When suggesting maintenance windows, use 12-6 AM Eastern.",
        "Budget year: Dec 1 – Nov 30. Most recent completed: Dec 1, 2024 – Nov 30, 2025.",
    ])

    return "\n".join(lines)


def get_known_issue(issue_id: str) -> Optional[KnownIssue]:
    """Look up a known issue by ID."""
    for ki in KNOWN_ISSUES:
        if ki.id.upper() == issue_id.upper():
            return ki
    return None


def get_database_info(db_name: str) -> Optional[DatabaseInfo]:
    """Look up database info by name."""
    for db in DATABASES:
        if db.name.lower() == db_name.lower():
            return db
    return None
