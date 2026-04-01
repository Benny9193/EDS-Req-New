"""Tests for the role/approval level system and user context."""

import pytest
from unittest.mock import MagicMock, patch

from agent.security.roles import (
    ApprovalLevel,
    LEVEL_LABELS,
    Permission,
    UserContext,
    get_level_label,
    get_permissions_for_level,
)


# ── ApprovalLevel enum ──────────────────────────────────────────────


class TestApprovalLevel:
    def test_values(self):
        assert ApprovalLevel.REQUESTOR == 0
        assert ApprovalLevel.PRINCIPAL == 1
        assert ApprovalLevel.BUSINESS_ADMIN == 2
        assert ApprovalLevel.ACCOUNTING == 3
        assert ApprovalLevel.BUYER == 5
        assert ApprovalLevel.SUPPORT == 7
        assert ApprovalLevel.EDS_ADMIN == 8
        assert ApprovalLevel.SYSTEM_ADMIN == 9
        assert ApprovalLevel.TAB_HOUSE == 11

    def test_labels_defined_for_all_levels(self):
        for level in ApprovalLevel:
            assert level.value in LEVEL_LABELS


# ── Permission accumulation ──────────────────────────────────────────


class TestPermissions:
    def test_level_0_requestor(self):
        perms = get_permissions_for_level(0)
        assert Permission.REQ_CREATE in perms
        assert Permission.REQ_VIEW_OWN in perms
        assert Permission.PO_VIEW_OWN in perms
        # Should NOT have approval or admin
        assert Permission.REQ_APPROVE not in perms
        assert Permission.PO_CREATE not in perms
        assert Permission.SYSTEM_CONFIG not in perms
        assert Permission.AGENT_SQL_EXECUTE not in perms

    def test_level_1_principal(self):
        perms = get_permissions_for_level(1)
        # Inherits level 0
        assert Permission.REQ_CREATE in perms
        # Plus approval
        assert Permission.REQ_APPROVE in perms
        assert Permission.REQ_VIEW_SCHOOL in perms
        assert Permission.PO_VIEW_SCHOOL in perms
        # Not district-level
        assert Permission.REQ_VIEW_DISTRICT not in perms

    def test_level_2_business_admin(self):
        perms = get_permissions_for_level(2)
        assert Permission.REQ_APPROVE in perms  # inherited
        assert Permission.REQ_VIEW_DISTRICT in perms
        assert Permission.BUDGET_VIEW_DISTRICT in perms
        assert Permission.BUDGET_EDIT in perms

    def test_level_3_accounting(self):
        perms = get_permissions_for_level(3)
        assert Permission.REPORTS_ALL in perms
        assert Permission.AGENT_REPORTS in perms
        assert Permission.BUDGET_EDIT in perms  # inherited from level 2

    def test_level_5_buyer(self):
        perms = get_permissions_for_level(5)
        assert Permission.PO_CREATE in perms
        assert Permission.PO_CANCEL in perms
        assert Permission.BID_AWARD in perms
        assert Permission.BID_MANAGE in perms
        assert Permission.VENDOR_APPROVE in perms
        assert Permission.AGENT_SQL_EXECUTE in perms
        assert Permission.AGENT_SCHEMA_VIEW in perms
        # Not admin
        assert Permission.SYSTEM_CONFIG not in perms

    def test_level_9_system_admin(self):
        perms = get_permissions_for_level(9)
        # Has everything
        assert Permission.SYSTEM_CONFIG in perms
        assert Permission.ROLE_ASSIGN in perms
        assert Permission.AGENT_SQL_EXECUTE in perms
        assert Permission.AGENT_SQL_WRITE in perms
        assert Permission.PO_CREATE in perms
        assert Permission.REQ_APPROVE in perms

    def test_cumulative_inheritance(self):
        """Each level should have all permissions from lower levels."""
        prev_perms = set()
        for level in sorted(ApprovalLevel):
            current = get_permissions_for_level(level)
            assert prev_perms.issubset(current), (
                f"Level {level} missing inherited perms: {prev_perms - current}"
            )
            prev_perms = current


# ── UserContext ──────────────────────────────────────────────────────


