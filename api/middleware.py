"""
Middleware and dependencies for EDS Universal Requisition API.

Provides:
- Session timeout constants (shared across modules)
- Authentication dependency for protected routes
- Rate limiting middleware
- Security headers middleware
"""

import os
import time
import logging
from collections import defaultdict
from typing import Optional
from fastapi import Request, HTTPException, status, Depends, Query
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from .database import execute_single

logger = logging.getLogger(__name__)


# ============================================
# Shared Session Constants
# ============================================

SESSION_TIMEOUT_HOURS = 8   # Maximum session age
SESSION_INACTIVITY_HOURS = 2  # Maximum time since last activity


# ============================================
# Authentication Dependency
# ============================================

async def get_current_user(
    session_id: int = Query(..., description="Session ID for authentication"),
) -> dict:
    """
    FastAPI dependency that validates a session and returns user info.

    Use as a dependency on any route that requires authentication:
        @router.get("/protected")
        async def protected_route(user: dict = Depends(get_current_user)):
            ...
    """
    result = execute_single("""
        SELECT
            s.SessionId,
            s.UserId,
            s.SchoolId,
            s.DistrictId,
            s.ApprovalLevel,
            u.FirstName,
            u.LastName,
            DATEDIFF(HOUR, s.SessionStart, GETDATE()) as session_age_hours,
            DATEDIFF(HOUR, ISNULL(s.SessionLast, s.SessionStart), GETDATE()) as inactive_hours
        FROM SessionTable s
        LEFT JOIN Users u ON s.UserId = u.UserId
        WHERE s.SessionId = ?
        AND s.SessionEnd IS NULL
    """, (session_id,))

    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired session",
        )

    # Check session age
    session_age = result.get("session_age_hours", 0) or 0
    if session_age > SESSION_TIMEOUT_HOURS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session has expired",
        )

    # Check inactivity
    inactive_hours = result.get("inactive_hours", 0) or 0
    if inactive_hours > SESSION_INACTIVITY_HOURS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session has expired due to inactivity",
        )

    return result


# ============================================
# Rate Limiting Middleware
# ============================================

# Paths exempt from rate limiting (static files, health checks)
_RATE_LIMIT_EXEMPT_PREFIXES = ("/js/", "/css/", "/images/", "/assets/", "/favicon")
_RATE_LIMIT_EXEMPT_PATHS = {"/api/health", "/api/status"}

# Maximum tracked IPs to prevent unbounded memory growth
_MAX_TRACKED_IPS = 50_000


class RateLimitMiddleware(BaseHTTPMiddleware):
    """
    Simple in-memory rate limiter using sliding window.
    Limits requests per IP address.

    Note: This is a single-process rate limiter. For multi-process
    deployments, use an external store (Redis, etc.) instead.
    """

    def __init__(self, app, requests_per_minute: int = 60):
        super().__init__(app)
        self.requests_per_minute = requests_per_minute
        self.window_seconds = 60
        self._requests: dict[str, list[float]] = defaultdict(list)
        self._behind_proxy = os.getenv("EDS_BEHIND_PROXY", "").lower() in ("true", "1", "yes")

    def _get_client_ip(self, request: Request) -> str:
        """
        Extract client IP address.
        Only trusts X-Forwarded-For when EDS_BEHIND_PROXY is set,
        otherwise uses the direct connection IP.
        """
        if self._behind_proxy:
            forwarded = request.headers.get("x-forwarded-for")
            if forwarded:
                # Take the first (client) IP from the chain
                return forwarded.split(",")[0].strip()
        return request.client.host if request.client else "unknown"

    def _clean_old_requests(self, ip: str, now: float) -> None:
        """Remove request timestamps outside the current window."""
        cutoff = now - self.window_seconds
        self._requests[ip] = [
            t for t in self._requests[ip] if t > cutoff
        ]
        # Remove empty entries to prevent unbounded memory growth
        if not self._requests[ip]:
            del self._requests[ip]

    async def dispatch(self, request: Request, call_next):
        path = request.url.path

        # Skip rate limiting for health checks and static files
        if path in _RATE_LIMIT_EXEMPT_PATHS:
            return await call_next(request)
        if any(path.startswith(prefix) for prefix in _RATE_LIMIT_EXEMPT_PREFIXES):
            return await call_next(request)

        ip = self._get_client_ip(request)
        now = time.time()

        self._clean_old_requests(ip, now)

        # Prevent unbounded memory growth from IP rotation attacks
        if ip not in self._requests and len(self._requests) >= _MAX_TRACKED_IPS:
            return await call_next(request)

        if len(self._requests.get(ip, [])) >= self.requests_per_minute:
            logger.warning("Rate limit exceeded for %s: %d requests/min", ip, len(self._requests[ip]))
            return JSONResponse(
                status_code=429,
                content={"detail": "Too many requests. Please try again later."},
                headers={"Retry-After": "60"},
            )

        self._requests[ip].append(now)
        return await call_next(request)


# ============================================
# Security Headers Middleware
# ============================================

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Add security headers to all responses."""

    # Content Security Policy (built once, reused per-request)
    # - unsafe-inline/unsafe-eval required by Alpine.js and Tailwind CDN
    # - cdn.tailwindcss.com for Tailwind CSS CDN build
    # - cdn.jsdelivr.net for Alpine.js
    # - cdnjs.cloudflare.com for Font Awesome
    _CSP = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline' 'unsafe-eval' "
        "https://cdn.jsdelivr.net https://cdn.tailwindcss.com; "
        "style-src 'self' 'unsafe-inline' "
        "https://cdn.jsdelivr.net https://cdnjs.cloudflare.com https://cdn.tailwindcss.com "
        "https://fonts.googleapis.com; "
        "font-src 'self' https://cdnjs.cloudflare.com https://fonts.gstatic.com; "
        "img-src 'self' data: https:; "
        "connect-src 'self'"
    )

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        response.headers["Content-Security-Policy"] = self._CSP
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"

        return response
