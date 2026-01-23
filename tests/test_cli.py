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


class TestURLInput:
    """Test URL input handling."""

    def test_detect_url(self):
        """Test that URLs are detected correctly."""
        from openapi_ts_client.cli import is_url

        assert is_url("https://example.com/openapi.json")
        assert is_url("http://localhost:8080/spec.json")
        assert not is_url("./openapi.json")
        assert not is_url("/absolute/path.json")
        assert not is_url("-")

    def test_generate_from_url_mocked(self, tmp_path: Path, monkeypatch):
        """Test generating client from a URL with mocked HTTP."""
        import json

        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test API", "version": "1.0.0"},
            "paths": {},
        }

        # Create a test file to simulate URL content
        spec_file = tmp_path / "url_spec.json"
        spec_file.write_text(json.dumps(spec))

        # Monkeypatch load_spec_from_url in the cli module
        from openapi_ts_client import cli

        def mock_load_spec_from_url(url):
            return spec

        monkeypatch.setattr(cli, "load_spec_from_url", mock_load_spec_from_url)

        output_dir = tmp_path / "output"
        result = cli.main(
            [
                "https://example.com/openapi.json",
                "-o",
                str(output_dir),
            ]
        )
        assert result == 0
        assert output_dir.exists()
