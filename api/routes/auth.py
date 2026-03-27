"""
Authentication routes for EDS Universal Requisition.
Uses sp_FA_AttemptLogin stored procedure for authentication.
"""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional
import logging

from api.database import get_db_cursor, execute_single
from api.middleware import SESSION_TIMEOUT_HOURS, SESSION_INACTIVITY_HOURS

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["authentication"])


class LoginRequest(BaseModel):
    """Login request model."""
    district_code: str = Field(..., max_length=4, description="4-character district code")
    user_number: str = Field(..., description="User number (CometId)")
    password: str = Field(..., description="User password")


class UserInfo(BaseModel):
    """User information model."""
    user_id: int
    user_name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None


class DistrictInfo(BaseModel):
    """District information model."""
    district_id: int
    district_code: str
    district_name: Optional[str] = None


class SessionInfo(BaseModel):
    """Session information model."""
    session_id: int
    school_id: Optional[int] = None
    approval_level: Optional[int] = None


class LoginResponse(BaseModel):
    """Login response model."""
    session_id: int
    user: UserInfo
    district: DistrictInfo
    session: SessionInfo


class SessionResponse(BaseModel):
    """Session details response."""
    session_id: int
    user_id: int
    district_id: int
    school_id: Optional[int] = None
    is_valid: bool = True
    valid: bool = True  # Alias for frontend compatibility (v3/v4/v6 check 'valid')


@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    """
    Authenticate user with district code, user number, and password.

    Uses the sp_FA_AttemptLogin stored procedure which:
    - Validates district code, user number (CometId), and password
    - Creates a session in SessionTable on success
    - Returns SessionId on success, NULL on failure
    """
    try:
        with get_db_cursor() as cursor:
            # Call the stored procedure
            cursor.execute(
                "EXEC sp_FA_AttemptLogin ?, ?, ?",
                (request.district_code, request.user_number, request.password)
            )

            # Get the result (SessionId)
            row = cursor.fetchone()

            if not row or row[0] is None:
                logger.warning("Login failed for district=%s, user=%s", request.district_code, request.user_number)
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid credentials"
                )

            session_id = row[0]
            logger.info("Login successful: session_id=%s", session_id)

            # Commit to ensure session is persisted before validation
            cursor.commit()

            # Query session details with user and district info
            cursor.execute("""
                SELECT
                    s.SessionId,
                    s.UserId,
                    s.DistrictId,
                    s.SchoolId,
                    s.ApprovalLevel,
                    u.UserName,
                    u.FirstName,
                    u.LastName,
                    u.Email,
                    d.DistrictCode,
                    d.Name as DistrictName
                FROM SessionTable s
                JOIN Users u ON s.UserId = u.UserId
                JOIN District d ON s.DistrictId = d.DistrictId
                WHERE s.SessionId = ?
            """, (session_id,))

            session_row = cursor.fetchone()

            if not session_row:
                logger.error("Session %s not found after creation", session_id)
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Session creation failed"
                )

            # Build response
            return LoginResponse(
                session_id=session_row.SessionId,
                user=UserInfo(
                    user_id=session_row.UserId,
                    user_name=session_row.UserName,
                    first_name=session_row.FirstName,
                    last_name=session_row.LastName,
                    email=session_row.Email
                ),
                district=DistrictInfo(
                    district_id=session_row.DistrictId,
                    district_code=session_row.DistrictCode,
                    district_name=session_row.DistrictName
                ),
                session=SessionInfo(
                    session_id=session_row.SessionId,
                    school_id=session_row.SchoolId,
                    approval_level=session_row.ApprovalLevel
                )
            )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Login error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Authentication service error"
        )


@router.get("/session/{session_id}", response_model=SessionResponse)
async def get_session(session_id: int):
    """
    Get session details by session ID.
    Validates session exists, is not ended, and is within timeout limits.
    Returns 401 if session is expired or invalid.
    """
    try:
        result = execute_single("""
            SELECT
                SessionId,
                UserId,
                DistrictId,
                SchoolId,
                SessionEnd,
                SessionStart,
                SessionLast,
                DATEDIFF(HOUR, SessionStart, GETDATE()) as session_age_hours,
                DATEDIFF(HOUR, ISNULL(SessionLast, SessionStart), GETDATE()) as inactive_hours
            FROM SessionTable
            WHERE SessionId = ?
        """, (session_id,))

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Session not found"
            )

        # Check if session has been ended (logged out)
        if result.get('SessionEnd') is not None:
            logger.info("Session %s has been ended", session_id)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Session has expired"
            )

        # Check session age timeout
        session_age = result.get('session_age_hours', 0) or 0
        if session_age > SESSION_TIMEOUT_HOURS:
            logger.info("Session %s exceeded max age: %sh > %sh", session_id, session_age, SESSION_TIMEOUT_HOURS)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Session has expired"
            )

        # Check inactivity timeout
        inactive_hours = result.get('inactive_hours', 0) or 0
        if inactive_hours > SESSION_INACTIVITY_HOURS:
            logger.info("Session %s inactive too long: %sh > %sh", session_id, inactive_hours, SESSION_INACTIVITY_HOURS)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Session has expired due to inactivity"
            )

        return SessionResponse(
            session_id=result['SessionId'],
            user_id=result['UserId'],
            district_id=result['DistrictId'],
            school_id=result.get('SchoolId'),
            is_valid=True
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Get session error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Session service error"
        )


@router.post("/logout")
async def logout(session_id: int):
    """
    Logout user by invalidating session.
    Sets SessionEnd timestamp to mark the session as ended.
    """
    try:
        with get_db_cursor() as cursor:
            # Set SessionEnd to invalidate the session
            cursor.execute("""
                UPDATE SessionTable
                SET SessionEnd = GETDATE()
                WHERE SessionId = ?
                AND SessionEnd IS NULL
            """, (session_id,))

            rows_affected = cursor.rowcount
            cursor.commit()

            if rows_affected == 0:
                logger.warning("Logout: session %s not found or already ended", session_id)
            else:
                logger.info("Logout successful for session_id=%s", session_id)

            return {"message": "Logged out successfully", "session_id": session_id}

    except Exception as e:
        logger.error("Logout error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Logout service error"
        )


@router.post("/session/{session_id}/touch")
async def touch_session(session_id: int):
    """
    Update session last activity timestamp.
    Call this periodically to keep session alive.
    """
    try:
        with get_db_cursor() as cursor:
            cursor.execute("""
                UPDATE SessionTable
                SET SessionLast = GETDATE()
                WHERE SessionId = ?
                AND SessionEnd IS NULL
            """, (session_id,))

            rows_affected = cursor.rowcount
            cursor.commit()

            if rows_affected == 0:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Session not found or expired"
                )

            return {"message": "Session updated", "session_id": session_id}

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Touch session error: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Session service error"
        )
