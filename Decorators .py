import time
import functools
from typing import Callable,Any
def timer(func):
    @functools.wraps
    def wrapper(*args, **kwargs):
        start : float = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return result
    return wrapper
def logger(func):
    @functools.wraps
    def  wrapper(*args, **kwargs):
        print(f" calling{func.__name__}()")
        result = func(*args, **kwargs)
        print(f"Done {func.__name__}")
        return result
    return wrapper


def validate_logs(func: Callable) -> Callable:
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        data = args[1] if len(args) > 1 else kwargs.get("logs", None)
        if not isinstance(data, list):
            raise TypeError(f"Expected list, got {type(data).__name__}")
        if len(data) == 0:
            raise ValueError("Logs list empty nahi ho sakti!")
        return func(*args, **kwargs)
    return wrapper