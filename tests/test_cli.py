"""Tests for the CLI module."""

import subprocess
import sys


class TestCLIBasics:
    """Test basic CLI functionality."""

    def test_help_flag(self):
        """Test that --help shows usage information."""
        result = subprocess.run(
            [sys.executable, "-m", "openapi_ts_client.cli", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "openapi-ts-client" in result.stdout.lower() or "usage" in result.stdout.lower()
        assert "--format" in result.stdout
        assert "--output" in result.stdout

    def test_version_flag(self):
        """Test that --version shows version."""
        result = subprocess.run(
            [sys.executable, "-m", "openapi_ts_client.cli", "--version"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        # Version should be in stdout or stderr (argparse puts it in different places)
        output = result.stdout + result.stderr
        assert "1.1.2" in output or "openapi-ts-client" in output.lower()
