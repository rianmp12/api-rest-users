from math import ceil

MAX_PAGE_SIZE = 50

def clamp_page(page: int) -> int:
    return 1 if page is None or page < 1 else page

def clamp_page_size(page_size: int) -> int:
    if page_size is None: return 10
    if page_size < 1: return 10
    return min(page_size, MAX_PAGE_SIZE)

def slice_page(items, page: int, page_size: int):
    start = (page - 1) * page_size
    end = start + page_size
    return items[start:end]

def meta(total: int, page: int, page_size: int) -> dict:
    return {
        "page": page,
        "page_size": page_size,
        "total_items": total,
        "total_pages": ceil(total / page_size) if page_size else 0,
        "has_next": (page * page_size) < total,
        "has_prev": page > 1
    }
