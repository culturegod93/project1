from typing import Any
from typing import Dict
from typing import List

import pytest

from src.filters import process_bank_operations
from src.filters import process_bank_search
from src.processing import filter_by_state

# Тестовые данные
transactions: List[Dict[str, Any]] = [
    {"id": 1, "state": "EXECUTED", "description": "Перевод с карты на карту", "date": "2023-08-01"},
    {"id": 2, "state": "CANCELED", "description": "Оплата счета", "date": "2023-08-02"},
    {"id": 3, "state": "EXECUTED", "description": "Перевод организации", "date": "2023-08-03"},
    {"id": 4, "state": "PENDING", "description": "Пополнение счета", "date": "2023-08-04"},
]

categories: List[str] = ["Перевод", "Оплата", "Пополнение", "Снятие"]


def test_filter_by_state_executed() -> None:
    filtered = filter_by_state(transactions, state="EXECUTED")
    assert len(filtered) == 2
    for t in filtered:
        assert t["state"] == "EXECUTED"


def test_filter_by_state_canceled() -> None:
    filtered = filter_by_state(transactions, state="CANCELED")
    assert len(filtered) == 1
    assert filtered[0]["state"] == "CANCELED"


def test_filter_by_state_invalid() -> None:
    filtered = filter_by_state(transactions, state="INVALID")
    assert filtered == []


def test_search_by_description_full_match() -> None:
    results = process_bank_search(transactions, "Перевод с карты на карту")
    assert len(results) == 1
    assert results[0]["id"] == 1


def test_search_by_description_partial_match() -> None:
    results = process_bank_search(transactions, "Перевод")
    assert len(results) == 2
    ids = [t["id"] for t in results]
    assert 1 in ids and 3 in ids


def test_search_by_description_no_match() -> None:
    results = process_bank_search(transactions, "Не существует")
    assert results == []


def test_search_case_insensitive() -> None:
    results = process_bank_search(transactions, "перевод")
    assert len(results) == 2
    ids = [t["id"] for t in results]
    assert 1 in ids and 3 in ids


def test_search_empty_data() -> None:
    results = process_bank_search([], "Перевод")
    assert results == []


def test_search_invalid_regex() -> None:
    results = process_bank_search(transactions, "[")
    assert results == []


def test_process_bank_operations() -> None:
    counts = process_bank_operations(transactions, categories)
    assert counts["Перевод"] == 2
    assert counts["Оплата"] == 1
    assert counts["Пополнение"] == 1
    assert counts["Снятие"] == 0


def test_process_bank_operations_empty_data() -> None:
    counts = process_bank_operations([], categories)
    for category in categories:
        assert counts[category] == 0
