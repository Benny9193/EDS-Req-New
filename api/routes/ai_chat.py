"""
AI Chat endpoint — conversational assistant with session support.

Uses the full EDSAgent with session management for multi-turn
conversations about the product catalog and database.
"""

import os
import json
import logging
import asyncio
from typing import Optional
from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

router = APIRouter(prefix="/chat", tags=["AI Chat"])
logger = logging.getLogger(__name__)

# Ollama keepalive: background task handle
_keepalive_task: Optional[asyncio.Task] = None

# Provider configuration: use LLM_PROVIDER env var, or auto-detect
# Falls back to "ollama" when no API key is set, "claude" when it is
_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
_LLM_PROVIDER = os.getenv("LLM_PROVIDER", "claude" if _API_KEY else "ollama")

# Feature flag: enabled when any provider is configured
# Claude requires API key; Ollama runs locally with no key
AI_CHAT_ENABLED = bool(_API_KEY) or _LLM_PROVIDER == "ollama"

# Keep agent instances per session (lightweight in-memory cache)
# In production, sessions are persisted by the agent's session_manager
_agent_cache: dict = {}
MAX_CACHED_AGENTS = 50

# Customer-facing system prompt for the web chat sidebar
# Overrides the default DBA-focused prompt in EDSAgent
WEB_CHAT_SYSTEM_PROMPT = """You are the EDS Shopping Assistant for the Educational Data Services Universal Requisition System.

You help school district staff find and order supplies. Be friendly, helpful, and concise.

IMPORTANT: You have tools to search the real product catalog database. ALWAYS use the search_products tool when users ask about products, supplies, or prices. ALWAYS use list_categories when they ask about categories. ALWAYS use search_vendors when they ask about vendors or suppliers. Never make up product names, prices, or SKUs — use your tools to get real data.

Your capabilities:
1. **Product Search**: Use the search_products tool to find real products by name, category, or description
2. **Price & Availability**: Use search_products to provide real pricing info
3. **Vendor Information**: Use search_vendors to find vendors and their catalogs
4. **Category Browsing**: Use list_categories to show available product categories
5. **Order Guidance**: Explain the ordering process, budget limits, and approval workflows

Guidelines:
- Be warm and conversational — you're helping teachers and school staff
- ALWAYS use your tools to look up real product data before responding about products
- Mention real prices and item codes from tool results
- If asked about something outside your scope, politely redirect
- Keep responses concise — a few sentences is usually enough
- Use bullet points for lists of products or options
- Format prices as dollar amounts (e.g., $4.99)

{context}"""


# ============================================
# Request / Response Models
# ============================================

class ChatRequest(BaseModel):
    """Request body for chat."""
    message: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="User message",
    )
    session_id: Optional[str] = Field(
        None,
        description="Session ID to continue a conversation (omit for new session)",
    )


class ChatMessage(BaseModel):
    """A single chat message."""
    role: str = Field(..., description="'user' or 'assistant'")
    content: str = Field(..., description="Message content")


class ChatResponse(BaseModel):
    """Response from the chat endpoint."""
    response: str = Field(..., description="Assistant's response text")
    session_id: str = Field(..., description="Session ID for continuing the conversation")
    sql_generated: Optional[str] = Field(None, description="SQL generated during the response")
    docs_retrieved: list[str] = Field(default_factory=list, description="Documentation snippets used")


# ============================================
# Agent Management
# ============================================

def _get_or_create_agent(session_id: Optional[str] = None):
    """
    Get an existing agent for a session, or create a new one.

    Returns (agent, session_id) tuple.
    """
    from agent.core.agent import EDSAgent

    if session_id and session_id in _agent_cache:
        agent = _agent_cache[session_id]
        return agent, session_id

    # Create a new agent with configured provider and web-friendly prompt
    agent = EDSAgent(provider_name=_LLM_PROVIDER, system_prompt=WEB_CHAT_SYSTEM_PROMPT)

    if session_id:
        # Try to resume an existing session
        try:
            actual_id = agent.start_session(session_id)
        except Exception:
            actual_id = agent.start_session()
    else:
        actual_id = agent.start_session()

    # Cache it (evict oldest if full)
    if len(_agent_cache) >= MAX_CACHED_AGENTS:
        oldest_key = next(iter(_agent_cache))
        try:
            _agent_cache[oldest_key].end_session()
        except Exception:
            pass
        del _agent_cache[oldest_key]

    _agent_cache[actual_id] = agent
    return agent, actual_id


def _remove_agent(session_id: str):
    """End and remove a cached agent session."""
    agent = _agent_cache.pop(session_id, None)
    if agent:
        try:
            agent.end_session()
        except Exception:
            pass


# ============================================
# Endpoints
# ============================================

