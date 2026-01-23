# CLI Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a command-line interface to openapi-ts-client, enabling use as both a library and a CLI tool.

**Architecture:** Create `cli.py` module with argparse for argument handling. Support file/URL/stdin input, config files for multi-client generation, and progress output with quiet/verbose modes. CLI calls existing `generate_typescript_client()` function.

**Tech Stack:** Python 3.8+, argparse (stdlib), urllib.request (stdlib), pytest

---

## Task 1: Create CLI skeleton with --help and --version

**Files:**
- Create: `src/openapi_ts_client/cli.py`
- Modify: `pyproject.toml:31` (add after dependencies section)
- Test: `tests/test_cli.py`

**Step 1: Write the failing test**

Create `tests/test_cli.py`:

```python
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
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli.py::TestCLIBasics -v`
Expected: FAIL with "No module named 'openapi_ts_client.cli'"

**Step 3: Write minimal implementation**

Create `src/openapi_ts_client/cli.py`:

```python
"""Command-line interface for openapi-ts-client."""

import argparse
import sys

from . import __version__


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog="openapi-ts-client",
        description="Generate TypeScript clients from OpenAPI specifications.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"openapi-ts-client {__version__}",
    )
    parser.add_argument(
        "input",
        nargs="?",
        help="OpenAPI spec file path, URL, or '-' for stdin",
    )
    parser.add_argument(
        "-f", "--format",
        choices=["fetch", "axios", "angular"],
        default="fetch",
        help="Output format (default: fetch)",
    )
    parser.add_argument(
        "-o", "--output",
        default="./generated",
        help="Output directory (default: ./generated)",
    )
    parser.add_argument(
        "-c", "--config",
        help="Config file path (default: openapi-ts-client.json)",
    )
    parser.add_argument(
        "--no-validate",
        action="store_true",
        help="Skip OpenAPI spec validation",
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress all output except errors",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed progress",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)

    # For now, just return 0 - implementation comes in later tasks
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_cli.py::TestCLIBasics -v`
Expected: PASS

**Step 5: Add entry point to pyproject.toml**

Add after line 34 (after `[project.urls]` section):

```toml
[project.scripts]
openapi-ts-client = "openapi_ts_client.cli:main"
```

**Step 6: Reinstall package and verify entry point**

Run: `pip install -e . && openapi-ts-client --help`
Expected: Shows help text

**Step 7: Commit**

```bash
git add src/openapi_ts_client/cli.py tests/test_cli.py pyproject.toml
git commit -m "feat(cli): add CLI skeleton with --help and --version"
```

---

## Task 2: Implement file input

**Files:**
- Modify: `src/openapi_ts_client/cli.py`
- Modify: `tests/test_cli.py`

**Step 1: Write the failing test**

Add to `tests/test_cli.py`:

```python
from pathlib import Path
import tempfile


class TestFileInput:
    """Test file input handling."""

    def test_generate_from_file(self, tmp_path: Path):
        """Test generating client from a file."""
        output_dir = tmp_path / "output"
        result = subprocess.run(
            [
                sys.executable, "-m", "openapi_ts_client.cli",
                "tests/fixtures/petstore/openapi.json",
                "-o", str(output_dir),
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
                sys.executable, "-m", "openapi_ts_client.cli",
                "nonexistent.json",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 1
        assert "not found" in result.stderr.lower() or "error" in result.stderr.lower()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli.py::TestFileInput -v`
Expected: FAIL (no output generated)

**Step 3: Write implementation**

Update `src/openapi_ts_client/cli.py`, replace `main` function:

```python
import json
from pathlib import Path

from . import ClientFormat, generate_typescript_client


def load_spec_from_file(file_path: str) -> dict:
    """Load OpenAPI spec from a file."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    return json.loads(path.read_text())


def get_client_format(format_str: str) -> ClientFormat:
    """Convert format string to ClientFormat enum."""
    return {
        "fetch": ClientFormat.FETCH,
        "axios": ClientFormat.AXIOS,
        "angular": ClientFormat.ANGULAR,
    }[format_str]


def main(argv: list[str] | None = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)

    if not args.input:
        parser.print_help()
        return 2

    try:
        # Load spec from file
        spec = load_spec_from_file(args.input)

        # Generate client
        client_format = get_client_format(args.format)
        generate_typescript_client(spec, client_format, args.output)

        if not args.quiet:
            print(f"Generated {args.format} client to {args.output}")

        return 0
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
```

