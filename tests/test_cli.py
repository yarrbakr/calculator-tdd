"""
Comprehensive tests for the CLI calculator interface.

This module tests the command-line interface for calculator operations,
ensuring proper functionality, error handling, and edge cases.
"""
import sys
from typing import List, Tuple
import pytest
from unittest.mock import patch, MagicMock


def test_addition_operation() -> None:
    """
    Test addition operation via CLI.
    
    Verifies that the CLI correctly performs addition of two numbers.
    """
    with patch('sys.argv', ['calculator', 'add', '5', '3']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(8.0)


def test_subtraction_operation() -> None:
    """
    Test subtraction operation via CLI.
    
    Verifies that the CLI correctly performs subtraction of two numbers.
    """
    with patch('sys.argv', ['calculator', 'subtract', '10', '4']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(6.0)


def test_multiplication_operation() -> None:
    """
    Test multiplication operation via CLI.
    
    Verifies that the CLI correctly performs multiplication of two numbers.
    """
    with patch('sys.argv', ['calculator', 'multiply', '6', '7']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(42.0)


def test_division_operation() -> None:
    """
    Test division operation via CLI.
    
    Verifies that the CLI correctly performs division of two numbers.
    """
    with patch('sys.argv', ['calculator', 'divide', '15', '3']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(5.0)


def test_division_by_zero_error() -> None:
    """
    Test division by zero error handling.
    
    Verifies that the CLI properly handles division by zero and shows an error message.
    """
    with patch('sys.argv', ['calculator', 'divide', '10', '0']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            with pytest.raises(SystemExit):
                main()
            # Verify error message is printed
            assert any('error' in str(call).lower() or 'zero' in str(call).lower() 
                      for call in mock_print.call_args_list)


def test_invalid_operation() -> None:
    """
    Test invalid operation handling.
    
    Verifies that the CLI handles unsupported operations gracefully.
    """
    with patch('sys.argv', ['calculator', 'invalid_op', '5', '3']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            with pytest.raises(SystemExit):
                main()
            # Verify error message for invalid operation
            assert any('invalid' in str(call).lower() or 'unknown' in str(call).lower() 
                      for call in mock_print.call_args_list)


def test_insufficient_arguments() -> None:
    """
    Test CLI behavior with insufficient arguments.
    
    Verifies that the CLI handles cases where not enough arguments are provided.
    """
    with patch('sys.argv', ['calculator', 'add', '5']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            with pytest.raises(SystemExit):
                main()
            # Verify error message for insufficient arguments
            assert any('usage' in str(call).lower() or 'arguments' in str(call).lower() 
                      for call in mock_print.call_args_list)


def test_extra_arguments() -> None:
    """
    Test CLI behavior with extra arguments.
    
    Verifies that the CLI handles cases where too many arguments are provided.
    """
    with patch('sys.argv', ['calculator', 'add', '5', '3', '2']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            with pytest.raises(SystemExit):
                main()
            # Verify error message for extra arguments
            assert any('usage' in str(call).lower() or 'arguments' in str(call).lower() 
                      for call in mock_print.call_args_list)


def test_invalid_number_format() -> None:
    """
    Test CLI behavior with invalid number formats.
    
    Verifies that the CLI handles non-numeric inputs gracefully.
    """
    with patch('sys.argv', ['calculator', 'add', 'abc', '3']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            with pytest.raises(SystemExit):
                main()
            # Verify error message for invalid number format
            assert any('invalid' in str(call).lower() or 'number' in str(call).lower() 
                      for call in mock_print.call_args_list)


def test_negative_numbers() -> None:
    """
    Test CLI operations with negative numbers.
    
    Verifies that the CLI correctly handles negative operands.
    """
    with patch('sys.argv', ['calculator', 'add', '-5', '3']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(-2.0)


def test_decimal_numbers() -> None:
    """
    Test CLI operations with decimal numbers.
    
    Verifies that the CLI correctly handles floating point operands.
    """
    with patch('sys.argv', ['calculator', 'multiply', '2.5', '4.0']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(10.0)


def test_help_flag() -> None:
    """
    Test CLI help functionality.
    
    Verifies that the CLI displays help information when requested.
    """
    with patch('sys.argv', ['calculator', '--help']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            with pytest.raises(SystemExit):
                main()
            # Verify help text is displayed
            assert len(mock_print.call_args_list) > 0


def test_help_short_flag() -> None:
    """
    Test CLI help functionality with short flag.
    
    Verifies that the CLI displays help information with -h flag.
    """
    with patch('sys.argv', ['calculator', '-h']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            with pytest.raises(SystemExit):
                main()
            # Verify help text is displayed
            assert len(mock_print.call_args_list) > 0


def test_version_flag() -> None:
    """
    Test CLI version functionality.
    
    Verifies that the CLI displays version information when requested.
    """
    with patch('sys.argv', ['calculator', '--version']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            # Verify version is printed (should be a string)
            assert len(mock_print.call_args_list) > 0


def test_zero_divided_by_number() -> None:
    """
    Test division of zero by a number.
    
    Verifies that dividing 0 by any number results in 0.
    """
    with patch('sys.argv', ['calculator', 'divide', '0', '5']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(0.0)


def test_subtract_negative_result() -> None:
    """
    Test subtraction resulting in negative number.
    
    Verifies that subtraction operations can result in negative values.
    """
    with patch('sys.argv', ['calculator', 'subtract', '3', '5']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(-2.0)


def test_divide_negative_numbers() -> None:
    """
    Test division with negative numbers.
    
    Verifies that division operations work correctly with negative operands.
    """
    with patch('sys.argv', ['calculator', 'divide', '-10', '2']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(-5.0)


def test_multiply_negative_numbers() -> None:
    """
    Test multiplication with negative numbers.
    
    Verifies that multiplication operations work correctly with negative operands.
    """
    with patch('sys.argv', ['calculator', 'multiply', '-3', '4']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(-12.0)


def test_large_numbers() -> None:
    """
    Test operations with large numbers.
    
    Verifies that the calculator handles large numbers correctly.
    """
    with patch('sys.argv', ['calculator', 'add', '999999999', '1']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(1000000000.0)


def test_precision_edge_case() -> None:
    """
    Test floating point precision edge cases.
    
    Verifies that calculator handles floating point precision issues appropriately.
    """
    with patch('sys.argv', ['calculator', 'add', '0.1', '0.2']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            main()
            # Result should be approximately 0.3, potentially with floating point precision
            result = mock_print.call_args[0][0]
            assert abs(result - 0.3) < 1e-9


def test_main_function_with_empty_args() -> None:
    """
    Test main function behavior with no arguments.
    
    Verifies that the CLI shows usage information when no arguments are provided.
    """
    with patch('sys.argv', ['calculator']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            with pytest.raises(SystemExit):
                main()
            # Should show usage information
            assert len(mock_print.call_args_list) > 0


def test_unsupported_operation_case_sensitivity() -> None:
    """
    Test that operations are case-sensitive and invalid case is handled.
    
    Verifies that uppercase or mixed-case operations are treated as invalid.
    """
    with patch('sys.argv', ['calculator', 'ADD', '2', '3']):
        from src.calculator.cli import main
        with patch('builtins.print') as mock_print:
            with pytest.raises(SystemExit):
                main()
            # Verify error message for invalid operation
            assert any('invalid' in str(call).lower() or 'unknown' in str(call).lower() 
                      for call in mock_print.call_args_list)