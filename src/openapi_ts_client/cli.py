"""Command-line interface for openapi-ts-client."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

from . import ClientFormat, generate_typescript_client

# Read version from pyproject.toml - this is the canonical version
__version__ = "1.1.2"


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
        "-f",
        "--format",
        choices=["fetch", "axios", "angular"],
        default="fetch",
        help="Output format (default: fetch)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="./generated",
        help="Output directory (default: ./generated)",
    )
    parser.add_argument(
        "-c",
        "--config",
        help="Config file path (default: openapi-ts-client.json)",
    )
    parser.add_argument(
        "--no-validate",
        action="store_true",
        help="Skip OpenAPI spec validation",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Suppress all output except errors",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show detailed progress",
    )
    return parser


def load_spec_from_file(file_path: str) -> dict:
    """Load OpenAPI spec from a file."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    return json.loads(path.read_text())


def is_url(input_str: str) -> bool:
    """Check if input is a URL."""
    return input_str.startswith("http://") or input_str.startswith("https://")


def load_spec_from_url(url: str) -> dict:
    """Load OpenAPI spec from a URL."""
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise ConnectionError(f"Failed to fetch URL: {url}\n  HTTP {e.code}: {e.reason}") from e
    except urllib.error.URLError as e:
        raise ConnectionError(f"Failed to fetch URL: {url}\n  {e.reason}") from e


def load_spec_from_stdin() -> dict:
    """Load OpenAPI spec from stdin."""
    content = sys.stdin.read()
    if not content.strip():
        raise ValueError("No input received from stdin")
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON from stdin: {e}") from e


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


if __name__ == "__main__":
    sys.exit(main())
