"""
Calculator module with basic arithmetic operations.
"""


def add(a: float | int, b: float | int) -> float | int:
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