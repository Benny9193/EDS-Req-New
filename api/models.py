"""
Pydantic models for the EDS API.
"""

from typing import List, Optional, Dict, Any, Union
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator
from enum import Enum


# ===========================================
# ERROR HANDLING
# ===========================================

class APIError(BaseModel):
    """Standardized API error response."""
    model_config = ConfigDict(json_schema_extra={
        "example": {
            "error_code": "VALIDATION_ERROR",
            "message": "Invalid item_id provided",
            "details": {"field": "item_id", "value": "abc", "reason": "Must be a valid integer"},
        }
    })

    error_code: str = Field(..., description="Machine-readable error code")
    message: str = Field(..., description="Human-readable error message")
    details: Dict[str, Any] = Field(default_factory=dict, description="Additional error context")


# ===========================================
# ENUMS
# ===========================================

class ProductStatus(str, Enum):
    """Product availability status."""
    IN_STOCK = "in-stock"
    LOW_STOCK = "low-stock"
    OUT_OF_STOCK = "out-of-stock"
    DISCONTINUED = "discontinued"


class RequisitionStatus(str, Enum):
    """Requisition workflow status.

    Maps to StatusTable.StatusId in the database:
      1 = On Hold (H), 2 = Pending Approval (P), 3 = Approved (A),
      4 = Rejected (R), 5 = At EDS (I), 6 = PO Printed (O)
    """
    ON_HOLD = "On Hold"
    PENDING_APPROVAL = "Pending Approval"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    AT_EDS = "At EDS"
    PO_PRINTED = "PO Printed"
    # Legacy values kept for backward compatibility
    DRAFT = "Draft"
    SUBMITTED = "Submitted"
    FULFILLED = "Fulfilled"
    CANCELLED = "Cancelled"

    @classmethod
    def can_update(cls, status: 'RequisitionStatus') -> bool:
        """Check if requisition can be updated in this status."""
        return status in (cls.ON_HOLD, cls.PENDING_APPROVAL, cls.DRAFT, cls.SUBMITTED)

    @classmethod
    def can_cancel(cls, status: 'RequisitionStatus') -> bool:
        """Check if requisition can be cancelled in this status."""
        return status in (cls.ON_HOLD, cls.PENDING_APPROVAL, cls.DRAFT, cls.SUBMITTED)

    @classmethod
    def can_approve(cls, status: 'RequisitionStatus') -> bool:
        """Check if requisition can be approved in this status."""
        return status in (cls.ON_HOLD, cls.PENDING_APPROVAL, cls.SUBMITTED)


class Product(BaseModel):
    """Product model for catalog items."""
    model_config = ConfigDict(use_enum_values=True)

    id: str = Field(..., description="Unique product identifier/SKU")
    name: str = Field(..., description="Product name")
    description: Optional[str] = Field("", description="Product description")
    vendor: str = Field(..., description="Vendor name")
    vendor_item_code: Optional[str] = Field(None, description="Vendor's item code")
    category: str = Field("General", description="Product category")
    image: Optional[str] = Field(None, description="Image URL")
    status: ProductStatus = Field(ProductStatus.IN_STOCK, description="Stock status")
    unit_of_measure: str = Field("Each", description="Unit of measure")
    unit_price: float = Field(..., description="Price per unit")
    tags: List[str] = Field(default_factory=list, description="Search tags")


class ProductListResponse(BaseModel):
    """Response model for product list endpoint."""
    products: List[Product]
    total: int
    page: int
    page_size: int
    total_pages: int


class Category(BaseModel):
    """Product category model."""
    id: int
    name: str
    product_count: Optional[int] = 0


class Vendor(BaseModel):
    """Vendor model."""
    id: int
    name: str
    code: Optional[str] = None
    product_count: Optional[int] = 0


class CartItem(BaseModel):
    """Shopping cart item."""
    product_id: str
    quantity: int = Field(ge=1)
    unit_price: float
    extended_price: float


class Cart(BaseModel):
    """Shopping cart."""
    items: List[CartItem] = []
    subtotal: float = 0.0


class SearchQuery(BaseModel):
    """Search query parameters."""
    query: Optional[str] = None
    category: Optional[str] = None
    vendor: Optional[str] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    status: Optional[ProductStatus] = None
    page: int = Field(1, ge=1)
    page_size: int = Field(20, ge=1, le=100)


class APIStatus(BaseModel):
    """API health/status response."""
    status: str
    database_connected: bool
    version: str
    ai_enabled: bool = False
    ai_provider: Optional[str] = None
    search_enabled: bool = False
    search_connected: bool = False


# ===========================================
# REQUISITION MODELS
# ===========================================

