"""API routes for the EDS DBA Agent chatbot.

Provides REST and SSE streaming endpoints for the web-based chat UI.
"""

import asyncio
import json
import logging
from typing import Optional

from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/agent", tags=["agent"])

# Lazy-loaded agent singleton
_agent = None


def _get_agent():
    global _agent
    if _agent is None:
        from agent.core.agent import EDSAgent
        _agent = EDSAgent()
    return _agent


# ── Request/Response models ──────────────────────────────────────────


class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    mode: str = "chat"


class ChatResponse(BaseModel):
    content: str
    session_id: Optional[str] = None
    tool_calls: list = []
    sql_generated: Optional[str] = None
    error: Optional[str] = None
    metadata: dict = {}


class SessionResponse(BaseModel):
    id: str
    mode: str
    provider: str
    message_count: int
    updated_at: str


class NewSessionRequest(BaseModel):
    mode: str = "chat"


# ── Endpoints ────────────────────────────────────────────────────────


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Send a message to the agent and get a response."""
    from agent.core.agent import AgentMode

    agent = _get_agent()

    try:
        mode = AgentMode(request.mode)
    except ValueError:
        mode = AgentMode.CHAT

    response = await asyncio.to_thread(
        agent.chat,
        request.message,
        session_id=request.session_id,
        mode=mode,
    )

    return ChatResponse(
        content=response.content or "",
        session_id=request.session_id,
        tool_calls=response.tool_calls,
        sql_generated=response.sql_generated,
        error=response.error,
        metadata=response.metadata,
    )


@router.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    """Stream a response from the agent via Server-Sent Events."""
    agent = _get_agent()

    async def event_generator():
        try:
            # Run the streaming generator in a thread
            chunks = await asyncio.to_thread(
                lambda: list(agent.chat_stream(
                    request.message, session_id=request.session_id,
                ))
            )
            for chunk in chunks:
                data = json.dumps({"type": "chunk", "content": chunk})
                yield f"data: {data}\n\n"

            yield f"data: {json.dumps({'type': 'done'})}\n\n"

        except Exception as e:
            error_data = json.dumps({"type": "error", "content": str(e)})
            yield f"data: {error_data}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@router.get("/sessions")
async def list_sessions(limit: int = Query(default=20, le=50)):
    """List recent chat sessions."""
    agent = _get_agent()
    sessions = agent.sessions.list_sessions(limit=limit)

    return [
        SessionResponse(
            id=s.id,
            mode=s.mode,
            provider=s.provider,
            message_count=len(s.messages),
            updated_at=s.updated_at,
        )
        for s in sessions
    ]


@router.post("/sessions", response_model=SessionResponse)
async def create_session(request: NewSessionRequest):
    """Create a new chat session."""
    agent = _get_agent()
    session = agent.sessions.create_session(mode=request.mode)

    return SessionResponse(
        id=session.id,
        mode=session.mode,
        provider=session.provider,
        message_count=0,
        updated_at=session.updated_at,
    )


@router.get("/sessions/{session_id}/messages")
async def get_session_messages(session_id: str):
    """Get messages for a specific session."""
    agent = _get_agent()
    session = agent.sessions.get_session(session_id)

    if not session:
        return {"error": "Session not found", "messages": []}

    return {
        "session_id": session_id,
        "messages": [
            {
                "role": m.role,
                "content": m.content,
                "timestamp": m.timestamp,
            }
            for m in session.messages
        ],
    }


@router.delete("/sessions/{session_id}")
async def delete_session(session_id: str):
    """Delete a chat session."""
    agent = _get_agent()
    deleted = agent.sessions.delete_session(session_id)
    return {"deleted": deleted}


@router.get("/status")
async def agent_status():
    """Get agent status."""
    agent = _get_agent()
    return agent.get_status()
