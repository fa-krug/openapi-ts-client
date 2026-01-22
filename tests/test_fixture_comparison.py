"""Fixture comparison tests for Angular client generation.

These tests verify that the generator produces output identical to the reference
fixtures in tests/fixtures/. Comparison is byte-for-byte exact.
"""

import difflib
import json
from pathlib import Path

import pytest

from openapi_ts_client import ClientFormat, generate_typescript_client

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def collect_files(directory: Path) -> dict[str, bytes]:
    """Collect all files in directory recursively, returning {relative_path: content}."""
    files = {}
    for file_path in directory.rglob("*"):
        if file_path.is_file():
            rel_path = str(file_path.relative_to(directory))
            files[rel_path] = file_path.read_bytes()
    return files


def format_diff(expected: bytes, actual: bytes, max_lines: int = 50) -> str:
    """Format a unified diff between expected and actual content."""
    try:
        expected_lines = expected.decode("utf-8").splitlines(keepends=True)
        actual_lines = actual.decode("utf-8").splitlines(keepends=True)
    except UnicodeDecodeError:
        return "(binary files differ)"

    diff = list(
        difflib.unified_diff(
            expected_lines,
            actual_lines,
            fromfile="expected (fixture)",
            tofile="actual (generated)",
        )
    )

    if len(diff) > max_lines:
        diff = diff[:max_lines] + [f"\n... ({len(diff) - max_lines} more lines)\n"]

    return "".join(diff)


@pytest.mark.parametrize("fixture_name", ["petstore", "space_zoo"])
def test_angular_generation_matches_fixture(fixture_name: str, tmp_path: Path) -> None:
    """Test that Angular generation produces output identical to fixture."""
    fixture_dir = FIXTURES_DIR / fixture_name
    spec_path = fixture_dir / "openapi.json"
    expected_dir = fixture_dir / "angular"

    # Load OpenAPI spec
    spec = json.loads(spec_path.read_text())

    # Generate Angular client
    generate_typescript_client(
        spec,
        output_format=ClientFormat.ANGULAR,
        output_path=tmp_path,
    )

    # Collect files from both directories
    expected_files = collect_files(expected_dir)
    actual_files = collect_files(tmp_path)

    expected_paths = set(expected_files.keys())
    actual_paths = set(actual_files.keys())

    # Check for missing files
    missing = expected_paths - actual_paths
    if missing:
        pytest.fail("Missing files in generated output:\n  " + "\n  ".join(sorted(missing)))

    # Check for extra files
    extra = actual_paths - expected_paths
    if extra:
        pytest.fail("Unexpected files in generated output:\n  " + "\n  ".join(sorted(extra)))

    # Compare content of each file
    mismatches = []
    for rel_path in sorted(expected_paths):
        expected_content = expected_files[rel_path]
        actual_content = actual_files[rel_path]

        if expected_content != actual_content:
            diff = format_diff(expected_content, actual_content)
            mismatches.append(f"MISMATCH: {rel_path}\n{diff}")

    if mismatches:
        pytest.fail("\n\n".join(mismatches))
