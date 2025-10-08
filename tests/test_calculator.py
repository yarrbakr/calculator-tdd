import pytest
from typing import Union
from contextlib import contextmanager
from src.calculator import subtract


@contextmanager
def does_not_raise():
    """Context manager that does not raise an exception."""
    yield


class TestSubtractFunction:
    """Test cases for the subtract function using TDD approach."""
    
    def test_subtract_positive_numbers(self) -> None:
        """Test subtraction of two positive numbers."""
        assert subtract(10.0, 5.0) == 5.0

    def test_subtract_negative_numbers(self) -> None:
        """Test subtraction of two negative numbers."""
        assert subtract(-10.0, -5.0) == -5.0

    def test_subtract_positive_and_negative(self) -> None:
        """Test subtraction of positive and negative numbers."""
        assert subtract(10.0, -5.0) == 15.0

    def test_subtract_negative_and_positive(self) -> None:
        """Test subtraction of negative and positive numbers."""
        assert subtract(-10.0, 5.0) == -15.0

    def test_subtract_with_zero(self) -> None:
        """Test subtraction with zero as one operand."""
        assert subtract(5.0, 0.0) == 5.0
        assert subtract(0.0, 5.0) == -5.0
        assert subtract(0.0, 0.0) == 0.0

    def test_subtract_identical_numbers(self) -> None:
        """Test subtraction of identical numbers (should be zero)."""
        assert subtract(5.0, 5.0) == 0.0
        assert subtract(-5.0, -5.0) == 0.0
        assert subtract(0.0, 0.0) == 0.0

    def test_subtract_floating_point_numbers(self) -> None:
        """Test subtraction of floating point numbers."""
        result = subtract(10.5, 3.2)
        assert result == pytest.approx(7.3)  # Account for floating point precision

    def test_subtract_large_numbers(self) -> None:
        """Test subtraction of very large numbers."""
        large_num1 = 10**10
        large_num2 = 10**9
        result = subtract(large_num1, large_num2)
        assert result == 9 * 10**9

    def test_subtract_small_numbers(self) -> None:
        """Test subtraction of very small numbers."""
        small_num1 = 1e-10
        small_num2 = 1e-11
        result = subtract(small_num1, small_num2)
        expected = 9e-11
        assert result == pytest.approx(expected)

    def test_subtract_integer_float_mixed(self) -> None:
        """Test subtraction with mixed integer and float types."""
        assert subtract(10.0, 5.5) == 4.5
        result = subtract(10.7, 5.0)
        assert result == pytest.approx(5.7)  # Handle floating point precision

    def test_subtract_decimal_precision(self) -> None:
        """Test subtraction with precise decimal values."""
        result = subtract(0.3, 0.1)
        # Use approximate comparison due to floating point precision
        assert result == pytest.approx(0.2)

    @pytest.mark.parametrize("a,b,expected", [
        (5.0, 3.0, 2.0),
        (10.0, 7.0, 3.0),
        (0.0, 5.0, -5.0),
        (5.0, 0.0, 5.0),
        (-5.0, -3.0, -2.0),
        (-5.0, 3.0, -8.0),
        (5.0, -3.0, 8.0),
    ])
    def test_subtract_parametrized(self, a: Union[int, float], b: Union[int, float], expected: Union[int, float]) -> None:
        """Parametrized test for various subtraction scenarios."""
        assert subtract(a, b) == expected

    def test_subtract_return_type_int(self) -> None:
        """Test that subtract returns correct type for integer inputs."""
        result = subtract(10, 5)
        assert isinstance(result, (int, float))
        assert result == 5

    def test_subtract_return_type_float(self) -> None:
        """Test that subtract returns correct type for float inputs."""
        result = subtract(10.0, 5.0)
        assert isinstance(result, float)
        assert result == 5.0

    def test_subtract_mixed_types_return_type(self) -> None:
        """Test that subtract returns correct type for mixed input types."""
        result1 = subtract(10, 5.0)  # int - float
        assert isinstance(result1, float)
        
        result2 = subtract(10.0, 5)  # float - int
        assert isinstance(result2, float)

    def test_subtract_extreme_values(self) -> None:
        """Test subtraction with extreme values (close to system limits)."""
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

    def test_subtract_with_infinity(self) -> None:
        """Test subtracting with infinity."""
        import math
        assert math.isinf(subtract(float('inf'), 5.0))
        assert math.isinf(subtract(5.0, float('-inf')))
        assert math.isnan(subtract(float('inf'), float('inf')))  # inf - inf = NaN
        assert math.isnan(subtract(float('-inf'), float('-inf')))  # -inf - (-inf) = NaN

    def test_subtract_with_nan(self) -> None:
        """Test subtracting with NaN."""
        import math
        result = subtract(float('nan'), 5.0)
        assert math.isnan(result)
        result = subtract(5.0, float('nan'))
        assert math.isnan(result)