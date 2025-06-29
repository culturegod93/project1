from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция сортировки списка словарей по значению ключа "state" """
    filtered = []

    for item in data:
        if item.get("state") == state:
            filtered.append(item)

    return filtered


def sort_by_date(data: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки списка словарей по значению ключа "date" """

    return sorted(data, key=lambda item: item["date"], reverse=reverse)


# Проверка
if __name__ == "__main__":
    operations = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print("Фильтрация по статусу EXECUTED:")
    for operation in filter_by_state(operations):
        print(operation)

    print("\nФильтрация по статусу CANCELED:")
    for operation in filter_by_state(operations, "CANCELED"):
        print(operation)

    print("\nСортировка по дате (убывание):")
    for operation in sort_by_date(operations):
        print(operation)

    print("\nСортировка по дате (возрастание):")
    for operation in sort_by_date(operations, reverse=False):
        print(operation)
