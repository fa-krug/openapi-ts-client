"""Shared pytest fixtures for openapi-ts-client tests."""

import json
import shutil
from pathlib import Path

import pytest
import yaml

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def load_spec(fixture_name: str) -> dict:
    """Load OpenAPI spec from fixture directory (supports JSON and YAML)."""
    json_path = FIXTURES_DIR / fixture_name / "openapi.json"
    yaml_path = FIXTURES_DIR / fixture_name / "openapi.yml"

    if json_path.exists():
        return json.loads(json_path.read_text())
    elif yaml_path.exists():
        return yaml.safe_load(yaml_path.read_text())
    else:
        raise FileNotFoundError(
            f"No OpenAPI spec found in {FIXTURES_DIR / fixture_name}. "
            f"Expected openapi.json or openapi.yml"
        )


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
