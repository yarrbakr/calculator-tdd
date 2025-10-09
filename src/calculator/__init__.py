cat > src/calculator/__init__.py << 'EOF'
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
            return a + b

        # Perform the addition
    
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
   
    # Export the functions
    __all__ = ['add', 'subtract', 'divide']
    EOF