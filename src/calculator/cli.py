"""CLI interface for the calculator with error handling."""
import sys
import argparse
from typing import List, Optional
from src.calculator.core import add, subtract, multiply, divide, power, integer_divide, modulo


def parse_number(value: str) -> float:
    """Parse a string value to a number, handling various input formats."""
    try:
        # Try to convert to float first
        num = float(value)
        return num
    except ValueError:
        # If it fails, raise a proper error
        raise ValueError(f"Invalid number format: '{value}'")


def safe_calculate(operation: str, x: str, y: str) -> Optional[float]:
    """Safely perform calculation with error handling."""
    try:
        num_x = parse_number(x)
        num_y = parse_number(y)
        
        if operation == "add":
            return add(num_x, num_y)
        elif operation == "subtract":
            return subtract(num_x, num_y)
        elif operation == "multiply":
            return multiply(num_x, num_y)
        elif operation == "divide":
            return divide(num_x, num_y)
        elif operation == "power":
            return power(num_x, num_y)
        elif operation == "integer_divide":
            return integer_divide(num_x, num_y)
        elif operation == "modulo":
            return modulo(num_x, num_y)
        else:
            print(f"Error: Unknown operation '{operation}'")
            return None
            
    except ValueError as e:
        print(f"Value Error: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"Division Error: {e}")
        return None
    except TypeError as e:
        print(f"Type Error: {e}")
        return None
    except OverflowError as e:
        print(f"Overflow Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def main(args: List[str] = None) -> int:
    """Main CLI function."""
    if args is None:
        args = sys.argv[1:]
    
    parser = argparse.ArgumentParser(description="Calculator with AI capabilities")
    parser.add_argument("operation", 
                       choices=["add", "subtract", "multiply", "divide", "power", "integer_divide", "modulo"],
                       help="Operation to perform")
    parser.add_argument("x", help="First operand")
    parser.add_argument("y", help="Second operand")
    
    try:
        parsed_args = parser.parse_args(args)
        result = safe_calculate(parsed_args.operation, parsed_args.x, parsed_args.y)
        
        if result is not None:
            print(f"Result: {result}")
            return 0
        else:
            print("Operation failed.")
            return 1
            
    except SystemExit:
        # argparse calls sys.exit on error, we'll handle that gracefully
        return 1
    except Exception as e:
        print(f"Error parsing arguments: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())