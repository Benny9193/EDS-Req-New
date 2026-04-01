"""EDS role and approval level definitions.

Defines the approval level hierarchy, per-level permissions, and
user context for role-aware agent behavior. The agent uses this to
understand what the current user can see and do.

Approval Level Hierarchy (from ApprovalLevels table):
  Level 0  — Requestor (teacher/staff): create requisitions, view own orders
  Level 1  — Principal/Director/Supervisor: approve school-level requisitions
  Level 2  — Business Administrator: approve district-level, manage budgets
  Level 3  — Accounting: financial verification, budget oversight
  Level 5  — Customer Service Rep / Buyer: create POs, manage bids, vendor ops
  Level 7  — Support Personnel: technical support, system monitoring
  Level 8  — EDS Administration: EDS-wide admin functions
  Level 9  — System Administrator: full system access, role assignment
  Level 11 — Tab House: highest level (legacy)
"""

from dataclasses import dataclass, field
from enum import IntEnum
from typing import Dict, FrozenSet, List, Optional, Set


class ApprovalLevel(IntEnum):
    """Numeric approval levels from the ApprovalLevels table."""

    REQUESTOR = 0
    PRINCIPAL = 1
    BUSINESS_ADMIN = 2
    ACCOUNTING = 3
    BUYER = 5
    SUPPORT = 7
    EDS_ADMIN = 8
    SYSTEM_ADMIN = 9
    TAB_HOUSE = 11


# Human-readable labels
LEVEL_LABELS: Dict[int, str] = {
    ApprovalLevel.REQUESTOR: "Requestor (Teacher/Staff)",
    ApprovalLevel.PRINCIPAL: "Principal / Director / Supervisor",
    ApprovalLevel.BUSINESS_ADMIN: "Business Administrator",
    ApprovalLevel.ACCOUNTING: "Accounting",
    ApprovalLevel.BUYER: "Customer Service Rep / Buyer",
    ApprovalLevel.SUPPORT: "Support Personnel",
    ApprovalLevel.EDS_ADMIN: "EDS Administration",
    ApprovalLevel.SYSTEM_ADMIN: "System Administrator",
    ApprovalLevel.TAB_HOUSE: "Tab House",
}


class Permission:
    """Permission constants for the EDS system."""

    # Requisition permissions
    REQ_CREATE = "req_create"
    REQ_VIEW_OWN = "req_view_own"
    REQ_VIEW_SCHOOL = "req_view_school"
    REQ_VIEW_DISTRICT = "req_view_district"
    REQ_VIEW_ALL = "req_view_all"
    REQ_APPROVE = "req_approve"
    REQ_CANCEL = "req_cancel"

    # Purchase order permissions
    PO_VIEW_OWN = "po_view_own"
    PO_VIEW_SCHOOL = "po_view_school"
    PO_VIEW_DISTRICT = "po_view_district"
    PO_VIEW_ALL = "po_view_all"
    PO_CREATE = "po_create"
    PO_CANCEL = "po_cancel"

    # Bid/award permissions
    BID_VIEW = "bid_view"
    BID_AWARD = "bid_award"
    BID_MANAGE = "bid_manage"

    # Vendor permissions
    VENDOR_VIEW = "vendor_view"
    VENDOR_APPROVE = "vendor_approve"
    VENDOR_MANAGE = "vendor_manage"

    # Budget permissions
    BUDGET_VIEW_OWN = "budget_view_own"
    BUDGET_VIEW_DISTRICT = "budget_view_district"
    BUDGET_EDIT = "budget_edit"

    # Admin permissions
    USER_MANAGE = "user_manage"
    ROLE_ASSIGN = "role_assign"
    SYSTEM_CONFIG = "system_config"
    REPORTS_ALL = "reports_all"

    # Agent-specific permissions
    AGENT_SQL_EXECUTE = "agent_sql_execute"
    AGENT_SQL_WRITE = "agent_sql_write"
    AGENT_SCHEMA_VIEW = "agent_schema_view"
    AGENT_REPORTS = "agent_reports"


