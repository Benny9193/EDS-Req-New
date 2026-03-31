"""
Saved lists persistence routes for EDS Universal Requisition.
Stores user-created supply lists server-side, keyed by session ID.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
import logging
import threading
import time

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/saved-lists", tags=["saved-lists"])

# In-memory store keyed by session_id
_lists_store: dict[str, list] = {}
_lists_lock = threading.Lock()


class SavedListItem(BaseModel):
    ItemNumber: Optional[str] = None
    Description: Optional[str] = None
    Price: Optional[float] = 0
    VendorName: Optional[str] = None
    quantity: int = 1


class SavedListPayload(BaseModel):
    name: str
    items: List[dict]


@router.get("/{session_id}")
async def get_saved_lists(session_id: str):
    """Get all saved lists for a session."""
    with _lists_lock:
        lists = _lists_store.get(session_id, [])
    return {"session_id": session_id, "lists": lists}


@router.post("/{session_id}")
async def save_list(session_id: str, payload: SavedListPayload):
    """Save a new list (or replace one with the same name)."""
    new_list = {
        "name": payload.name,
        "items": payload.items,
        "count": len(payload.items),
        "savedAt": time.strftime("%m/%d/%Y"),
    }
    with _lists_lock:
        user_lists = _lists_store.get(session_id, [])
        # Replace existing list with same name
        user_lists = [lst for lst in user_lists if lst["name"] != payload.name]
        user_lists.insert(0, new_list)
        _lists_store[session_id] = user_lists
    logger.info(f"Saved list '{payload.name}' for session {session_id}: {len(payload.items)} items")
    return new_list


@router.delete("/{session_id}/{list_name}")
async def delete_list(session_id: str, list_name: str):
    """Delete a saved list by name."""
    with _lists_lock:
        user_lists = _lists_store.get(session_id, [])
        _lists_store[session_id] = [lst for lst in user_lists if lst["name"] != list_name]
    return {"message": f"List '{list_name}' deleted"}
