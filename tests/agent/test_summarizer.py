"""Tests for the context window manager and conversation summarizer."""

import pytest
from unittest.mock import MagicMock, patch

from agent.memory.summarizer import ContextWindowManager, ConversationSummarizer


# ── ContextWindowManager ─────────────────────────────────────────────


class TestContextWindowManager:
    @pytest.fixture
    def mgr(self):
        return ContextWindowManager(
            total_budget=10_000,
            history_budget=5_000,
            doc_budget=2_000,
            learned_context_budget=500,
        )

    def test_trim_history_within_budget(self, mgr):
        msgs = [
            {"role": "user", "content": "short message"},
            {"role": "assistant", "content": "short reply"},
        ]
        trimmed = mgr.trim_history(msgs)
        assert len(trimmed) == 2

    def test_trim_history_drops_oldest(self, mgr):
        # Create messages that exceed history_budget
        msgs = [
            {"role": "user", "content": f"Message {i} " + "x" * 2000}
            for i in range(20)
        ]
        trimmed = mgr.trim_history(msgs)
        assert len(trimmed) < len(msgs)
        # Most recent should be kept
        assert "Message 19" in trimmed[-1]["content"]

    def test_trim_history_with_summary(self, mgr):
        msgs = [
            {"role": "user", "content": "hello"},
            {"role": "assistant", "content": "hi"},
        ]
        summary = "Previously discussed vendor queries."
        trimmed = mgr.trim_history(msgs, summary=summary)
        assert trimmed[0]["role"] == "system"
        assert "Previously discussed" in trimmed[0]["content"]

    def test_trim_docs_within_budget(self, mgr):
        docs = [
            {"content": "Short doc", "score": 0.9},
            {"content": "Another short doc", "score": 0.8},
        ]
        trimmed = mgr.trim_docs(docs)
        assert len(trimmed) == 2

    def test_trim_docs_drops_lowest_scored(self, mgr):
        docs = [
            {"content": "x" * 4000, "score": 0.9},
            {"content": "y" * 4000, "score": 0.8},
            {"content": "z" * 4000, "score": 0.7},
        ]
        trimmed = mgr.trim_docs(docs)
        assert len(trimmed) < len(docs)
        # Best scored should be kept first
        assert trimmed[0]["content"].startswith("x")

    def test_trim_learned_context(self, mgr):
        short = "Some preferences"
        assert mgr.trim_learned_context(short) == short

    def test_trim_learned_context_truncates(self, mgr):
        long = "x" * 10_000
        trimmed = mgr.trim_learned_context(long)
        assert len(trimmed) < len(long)
        assert trimmed.endswith("[...truncated]")

    def test_get_available_tokens(self, mgr):
        available = mgr.get_available_tokens(
            system_tokens=500, history_tokens=2000, doc_tokens=500,
        )
        # total_budget(10000) - 500 - 2000 - 500 - response_buffer(4000) = 3000
        assert available == 3000

    def test_get_available_tokens_no_negative(self, mgr):
        available = mgr.get_available_tokens(
            system_tokens=5000, history_tokens=5000, doc_tokens=5000,
        )
        assert available == 0


# ── ConversationSummarizer ───────────────────────────────────────────


class TestConversationSummarizer:
    def test_should_summarize_under_threshold(self):
        s = ConversationSummarizer()
        msgs = [{"role": "user", "content": "hi"}] * 10
        assert s.should_summarize(msgs) is False

    def test_should_summarize_messages_threshold(self):
        s = ConversationSummarizer()
        msgs = [{"role": "user", "content": "hi"}] * 35
        # 35 messages but very few tokens — won't trigger
        assert s.should_summarize(msgs) is False

    def test_should_summarize_both_thresholds(self):
        s = ConversationSummarizer()
        # 35 messages with enough tokens (each ~500 tokens = ~2000 chars)
        msgs = [{"role": "user", "content": "x" * 6000}] * 35
        assert s.should_summarize(msgs) is True

    @patch("agent.llm.registry.get_provider")
    @patch("agent.config.get_llm_config")
    def test_summarize_calls_llm(self, mock_config, mock_provider):
        from agent.llm.base import LLMResponse

        mock_config.return_value = {}
        mock_llm = MagicMock()
        mock_llm.complete.return_value = LLMResponse(
            content="The user asked about vendor tables and received SQL queries.",
            model="test",
        )
        mock_provider.return_value = mock_llm

        s = ConversationSummarizer()
        msgs = [
            {"role": "user", "content": "What vendor tables exist?"},
            {"role": "assistant", "content": "The Vendors table has VendorId, VendorName..."},
        ]
        summary = s.summarize(msgs)
        assert "vendor" in summary.lower()

    def test_summarize_fallback_on_error(self):
        s = ConversationSummarizer(provider_name="nonexistent")
        msgs = [
            {"role": "user", "content": "Tell me about vendor queries"},
            {"role": "assistant", "content": "Here is a query for vendors"},
        ]
        # Should not raise, should fall back to keyword extraction
        summary = s.summarize(msgs)
        assert isinstance(summary, str)
        assert len(summary) > 0


# ── Agent integration ────────────────────────────────────────────────


class TestContextManagerAgentIntegration:
    @patch("agent.core.agent.get_provider")
    def test_context_manager_property(self, mock_provider):
        from agent.core.agent import EDSAgent

        mock_llm = MagicMock()
        mock_llm.model_name = "test"
        mock_provider.return_value = mock_llm

        agent = EDSAgent()
        mgr = agent.context_manager
        assert mgr is not None
        assert mgr.history_budget > 0

    @patch("agent.core.agent.get_provider")
    def test_learned_context_trimmed(self, mock_provider):
        from agent.core.agent import EDSAgent

        mock_llm = MagicMock()
        mock_llm.model_name = "test"
        mock_llm.complete.return_value = MagicMock(
            content="response", model="test", tool_calls=[],
            usage={"input_tokens": 10, "output_tokens": 5},
        )
        mock_provider.return_value = mock_llm

        agent = EDSAgent(config={"memory": {"learned_context_budget": 100}})
        agent._llm_provider = mock_llm
        agent._provider_name = "test"

        # Chat should work even with context manager active
        response = agent.chat("hello")
        assert response.content == "response"
