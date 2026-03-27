"""
Template Orders API endpoints.

Provides default and user-created order templates with real catalog product references.
"""

import uuid
import logging
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

from ..database import execute_query
from ..cache import get_cache, CACHE_TTL_LONG

router = APIRouter(prefix="/templates", tags=["Templates"])
logger = logging.getLogger(__name__)

# In-memory store for user-created templates (keyed by session_id)
_user_templates: dict = {}


class TemplateItem(BaseModel):
    item_id: int
    item_code: str
    name: str
    price: float
    qty: int
    vendor: str
    unit: str = "Each"


class Template(BaseModel):
    id: str
    name: str
    category: str
    icon: str
    color: str
    description: str
    items: List[TemplateItem]
    is_default: bool = True


class CreateTemplateRequest(BaseModel):
    name: str
    category: str = "Custom"
    description: str = ""
    items: List[dict]


# Default template definitions with real ItemIds from the catalog
DEFAULT_TEMPLATE_DEFS = [
    {
        "id": "elem-classroom", "name": "Elementary Classroom Basics", "category": "Classroom",
        "icon": "fas fa-school", "color": "var(--eds-primary)",
        "description": "Essential supplies for a K-5 classroom: pencils, crayons, notebooks, folders, and glue sticks.",
        "item_ids": [3904313, 3812687, 4096096, 3710179, 3296743],
        "qtys": [4, 2, 6, 10, 3]
    },
    {
        "id": "hs-classroom", "name": "High School Starter Kit", "category": "Classroom",
        "icon": "fas fa-graduation-cap", "color": "#6366f1",
        "description": "Standard supplies for secondary classrooms: binders, paper, pens, highlighters, and calculators.",
        "item_ids": [4387297, 6426535, 2168179, 4396832, 2816594],
        "qtys": [5, 4, 3, 2, 2]
    },
    {
        "id": "office-basics", "name": "Administrative Office", "category": "Office",
        "icon": "fas fa-print", "color": "#059669",
        "description": "Front office and admin essentials: copy paper, toner, staples, sticky notes, and file folders.",
        "item_ids": [2169998, 3100685, 3740582, 3083813, 9519686],
        "qtys": [5, 2, 2, 1, 1]
    },
    {
        "id": "art-supplies", "name": "Art Room Essentials", "category": "Art & Music",
        "icon": "fas fa-paint-brush", "color": "#ec4899",
        "description": "Core art supplies: watercolor sets, sketch pads, colored pencils, brushes, and acrylic paint.",
        "item_ids": [1591002, 1999933, 454812, 325579, 2906786],
        "qtys": [6, 8, 4, 3, 2]
    },
    {
        "id": "pe-equipment", "name": "PE Equipment Pack", "category": "Athletics",
        "icon": "fas fa-basketball-ball", "color": "#f59e0b",
        "description": "Physical education basics: basketballs, jump ropes, cones, pinnies, and a ball pump.",
        "item_ids": [565659, 1762990, 2911339, 3797822, 1941953],
        "qtys": [6, 10, 2, 2, 1]
    },
    {
        "id": "tech-lab", "name": "Computer Lab Refresh", "category": "Technology",
        "icon": "fas fa-mouse", "color": "#3b82f6",
        "description": "Tech lab supplies: mice, headsets, screen wipes, USB drives, and cable organizers.",
        "item_ids": [3074182, 3059565, 2171015, 6373957, 4566944],
        "qtys": [10, 10, 3, 5, 2]
    },
    {
        "id": "music-room", "name": "Music Room Supplies", "category": "Art & Music",
        "icon": "fas fa-music", "color": "#8b5cf6",
        "description": "Band and choir room needs: recorders, music stands, sheet protectors, and metronomes.",
        "item_ids": [2011638, 3887587, 6426464, 3855171],
        "qtys": [15, 5, 3, 2]
    },
    {
        "id": "teacher-desk", "name": "Teacher Desk Setup", "category": "Office",
        "icon": "fas fa-desk", "color": "#0891b2",
        "description": "Personal desk supplies for teachers: planner, dry-erase markers, tape, scissors, and a desk organizer.",
        "item_ids": [444814, 4426223, 4669161, 446743, 3743408],
        "qtys": [1, 2, 1, 1, 1]
    },
]


