import json
from pathlib import Path
from typing import Any


def read_json(file_path: str) -> list[dict[str, Any]]:
    """
    Прочитать JSON-файл и вернуть список транзакций.

    Возвращает пустой список, если:
    - файл не найден;
    - не является файлом;
    - JSON пустой/невалидный;
    - корень JSON не список.

    :param file_path: путь к JSON-файлу
    :return: список словарей с транзакциями или []
    """
    path = Path(file_path)

    if not path.exists() or not path.is_file():
        return []

    try:
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            return []
        data = json.loads(text)
    except (OSError, json.JSONDecodeError):
        return []

    return data if isinstance(data, list) else []
