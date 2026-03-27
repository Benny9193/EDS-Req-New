"""
Cart persistence routes for EDS Universal Requisition.
Stores cart data server-side keyed by session ID.
"""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional, Any, Union
import logging
import threading

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/cart", tags=["cart"])

# In-memory cart store keyed by session_id (str to support demo mode)
_cart_store: dict[str, list] = {}
_cart_lock = threading.Lock()


class CartItem(BaseModel):
    """A single cart item."""
    ItemNumber: Optional[str] = None
    item_number: Optional[str] = None
    id: Optional[Any] = None
    name: Optional[str] = None
    description: Optional[str] = None
    Price: Optional[float] = None
    price: Optional[float] = None
    UnitPrice: Optional[float] = None
    quantity: int = 1
    vendor: Optional[str] = None
    VendorName: Optional[str] = None
    category: Optional[str] = None


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
    with _cart_lock:
        cart = _cart_store.get(session_id, [])
    return {"session_id": session_id, "cart": cart}


@router.put("/{session_id}")
async def save_cart(session_id: str, payload: CartPayload):
    """Save/replace the entire cart for a session."""
    if str(payload.session_id) != session_id:
        raise HTTPException(status_code=400, detail="Session ID mismatch")
    with _cart_lock:
        _cart_store[session_id] = payload.cart
    logger.info(f"Cart saved for session {session_id}: {len(payload.cart)} items")
    return {"session_id": session_id, "cart": payload.cart, "item_count": len(payload.cart)}


@router.delete("/{session_id}")
async def clear_cart(session_id: str):
    """Clear the cart for a session."""
    with _cart_lock:
        _cart_store.pop(session_id, None)
    return {"session_id": session_id, "cart": [], "message": "Cart cleared"}
