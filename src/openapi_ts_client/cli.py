"""Command-line interface for openapi-ts-client."""

from __future__ import annotations

import argparse
import sys

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


def main(argv: list[str] | None = None) -> int:
    """Main entry point for the CLI."""
    parser = create_parser()
    parser.parse_args(argv)

    # For now, just return 0 - implementation comes in later tasks
    return 0


if __name__ == "__main__":
    sys.exit(main())