class RequisitionItem(BaseModel):
    """Line item for a requisition submission."""
    item_id: str = Field(..., description="Product/Item ID")
    quantity: int = Field(..., ge=1, le=9999, description="Quantity ordered")
    unit_price: float = Field(..., ge=0, le=999999.99, description="Unit price at time of order")
    description: Optional[str] = Field(None, max_length=500, description="Item description")
    vendor_item_code: Optional[str] = Field(None, max_length=50, description="Vendor item code")

    @field_validator('item_id')
    @classmethod
    def validate_item_id(cls, v: str) -> str:
        """Validate item_id is a valid integer string."""
        if not v or not v.strip():
            raise ValueError("item_id cannot be empty")
        # Remove whitespace
        v = v.strip()
        # Check if it can be converted to an integer
        try:
            int_val = int(v)
            if int_val <= 0:
                raise ValueError("item_id must be a positive integer")
        except ValueError:
            raise ValueError(f"item_id must be a valid integer, got: {v}")
        return v


class RequisitionSubmission(BaseModel):
    """Request to submit a requisition from cart."""
    session_id: Union[int, str] = Field(..., description="User's session ID for authentication")
    items: List[RequisitionItem] = Field(..., min_length=1, max_length=100, description="Line items to order")
    notes: Optional[str] = Field(None, max_length=2000, description="Order notes")
    shipping_location: Optional[str] = Field(None, max_length=200, description="Delivery location")
    attention_to: Optional[str] = Field(None, max_length=100, description="Attention to recipient")
    delivery_preference: Optional[str] = Field("standard", description="Delivery preference")
    shipping_notes: Optional[str] = Field(None, max_length=2000, description="Shipping instructions")
    purpose: Optional[str] = Field(None, max_length=500, description="Purpose of requisition")
    account_code: Optional[str] = Field(None, max_length=50, description="Budget account code")
    internal_notes: Optional[str] = Field(None, max_length=2000, description="Internal notes")


class RequisitionResponse(BaseModel):
    """Response after requisition submission."""
    requisition_id: int
    requisition_number: str
    status: str
    total_amount: float
    item_count: int
    created_at: str


class RequisitionLineItem(BaseModel):
    """Line item with product details for requisition retrieval."""
    line_id: int = Field(..., description="Detail record ID")
    item_id: int = Field(..., description="Product ID")
    product_name: str = Field(..., description="Product name")
    sku: str = Field(..., description="Product SKU/vendor item code")
    vendor: str = Field("", description="Vendor name")
    quantity: int = Field(..., description="Quantity ordered")
    unit_price: float = Field(..., description="Unit price")
    extended_price: float = Field(..., description="Line total (qty * price)")
    image_url: Optional[str] = Field(None, description="Product image URL")


class RequisitionListItem(BaseModel):
    """Summary item for requisition list."""
    model_config = ConfigDict(use_enum_values=True)

    requisition_id: int
    requisition_number: str
    status: RequisitionStatus
    total_amount: float
    item_count: int
    created_at: datetime
    notes_preview: Optional[str] = Field(None, description="First 100 chars of notes")


class RequisitionDetail(BaseModel):
    """Full requisition detail with line items."""
    model_config = ConfigDict(use_enum_values=True)

    requisition_id: int
    requisition_number: str
    status: str
    items: List[RequisitionLineItem]
    total_amount: float
    notes: Optional[str] = None
    shipping_location: Optional[str] = None
    attention_to: Optional[str] = None
    created_at: datetime
    modified_at: Optional[datetime] = None
    approved_at: Optional[datetime] = None
    approved_by: Optional[str] = None
    rejection_reason: Optional[str] = None


class RequisitionListResponse(BaseModel):
    """Paginated response for requisition list."""
    items: List[RequisitionListItem]
    total: int
    page: int
    page_size: int
    total_pages: int
    status_counts: Dict[str, int] = Field(default_factory=dict, description="Count per status")


class RequisitionUpdate(BaseModel):
    """Request to update a requisition."""
    notes: Optional[str] = Field(None, max_length=2000)
    shipping_location: Optional[str] = Field(None, max_length=200)
    attention_to: Optional[str] = Field(None, max_length=100)


class RequisitionApproval(BaseModel):
    """Request to approve a requisition."""
    session_id: Union[int, str] = Field(..., description="Approver's session ID")
    comments: Optional[str] = Field(None, max_length=500)


class RequisitionRejection(BaseModel):
    """Request to reject a requisition."""
    session_id: Union[int, str] = Field(..., description="Approver's session ID")
    reason: str = Field(..., min_length=10, max_length=500, description="Rejection reason")
