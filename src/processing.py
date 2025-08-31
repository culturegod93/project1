from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Фильтрация списка операций по заданному статусу state"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Сортировка списка операций по дате. Элементы без даты отправляются в конец"""

    def safe_date(item: dict[str, Any]) -> str:
        return item.get("date") or ("9999-12-31T23:59:59" if reverse else "0000-01-01T00:00:00")

    return sorted(data, key=safe_date, reverse=reverse)
