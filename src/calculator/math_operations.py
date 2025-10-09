"""
Math operations module for the calculator.

This module contains basic mathematical operations.
"""
from typing import Union


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers and return the result.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
        
    Returns:
        The product of a and b
    """
    # Handle special cases with infinity and NaN
    import math
    
    # If either operand is NaN, result is NaN
    if isinstance(a, float) and math.isnan(a) or isinstance(b, float) and math.isnan(b):
        return float('nan')
    
    # If one operand is infinity and the other is 0, result is NaN
    if (isinstance(a, float) and math.isinf(a) and b == 0) or \
       (isinstance(b, float) and math.isinf(b) and a == 0):
        return float('nan')
    
    # Perform the multiplication
    result = a * b
    
    # Return the result (Python handles the type automatically)
    return result