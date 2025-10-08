import pytest
from typing import Generator
from contextlib import contextmanager
from src.calculator import add


@contextmanager
def does_not_raise():
    """Context manager that does not raise an exception."""
    yield


class TestAddFunction:
    """Test cases for the add function using TDD approach."""
    
    def test_add_positive_numbers(self) -> None:
        """Test adding two positive numbers."""
        assert add(2.0, 3.0) == 5.0
        
    def test_add_negative_numbers(self) -> None:
        """Test adding two negative numbers."""
        assert add(-2.0, -3.0) == -5.0
        
    def test_add_positive_and_negative(self) -> None:
        """Test adding positive and negative numbers."""
        assert add(5.0, -3.0) == 2.0
        
    def test_add_negative_and_positive(self) -> None:
        """Test adding negative and positive numbers."""
        assert add(-5.0, 3.0) == -2.0
        
    def test_add_zero_to_number(self) -> None:
        """Test adding zero to a number."""
        assert add(5.0, 0.0) == 5.0
        assert add(0.0, 5.0) == 5.0
        
    def test_add_with_zero(self) -> None:
        """Test adding two zeros."""
        assert add(0.0, 0.0) == 0.0
        
    def test_add_floating_point_numbers(self) -> None:
        """Test adding floating point numbers with precision."""
        result = add(0.1, 0.2)
        # Using pytest.approx to handle floating point precision issues
        assert result == pytest.approx(0.3)
        
    def test_add_large_numbers(self) -> None:
        """Test adding large numbers."""
        assert add(1000000.0, 2000000.0) == 3000000.0
        
    def test_add_small_numbers(self) -> None:
        """Test adding very small numbers."""
        assert add(0.000001, 0.000002) == 0.000003
        
    def test_add_negative_zero(self) -> None:
        """Test adding with negative zero."""
        assert add(5.0, -0.0) == 5.0
        assert add(-0.0, 5.0) == 5.0
        
    def test_add_integers_passed_as_floats(self) -> None:
        """Test adding integers passed as floats."""
        assert add(5.0, 3.0) == 8.0
        
    def test_add_decimal_precision(self) -> None:
        """Test adding numbers with many decimal places."""
        result = add(1.123456789, 2.987654321)
        assert result == pytest.approx(4.11111111, abs=1e-8)
        
    def test_add_very_large_and_very_small(self) -> None:
        """Test adding very large and very small numbers."""
        large_num = 1e10
        small_num = 1e-10
        result = add(large_num, small_num)
        assert result == pytest.approx(large_num)  # Small number might be negligible
        
    def test_add_with_infinity(self) -> None:
        """Test adding with infinity."""
        import math
        assert math.isinf(add(float('inf'), 5.0))
        assert math.isinf(add(5.0, float('inf')))
        assert math.isnan(add(float('inf'), float('-inf')))  # inf + (-inf) = NaN
        
    def test_add_with_nan(self) -> None:
        """Test adding with NaN."""
        import math
        result = add(float('nan'), 5.0)
        assert math.isnan(result)
        result = add(5.0, float('nan'))
        assert math.isnan(result)