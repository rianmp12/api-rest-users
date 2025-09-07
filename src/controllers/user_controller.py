from fastapi import APIRouter, Query
from src.schemas.dto import Envelope
from src.services.users_service import list_users, get_user

router = APIRouter()

@router.get("/users", response_model=Envelope)
def get_users(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=50),
    q: str | None = Query(None),
    role: str | None = Query(None),
    is_active: bool | None = Query(None),
    sort: str | None = Query(None)
):
    result = list_users({
        "page": page,
        "page_size": page_size,
        "q": q,
        "role": role,
        "is_active": is_active,
        "sort": sort
    })
    return {
        "success": True,
        "data": result["data"],
        "pagination": result["pagination"],
        "error": None
    }

@router.get("/users/{user_id}", response_model=Envelope)
def get_user_by_id(user_id: int):
    user = get_user(user_id)
    if not user:
        return {
            "success": False,
            "data": None,
            "pagination": None,
            "error": {"code": "NOT_FOUND", "message": "User not found", "details": {"id": user_id}}
        }
    return {"success": True, "data": user, "pagination": None, "error": None}
