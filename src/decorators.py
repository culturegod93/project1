import logging
from functools import wraps
from typing import Any
from typing import Callable


def log(filename: str | None = None) -> Callable:
    """
    Декоратор для логирования вызовов функции.

    Аргументы:
        filename (str | None): имя файла для логирования.
            Если не указано — лог выводится в консоль.

    Логирует:
        - успешный вызов функции: "{func_name} ok"
        - ошибку при вызове функции: "{func_name} error: {exc_type}. Inputs: {args}, {kwargs}"
    """

    def decorator(func: Callable) -> Callable:
        logger = logging.getLogger(f"{__name__}.{func.__name__}")
        logger.setLevel(logging.INFO)

        handler: logging.Handler
        if filename:
            handler = logging.FileHandler(filename, encoding="utf-8", mode="a")
        else:
            handler = logging.StreamHandler()

        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(handler)

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                handler.flush()
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                handler.flush()
                raise

        return wrapper

    return decorator
