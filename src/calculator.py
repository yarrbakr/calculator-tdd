"""
Calculator module containing basic arithmetic operations.
"""

from typing import Union


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtract two numbers."""
    return a - b