# Permissions granted at each approval level (cumulative — higher levels inherit lower)
_LEVEL_PERMISSIONS: Dict[int, FrozenSet[str]] = {
    ApprovalLevel.REQUESTOR: frozenset({
        Permission.REQ_CREATE,
        Permission.REQ_VIEW_OWN,
        Permission.PO_VIEW_OWN,
        Permission.BUDGET_VIEW_OWN,
        Permission.VENDOR_VIEW,
        Permission.BID_VIEW,
    }),
    ApprovalLevel.PRINCIPAL: frozenset({
        Permission.REQ_APPROVE,
        Permission.REQ_VIEW_SCHOOL,
        Permission.REQ_CANCEL,
        Permission.PO_VIEW_SCHOOL,
    }),
    ApprovalLevel.BUSINESS_ADMIN: frozenset({
        Permission.REQ_VIEW_DISTRICT,
        Permission.PO_VIEW_DISTRICT,
        Permission.BUDGET_VIEW_DISTRICT,
        Permission.BUDGET_EDIT,
    }),
    ApprovalLevel.ACCOUNTING: frozenset({
        Permission.REPORTS_ALL,
        Permission.AGENT_REPORTS,
    }),
    ApprovalLevel.BUYER: frozenset({
        Permission.PO_CREATE,
        Permission.PO_CANCEL,
        Permission.PO_VIEW_ALL,
        Permission.REQ_VIEW_ALL,
        Permission.BID_AWARD,
        Permission.BID_MANAGE,
        Permission.VENDOR_APPROVE,
        Permission.VENDOR_MANAGE,
        Permission.AGENT_SQL_EXECUTE,
        Permission.AGENT_SCHEMA_VIEW,
    }),
    ApprovalLevel.SUPPORT: frozenset({
        Permission.USER_MANAGE,
    }),
    ApprovalLevel.EDS_ADMIN: frozenset({
        Permission.AGENT_SQL_WRITE,
    }),
    ApprovalLevel.SYSTEM_ADMIN: frozenset({
        Permission.ROLE_ASSIGN,
        Permission.SYSTEM_CONFIG,
    }),
    ApprovalLevel.TAB_HOUSE: frozenset(),  # No additional permissions beyond level 9
}


def get_permissions_for_level(level: int) -> Set[str]:
    """Get the full set of permissions for an approval level (cumulative).

    Higher levels inherit all permissions from lower levels.
    """
    permissions: Set[str] = set()
    for lvl in sorted(_LEVEL_PERMISSIONS.keys()):
        if lvl <= level:
            permissions |= _LEVEL_PERMISSIONS[lvl]
    return permissions


def get_level_label(level: int) -> str:
    """Get a human-readable label for an approval level."""
    return LEVEL_LABELS.get(level, f"Unknown (Level {level})")


@dataclass
class UserContext:
    """Represents the current user's context for role-aware agent behavior.

    Loaded from the SessionTable when a user logs into the agent.
    """

    user_id: int
    approval_level: int
    district_id: Optional[int] = None
    school_id: Optional[int] = None
    user_name: str = ""
    district_name: str = ""
    school_name: str = ""
    permissions: Set[str] = field(default_factory=set)

    def __post_init__(self):
        if not self.permissions:
            self.permissions = get_permissions_for_level(self.approval_level)

    def has_permission(self, permission: str) -> bool:
        return permission in self.permissions

    def can_approve(self) -> bool:
        return self.has_permission(Permission.REQ_APPROVE)

    def can_execute_sql(self) -> bool:
        return self.has_permission(Permission.AGENT_SQL_EXECUTE)

    def can_write_sql(self) -> bool:
        return self.has_permission(Permission.AGENT_SQL_WRITE)

    def can_view_all_districts(self) -> bool:
        return self.approval_level >= ApprovalLevel.BUYER

    @property
    def level_label(self) -> str:
        return get_level_label(self.approval_level)

    def to_prompt_context(self) -> str:
        """Generate context string for injection into the agent system prompt."""
        lines = [
            f"Current user: {self.user_name or f'User #{self.user_id}'}",
            f"Role: {self.level_label} (Level {self.approval_level})",
        ]
        if self.district_name:
            lines.append(f"District: {self.district_name}")
        if self.school_name:
            lines.append(f"School: {self.school_name}")

        # Describe scope
        if self.can_view_all_districts():
            lines.append("Data scope: All districts")
        elif self.has_permission(Permission.REQ_VIEW_DISTRICT):
            lines.append(f"Data scope: District #{self.district_id}")
        elif self.has_permission(Permission.REQ_VIEW_SCHOOL):
            lines.append(f"Data scope: School #{self.school_id}")
        else:
            lines.append("Data scope: Own records only")

        # Key capabilities
        caps = []
        if self.can_approve():
            caps.append("approve requisitions")
        if self.has_permission(Permission.PO_CREATE):
            caps.append("create POs")
        if self.has_permission(Permission.BID_MANAGE):
            caps.append("manage bids")
        if self.has_permission(Permission.BUDGET_EDIT):
            caps.append("edit budgets")
        if self.has_permission(Permission.SYSTEM_CONFIG):
            caps.append("system configuration")
        if caps:
            lines.append(f"Can: {', '.join(caps)}")

        # Agent-specific restrictions
        restrictions = []
        if not self.can_execute_sql():
            restrictions.append("Cannot execute SQL queries directly")
        if not self.can_write_sql():
            restrictions.append("SQL queries are read-only")
        if not self.has_permission(Permission.AGENT_REPORTS):
            restrictions.append("Cannot generate reports")
        if restrictions:
            lines.append("Restrictions: " + "; ".join(restrictions))

        return "\n".join(lines)
