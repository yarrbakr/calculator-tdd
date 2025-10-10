"""Basic calculator implementation with error handling."""
from typing import Union

Number = Union[int, float]

def _validate_inputs(*args) -> None:
    """Validate that all inputs are numeric and not complex or boolean."""
    for arg in args:
        # Explicitly check for booleans first since they are a subclass of int
        if isinstance(arg, bool):
            raise TypeError(f"Boolean values are not allowed. Got {type(arg).__name__}: {arg}")
        if not isinstance(arg, (int, float)):
            # Raise error for complex numbers, strings, lists, etc.
            raise TypeError(f"Only int and float values allowed. Got {type(arg).__name__}: {arg}")
        # Check for complex numbers (they're technically float but we need special handling)
        if isinstance(arg, complex):
            raise TypeError(f"Complex numbers are not supported. Got {type(arg).__name__}: {arg}")

def add(x: Number, y: Number) -> float:
    """Add two numbers."""
    _validate_inputs(x, y)
    return float(x + y)

def subtract(x: Number, y: Number) -> float:
    """Subtract y from x."""
    _validate_inputs(x, y)
    return float(x - y)

def multiply(x: Number, y: Number) -> float:
    """Multiply two numbers."""
    _validate_inputs(x, y)
    return float(x * y)

def divide(x: Number, y: Number) -> float:
    """Divide x by y."""
    _validate_inputs(x, y)
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return float(x / y)

def power(x: Number, y: Number) -> float:
    """Raise x to the power of y."""
    _validate_inputs(x, y)
    if x == 0 and y < 0:
        raise ZeroDivisionError("Raising zero to a negative power is undefined")
    try:
        result = x ** y
        if isinstance(result, complex):
            raise TypeError("Result is complex, which is not supported")
        return float(result)
    except OverflowError:
        raise OverflowError(f"Result of {x} ** {y} is too large to represent")
    except (ValueError, TypeError) as e:
        raise TypeError(f"Invalid operation: {x} ** {y}") from e

def integer_divide(x: Number, y: Number) -> int:
    """Perform integer division of x by y."""
    _validate_inputs(x, y)
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return int(x // y)

def modulo(x: Number, y: Number) -> float:
    """Calculate x modulo y."""
    _validate_inputs(x, y)
    if y == 0:
        raise ZeroDivisionError("Cannot perform modulo with zero")
    return float(x % y)