Add imports at top:

```python
import json
from pathlib import Path

from . import ClientFormat, generate_typescript_client
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_cli.py::TestFileInput -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/cli.py tests/test_cli.py
git commit -m "feat(cli): implement file input"
```

---

## Task 3: Implement URL input

**Files:**
- Modify: `src/openapi_ts_client/cli.py`
- Modify: `tests/test_cli.py`

**Step 1: Write the failing test**

Add to `tests/test_cli.py`:

```python
from unittest.mock import patch, MagicMock


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

    def test_generate_from_url(self, tmp_path: Path):
        """Test generating client from a URL."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test API", "version": "1.0.0"},
            "paths": {},
        }

        with patch("openapi_ts_client.cli.load_spec_from_url") as mock_load:
            mock_load.return_value = spec

            output_dir = tmp_path / "output"
            result = subprocess.run(
                [
                    sys.executable, "-m", "openapi_ts_client.cli",
                    "https://example.com/openapi.json",
                    "-o", str(output_dir),
                ],
                capture_output=True,
                text=True,
            )
            assert result.returncode == 0, f"stderr: {result.stderr}"
            mock_load.assert_called_once_with("https://example.com/openapi.json")
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli.py::TestURLInput -v`
Expected: FAIL (is_url not defined)

**Step 3: Write implementation**

Add to `src/openapi_ts_client/cli.py`:

```python
import urllib.request
import urllib.error


def is_url(input_str: str) -> bool:
    """Check if input is a URL."""
    return input_str.startswith("http://") or input_str.startswith("https://")


def load_spec_from_url(url: str) -> dict:
    """Load OpenAPI spec from a URL."""
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise ConnectionError(f"Failed to fetch URL: {url}\n  {e.reason}")
    except urllib.error.HTTPError as e:
        raise ConnectionError(f"Failed to fetch URL: {url}\n  HTTP {e.code}: {e.reason}")
```

Update `main` function to use URL detection:

```python
def main(argv: list[str] | None = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)

    if not args.input:
        parser.print_help()
        return 2

    try:
        # Load spec based on input type
        if is_url(args.input):
            spec = load_spec_from_url(args.input)
        else:
            spec = load_spec_from_file(args.input)

        # Generate client
        client_format = get_client_format(args.format)
        generate_typescript_client(spec, client_format, args.output)

        if not args.quiet:
            print(f"Generated {args.format} client to {args.output}")

        return 0
    except (FileNotFoundError, ConnectionError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_cli.py::TestURLInput -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/cli.py tests/test_cli.py
git commit -m "feat(cli): implement URL input"
```

---

## Task 4: Implement stdin input

**Files:**
- Modify: `src/openapi_ts_client/cli.py`
- Modify: `tests/test_cli.py`

**Step 1: Write the failing test**

Add to `tests/test_cli.py`:

```python
class TestStdinInput:
    """Test stdin input handling."""

    def test_generate_from_stdin(self, tmp_path: Path):
        """Test generating client from stdin."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Stdin API", "version": "1.0.0"},
            "paths": {},
        }

        output_dir = tmp_path / "output"
        result = subprocess.run(
            [
                sys.executable, "-m", "openapi_ts_client.cli",
                "-",
                "-o", str(output_dir),
            ],
            input=json.dumps(spec),
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert output_dir.exists()

    def test_empty_stdin(self, tmp_path: Path):
        """Test error on empty stdin."""
        output_dir = tmp_path / "output"
        result = subprocess.run(
            [
                sys.executable, "-m", "openapi_ts_client.cli",
                "-",
                "-o", str(output_dir),
            ],
            input="",
            capture_output=True,
            text=True,
        )
        assert result.returncode == 1
        assert "error" in result.stderr.lower()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli.py::TestStdinInput -v`
Expected: FAIL

**Step 3: Write implementation**

Add to `src/openapi_ts_client/cli.py`:

```python
def load_spec_from_stdin() -> dict:
    """Load OpenAPI spec from stdin."""
    content = sys.stdin.read()
    if not content.strip():
        raise ValueError("No input received from stdin")
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON from stdin: {e}")
```

Update `main` function:

