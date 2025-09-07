from typing import List, Tuple

ALLOWED_SORT = {"id", "name", "email", "role", "is_active", "created_at"}

def parse_sort(sort_param: str | None) -> List[Tuple[str, bool]]:
    # "name,-email" -> [("name", False), ("email", True)]
    if not sort_param:
        return [("name", False)]  # default asc
    fields: List[Tuple[str, bool]] = []
    for raw in sort_param.split(","):
        raw = raw.strip()
        if not raw:
            continue
        desc = raw.startswith("-")
        key = raw[1:] if desc else raw
        if key not in ALLOWED_SORT:
            continue
        fields.append((key, desc))
    return fields or [("name", False)]

def sort_items(items: list, fields: List[Tuple[str, bool]]):
    # aplica de trás para frente para manter estabilidade
    for key, desc in reversed(fields):
        items.sort(key=lambda x: (x.get(key) if x.get(key) is not None else ""), reverse=desc)
    return items
