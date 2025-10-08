"""Comprehensive error handling tests for the calculator module."""
from typing import NoReturn
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.calculator.core import add, subtract, multiply, divide, power, integer_divide, modulo


def test_division_by_zero_error() -> None:
    """Test that division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_integer_divide_by_zero_error() -> None:
    """Test that integer division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        integer_divide(10, 0)


def test_modulo_by_zero_error() -> None:
    """Test that modulo with zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        modulo(10, 0)


def test_power_overflow_error() -> None:
    """Test that extremely large power operations raise OverflowError."""
    with pytest.raises(OverflowError):
        power(10, 1000000)


def test_invalid_input_type_add() -> None:
    """Test that invalid input types raise TypeError for add function."""
    with pytest.raises(TypeError):
        add("5", 3)  # type: ignore


def test_invalid_input_type_subtract() -> None:
    """Test that invalid input types raise TypeError for subtract function."""
    with pytest.raises(TypeError):
        subtract(10, "3")  # type: ignore


def test_invalid_input_type_multiply() -> None:
    """Test that invalid input types raise TypeError for multiply function."""
    with pytest.raises(TypeError):
        multiply("2", 4.5)  # type: ignore


def test_invalid_input_type_divide() -> None:
    """Test that invalid input types raise TypeError for divide function."""
    with pytest.raises(TypeError):
        divide(10, "2")  # type: ignore


def test_invalid_input_type_power() -> None:
    """Test that invalid input types raise TypeError for power function."""
    with pytest.raises(TypeError):
        power("2", 3)  # type: ignore


def test_invalid_input_type_integer_divide() -> None:
    """Test that invalid input types raise TypeError for integer_divide function."""
    with pytest.raises(TypeError):
        integer_divide(10, "2")  # type: ignore


def test_invalid_input_type_modulo() -> None:
    """Test that invalid input types raise TypeError for modulo function."""
    with pytest.raises(TypeError):
        modulo(10, "3")  # type: ignore


def test_divide_with_none_input() -> None:
    """Test that None inputs raise TypeError for divide function."""
    with pytest.raises(TypeError):
        divide(None, 5)  # type: ignore


def test_multiply_with_none_input() -> None:
    """Test that None inputs raise TypeError for multiply function."""
    with pytest.raises(TypeError):
        multiply(5, None)  # type: ignore


def test_power_with_none_input() -> None:
    """Test that None inputs raise TypeError for power function."""
    with pytest.raises(TypeError):
        power(None, 2)  # type: ignore


def test_complex_number_input_error() -> None:
    """Test that complex number inputs raise TypeError."""
    with pytest.raises(TypeError):
        add(1+2j, 3)  # type: ignore


def test_boolean_input_error() -> None:
    """Test that boolean inputs are not allowed (should raise TypeError)."""
    # Note: In Python, booleans are technically a subclass of int,
    # so we may need to explicitly check for booleans if we want to reject them
    with pytest.raises(TypeError):
        add(True, 5)  # type: ignore


def test_list_input_error() -> None:
    """Test that list inputs raise TypeError."""
    with pytest.raises(TypeError):
        multiply([1, 2], 3)  # type: ignore


def test_string_number_input_error() -> None:
    """Test that string representations of numbers are not automatically converted."""
    with pytest.raises(TypeError):
        subtract("10", 5)  # type: ignore


def test_object_input_error() -> None:
    """Test that object inputs raise TypeError."""
    class MyClass:
        pass
    
    obj = MyClass()
    with pytest.raises(TypeError):
        add(obj, 5)  # type: ignore


def test_empty_string_input_error() -> None:
    """Test that empty string inputs raise TypeError."""
    with pytest.raises(TypeError):
        divide("", 5)  # type: ignore


def test_invalid_argument_count() -> None:
    """Test that calling functions with wrong number of arguments raises TypeError."""
    with pytest.raises(TypeError):
        add(5)  # type: ignore


def test_extra_argument_error() -> None:
    """Test that calling functions with too many arguments raises TypeError."""
    with pytest.raises(TypeError):
        multiply(2, 3, 4)  # type: ignore


def test_infinity_divide_error() -> None:
    """Test division with infinity values."""
    import math
    result = divide(math.inf, 5)
    assert math.isinf(result)


def test_negative_infinity_modulo_error() -> None:
    """Test modulo operation with negative infinity - should work correctly."""
    import math
    # Modulo with infinity is actually valid in Python, so this should not raise an error
    result = modulo(10, -math.inf)
    # The result should be finite or infinite, but not NaN
    assert not math.isnan(result)
    # In Python, 10 % -inf = -inf, which is the expected mathematical result


def test_nan_input_error() -> None:
    """Test operations with NaN inputs."""
    import math
    # Operations with NaN should return NaN, not raise an error
    # So this test should be about ensuring proper behavior with NaN
    result = add(math.nan, 5)
    assert math.isnan(result)


def test_large_number_overflow() -> None:
    """Test operations that could cause numeric overflow."""
    large_num = 10**308
    with pytest.raises(OverflowError):
        power(large_num, 10)  # This should cause overflow


def test_recursive_structure_input() -> None:
    """Test that recursive data structures raise appropriate errors."""
    # Create a recursive structure that might cause issues
    a = [1]
    a.append(a)  # Recursive list
    with pytest.raises(TypeError):
        add(a, 5)  # type: ignore