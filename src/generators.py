from typing import Any
from typing import Dict
from typing import Iterator


def filter_by_currency(data: list[Dict[str, Any]], currency: str = "USD") -> Iterator[Dict[str, Any]]:
    """Фильтрует список словарей по значению валюты и возвращает итератор"""
    return (item for item in data if item.get("currency") == currency)


def transaction_descriptions(data: list[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, возвращающий описания транзакций"""
    for item in data:
        description = item.get("description")
        if description:
            yield description


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров карт в диапазоне от start до stop"""
    for number in range(start, stop):
        yield f"{number:016d}"  # форматируем как 16-значный номер карты
