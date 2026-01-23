"""Shared pytest fixtures for openapi-ts-client tests."""

import shutil

import pytest


def pytest_configure(config):
    """Verify required tools are available."""
    missing = []
    if shutil.which("tsc") is None:
        missing.append("tsc (TypeScript compiler)")
    if shutil.which("tsx") is None:
        missing.append("tsx (TypeScript execute)")

    if missing:
        raise pytest.UsageError(
            f"Required tools not found: {', '.join(missing)}\n"
            "Install with: npm install -g typescript tsx"
        )


@pytest.fixture(scope="session")
def ts_parser():
    """Shared tree-sitter TypeScript parser."""
    import tree_sitter_typescript as ts_typescript
    from tree_sitter import Language, Parser

    parser = Parser()
    parser.language = Language(ts_typescript.language_typescript())
    return parser
