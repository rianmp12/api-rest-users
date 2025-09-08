from fastapi import APIRouter, Query, HTTPException, status
from src.models.user import UserResponse, UsersListResponse
from src.services.users_service import list_users, get_user

router = APIRouter()

@router.get("/users", 
            response_model=UsersListResponse,
            summary="Listar usuários",
            description="Retorna usuários com filtros (`q`, `role`, `is_active`), "
            "ordenação (`sort`) e paginação (`page`, `page_size`).")
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
        "data": result["data"],
        "pagination": result["pagination"]
    }

@router.get("/users/{user_id}", 
            response_model=UserResponse,
            summary="Obter usuário por ID",
            description="Retorna um único usuário pelo `id`.")
def get_user_by_id(user_id: int):
    user = get_user(user_id)
    if not user:
         raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return UserResponse(
        id=user["id"],
        name=user["name"],
        email=user["email"],
        role=user["role"],
        is_active=user["is_active"],
        created_at=user["created_at"]
    )