```python
def main(argv: list[str] | None = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)

    if not args.input:
        parser.print_help()
        return 2

    try:
        # Load spec based on input type
        if args.input == "-":
            spec = load_spec_from_stdin()
        elif is_url(args.input):
            spec = load_spec_from_url(args.input)
        else:
            spec = load_spec_from_file(args.input)

        # Generate client
        client_format = get_client_format(args.format)
        generate_typescript_client(spec, client_format, args.output)

        if not args.quiet:
            print(f"Generated {args.format} client to {args.output}")

        return 0
    except (FileNotFoundError, ConnectionError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_cli.py::TestStdinInput -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/cli.py tests/test_cli.py
git commit -m "feat(cli): implement stdin input"
```

---

## Task 5: Implement config file support

**Files:**
- Modify: `src/openapi_ts_client/cli.py`
- Modify: `tests/test_cli.py`

**Step 1: Write the failing test**

Add to `tests/test_cli.py`:

```python
import os


class TestConfigFile:
    """Test config file handling."""

    def test_single_client_config(self, tmp_path: Path):
        """Test config with single client shorthand."""
        config = {
            "input": "tests/fixtures/petstore/openapi.json",
            "format": "axios",
            "output": str(tmp_path / "output"),
        }
        config_file = tmp_path / "openapi-ts-client.json"
        config_file.write_text(json.dumps(config))

        result = subprocess.run(
            [sys.executable, "-m", "openapi_ts_client.cli"],
            capture_output=True,
            text=True,
            cwd=tmp_path,
        )
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert (tmp_path / "output" / "index.ts").exists()

    def test_multi_client_config(self, tmp_path: Path):
        """Test config with multiple clients."""
        config = {
            "clients": [
                {
                    "input": "tests/fixtures/petstore/openapi.json",
                    "format": "fetch",
                    "output": str(tmp_path / "fetch-client"),
                },
                {
                    "input": "tests/fixtures/petstore/openapi.json",
                    "format": "axios",
                    "output": str(tmp_path / "axios-client"),
                },
            ]
        }
        config_file = tmp_path / "openapi-ts-client.json"
        config_file.write_text(json.dumps(config))

        # Need to use absolute paths since we're changing cwd
        result = subprocess.run(
            [sys.executable, "-m", "openapi_ts_client.cli"],
            capture_output=True,
            text=True,
            cwd=tmp_path,
            env={**os.environ, "PYTHONPATH": str(Path.cwd())},
        )
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert (tmp_path / "fetch-client").exists()
        assert (tmp_path / "axios-client").exists()

    def test_custom_config_path(self, tmp_path: Path):
        """Test --config flag for custom config path."""
        config = {
            "input": "tests/fixtures/petstore/openapi.json",
            "output": str(tmp_path / "output"),
        }
        config_file = tmp_path / "custom-config.json"
        config_file.write_text(json.dumps(config))

        result = subprocess.run(
            [
                sys.executable, "-m", "openapi_ts_client.cli",
                "--config", str(config_file),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"stderr: {result.stderr}"

    def test_explicit_input_ignores_config(self, tmp_path: Path):
        """Test that explicit input argument ignores config file."""
        config = {
            "input": "wrong-file.json",
            "output": str(tmp_path / "config-output"),
        }
        config_file = tmp_path / "openapi-ts-client.json"
        config_file.write_text(json.dumps(config))

        output_dir = tmp_path / "cli-output"
        result = subprocess.run(
            [
                sys.executable, "-m", "openapi_ts_client.cli",
                "tests/fixtures/petstore/openapi.json",
                "-o", str(output_dir),
            ],
            capture_output=True,
            text=True,
            cwd=tmp_path,
        )
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert output_dir.exists()
        assert not (tmp_path / "config-output").exists()

    def test_invalid_config_file(self, tmp_path: Path):
        """Test error on invalid config file."""
        config_file = tmp_path / "openapi-ts-client.json"
        config_file.write_text("not valid json")

        result = subprocess.run(
            [sys.executable, "-m", "openapi_ts_client.cli"],
            capture_output=True,
            text=True,
            cwd=tmp_path,
        )
        assert result.returncode == 2
        assert "config" in result.stderr.lower() or "error" in result.stderr.lower()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli.py::TestConfigFile -v`
Expected: FAIL

**Step 3: Write implementation**

Add to `src/openapi_ts_client/cli.py`:

