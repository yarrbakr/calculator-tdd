"""
Comprehensive tests for the divide function.

This test module covers various scenarios for division operations including:
- Normal division operations
- Edge cases with positive and negative numbers
- Decimal numbers
- Zero dividends
- Large numbers
- Type handling
"""

from typing import Union, Type
import pytest


def test_divide_positive_integers() -> None:
    """Test division of positive integers."""
    from calculator import divide
    assert divide(10, 2) == 5.0
    assert divide(15, 3) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_negative_numbers() -> None:
    """Test division with negative numbers."""
    from calculator import divide
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0


def test_divide_by_one() -> None:
    """Test division by one."""
    from calculator import divide
    assert divide(5, 1) == 5.0
    assert divide(-5, 1) == -5.0
    assert divide(0, 1) == 0.0


def test_divide_zero_by_number() -> None:
    """Test dividing zero by a number."""
    from calculator import divide
    assert divide(0, 5) == 0.0
    assert divide(0, -3) == 0.0
    assert divide(0, 100) == 0.0


def test_divide_decimal_numbers() -> None:
    """Test division with decimal numbers."""
    from calculator import divide
    assert divide(5.5, 2.0) == 2.75
    # Using approximate equality for floating point precision issues
    import math
    assert math.isclose(divide(3.3, 1.1), 3.0)
    assert abs(divide(10.0, 3.0) - 3.333333333333333) < 0.000000000000001


def test_divide_large_numbers() -> None:
    """Test division with large numbers."""
    from calculator import divide
    assert divide(1000000, 1000) == 1000.0
    assert divide(123456789, 987654321) == 123456789 / 987654321


def test_divide_small_numbers() -> None:
    """Test division with small numbers."""
    from calculator import divide
    assert divide(0.1, 0.01) == 10.0
    assert divide(0.001, 0.0001) == 10.0


def test_divide_integer_and_float() -> None:
    """Test division with mixed integer and float types."""
    from calculator import divide
    assert divide(10, 2.5) == 4.0
    assert divide(10.0, 2) == 5.0


def test_divide_returns_float() -> None:
    """Test that division always returns a float."""
    from calculator import divide
    result = divide(4, 2)
    assert isinstance(result, float)
    assert result == 2.0

    result = divide(5, 2)
    assert isinstance(result, float)
    assert result == 2.5


def test_divide_fractional_results() -> None:
    """Test divisions that result in fractional values."""
    from calculator import divide
    assert divide(1, 3) == 1/3
    assert divide(22, 7) == 22/7
    assert abs(divide(1, 6) - 0.16666666666666666) < 1e-15


def test_divide_negative_dividend_positive_divisor() -> None:
    """Test negative dividend with positive divisor."""
    from calculator import divide
    assert divide(-15, 3) == -5.0
    assert divide(-7, 2) == -3.5


def test_divide_positive_dividend_negative_divisor() -> None:
    """Test positive dividend with negative divisor."""
    from calculator import divide
    assert divide(15, -3) == -5.0
    assert divide(7, -2) == -3.5


def test_divide_negative_dividend_negative_divisor() -> None:
    """Test negative dividend with negative divisor."""
    from calculator import divide
    assert divide(-15, -3) == 5.0
    assert divide(-7, -2) == 3.5


def test_divide_one_by_one() -> None:
    """Test 1 divided by 1."""
    from calculator import divide
    assert divide(1, 1) == 1.0


def test_divide_number_by_itself() -> None:
    """Test any non-zero number divided by itself."""
    from calculator import divide
    assert divide(5, 5) == 1.0
    assert divide(100, 100) == 1.0
    assert divide(3.14, 3.14) == 1.0


def test_divide_with_remainders() -> None:
    """Test divisions that result in numbers with decimal remainders."""
    from calculator import divide
    assert divide(10, 3) == 10/3
    assert divide(7, 3) == 7/3
    assert divide(20, 6) == 20/6