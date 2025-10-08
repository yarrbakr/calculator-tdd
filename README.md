# Calculator with AI

This project integrates a calculator application with AI capabilities. It uses modern Python features and includes comprehensive testing.

## MCP Server Integration

This project includes configuration for Model Context Protocol (MCP) servers to access documentation for key tools:

- **UV Documentation**: Access to UV package manager documentation
- **pytest Documentation**: Access to pytest testing framework documentation  
- **Git Documentation**: Access to Git version control documentation

The configuration is located in `.qwen/mcp-servers.json`.

## Setup

1. Install dependencies: `uv sync`
2. Run tests: `uv run pytest`

## Development

The project uses Python 3.12+ and leverages modern type hints for better code quality.