```python
DEFAULT_CONFIG_NAME = "openapi-ts-client.json"


def load_config(config_path: str | None) -> dict | None:
    """Load config file if it exists."""
    if config_path:
        path = Path(config_path)
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")
    else:
        path = Path(DEFAULT_CONFIG_NAME)
        if not path.exists():
            return None

    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid config file: {path}\n  {e}")


def normalize_config(config: dict) -> list[dict]:
    """Normalize config to list of client configs."""
    if "clients" in config:
        return config["clients"]
    # Single client shorthand
    return [config]


def validate_client_config(client: dict, index: int) -> None:
    """Validate a single client config."""
    if "input" not in client:
        raise ValueError(f"Config client #{index + 1} missing required 'input' field")


def generate_from_config(config: dict, args) -> int:
    """Generate clients from config file."""
    clients = normalize_config(config)

    for i, client in enumerate(clients):
        validate_client_config(client, i)

        input_path = client["input"]
        format_str = client.get("format", "fetch")
        output_path = client.get("output", "./generated")

        # Load spec
        if is_url(input_path):
            spec = load_spec_from_url(input_path)
        else:
            spec = load_spec_from_file(input_path)

        # Generate
        client_format = get_client_format(format_str)
        generate_typescript_client(spec, client_format, output_path)

        if not args.quiet:
            if len(clients) > 1:
                print(f"[{i + 1}/{len(clients)}] Generated {format_str} client to {output_path}")
            else:
                print(f"Generated {format_str} client to {output_path}")

    return 0
```

Update `main` function:

```python
def main(argv: list[str] | None = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)

    try:
        # If explicit input given, use it (ignore config)
        if args.input:
            # Load spec based on input type
            if args.input == "-":
                spec = load_spec_from_stdin()
            elif is_url(args.input):
                spec = load_spec_from_url(args.input)
            else:
                spec = load_spec_from_file(args.input)

            # Generate client
            client_format = get_client_format(args.format)
            generate_typescript_client(spec, client_format, args.output)

            if not args.quiet:
                print(f"Generated {args.format} client to {args.output}")

            return 0

        # No input - try config file
        config = load_config(args.config)
        if config is None:
            print("Error: No input provided and no config file found", file=sys.stderr)
            print("  Usage: openapi-ts-client <input> [options]", file=sys.stderr)
            return 2

        return generate_from_config(config, args)

    except (FileNotFoundError, ConnectionError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_cli.py::TestConfigFile -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/cli.py tests/test_cli.py
git commit -m "feat(cli): implement config file support"
```

---

## Task 6: Implement progress output formatting

**Files:**
- Modify: `src/openapi_ts_client/cli.py`
- Modify: `tests/test_cli.py`

**Step 1: Write the failing test**

Add to `tests/test_cli.py`:

```python
class TestOutputFormatting:
    """Test output formatting options."""

    def test_quiet_mode_no_output(self, tmp_path: Path):
        """Test that --quiet suppresses output."""
        output_dir = tmp_path / "output"
        result = subprocess.run(
            [
                sys.executable, "-m", "openapi_ts_client.cli",
                "tests/fixtures/petstore/openapi.json",
                "-o", str(output_dir),
                "-q",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert result.stdout == ""

    def test_default_output_shows_progress(self, tmp_path: Path):
        """Test that default output shows progress."""
        output_dir = tmp_path / "output"
        result = subprocess.run(
            [
                sys.executable, "-m", "openapi_ts_client.cli",
                "tests/fixtures/petstore/openapi.json",
                "-o", str(output_dir),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "Generated" in result.stdout or "generated" in result.stdout

    def test_verbose_mode_shows_details(self, tmp_path: Path):
        """Test that --verbose shows detailed output."""
        output_dir = tmp_path / "output"
        result = subprocess.run(
            [
                sys.executable, "-m", "openapi_ts_client.cli",
                "tests/fixtures/petstore/openapi.json",
                "-o", str(output_dir),
                "-v",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        # Verbose should show more details
        output = result.stdout.lower()
        assert "reading" in output or "generating" in output or "petstore" in output.lower()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli.py::TestOutputFormatting -v`
Expected: Partial pass, verbose test may fail

**Step 3: Write implementation**

Add output helper class to `src/openapi_ts_client/cli.py`:

```python
class Output:
    """Handle CLI output based on verbosity settings."""

    def __init__(self, quiet: bool = False, verbose: bool = False):
        self.quiet = quiet
        self.verbose = verbose

    def info(self, message: str) -> None:
        """Print info message (unless quiet)."""
        if not self.quiet:
            print(message)

    def detail(self, message: str) -> None:
        """Print detail message (only in verbose mode)."""
        if self.verbose and not self.quiet:
            print(f"  {message}")

    def success(self, message: str) -> None:
        """Print success message (unless quiet)."""
        if not self.quiet:
            print(f"✓ {message}")

    def error(self, message: str) -> None:
        """Print error message (always shown)."""
        print(f"Error: {message}", file=sys.stderr)
```

