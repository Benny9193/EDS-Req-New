"""
Cart persistence routes for EDS Universal Requisition.
Stores cart data server-side keyed by session ID.
"""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Union
import asyncio
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/cart", tags=["cart"])

# In-memory cart store keyed by session_id (str to support demo mode)
_cart_store: dict[str, list] = {}
_cart_lock = asyncio.Lock()


class CartPayload(BaseModel):
    """Full cart replacement payload."""
    session_id: Union[int, str]
    cart: List[dict]


class CartResponse(BaseModel):
    """Cart response."""
    session_id: Union[int, str]
    cart: List[dict]


@router.get("/{session_id}")
async def get_cart(session_id: str):
    """Get the cart for a session."""
    async with _cart_lock:
        cart = _cart_store.get(session_id, [])
    return {"session_id": session_id, "cart": cart}


@router.put("/{session_id}")
async def save_cart(session_id: str, payload: CartPayload):
    """Save/replace the entire cart for a session."""
    if str(payload.session_id) != session_id:
        raise HTTPException(status_code=400, detail="Session ID mismatch")
    async with _cart_lock:
        _cart_store[session_id] = payload.cart
    logger.info("Cart saved for session %s: %d items", session_id, len(payload.cart))
    return {"session_id": session_id, "cart": payload.cart, "item_count": len(payload.cart)}


@router.delete("/{session_id}")
async def clear_cart(session_id: str):
    """Clear the cart for a session."""
    async with _cart_lock:
        _cart_store.pop(session_id, None)
    return {"session_id": session_id, "cart": [], "message": "Cart cleared"}