async def _resolve_items(item_ids: List[int], qtys: List[int]) -> List[TemplateItem]:
    """Look up real product details for a list of ItemIds."""
    if not item_ids:
        return []

    cache = get_cache()
    cache_key = f"tpl_items_{'_'.join(str(i) for i in sorted(item_ids))}"
    cached = await cache.get(cache_key)
    if cached is not None:
        # Return copies with correct quantities (don't mutate cached objects)
        id_to_qty = dict(zip(item_ids, qtys))
        return [item.model_copy(update={"qty": id_to_qty.get(item.item_id, 1)}) for item in cached]

    placeholders = ",".join("?" for _ in item_ids)
    query = f"""
        SELECT i.ItemId, i.ItemCode, i.Description,
               ISNULL(i.ListPrice, 0) as Price,
               ISNULL(v.Name, 'Unknown Vendor') as Vendor,
               ISNULL(u.Code, 'Each') as Unit
        FROM Items i
        LEFT JOIN Vendors v ON i.VendorId = v.VendorId
        LEFT JOIN Units u ON i.UnitId = u.UnitId
        WHERE i.ItemId IN ({placeholders})
    """
    rows = execute_query(query, tuple(item_ids))

    id_to_qty = dict(zip(item_ids, qtys))
    items = []
    for r in rows:
        items.append(TemplateItem(
            item_id=r["ItemId"],
            item_code=r["ItemCode"] or "",
            name=(r["Description"] or "Unknown").strip(),
            price=float(r["Price"]),
            qty=id_to_qty.get(r["ItemId"], 1),
            vendor=(r["Vendor"] or "Unknown Vendor").strip(),
            unit=r["Unit"] or "Each"
        ))

    # Sort to match the original item_ids order
    id_order = {iid: idx for idx, iid in enumerate(item_ids)}
    items.sort(key=lambda x: id_order.get(x.item_id, 999))

    await cache.set(cache_key, items, CACHE_TTL_LONG)
    return items


@router.get("")
async def get_templates(session_id: Optional[str] = Query(None)) -> List[Template]:
    """Get all templates (defaults + user-created for this session)."""
    templates = []

    # Build default templates with real product data
    for tdef in DEFAULT_TEMPLATE_DEFS:
        try:
            items = await _resolve_items(tdef["item_ids"], tdef["qtys"])
            templates.append(Template(
                id=tdef["id"],
                name=tdef["name"],
                category=tdef["category"],
                icon=tdef["icon"],
                color=tdef["color"],
                description=tdef["description"],
                items=items,
                is_default=True
            ))
        except Exception as e:
            logger.error("Failed to resolve template %s: %s", tdef['id'], e)

    # Add user-created templates for this session
    if session_id and session_id in _user_templates:
        templates.extend(_user_templates[session_id])

    return templates


@router.post("")
async def create_template(req: CreateTemplateRequest, session_id: Optional[str] = Query(None)) -> Template:
    """Create a user template from cart items."""
    if not session_id:
        raise HTTPException(status_code=400, detail="Session ID required")
    if not req.name or not req.name.strip():
        raise HTTPException(status_code=400, detail="Template name required")
    if not req.items:
        raise HTTPException(status_code=400, detail="Template must have at least one item")

    items = []
    for it in req.items:
        items.append(TemplateItem(
            item_id=it.get("item_id") or it.get("ItemId") or it.get("id") or 0,
            item_code=it.get("item_code") or it.get("ItemCode") or it.get("ItemNumber") or "",
            name=it.get("name") or it.get("Description") or "Unknown",
            price=float(it.get("price") or it.get("Price") or it.get("UnitPrice") or 0),
            qty=int(it.get("qty") or it.get("quantity") or 1),
            vendor=it.get("vendor") or it.get("VendorName") or "Unknown",
            unit=it.get("unit") or it.get("UnitOfMeasure") or "Each"
        ))

    tpl = Template(
        id=f"user-{uuid.uuid4().hex[:8]}",
        name=req.name.strip(),
        category=req.category or "Custom",
        icon="fas fa-star",
        color="#6b7280",
        description=req.description.strip() if req.description else f"Custom template with {len(items)} items",
        items=items,
        is_default=False
    )

    if session_id not in _user_templates:
        _user_templates[session_id] = []
    _user_templates[session_id].append(tpl)

    return tpl


@router.delete("/{template_id}")
async def delete_template(template_id: str, session_id: Optional[str] = Query(None)):
    """Delete a user-created template."""
    if not session_id:
        raise HTTPException(status_code=400, detail="Session ID required")

    if template_id.startswith("user-") and session_id in _user_templates:
        before = len(_user_templates[session_id])
        _user_templates[session_id] = [t for t in _user_templates[session_id] if t.id != template_id]
        if len(_user_templates[session_id]) < before:
            return {"deleted": True}

    raise HTTPException(status_code=404, detail="Template not found or cannot be deleted")