Update `main` function to use Output class:

```python
def main(argv: list[str] | None = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args(argv)
    out = Output(quiet=args.quiet, verbose=args.verbose)

    try:
        # If explicit input given, use it (ignore config)
        if args.input:
            out.info(f"Generating {args.format} client...")

            # Load spec based on input type
            if args.input == "-":
                out.detail("Reading spec from stdin")
                spec = load_spec_from_stdin()
            elif is_url(args.input):
                out.detail(f"Fetching spec from {args.input}")
                spec = load_spec_from_url(args.input)
            else:
                out.detail(f"Reading spec from {args.input}")
                spec = load_spec_from_file(args.input)

            # Log spec details in verbose mode
            if args.verbose:
                info = spec.get("info", {})
                out.detail(f"API: {info.get('title', 'Unknown')} v{info.get('version', '?')}")
                schemas = spec.get("components", {}).get("schemas", {})
                out.detail(f"Models: {len(schemas)}")

            # Generate client
            client_format = get_client_format(args.format)
            generate_typescript_client(spec, client_format, args.output)

            out.success(f"Generated to {args.output}")

            return 0

        # No input - try config file
        config = load_config(args.config)
        if config is None:
            out.error("No input provided and no config file found")
            print("  Usage: openapi-ts-client <input> [options]", file=sys.stderr)
            return 2

        return generate_from_config(config, args, out)

    except (FileNotFoundError, ConnectionError) as e:
        out.error(str(e))
        return 1
    except ValueError as e:
        out.error(str(e))
        return 2
    except Exception as e:
        out.error(str(e))
        return 1
```

Update `generate_from_config` to accept `out` parameter:

```python
def generate_from_config(config: dict, args, out: Output) -> int:
    """Generate clients from config file."""
    clients = normalize_config(config)

    if len(clients) > 1:
        out.info(f"Generating {len(clients)} clients...")

    for i, client in enumerate(clients):
        validate_client_config(client, i)

        input_path = client["input"]
        format_str = client.get("format", "fetch")
        output_path = client.get("output", "./generated")

        if len(clients) > 1:
            out.info(f"\n[{i + 1}/{len(clients)}] {format_str} → {output_path}")
        else:
            out.info(f"Generating {format_str} client...")

        # Load spec
        if is_url(input_path):
            out.detail(f"Fetching spec from {input_path}")
            spec = load_spec_from_url(input_path)
        else:
            out.detail(f"Reading spec from {input_path}")
            spec = load_spec_from_file(input_path)

        # Generate
        client_format = get_client_format(format_str)
        generate_typescript_client(spec, client_format, output_path)

        out.success(f"Generated to {output_path}")

    if len(clients) > 1:
        out.info("\nDone.")

    return 0
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_cli.py::TestOutputFormatting -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/cli.py tests/test_cli.py
git commit -m "feat(cli): implement progress output formatting"
```

---

## Task 7: Implement --no-validate flag

**Files:**
- Modify: `src/openapi_ts_client/generator.py`
- Modify: `src/openapi_ts_client/cli.py`
- Modify: `tests/test_cli.py`

**Step 1: Write the failing test**

Add to `tests/test_cli.py`:

```python
class TestValidation:
    """Test validation options."""

    def test_no_validate_skips_validation(self, tmp_path: Path):
        """Test that --no-validate skips spec validation."""
        # Create an invalid spec (missing required info.title)
        invalid_spec = {
            "openapi": "3.0.0",
            "info": {"version": "1.0.0"},  # missing title
            "paths": {},
        }
        spec_file = tmp_path / "invalid.json"
        spec_file.write_text(json.dumps(invalid_spec))

        output_dir = tmp_path / "output"

        # Without --no-validate, should fail
        result = subprocess.run(
            [
                sys.executable, "-m", "openapi_ts_client.cli",
                str(spec_file),
                "-o", str(output_dir),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 1

        # With --no-validate, should succeed (or at least get further)
        result = subprocess.run(
            [
                sys.executable, "-m", "openapi_ts_client.cli",
                str(spec_file),
                "-o", str(output_dir),
                "--no-validate",
            ],
            capture_output=True,
            text=True,
        )
        # May still fail in generation, but not in validation
        # Check that it didn't fail with validation error
        if result.returncode != 0:
            assert "info.title" not in result.stderr.lower()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli.py::TestValidation -v`
