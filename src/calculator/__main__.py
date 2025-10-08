"""
Command Line Interface for the calculator application.

This module provides a CLI that supports basic arithmetic operations.
"""
import argparse
import sys
from typing import Union, Optional, NoReturn
import operator


def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Subtract two numbers."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y


def divide(x: float, y: float) -> float:
    """Divide two numbers."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


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
    parser = argparse.ArgumentParser(
        description="Calculator CLI - Perform basic arithmetic operations",
        prog="calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  calculator add 5 3
  calculator subtract 10 4
  calculator multiply 2.5 4
  calculator divide 15 3
  calculator --help
        """.strip()
    )
    
    parser.add_argument(
        'operation',
        nargs='?',
        help="Operation to perform: add, subtract, multiply, divide"
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
    
    return parser


def print_version() -> None:
    """Print version information."""
    print("Calculator CLI v1.0.0")


def print_help(parser: argparse.ArgumentParser) -> NoReturn:
    """Print help information and exit."""
    parser.print_help()
    sys.exit(0)


def main() -> None:
    """Main entry point for the calculator CLI."""
    parser = create_parser()
    
    # If no arguments provided, show help
    if len(sys.argv) == 1:
        print_help(parser)
    
    args = parser.parse_args()
    
    # Handle version flag
    if args.version:
        print_version()
        return
    
    # Handle operation and operands
    if not args.operation:
        print("Error: Operation is required")
        print_help(parser)
    
    # Validate operation name
    valid_operations = ['add', 'subtract', 'multiply', 'divide']
    if args.operation.lower() not in valid_operations:
        print(f"Error: Invalid operation '{args.operation}'. Valid operations are: {', '.join(valid_operations)}")
        sys.exit(1)
    
    # Check number of operands
    if len(args.operands) != 2:
        print(f"Error: Expected 2 operands for {args.operation}, got {len(args.operands)}")
        print_help(parser)
    
    # Parse operands
    try:
        x = float(args.operands[0])
        y = float(args.operands[1])
    except ValueError:
        print("Error: Operands must be valid numbers")
        sys.exit(1)
    
    # Perform calculation
    try:
        result = calculate(args.operation.lower(), x, y)
        print(result)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()