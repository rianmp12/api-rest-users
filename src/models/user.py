from pydantic import BaseModel
from typing import List, Optional

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    is_active: bool
    created_at: Optional[str] = None

class Pagination(BaseModel):
    page: int
    page_size: int
    total_items: int
    total_pages: int
    has_next: bool
    has_prev: bool

class UsersListResponse(BaseModel):
    data: List[UserResponse]
    pagination: Pagination