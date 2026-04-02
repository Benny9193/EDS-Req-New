"""Context window management and conversation summarization.

Enforces token budgets across system prompt, history, documentation,
and learned context. When history gets too long, older messages are
summarized via the LLM to compress the conversation.
"""

import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

SUMMARY_PROMPT = """You are summarizing a conversation between a database administrator and an AI assistant.
Create a concise summary that captures:
1. The main questions or tasks discussed
2. Key SQL queries generated or executed
3. Important findings or conclusions
4. Any user preferences or patterns observed
5. Database tables or procedures referenced

Keep the summary under 500 words and focus on information useful for continuing the conversation."""


class ContextWindowManager:
    """Manages token budgets to keep messages within the LLM context window.

    Truncates history (oldest first) and documentation (lowest-score first)
    to fit within allocated budgets.
    """

    def __init__(
        self,
        total_budget: int = 100_000,
        system_budget: int = 2_000,
        doc_budget: int = 15_000,
        history_budget: int = 60_000,
        learned_context_budget: int = 3_000,
        response_buffer: int = 4_000,
    ):
        self.total_budget = total_budget
        self.system_budget = system_budget
        self.doc_budget = doc_budget
        self.history_budget = history_budget
        self.learned_context_budget = learned_context_budget
        self.response_buffer = response_buffer

    def _estimate_tokens(self, text: str) -> int:
        return len(text) // 4

    def trim_history(
        self,
        messages: List[Dict[str, str]],
        summary: Optional[str] = None,
    ) -> List[Dict[str, str]]:
        """Trim conversation history to fit within history_budget.

        Drops oldest messages first. If a summary is provided, it's prepended
        as a system-level context message.
        """
        budget = self.history_budget
        if summary:
            budget -= self._estimate_tokens(summary)

        # Work backwards from most recent, accumulating tokens
        kept = []
        used = 0
        for msg in reversed(messages):
            tokens = self._estimate_tokens(msg.get("content", ""))
            if used + tokens > budget:
                break
            kept.append(msg)
            used += tokens

        kept.reverse()

        if summary and kept:
            kept.insert(0, {
                "role": "system",
                "content": f"[Previous conversation summary]\n{summary}",
            })

        return kept

    def trim_docs(
        self,
        docs: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """Trim retrieved documents to fit within doc_budget.

        Assumes docs are sorted by relevance (best first). Drops lowest-scored
        docs that exceed the budget.
        """
        kept = []
        used = 0
        for doc in docs:
            tokens = self._estimate_tokens(doc.get("content", ""))
            if used + tokens > self.doc_budget:
                break
            kept.append(doc)
            used += tokens
        return kept

    def trim_learned_context(self, context: str) -> str:
        """Truncate learned context to fit within budget."""
        max_chars = self.learned_context_budget * 4
        if len(context) > max_chars:
            return context[:max_chars] + "\n[...truncated]"
        return context

    def get_available_tokens(
        self,
        system_tokens: int = 0,
        history_tokens: int = 0,
        doc_tokens: int = 0,
    ) -> int:
        """Calculate remaining tokens available for the response."""
        used = system_tokens + history_tokens + doc_tokens + self.response_buffer
        return max(0, self.total_budget - used)


class ConversationSummarizer:
    """Summarizes conversation history using the LLM.

    Triggered when both message count and token thresholds are exceeded.
    """

    def __init__(self, provider_name: str = "claude"):
        self._provider_name = provider_name

    def should_summarize(
        self,
        messages: List,
        threshold_messages: int = 30,
        threshold_tokens: int = 50_000,
    ) -> bool:
        """Check if summarization is needed."""
        if len(messages) < threshold_messages:
            return False

        total_tokens = sum(len(m.get("content", "")) // 4 for m in messages)
        return total_tokens >= threshold_tokens

    def summarize(
        self,
        messages: List[Dict[str, str]],
    ) -> str:
        """Summarize a list of conversation messages.

        Returns a concise summary string suitable for prepending to
        future conversations.
        """
        from agent.llm.base import Message, MessageRole
        from agent.llm.registry import get_provider
        from agent.config import get_llm_config

        # Build the conversation text to summarize
        conversation = []
        for msg in messages:
            role = msg.get("role", "unknown")
            content = msg.get("content", "")
            conversation.append(f"{role}: {content}")

        conversation_text = "\n\n".join(conversation)

        # Truncate if extremely long (summarize in chunks if needed)
        max_chars = 100_000
        if len(conversation_text) > max_chars:
            conversation_text = conversation_text[:max_chars] + "\n[...truncated]"

        prompt = f"{SUMMARY_PROMPT}\n\nConversation:\n{conversation_text}"

        try:
            provider_config = get_llm_config(self._provider_name)
            provider = get_provider(self._provider_name, provider_config)

            llm_messages = [
                Message(role=MessageRole.USER, content=prompt),
            ]
            response = provider.complete(llm_messages, temperature=0.0, max_tokens=1024)
            return response.content.strip()

        except Exception as e:
            logger.error("Summarization failed: %s", e)
            # Fallback: just list the topics discussed
            topics = set()
            for msg in messages:
                content = msg.get("content", "").lower()
                for keyword in ["vendor", "table", "query", "index", "procedure",
                                "order", "requisition", "budget", "report"]:
                    if keyword in content:
                        topics.add(keyword)
            if topics:
                return f"Previous discussion covered: {', '.join(sorted(topics))}"
            return "Previous conversation context (summary unavailable)"
