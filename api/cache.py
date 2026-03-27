"""
Simple in-memory cache with TTL for EDS API.

Provides caching for relatively static data like categories and vendors
to reduce database load on frequently accessed endpoints.
"""

import time
import functools
import asyncio
from typing import Any, Dict, Optional, Callable
import logging

logger = logging.getLogger(__name__)


class SimpleCache:
    """
    Thread-safe in-memory cache with TTL support.

    Usage:
        cache = SimpleCache()
        cache.set("key", value, ttl=3600)  # Cache for 1 hour
        value = cache.get("key")
    """

    def __init__(self):
        self._cache: Dict[str, tuple] = {}  # key -> (value, expiry_time)
        self._lock = asyncio.Lock()

    async def get(self, key: str) -> Optional[Any]:
        """Get a value from cache. Returns None if expired or not found."""
        if key not in self._cache:
            return None

        value, expiry = self._cache[key]
        if time.time() > expiry:
            # Expired - remove and return None
            async with self._lock:
                self._cache.pop(key, None)
            return None

        return value

    async def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        """
        Set a value in cache with TTL.

        Args:
            key: Cache key
            value: Value to cache
            ttl: Time to live in seconds (default: 1 hour)
        """
        expiry = time.time() + ttl
        async with self._lock:
            self._cache[key] = (value, expiry)

    async def delete(self, key: str) -> bool:
        """Delete a key from cache. Returns True if key existed."""
        async with self._lock:
            return self._cache.pop(key, None) is not None

    async def clear(self) -> None:
        """Clear all cached values."""
        async with self._lock:
            self._cache.clear()

    def get_sync(self, key: str) -> Optional[Any]:
        """Synchronous get for non-async contexts."""
        if key not in self._cache:
            return None

        value, expiry = self._cache[key]
        if time.time() > expiry:
            self._cache.pop(key, None)
            return None

        return value

    def set_sync(self, key: str, value: Any, ttl: int = 3600) -> None:
        """Synchronous set for non-async contexts."""
        expiry = time.time() + ttl
        self._cache[key] = (value, expiry)

    @property
    def size(self) -> int:
        """Current number of items in cache (may include expired)."""
        return len(self._cache)


# Global cache instance
_cache = SimpleCache()


def get_cache() -> SimpleCache:
    """Get the global cache instance."""
    return _cache


def cached(ttl: int = 3600, key_prefix: str = ""):
    """
    Decorator to cache async function results.

    Args:
        ttl: Time to live in seconds
        key_prefix: Prefix for cache key (function name used if empty)

    Usage:
        @cached(ttl=3600, key_prefix="categories")
        async def get_categories():
            return await fetch_from_db()

    Note: Only works for functions with no arguments or simple hashable arguments.
    For functions with complex arguments, use the cache directly.
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Build cache key from function name and arguments
            prefix = key_prefix or func.__name__

            # Create key from args/kwargs (simple approach)
            arg_str = ""
            if args:
                arg_str += "_" + "_".join(str(a) for a in args)
            if kwargs:
                arg_str += "_" + "_".join(f"{k}={v}" for k, v in sorted(kwargs.items()))

            cache_key = f"{prefix}{arg_str}"

            # Try to get from cache
            cached_value = await _cache.get(cache_key)
            if cached_value is not None:
                logger.debug(f"Cache hit: {cache_key}")
                return cached_value

            # Cache miss - call function
            logger.debug(f"Cache miss: {cache_key}")
            result = await func(*args, **kwargs)

            # Store in cache
            if result is not None:
                await _cache.set(cache_key, result, ttl)

            return result

        # Add method to invalidate this function's cache
        async def invalidate(*args, **kwargs):
            prefix = key_prefix or func.__name__
            arg_str = ""
            if args:
                arg_str += "_" + "_".join(str(a) for a in args)
            if kwargs:
                arg_str += "_" + "_".join(f"{k}={v}" for k, v in sorted(kwargs.items()))
            cache_key = f"{prefix}{arg_str}"
            await _cache.delete(cache_key)

        wrapper.invalidate = invalidate
        return wrapper

    return decorator


# Cache TTL constants (in seconds)
CACHE_TTL_SHORT = 300       # 5 minutes
CACHE_TTL_MEDIUM = 1800     # 30 minutes
CACHE_TTL_LONG = 3600       # 1 hour
CACHE_TTL_VERY_LONG = 7200  # 2 hours
