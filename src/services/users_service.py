from src.repositories.user_repository import load_users
from math import ceil

def list_users(params: dict):
    data = load_users()

    if params.get("q"):
        q = params["q"].lower()
        data = [u for u in data if q in u["name"].lower() or q in u["email"].lower()]
    if params.get("role"):
        data = [u for u in data if u["role"].lower() == params["role"].lower()]
    if params.get("is_active") is not None:
        data = [u for u in data if u["is_active"] == params["is_active"]]

    sort = params.get("sort")
    if sort:
        fields = [f.strip() for f in sort.split(",")]
        for f in reversed(fields):
            reverse = f.startswith("-")
            key = f[1:] if reverse else f
            data.sort(key=lambda x: x.get(key), reverse=reverse)

    page = params.get("page", 1)
    page_size = params.get("page_size", 10)
    total_items = len(data)
    total_pages = ceil(total_items / page_size) if page_size else 1

    start = (page - 1) * page_size
    end = start + page_size
    paged = data[start:end]

    return {
        "data": paged,
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "has_prev": page > 1,
        },
    }

def get_user(user_id: int):
    data = load_users()
    for u in data:
        if u["id"] == user_id:
            return u
    return None
