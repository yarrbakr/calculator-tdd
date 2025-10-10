"""
Command Line Interface for the calculator application.

This module provides a CLI that supports basic arithmetic operations.
"""
import argparse
import sys
from typing import Union, Optional, NoReturn, List
import operator
from . import add, subtract, multiply, divide, power, integer_divide, modulo  # Import our calculator functions


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


def calculate(operation: str, x: float, y: float) -> float:
    """
    Perform the specified operation on two numbers.
    
    Args:
        operation: The operation to perform ('add', 'subtract', 'multiply', 'divide')
        x: The first operand
        y: The second operand
        
    Returns:
        The result of the operation
        
    Raises:
        ValueError: If the operation is not supported
        ZeroDivisionError: If division by zero is attempted
    """
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    if operation not in operations:
        raise ValueError(f"Invalid operation: {operation}")
    
    return operations[operation](x, y)


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    # Don't auto-exit on help by using add_help=False and handling it manually
    parser = argparse.ArgumentParser(
        description="Calculator CLI - Perform arithmetic operations with error handling",
        prog="calculator",
        add_help=False,  # Disable auto help so we can handle it manually
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  calculator add 5 3
  calculator subtract 10 4
  calculator multiply 2.5 4
  calculator divide 15 3
  calculator power 2 3
  calculator modulo 10 3
  calculator --help
        """.strip()
    )
    
    parser.add_argument(
        'operation',
        nargs='?',
        choices=["add", "subtract", "multiply", "divide", "power", "integer_divide", "modulo"],
        help="Operation to perform"
    )
    
    parser.add_argument(
        'operands',
        nargs='*',
        help="Operands for the operation"
    )
    
    parser.add_argument(
        '--version',
        action='store_true',
        help="Show version information"
    )
    
    # Add help manually to avoid auto-exit
    parser.add_argument(
        '-h', '--help',
        action='store_true',
        help="show this help message and exit"
    )
    
    return parser


def print_version() -> None:
    """Print version information."""
    print("Calculator CLI v1.0.0")


def print_help(parser: argparse.ArgumentParser) -> NoReturn:
    """Print help information and exit."""
    parser.print_help()
    sys.exit(0)


def main(args: List[str] = None) -> int:
    """Main entry point for the calculator CLI."""
    if args is None:
        args = sys.argv[1:]
    
    parser = create_parser()
    
    # Check for help before parsing to avoid exit
    if '--help' in args or '-h' in args:
        # Capture help text to print using Python's print function
        import io
        import sys as sys_module
        old_stdout = sys_module.stdout
        sys_module.stdout = captured_output = io.StringIO()
        try:
            parser.print_help()
            help_text = captured_output.getvalue()
        finally:
            sys_module.stdout = old_stdout
        print(help_text, end='')  # Use Python's print function to output help
        sys.exit(0)
    
    # If no arguments provided (other than the script name), show help
    if len(args) == 0:
        # Capture help text to print using Python's print function
        import io
        import sys as sys_module
        old_stdout = sys_module.stdout
        sys_module.stdout = captured_output = io.StringIO()
        try:
            parser.print_help()
            help_text = captured_output.getvalue()
        finally:
            sys_module.stdout = old_stdout
        print(help_text, end='')  # Use Python's print function to output help
        sys.exit(0)
    
    try:
        # Parse arguments without exiting on error
        args_parsed = parser.parse_args(args) 
    except SystemExit:
        # argparse calls sys.exit on error, we'll handle that gracefully
        return 1
    
    # Handle version flag
    if args_parsed.version:
        print_version()
        return 0
    
    # Handle operation and operands
    if not args_parsed.operation:
        print("Error: Operation is required")
        # Capture help text to print using Python's print function
        import io
        import sys as sys_module
        old_stdout = sys_module.stdout
        sys_module.stdout = captured_output = io.StringIO()
        try:
            parser.print_help()
            help_text = captured_output.getvalue()
        finally:
            sys_module.stdout = old_stdout
        print(help_text, end='')  # Use Python's print function to output help
        return 1
    
    # Validate operation name - must be case-sensitive
    valid_operations = ["add", "subtract", "multiply", "divide", "power", "integer_divide", "modulo"]
    if args_parsed.operation not in valid_operations:  # Case-sensitive check
        print(f"Error: Invalid operation '{args_parsed.operation}'. Valid operations are: {', '.join(valid_operations)}")
        return 1
    
    # Check number of operands
    if len(args_parsed.operands) != 2:
        print(f"Error: Expected 2 operands for {args_parsed.operation}, got {len(args_parsed.operands)}")
        # Capture help text to print using Python's print function
        import io
        import sys as sys_module
        old_stdout = sys_module.stdout
        sys_module.stdout = captured_output = io.StringIO()
        try:
            parser.print_help()
            help_text = captured_output.getvalue()
        finally:
            sys_module.stdout = old_stdout
        print(help_text, end='')  # Use Python's print function to output help
        return 1
    
    # Perform calculation with error handling
    result = safe_calculate(args_parsed.operation, args_parsed.operands[0], args_parsed.operands[1])
    
    if result is not None:
        print(f"Result: {result}")
        return 0
    else:
        print("Operation failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
