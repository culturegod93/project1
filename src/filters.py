import logging
import re
from collections import Counter
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List

# Создаём папку logs, если её нет
Path("logs").mkdir(exist_ok=True)

# Настройка логгера
logger = logging.getLogger("filters")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/filters.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def process_bank_search(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по совпадению строки в поле 'description'.

    :param data: список операций (список словарей)
    :param search: строка для поиска
    :return: список операций, у которых есть совпадение
    """
    try:
        pattern = re.compile(search, re.IGNORECASE)
        result = [item for item in data if "description" in item and pattern.search(item["description"])]
        logger.debug(f"Поиск по '{search}' найдено {len(result)} совпадений")
        return result
    except re.error as e:
        logger.error(f"Ошибка в регулярном выражении '{search}': {e}")
        return []
    except Exception as e:
        logger.error(f"Ошибка при поиске операций: {e}")
        return []


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям.

    :param data: список операций
    :param categories: список категорий для подсчёта
    :return: словарь {категория: количество}
    """
    try:
        counter: Counter = Counter()
        for category in categories:
            counter[category] = sum(
                1 for item in data if "description" in item and category.lower() in item["description"].lower()
            )
        logger.debug(f"Подсчёт категорий завершён: {dict(counter)}")
        return dict(counter)
    except Exception as e:
        logger.error(f"Ошибка при подсчёте категорий: {e}")
        return {}
