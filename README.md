# Calculator with AI

A comprehensive calculator application with AI capabilities, featuring robust arithmetic operations, error handling, and command-line interface. Built with modern Python features and comprehensive testing.

## Features

- **Basic Arithmetic Operations**: Add, subtract, multiply, divide
- **Advanced Operations**: Power, integer division, modulo
- **Error Handling**: Comprehensive error handling for edge cases (division by zero, invalid inputs, infinity, NaN)
- **Command-Line Interface (CLI)**: Easy-to-use command-line interface for all operations
- **Type Safety**: Full type hints for better code quality and IDE support
- **Comprehensive Testing**: Extensive test coverage for all operations and edge cases
- **Cross-Platform**: Supports WSL, macOS, and Linux

## Installation

### Prerequisites
- Python 3.12 or higher
- UV package manager

### Setup
1. Clone the repository
2. Install dependencies using UV:
   ```bash
   uv sync
   ```
   
   Or install the package manager if you don't have it:
   ```bash
   pip install uv
   uv sync
   ```

## Platform Support

- **Windows**: Works with WSL (Windows Subsystem for Linux)
- **macOS**: Fully supported
- **Linux**: Fully supported

## Usage

### Module Import

You can import and use the calculator functions directly in Python:

```python
from src.calculator import add, subtract, multiply, divide, power, integer_divide, modulo

# Basic operations
result = add(10, 5)          # 15.0
result = subtract(10, 3)     # 7.0
result = multiply(4, 3)      # 12.0
result = divide(10, 2)       # 5.0

# Advanced operations
result = power(2, 3)         # 8.0
result = integer_divide(7, 2) # 3
result = modulo(7, 3)        # 1.0

# Error handling
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

### Command-Line Interface (CLI)

The calculator provides a command-line interface for easy use:

```bash
# Basic operations
python -m src.calculator.cli add 10 5
python -m src.calculator.cli subtract 10 3
python -m src.calculator.cli multiply 4 3
python -m src.calculator.cli divide 10 2

# Advanced operations
python -m src.calculator.cli power 2 3
python -m src.calculator.cli integer_divide 7 2
python -m src.calculator.cli modulo 7 3

# Get help
python -m src.calculator.cli --help
python -m src.calculator.cli -h

# Get version
python -m src.calculator.cli --version
```

## Running Tests

Run the complete test suite with coverage:
```bash
uv run pytest tests/ --cov=src --cov-report=html --cov-report=term -v
```

Or run tests without coverage:
```bash
uv run pytest tests/
```

Run specific test files:
```bash
uv run pytest tests/test_calculator.py
uv run pytest tests/test_cli.py
uv run pytest tests/test_division.py
```

## All Operations with Examples

### Basic Operations

#### Add
```bash
python -m src.calculator.cli add 5 3     # Output: 8.0
python -m src.calculator.cli add -2 7    # Output: 5.0
python -m src.calculator.cli add 0.5 1.3 # Output: 1.8
```

#### Subtract
```bash
python -m src.calculator.cli subtract 10 4   # Output: 6.0
python -m src.calculator.cli subtract 3 -2   # Output: 5.0
python -m src.calculator.cli subtract 0 5    # Output: -5.0
```

#### Multiply
```bash
python -m src.calculator.cli multiply 6 7     # Output: 42.0
python -m src.calculator.cli multiply -3 4    # Output: -12.0
python -m src.calculator.cli multiply 2.5 4.0 # Output: 10.0
```

#### Divide
```bash
python -m src.calculator.cli divide 15 3   # Output: 5.0
python -m src.calculator.cli divide 10 4   # Output: 2.5
python -m src.calculator.cli divide -8 2   # Output: -4.0
```

### Advanced Operations

#### Power (Exponentiation)
```bash
python -m src.calculator.cli power 2 3     # Output: 8.0
python -m src.calculator.cli power 5 2     # Output: 25.0
python -m src.calculator.cli power 4 0.5   # Output: 2.0 (square root of 4)
```

#### Integer Division (Floor Division)
```bash
python -m src.calculator.cli integer_divide 7 2   # Output: 3
python -m src.calculator.cli integer_divide 10 3  # Output: 3
python -m src.calculator.cli integer_divide 15 4  # Output: 3
```

#### Modulo (Remainder)
```bash
python -m src.calculator.cli modulo 7 3     # Output: 1.0
python -m src.calculator.cli modulo 10 3    # Output: 1.0
python -m src.calculator.cli modulo 15 4    # Output: 3.0
```

### Error Handling Examples

#### Division by Zero
```bash
python -m src.calculator.cli divide 10 0    # Output: Division Error: Cannot divide by zero
python -m src.calculator.cli integer_divide 5 0  # Output: Division Error: Cannot divide by zero
```

#### Invalid Operations
```bash
python -m src.calculator.cli invalid_op 5 3    # Error: Invalid operation 'invalid_op'
python -m src.calculator.cli add 5             # Error: Expected 2 operands for add, got 1
```

## MCP Server Integration

This project includes configuration for Model Context Protocol (MCP) servers to access documentation for key tools:

- **UV Documentation**: Access to UV package manager documentation
- **pytest Documentation**: Access to pytest testing framework documentation  
- **Git Documentation**: Access to Git version control documentation

The configuration is located in `.qwen/mcp-servers.json`.

## Development

The project uses Python 3.12+ and leverages modern type hints for better code quality.