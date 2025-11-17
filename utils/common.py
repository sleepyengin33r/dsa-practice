"""
Common utility functions used across multiple problems.
"""

from typing import List, Optional


def print_array(arr: List[int], label: str = "Array") -> None:
    """
    Pretty print an array.
    
    Args:
        arr: List to print
        label: Label for the array
    """
    print(f"{label}: {arr}")


def compare_arrays(arr1: List, arr2: List) -> bool:
    """
    Compare two arrays for equality.
    
    Args:
        arr1: First array
        arr2: Second array
    
    Returns:
        True if arrays are equal, False otherwise
    """
    if len(arr1) != len(arr2):
        return False
    return all(a == b for a, b in zip(arr1, arr2))


def generate_test_array(size: int, min_val: int = 0, max_val: int = 100) -> List[int]:
    """
    Generate a random test array.
    
    Args:
        size: Size of the array
        min_val: Minimum value
        max_val: Maximum value
    
    Returns:
        Random array
    """
    import random
    return [random.randint(min_val, max_val) for _ in range(size)]


def timing_decorator(func):
    """
    Decorator to measure execution time of a function.
    
    Usage:
        @timing_decorator
        def my_function():
            pass
    """
    import time
    from functools import wraps
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time:.6f} seconds")
        return result
    
    return wrapper

