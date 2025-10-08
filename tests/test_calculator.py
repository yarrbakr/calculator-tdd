import pytest
from typing import Union


def test_subtract_positive_numbers() -> None:
    """Test subtraction of two positive numbers."""
    from src.calculator import subtract
    result = subtract(10, 5)
    assert result == 5


def test_subtract_negative_numbers() -> None:
    """Test subtraction of two negative numbers."""
    from src.calculator import subtract
    result = subtract(-10, -5)
    assert result == -5


def test_subtract_positive_and_negative() -> None:
    """Test subtraction of positive and negative numbers."""
    from src.calculator import subtract
    result = subtract(10, -5)
    assert result == 15


def test_subtract_negative_and_positive() -> None:
    """Test subtraction of negative and positive numbers."""
    from src.calculator import subtract
    result = subtract(-10, 5)
    assert result == -15


def test_subtract_with_zero() -> None:
    """Test subtraction with zero as one operand."""
    from src.calculator import subtract
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
    assert subtract(0, 0) == 0


def test_subtract_identical_numbers() -> None:
    """Test subtraction of identical numbers (should be zero)."""
    from src.calculator import subtract
    assert subtract(5, 5) == 0
    assert subtract(-5, -5) == 0
    assert subtract(0, 0) == 0


def test_subtract_floating_point_numbers() -> None:
    """Test subtraction of floating point numbers."""
    from src.calculator import subtract
    result = subtract(10.5, 3.2)
    assert abs(result - 7.3) < 1e-10  # Account for floating point precision


def test_subtract_large_numbers() -> None:
    """Test subtraction of very large numbers."""
    from src.calculator import subtract
    large_num1 = 10**10
    large_num2 = 10**9
    result = subtract(large_num1, large_num2)
    assert result == 9 * 10**9


def test_subtract_small_numbers() -> None:
    """Test subtraction of very small numbers."""
    from src.calculator import subtract
    small_num1 = 1e-10
    small_num2 = 1e-11
    result = subtract(small_num1, small_num2)
    expected = 9e-11
    assert abs(result - expected) < 1e-20


def test_subtract_integer_float_mixed() -> None:
    """Test subtraction with mixed integer and float types."""
    from src.calculator import subtract
    assert subtract(10, 5.5) == 4.5
    result = subtract(10.7, 5)
    assert abs(result - 5.7) < 1e-10  # Handle floating point precision


def test_subtract_decimal_precision() -> None:
    """Test subtraction with precise decimal values."""
    from src.calculator import subtract
    result = subtract(0.3, 0.1)
    # Use approximate comparison due to floating point precision
    assert abs(result - 0.2) < 1e-10


@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (10, 7, 3),
    (0, 5, -5),
    (5, 0, 5),
    (-5, -3, -2),
    (-5, 3, -8),
    (5, -3, 8),
])
def test_subtract_parametrized(a: Union[int, float], b: Union[int, float], expected: Union[int, float]) -> None:
    """Parametrized test for various subtraction scenarios."""
    from src.calculator import subtract
    assert subtract(a, b) == expected


def test_subtract_return_type_int() -> None:
    """Test that subtract returns correct type for integer inputs."""
    from src.calculator import subtract
    result = subtract(10, 5)
    assert isinstance(result, int)
    assert result == 5


def test_subtract_return_type_float() -> None:
    """Test that subtract returns correct type for float inputs."""
    from src.calculator import subtract
    result = subtract(10.0, 5.0)
    assert isinstance(result, float)
    assert result == 5.0


def test_subtract_mixed_types_return_type() -> None:
    """Test that subtract returns correct type for mixed input types."""
    from src.calculator import subtract
    result1 = subtract(10, 5.0)  # int - float
    assert isinstance(result1, float)
    
    result2 = subtract(10.0, 5)  # float - int
    assert isinstance(result2, float)


def test_subtract_extreme_values() -> None:
    """Test subtraction with extreme values (close to system limits)."""
    from src.calculator import subtract
    import sys
    
    # Test with large integers
    large_pos = sys.maxsize
    large_neg = -sys.maxsize - 1
    # Note: actual result depends on how calculator handles overflow
    result = subtract(large_pos, 1)
    assert result == sys.maxsize - 1

    # Test with very negative numbers
    result = subtract(large_neg, -1)
    assert result == -sys.maxsize