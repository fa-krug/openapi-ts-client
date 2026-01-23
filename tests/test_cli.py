"""Tests for the CLI module."""

import subprocess
import sys
from pathlib import Path


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


class TestFileInput:
    """Test file input handling."""

    def test_generate_from_file(self, tmp_path: Path):
        """Test generating client from a file."""
        output_dir = tmp_path / "output"
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "openapi_ts_client.cli",
                "tests/fixtures/petstore/openapi.json",
                "-o",
                str(output_dir),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert output_dir.exists()
        assert (output_dir / "index.ts").exists()

    def test_file_not_found(self):
        """Test error when file doesn't exist."""
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "openapi_ts_client.cli",
                "nonexistent.json",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 1
        assert "not found" in result.stderr.lower() or "error" in result.stderr.lower()
