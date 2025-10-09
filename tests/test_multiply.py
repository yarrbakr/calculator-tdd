"""
Comprehensive tests for the multiply function.

This test file contains all edge cases and scenarios for multiplication operations.
All tests will fail initially (RED) since the multiply function doesn't exist yet.
"""
from typing import Union, List, Tuple
import sys
import os

# Add src directory to path to import calculator modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_multiply_basic_positive_integers() -> None:
    """Test basic multiplication of positive integers."""
    from calculator.math_operations import multiply
    result = multiply(3, 4)
    assert result == 12


def test_multiply_basic_negative_integers() -> None:
    """Test basic multiplication of negative integers."""
    from calculator.math_operations import multiply
    result = multiply(-3, 4)
    assert result == -12


def test_multiply_two_negative_integers() -> None:
    """Test multiplication of two negative integers."""
    from calculator.math_operations import multiply
    result = multiply(-3, -4)
    assert result == 12


def test_multiply_by_zero() -> None:
    """Test multiplication by zero."""
    from calculator.math_operations import multiply
    result = multiply(5, 0)
    assert result == 0


def test_multiply_zero_by_number() -> None:
    """Test multiplying zero by a number."""
    from calculator.math_operations import multiply
    result = multiply(0, 7)
    assert result == 0


def test_multiply_by_one() -> None:
    """Test multiplication by one (identity property)."""
    from calculator.math_operations import multiply
    result = multiply(8, 1)
    assert result == 8


def test_multiply_one_by_number() -> None:
    """Test multiplying one by a number."""
    from calculator.math_operations import multiply
    result = multiply(1, 9)
    assert result == 9


def test_multiply_floating_point_numbers() -> None:
    """Test multiplication of floating-point numbers."""
    from calculator.math_operations import multiply
    result = multiply(2.5, 4.0)
    assert abs(result - 10.0) < 0.0001  # Account for floating point precision


def test_multiply_negative_floats() -> None:
    """Test multiplication of negative floating-point numbers."""
    from calculator.math_operations import multiply
    result = multiply(-2.5, 4.0)
    assert abs(result - (-10.0)) < 0.0001


def test_multiply_large_numbers() -> None:
    """Test multiplication of large numbers."""
    from calculator.math_operations import multiply
    result = multiply(1000000, 1000000)
    assert result == 1000000000000


def test_multiply_small_numbers() -> None:
    """Test multiplication of small decimal numbers."""
    from calculator.math_operations import multiply
    result = multiply(0.1, 0.2)
    assert abs(result - 0.02) < 0.0001


def test_multiply_by_negative_one() -> None:
    """Test multiplication by negative one."""
    from calculator.math_operations import multiply
    result = multiply(15, -1)
    assert result == -15


def test_multiply_negative_one_by_number() -> None:
    """Test multiplying negative one by a number."""
    from calculator.math_operations import multiply
    result = multiply(-1, 25)
    assert result == -25


def test_multiply_commutative_property() -> None:
    """Test that multiplication follows the commutative property (a*b = b*a)."""
    from calculator.math_operations import multiply
    assert multiply(7, 9) == multiply(9, 7)


def test_multiply_associative_property() -> None:
    """Test that multiplication follows the associative property (a*(b*c) = (a*b)*c)."""
    from calculator.math_operations import multiply
    # Since multiply only takes two arguments, we'll test nested calls
    assert multiply(2, multiply(3, 4)) == multiply(multiply(2, 3), 4)


def test_multiply_with_fraction() -> None:
    """Test multiplication with fractional numbers."""
    from calculator.math_operations import multiply
    result = multiply(0.5, 0.5)
    assert abs(result - 0.25) < 0.0001


def test_multiply_positive_large_negative_small() -> None:
    """Test multiplication of a large positive number with a small negative number."""
    from calculator.math_operations import multiply
    result = multiply(100000, -0.01)
    assert abs(result - (-1000)) < 0.0001


def test_multiply_zero_by_zero() -> None:
    """Test multiplying zero by zero."""
    from calculator.math_operations import multiply
    result = multiply(0, 0)
    assert result == 0


def test_multiply_integer_and_float() -> None:
    """Test multiplication of integer and floating-point number."""
    from calculator.math_operations import multiply
    result = multiply(5, 2.5)
    assert abs(result - 12.5) < 0.0001


def test_multiply_with_infinity() -> None:
    """Test multiplication with infinity."""
    from calculator.math_operations import multiply
    import math
    result = multiply(float('inf'), 5)
    assert math.isinf(result) and result > 0


def test_multiply_with_negative_infinity() -> None:
    """Test multiplication with negative infinity."""
    from calculator.math_operations import multiply
    import math
    result = multiply(float('-inf'), 5)
    assert math.isinf(result) and result < 0


def test_multiply_infinity_by_zero() -> None:
    """Test multiplication of infinity by zero (should be NaN)."""
    from calculator.math_operations import multiply
    import math
    result = multiply(float('inf'), 0)
    assert math.isnan(result)


def test_multiply_negative_infinity_by_zero() -> None:
    """Test multiplication of negative infinity by zero (should be NaN)."""
    from calculator.math_operations import multiply
    import math
    result = multiply(float('-inf'), 0)
    assert math.isnan(result)


def test_multiply_nan_input() -> None:
    """Test multiplication with NaN input."""
    from calculator.math_operations import multiply
    import math
    result = multiply(float('nan'), 5)
    assert math.isnan(result)


def test_multiply_nan_times_zero() -> None:
    """Test multiplication of NaN with zero."""
    from calculator.math_operations import multiply
    import math
    result = multiply(float('nan'), 0)
    assert math.isnan(result)


def test_multiply_decimal_precision() -> None:
    """Test multiplication maintaining decimal precision."""
    from calculator.math_operations import multiply
    result = multiply(0.123456789, 9.87654321)
    expected = 1.21932631112635189
    assert abs(result - expected) < 0.0001


def test_multiply_rounding_behavior() -> None:
    """Test behavior with numbers that might cause rounding issues."""
    from calculator.math_operations import multiply
    result = multiply(0.1, 0.1)
    assert abs(result - 0.01) < 0.0001


def test_multiply_order_of_magnitude() -> None:
    """Test multiplication where order of magnitude changes significantly."""
    from calculator.math_operations import multiply
    result = multiply(1000000, 0.000001)
    assert abs(result - 1.0) < 0.000001