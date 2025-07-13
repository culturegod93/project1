import functools
import logging
from typing import Any
from typing import Callable
from typing import Optional


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)

        handler: logging.Handler
        if filename:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler()

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                logger.info(f"Called {func.__name__} with args={args}, kwargs={kwargs} -> {result}")
                return result
            except Exception as e:
                logger.error(f"Error in {func.__name__} with args={args}, kwargs={kwargs}: {e}")
                raise

        return wrapper

    return decorator
