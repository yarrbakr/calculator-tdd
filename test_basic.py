def test_mcp_configuration_exists():
    """Test that verifies the MCP configuration file exists."""
    import os
    
    mcp_config_path = ".qwen/mcp-servers.json"
    assert os.path.exists(mcp_config_path), f"MCP configuration file does not exist at {mcp_config_path}"
    
    # Read the configuration file
    with open(mcp_config_path, 'r') as f:
        import json
        config = json.load(f)
    
    # Verify that all required documentation servers are configured
    required_servers = ['uv-docs', 'pytest-docs', 'git-docs']
    for server in required_servers:
        assert server in config['servers'], f"Required server {server} not found in configuration"
    
    print("MCP configuration verified successfully!")
    print(f"Configured servers: {list(config['servers'].keys())}")


def test_dependencies_installed():
    """Test that verifies dependencies were installed correctly."""
    import sys
    import subprocess
    
    # Check if pytest can be imported
    try:
        import pytest
        print(f"pytest version: {pytest.__version__}")
    except ImportError:
        raise AssertionError("pytest not found in environment")
    
    # Check if we can run pytest
    result = subprocess.run([sys.executable, '-m', 'pytest', '--version'], 
                          capture_output=True, text=True)
    assert result.returncode == 0, "pytest command failed"
    
    print("Dependencies verified successfully!")