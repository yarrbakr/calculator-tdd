"""
Calculator package initialization.
"""
"""
Calculator module with basic arithmetic operations.
"""
from typing import Union
    
Number = Union[int, float]
    
def add(a: Number, b: Number) -> Number:
    """
    Add two numbers together.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        The sum of a and b
    """
    # Handle special float cases (infinity and NaN)
    if isinstance(a, float) and isinstance(b, float):
        import math
        # If either value is NaN, result should be NaN
        if math.isnan(a) or math.isnan(b):
            return float('nan')
        # If one is infinity and the other is negative infinity, result is NaN
        if (math.isinf(a) and math.isinf(b) and (a > 0) != (b > 0)):
            return float('nan')
        # If either value is infinity, return infinity
        if math.isinf(a):
            return a
        if math.isinf(b):
            return b

    # Perform the addition
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """
    Subtract two numbers.

    Args:
        a: First number (minuend)
        b: Second number (subtrahend)

    Returns:
        The difference of a and b (a - b)
    """
    # Handle special float cases (infinity and NaN)
    if isinstance(a, float) and isinstance(b, float):
        import math
        # If either value is NaN, result should be NaN
        if math.isnan(a) or math.isnan(b):
            return float('nan')
        # If we have inf - inf or -inf - (-inf), it's indeterminate (NaN)
        if (math.isinf(a) and math.isinf(b) and (a > 0) == (b > 0)):
            return float('nan')
        # If a is infinity, return a
        if math.isinf(a):
            return a
        # If b is infinity, return -a if a is also infinite with same sign,
        # otherwise return the infinity with the appropriate sign
        if math.isinf(b):
            return -b if a == 0 else (float('inf') if (a > 0) != (b > 0) else float('-inf'))

    # Perform the subtraction
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers.

    Args:
        a: First number (multiplicand)
        b: Second number (multiplier)

    Returns:
        The product of a and b (a * b)
    """
    # Handle special float cases (infinity and NaN)
    if isinstance(a, float) or isinstance(b, float):
        import math
        # If either value is NaN, result should be NaN
        if math.isnan(a) or math.isnan(b):
            return float('nan')
        # Handle infinity cases
        if math.isinf(a) and b == 0:
            return float('nan')
        elif math.isinf(b) and a == 0:
            return float('nan')
        elif math.isinf(a) and b != 0:
            # inf * non-zero = (+/-) inf
            return a if (b > 0) == (a > 0) else -a
        elif math.isinf(b) and a != 0:
            # non-zero * inf = (+/-) inf
            return b if (a > 0) == (b > 0) else -b

    # Perform the multiplication
    return a * b

def divide(a: Number, b: Number) -> float:
    """
    Divide two numbers.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        The quotient of a and b (a / b)

    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    # Handle special float cases (infinity and NaN)
    if isinstance(a, float) or isinstance(b, float):
        import math
        # If either value is NaN, result should be NaN
        if math.isnan(a) or math.isnan(b):
            return float('nan')
        # Handle infinity cases
        if math.isinf(a) and not math.isinf(b):
            # inf / finite = (+/-) inf
            return a if (b > 0) == (a > 0) else -a
        elif not math.isinf(a) and math.isinf(b):
            # finite / inf = 0 (with proper sign)
            return 0.0 if (a > 0) == (b > 0) else -0.0
        elif math.isinf(a) and math.isinf(b):
            # inf / inf = indeterminate (NaN)
            return float('nan')

    # Perform the division
    return float(a / b)

def power(a: Number, b: Number) -> float:
    """
    Raise a number to the power of another number.

    Args:
        a: Base number
        b: Exponent

    Returns:
        The result of a raised to the power of b (a ** b)
    """
    # Handle special float cases (infinity and NaN)
    if isinstance(a, float) or isinstance(b, float):
        import math
        # If either value is NaN, result should be NaN
        if math.isnan(a) or math.isnan(b):
            return float('nan')
        # Handle infinity cases
        if math.isinf(b) and a == 1:
            return 1.0  # 1^inf = 1
        if math.isinf(b) and abs(a) > 1:
            return float('inf') if b > 0 else 0.0
        if math.isinf(b) and abs(a) < 1:
            return 0.0 if b > 0 else float('inf')
        if math.isinf(a) and b > 0:
            return a if (b > 0) else 0.0
        if math.isinf(a) and b < 0:
            return 0.0

    # Perform the exponentiation
    try:
        return float(a ** b)
    except OverflowError:
        import math
        return float('inf') if (a > 0 or (a < 0 and int(b) % 2 == 0)) else float('-inf')

def integer_divide(a: Number, b: Number) -> int:
    """
    Perform integer division of two numbers.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        The integer result of a divided by b (a // b)

    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    # Handle special cases
    if isinstance(a, float) or isinstance(b, float):
        import math
        if math.isnan(a) or math.isnan(b):
            return float('nan')
        if math.isinf(a) and not math.isinf(b):
            # inf // finite number
            return int(a)
        elif not math.isinf(a) and math.isinf(b):
            # finite // inf = 0
            return 0
        elif math.isinf(a) and math.isinf(b):
            # inf // inf is indeterminate
            return float('nan')

    # Perform integer division
    return int(a // b)

def modulo(a: Number, b: Number) -> Number:
    """
    Calculate the remainder of division of two numbers.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        The remainder of a divided by b (a % b)

    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    # Handle special cases
    if isinstance(a, float) or isinstance(b, float):
        import math
        if math.isnan(a) or math.isnan(b):
            return float('nan')
        if math.isinf(a) and not math.isinf(b):
            # inf % finite number is undefined but we return nan
            return float('nan')
        elif not math.isinf(a) and math.isinf(b):
            # finite % inf is the finite number
            return a

    # Perform modulo operation
    return a % b


# Export the functions
__all__ = ['add', 'subtract', 'multiply', 'divide', 'power', 'integer_divide', 'modulo']
