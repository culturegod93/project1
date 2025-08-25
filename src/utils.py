import json
import logging
from pathlib import Path
from typing import Any

# Создаём папку logs, если её нет
Path("logs").mkdir(exist_ok=True)

# Настраиваем логгер для модуля utils
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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
        logger.error(f"Файл не найден или не является файлом: {file_path}")
        return []

    try:
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            logger.warning(f"Файл пустой: {file_path}")
            return []
        data = json.loads(text)
    except (OSError, json.JSONDecodeError) as e:
        logger.error(f"Ошибка при чтении JSON-файла {file_path}: {e}")
        return []

    if not isinstance(data, list):
        logger.warning(f"Корень JSON не является списком: {file_path}")
        return []

    logger.debug(f"JSON-файл успешно прочитан: {file_path}, количество записей: {len(data)}")
    return data
