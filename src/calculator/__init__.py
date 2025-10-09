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
  
  
   # Export the functions
   __all__ = ['add', 'subtract']