Expected: FAIL

**Step 3: Write implementation**

Update `src/openapi_ts_client/generator.py`, modify `generate_typescript_client` signature:

```python
def generate_typescript_client(
    openapi_spec: Union[Dict[str, Any], str],
    output_format: ClientFormat = ClientFormat.FETCH,
    output_path: Union[str, Path, None] = None,
    skip_validation: bool = False,
) -> str:
```

And update the validation call (around line 102):

```python
    # Validate OpenAPI specification
    if not skip_validation:
        func_logger.info("Validating OpenAPI specification")
        openapi_version = _validate_openapi_spec(parsed_spec, func_logger)
    else:
        func_logger.info("Skipping OpenAPI specification validation")
        openapi_version = parsed_spec.get("openapi") or parsed_spec.get("swagger", "unknown")
```

Update `src/openapi_ts_client/cli.py` to pass the flag:

In the main function where `generate_typescript_client` is called:

```python
generate_typescript_client(spec, client_format, args.output, skip_validation=args.no_validate)
```

And in `generate_from_config`:

```python
generate_typescript_client(spec, client_format, output_path, skip_validation=args.no_validate)
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_cli.py::TestValidation -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generator.py src/openapi_ts_client/cli.py tests/test_cli.py
git commit -m "feat(cli): implement --no-validate flag"
```

---

## Task 8: Run full test suite and verify

**Step 1: Run all CLI tests**

Run: `pytest tests/test_cli.py -v`
Expected: All PASS

**Step 2: Run full test suite**

Run: `pytest tests/ -v`
Expected: All existing tests still pass

**Step 3: Manual verification**

```bash
# Reinstall
pip install -e .

# Test basic usage
openapi-ts-client tests/fixtures/petstore/openapi.json -o /tmp/test-cli

# Test with format
openapi-ts-client tests/fixtures/petstore/openapi.json -f axios -o /tmp/test-axios

# Test verbose
openapi-ts-client tests/fixtures/petstore/openapi.json -v -o /tmp/test-verbose

# Test quiet
openapi-ts-client tests/fixtures/petstore/openapi.json -q -o /tmp/test-quiet

# Test stdin
cat tests/fixtures/petstore/openapi.json | openapi-ts-client - -o /tmp/test-stdin

# Verify output exists
ls /tmp/test-cli
```

**Step 4: Commit any final fixes**

```bash
git add -A
git commit -m "test(cli): verify full test suite passes"
```

---

## Task 9: Update documentation

**Files:**
- Modify: `README.md`

**Step 1: Add CLI section to README**

Add after the installation section:

```markdown
## CLI Usage

```bash
# Generate from file
openapi-ts-client ./openapi.json

# Specify output format and directory
openapi-ts-client ./openapi.json -f axios -o ./src/api

# Generate from URL
openapi-ts-client https://api.example.com/openapi.json

# Generate from stdin
cat openapi.json | openapi-ts-client -

# Use config file
openapi-ts-client --config ./my-config.json

# Verbose output
openapi-ts-client ./openapi.json -v
```

### Config File

Create `openapi-ts-client.json` for repeated use:

```json
{
  "clients": [
    {
      "input": "./specs/users-api.json",
      "format": "fetch",
      "output": "./src/api/users"
    },
    {
      "input": "./specs/orders-api.json",
      "format": "axios",
      "output": "./src/api/orders"
    }
  ]
}
```

Then run:

```bash
openapi-ts-client
```

### Options

| Option | Description | Default |
|--------|-------------|---------|
| `-f, --format` | Output format: fetch, axios, angular | fetch |
| `-o, --output` | Output directory | ./generated |
| `-c, --config` | Config file path | openapi-ts-client.json |
| `--no-validate` | Skip OpenAPI spec validation | - |
| `-q, --quiet` | Suppress all output except errors | - |
| `-v, --verbose` | Show detailed progress | - |
```

**Step 2: Commit**

```bash
git add README.md
git commit -m "docs: add CLI usage documentation"
```

---

## Summary

After completing all tasks:

1. CLI is fully functional with file/URL/stdin input
2. Config file supports single and multi-client generation
3. Progress output has quiet/verbose modes
4. --no-validate flag skips spec validation
5. All tests pass
6. Documentation updated

Run `pytest tests/ -v` to verify everything works.