@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Send a message to the AI assistant.

    Supports multi-turn conversations via session_id.
    Omit session_id to start a new conversation.

    Examples:
    - {"message": "What tables exist in the database?"}
    - {"message": "Show me the top 5 vendors by item count", "session_id": "abc-123"}
    - {"message": "Now filter those to only active ones", "session_id": "abc-123"}
    """
    if not AI_CHAT_ENABLED:
        raise HTTPException(
            status_code=503,
            detail="AI chat is not available. Configure ANTHROPIC_API_KEY or set LLM_PROVIDER=ollama.",
        )

    try:
        agent, session_id = _get_or_create_agent(request.session_id)

        # Send message to agent
        result = agent.chat(
            message=request.message,
            include_docs=True,
        )

        return ChatResponse(
            response=result.content,
            session_id=session_id,
            sql_generated=result.sql_generated,
            docs_retrieved=result.docs_retrieved,
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Chat failed: %s", e, exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Chat encountered an error",
        )


@router.post("/warmup")
async def warmup_model():
    """
    Pre-load the Ollama model into memory.

    Call this on app startup or before the first user interaction
    to avoid cold-start delays. Returns immediately if the model
    is already loaded or AI is not using Ollama.
    """
    if not AI_CHAT_ENABLED:
        return {"status": "skipped", "reason": "AI chat not enabled"}

    if _LLM_PROVIDER != "ollama":
        return {"status": "skipped", "reason": f"Using {_LLM_PROVIDER}, not Ollama"}

    ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "qwen2.5:14b")

    try:
        import httpx
    except ImportError:
        return {"status": "error", "reason": "httpx not installed"}

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(
                f"{ollama_host}/api/generate",
                json={
                    "model": model,
                    "prompt": "hello",
                    "stream": False,
                    "options": {"num_predict": 1},
                },
            )
            if resp.status_code == 200:
                logger.info("Model %s warmed up successfully", model)
                return {"status": "ok", "model": model, "message": "Model loaded and ready"}
            else:
                return {"status": "error", "reason": f"Ollama returned {resp.status_code}"}
    except Exception as e:
        logger.warning("Model warmup failed: %s", e)
        return {"status": "error", "reason": str(e)}


@router.post("/stream")
async def chat_stream(request: ChatRequest):
    """
    Streaming chat endpoint using Server-Sent Events.

    Returns text chunks in real-time as the assistant generates its response.
    Each SSE event is a JSON object with a 'type' field:
    - {"type": "chunk", "content": "..."} — partial response text
    - {"type": "done", "session_id": "..."} — stream complete
    - {"type": "error", "message": "..."} — error occurred
    """
    if not AI_CHAT_ENABLED:
        raise HTTPException(
            status_code=503,
            detail="AI chat is not available. Configure ANTHROPIC_API_KEY or set LLM_PROVIDER=ollama.",
        )

    try:
        agent, session_id = _get_or_create_agent(request.session_id)
    except Exception as e:
        logger.error("Failed to create agent for stream: %s", e, exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="Chat stream setup failed",
        )

    async def event_generator():
        try:
            for chunk in agent.chat_stream(message=request.message):
                # Special status markers from the agent (e.g., tool-call phases)
                if chunk.startswith("[STATUS:") and chunk.endswith("]"):
                    status_text = chunk[8:-1]
                    data = json.dumps({"type": "status", "content": status_text})
                else:
                    data = json.dumps({"type": "chunk", "content": chunk})
                yield f"data: {data}\n\n"

            data = json.dumps({"type": "done", "session_id": session_id})
            yield f"data: {data}\n\n"
        except Exception as e:
            logger.error("Chat stream error: %s", e, exc_info=True)
            # User-friendly error message
            if "connection" in str(e).lower() or "timeout" in str(e).lower():
                user_msg = "I'm having trouble connecting to the database. Please try again in a moment."
            elif "model" in str(e).lower() or "ollama" in str(e).lower():
                user_msg = "The AI model is temporarily unavailable. Please try again shortly."
            else:
                user_msg = "Something went wrong. Please try your question again."
            data = json.dumps({"type": "error", "message": user_msg})
            yield f"data: {data}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@router.delete("/{session_id}")
async def end_chat(session_id: str):
    """
    End a chat session.

    Cleans up the session state. The session_id cannot be reused after this.
    """
    _remove_agent(session_id)
    return {"status": "ok", "message": f"Session {session_id} ended"}


# ============================================
# Ollama Keepalive
# ============================================
# Ollama auto-unloads models after ~5 minutes of inactivity.
# This background task sends a tiny request every 4 minutes
# to keep the model warm and avoid cold-start timeouts.

KEEPALIVE_INTERVAL_SECONDS = 240  # 4 minutes


async def _ollama_keepalive_loop():
    """Background loop that pings Ollama to keep the model loaded."""
    try:
        import httpx
    except ImportError:
        logger.info("httpx not installed — Ollama keepalive disabled")
        return

    ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    model = os.getenv("OLLAMA_MODEL", "qwen2.5:14b")

    logger.info("Ollama keepalive started (model=%s, interval=%ds)", model, KEEPALIVE_INTERVAL_SECONDS)

    async with httpx.AsyncClient(timeout=30.0) as client:
        while True:
            await asyncio.sleep(KEEPALIVE_INTERVAL_SECONDS)
            try:
                # Minimal generate request to keep model in memory
                resp = await client.post(
                    f"{ollama_host}/api/generate",
                    json={
                        "model": model,
                        "prompt": "hi",
                        "stream": False,
                        "options": {"num_predict": 1},
                    },
                )
                if resp.status_code == 200:
                    logger.debug("Ollama keepalive ping OK")
                else:
                    logger.warning("Ollama keepalive ping returned %d", resp.status_code)
            except Exception as e:
                logger.debug("Ollama keepalive ping failed: %s", e)


def start_ollama_keepalive():
    """Start the Ollama keepalive background task (call from app startup)."""
    global _keepalive_task
    if _LLM_PROVIDER == "ollama" and AI_CHAT_ENABLED and _keepalive_task is None:
        _keepalive_task = asyncio.create_task(_ollama_keepalive_loop())


def stop_ollama_keepalive():
    """Stop the Ollama keepalive background task (call from app shutdown)."""
    global _keepalive_task
    if _keepalive_task is not None:
        _keepalive_task.cancel()
        _keepalive_task = None