class TestUserContext:
    def test_requestor_context(self):
        ctx = UserContext(user_id=100, approval_level=0, user_name="Jane Teacher")
        assert not ctx.can_approve()
        assert not ctx.can_execute_sql()
        assert not ctx.can_write_sql()
        assert not ctx.can_view_all_districts()
        assert ctx.level_label == "Requestor (Teacher/Staff)"

    def test_principal_context(self):
        ctx = UserContext(user_id=200, approval_level=1)
        assert ctx.can_approve()
        assert not ctx.can_execute_sql()
        assert ctx.has_permission(Permission.REQ_VIEW_SCHOOL)

    def test_buyer_context(self):
        ctx = UserContext(user_id=300, approval_level=5)
        assert ctx.can_approve()
        assert ctx.can_execute_sql()
        assert not ctx.can_write_sql()
        assert ctx.can_view_all_districts()

    def test_system_admin_context(self):
        ctx = UserContext(user_id=1, approval_level=9)
        assert ctx.can_approve()
        assert ctx.can_execute_sql()
        assert ctx.can_write_sql()
        assert ctx.can_view_all_districts()
        assert ctx.has_permission(Permission.SYSTEM_CONFIG)

    def test_to_prompt_context_requestor(self):
        ctx = UserContext(
            user_id=100, approval_level=0,
            user_name="Jane Teacher",
            school_name="Lincoln Elementary",
            school_id=42,
        )
        prompt = ctx.to_prompt_context()
        assert "Jane Teacher" in prompt
        assert "Requestor" in prompt
        assert "Level 0" in prompt
        assert "Own records only" in prompt
        assert "Cannot execute SQL" in prompt

    def test_to_prompt_context_principal(self):
        ctx = UserContext(
            user_id=200, approval_level=1,
            user_name="John Principal",
            school_id=42,
        )
        prompt = ctx.to_prompt_context()
        assert "approve requisitions" in prompt
        assert "School #42" in prompt

    def test_to_prompt_context_admin(self):
        ctx = UserContext(
            user_id=1, approval_level=9,
            user_name="Admin",
            district_name="Central District",
        )
        prompt = ctx.to_prompt_context()
        assert "System Administrator" in prompt
        assert "All districts" in prompt
        assert "system configuration" in prompt

    def test_permissions_auto_populated(self):
        ctx = UserContext(user_id=1, approval_level=5)
        assert len(ctx.permissions) > 0
        assert Permission.PO_CREATE in ctx.permissions


# ── Agent integration ────────────────────────────────────────────────


class TestAgentRoleIntegration:
    @patch("agent.core.agent.get_provider")
    def test_set_user_context(self, mock_provider):
        from agent.core.agent import EDSAgent

        mock_llm = MagicMock()
        mock_llm.model_name = "test"
        mock_provider.return_value = mock_llm

        agent = EDSAgent()
        agent.set_user_context(
            user_id=100,
            approval_level=0,
            user_name="Jane Teacher",
            school_id=42,
            school_name="Lincoln Elementary",
        )

        assert agent.user_context is not None
        assert agent.user_context.approval_level == 0
        assert not agent.user_context.can_execute_sql()

    @patch("agent.core.agent.get_provider")
    def test_status_includes_user(self, mock_provider):
        from agent.core.agent import EDSAgent

        mock_llm = MagicMock()
        mock_llm.model_name = "test"
        mock_provider.return_value = mock_llm

        agent = EDSAgent()
        agent._llm_provider = mock_llm
        agent._provider_name = "test"

        agent.set_user_context(user_id=1, approval_level=9, user_name="Admin")
        status = agent.get_status()
        assert "user" in status
        assert status["user"]["level"] == 9
        assert status["user"]["role"] == "System Administrator"

    @patch("agent.core.agent.get_provider")
    def test_no_user_context_status(self, mock_provider):
        from agent.core.agent import EDSAgent

        mock_llm = MagicMock()
        mock_llm.model_name = "test"
        mock_provider.return_value = mock_llm

        agent = EDSAgent()
        agent._llm_provider = mock_llm
        agent._provider_name = "test"

        status = agent.get_status()
        assert "user" not in status
