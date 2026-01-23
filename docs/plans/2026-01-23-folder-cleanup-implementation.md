# Destination Folder Cleanup Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add safeguards for non-empty destination folders with `clean`/`force` options for both function API and CLI.

**Architecture:** Add helper functions to detect non-hidden files and clear directories. The generator function gains `clean` and `force` boolean parameters. The CLI adds `--clean` and `--force` flags plus an interactive prompt when running in TTY mode.

**Tech Stack:** Python 3, pathlib, shutil, sys.stdin.isatty()

---

### Task 1: Add OutputDirectoryNotEmptyError Exception

**Files:**
- Create: `src/openapi_ts_client/exceptions.py`
- Modify: `src/openapi_ts_client/__init__.py`
- Test: `tests/test_generator.py`

**Step 1: Write the failing test**

Add to `tests/test_generator.py`:

```python
class TestOutputDirectoryNotEmpty:
    """Tests for non-empty output directory handling."""

    def test_error_is_importable(self):
        """Test that OutputDirectoryNotEmptyError can be imported."""
        from openapi_ts_client import OutputDirectoryNotEmptyError
        assert issubclass(OutputDirectoryNotEmptyError, Exception)
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_generator.py::TestOutputDirectoryNotEmpty::test_error_is_importable -v`
Expected: FAIL with "cannot import name 'OutputDirectoryNotEmptyError'"

**Step 3: Create exceptions module**

Create `src/openapi_ts_client/exceptions.py`:

```python
"""Custom exceptions for openapi-ts-client."""


class OutputDirectoryNotEmptyError(Exception):
    """Raised when output directory is not empty and neither clean nor force is set."""

    def __init__(self, path, file_count: int):
        self.path = path
        self.file_count = file_count
        super().__init__(
            f"Output directory '{path}' is not empty (contains {file_count} files). "
            f"Use clean=True to clear the directory first, or force=True to continue anyway."
        )
```

**Step 4: Export from __init__.py**

In `src/openapi_ts_client/__init__.py`, add import and export:

```python
from .exceptions import OutputDirectoryNotEmptyError

__all__ = [
    "generate_typescript_client",
    "ClientFormat",
    "OutputDirectoryNotEmptyError",
    "__version__",
]
```

**Step 5: Run test to verify it passes**

Run: `pytest tests/test_generator.py::TestOutputDirectoryNotEmpty::test_error_is_importable -v`
Expected: PASS

**Step 6: Commit**

```bash
git add src/openapi_ts_client/exceptions.py src/openapi_ts_client/__init__.py tests/test_generator.py
git commit -m "feat: add OutputDirectoryNotEmptyError exception"
```

---

### Task 2: Add _get_non_hidden_files Helper

**Files:**
- Modify: `src/openapi_ts_client/generator.py`
- Test: `tests/test_generator.py`

**Step 1: Write the failing test**

Add to `tests/test_generator.py`:

```python
class TestGetNonHiddenFiles:
    """Tests for _get_non_hidden_files helper."""

    def test_empty_directory_returns_empty_list(self, tmp_path: Path):
        """Test that empty directory returns empty list."""
        from openapi_ts_client.generator import _get_non_hidden_files
        result = _get_non_hidden_files(tmp_path)
        assert result == []

    def test_returns_non_hidden_files(self, tmp_path: Path):
        """Test that non-hidden files are returned."""
        from openapi_ts_client.generator import _get_non_hidden_files
        (tmp_path / "file1.ts").touch()
        (tmp_path / "file2.ts").touch()
        result = _get_non_hidden_files(tmp_path)
        assert len(result) == 2

    def test_ignores_dotfiles(self, tmp_path: Path):
        """Test that dotfiles are ignored."""
        from openapi_ts_client.generator import _get_non_hidden_files
        (tmp_path / ".gitkeep").touch()
        (tmp_path / ".gitignore").touch()
        result = _get_non_hidden_files(tmp_path)
        assert result == []

    def test_mixed_files(self, tmp_path: Path):
        """Test with mix of hidden and non-hidden files."""
        from openapi_ts_client.generator import _get_non_hidden_files
        (tmp_path / ".gitkeep").touch()
        (tmp_path / "index.ts").touch()
        (tmp_path / "models").mkdir()
        result = _get_non_hidden_files(tmp_path)
        assert len(result) == 2
        names = [p.name for p in result]
        assert "index.ts" in names
        assert "models" in names

    def test_nonexistent_directory_returns_empty(self, tmp_path: Path):
        """Test that nonexistent directory returns empty list."""
        from openapi_ts_client.generator import _get_non_hidden_files
        nonexistent = tmp_path / "nonexistent"
        result = _get_non_hidden_files(nonexistent)
        assert result == []
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_generator.py::TestGetNonHiddenFiles -v`
Expected: FAIL with "cannot import name '_get_non_hidden_files'"

**Step 3: Implement _get_non_hidden_files**

Add to `src/openapi_ts_client/generator.py` (after imports, before generate_typescript_client):

```python
def _get_non_hidden_files(directory: Path) -> list:
    """Return list of non-hidden files/dirs in directory.

    Hidden files are those starting with a dot (e.g., .gitkeep, .gitignore).

    Args:
        directory: The directory to scan.

    Returns:
        List of Path objects for non-hidden files and directories.
    """
    if not directory.exists():
        return []
    return [p for p in directory.iterdir() if not p.name.startswith(".")]
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_generator.py::TestGetNonHiddenFiles -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generator.py tests/test_generator.py
git commit -m "feat: add _get_non_hidden_files helper function"
```

---

### Task 3: Add _clear_directory Helper

**Files:**
- Modify: `src/openapi_ts_client/generator.py`
- Test: `tests/test_generator.py`

**Step 1: Write the failing test**

Add to `tests/test_generator.py`:

```python
class TestClearDirectory:
    """Tests for _clear_directory helper."""

    def test_clears_all_files(self, tmp_path: Path):
        """Test that all files are cleared."""
        from openapi_ts_client.generator import _clear_directory
        (tmp_path / "file1.ts").touch()
        (tmp_path / "file2.ts").touch()
        _clear_directory(tmp_path)
        assert list(tmp_path.iterdir()) == []

    def test_clears_subdirectories(self, tmp_path: Path):
        """Test that subdirectories are cleared."""
        from openapi_ts_client.generator import _clear_directory
        subdir = tmp_path / "models"
        subdir.mkdir()
        (subdir / "User.ts").touch()
        _clear_directory(tmp_path)
        assert list(tmp_path.iterdir()) == []

    def test_preserves_directory_itself(self, tmp_path: Path):
        """Test that the directory itself is preserved."""
        from openapi_ts_client.generator import _clear_directory
        (tmp_path / "file.ts").touch()
        _clear_directory(tmp_path)
        assert tmp_path.exists()
        assert tmp_path.is_dir()

    def test_clears_dotfiles_too(self, tmp_path: Path):
        """Test that dotfiles are also cleared."""
        from openapi_ts_client.generator import _clear_directory
        (tmp_path / ".gitkeep").touch()
        (tmp_path / "index.ts").touch()
        _clear_directory(tmp_path)
        assert list(tmp_path.iterdir()) == []

    def test_empty_directory_no_error(self, tmp_path: Path):
        """Test that empty directory doesn't raise error."""
        from openapi_ts_client.generator import _clear_directory
        _clear_directory(tmp_path)
        assert tmp_path.exists()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_generator.py::TestClearDirectory -v`
Expected: FAIL with "cannot import name '_clear_directory'"

**Step 3: Implement _clear_directory**

Add to `src/openapi_ts_client/generator.py` (after _get_non_hidden_files):

```python
import shutil


def _clear_directory(directory: Path) -> None:
    """Remove all contents of directory (but not the directory itself).

    Removes both hidden and non-hidden files and subdirectories.

    Args:
        directory: The directory to clear.
    """
    if not directory.exists():
        return
    for item in directory.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_generator.py::TestClearDirectory -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generator.py tests/test_generator.py
git commit -m "feat: add _clear_directory helper function"
```

---

### Task 4: Add clean/force Parameters to generate_typescript_client

**Files:**
- Modify: `src/openapi_ts_client/generator.py`
- Test: `tests/test_generator.py`

**Step 1: Write the failing tests**

Add to `tests/test_generator.py`:

```python
class TestOutputDirectoryNotEmpty:
    """Tests for non-empty output directory handling."""

    def test_error_is_importable(self):
        """Test that OutputDirectoryNotEmptyError can be imported."""
        from openapi_ts_client import OutputDirectoryNotEmptyError
        assert issubclass(OutputDirectoryNotEmptyError, Exception)

    def test_nonempty_raises_error_by_default(self, tmp_path: Path):
        """Test that non-empty directory raises error without flags."""
        from openapi_ts_client import OutputDirectoryNotEmptyError
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test API", "version": "1.0.0"},
            "paths": {},
        }
        (tmp_path / "existing.ts").touch()
        with pytest.raises(OutputDirectoryNotEmptyError) as excinfo:
            generate_typescript_client(spec, output_path=tmp_path)
        assert "not empty" in str(excinfo.value)
        assert "1 files" in str(excinfo.value)

    def test_clean_true_clears_directory(self, tmp_path: Path):
        """Test that clean=True clears the directory."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test API", "version": "1.0.0"},
            "paths": {},
        }
        (tmp_path / "old_file.ts").touch()
        generate_typescript_client(spec, output_path=tmp_path, clean=True)
        assert not (tmp_path / "old_file.ts").exists()
        assert (tmp_path / "index.ts").exists()

    def test_force_true_continues_without_clearing(self, tmp_path: Path):
        """Test that force=True continues without clearing."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test API", "version": "1.0.0"},
            "paths": {},
        }
        (tmp_path / "keep_me.txt").touch()
        generate_typescript_client(spec, output_path=tmp_path, force=True)
        assert (tmp_path / "keep_me.txt").exists()
        assert (tmp_path / "index.ts").exists()

    def test_clean_and_force_raises_error(self, tmp_path: Path):
        """Test that both clean and force raises ValueError."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test API", "version": "1.0.0"},
            "paths": {},
        }
        with pytest.raises(ValueError) as excinfo:
            generate_typescript_client(spec, output_path=tmp_path, clean=True, force=True)
        assert "mutually exclusive" in str(excinfo.value).lower()

    def test_dotfiles_only_treated_as_empty(self, tmp_path: Path):
        """Test that directory with only dotfiles is treated as empty."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test API", "version": "1.0.0"},
            "paths": {},
        }
        (tmp_path / ".gitkeep").touch()
        (tmp_path / ".gitignore").touch()
        # Should not raise - dotfiles are ignored
        result = generate_typescript_client(spec, output_path=tmp_path)
        assert "Test API" in result

    def test_empty_directory_proceeds(self, tmp_path: Path):
        """Test that empty directory proceeds normally."""
        spec = {
            "openapi": "3.0.0",
            "info": {"title": "Test API", "version": "1.0.0"},
            "paths": {},
        }
        result = generate_typescript_client(spec, output_path=tmp_path)
        assert "Test API" in result
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_generator.py::TestOutputDirectoryNotEmpty::test_nonempty_raises_error_by_default -v`
Expected: FAIL (currently proceeds without error)

**Step 3: Update generate_typescript_client signature and add logic**

In `src/openapi_ts_client/generator.py`:

1. Add import at top:
```python
from .exceptions import OutputDirectoryNotEmptyError
```

2. Update function signature:
```python
def generate_typescript_client(
    openapi_spec: Union[Dict[str, Any], str],
    output_format: ClientFormat = ClientFormat.FETCH,
    output_path: Union[str, Path, None] = None,
    skip_validation: bool = False,
    clean: bool = False,
    force: bool = False,
) -> str:
```

3. Add validation after `output_path` default handling (after line ~76, before "Log input parameters"):
```python
    # Validate clean and force are not both set
    if clean and force:
        raise ValueError("clean and force are mutually exclusive - use one or the other")
```

4. Add directory check after `_resolve_output_path` call (after line ~120, replace the existing output path resolution section):
```python
    # Resolve and validate output path
    func_logger.info("Resolving output path")
    resolved_output_path = _resolve_output_path(output_path, func_logger)

    # Check for non-empty directory
    non_hidden = _get_non_hidden_files(resolved_output_path)
    if non_hidden:
        if clean:
            func_logger.info(f"Clearing output directory: {resolved_output_path}")
            _clear_directory(resolved_output_path)
        elif force:
            func_logger.warning(
                f"Output directory is not empty ({len(non_hidden)} files), "
                f"continuing due to force=True"
            )
        else:
            raise OutputDirectoryNotEmptyError(resolved_output_path, len(non_hidden))
```

**Step 4: Update docstring**

Update the docstring for generate_typescript_client to include new parameters:
```python
    """
    Generate a TypeScript client from an OpenAPI specification.

    ...existing docs...

        clean: If True, clear the output directory before generating.
            Cannot be used with force=True.
        force: If True, continue even if output directory is not empty.
            Files may be overwritten. Cannot be used with clean=True.

    Returns:
        ...

    Raises:
        ValueError: If the provided specification is not a valid OpenAPI spec,
            or if both clean and force are True.
        TypeError: If the openapi_spec parameter is neither a dict nor a string.
        OutputDirectoryNotEmptyError: If output directory is not empty and
            neither clean nor force is set.
    """
```

**Step 5: Run tests to verify they pass**

Run: `pytest tests/test_generator.py::TestOutputDirectoryNotEmpty -v`
Expected: PASS (all tests)

**Step 6: Run all generator tests**

Run: `pytest tests/test_generator.py -v`
Expected: Some existing tests may fail (they create non-empty dirs). Fix by adding `force=True` to existing tests or using empty temp directories.

**Step 7: Fix existing tests if needed**

Tests like `test_custom_output_path_string` may need `force=True` added since temp dirs can be reused. Review failures and update.

**Step 8: Commit**

```bash
git add src/openapi_ts_client/generator.py tests/test_generator.py
git commit -m "feat: add clean/force parameters to generate_typescript_client"
```

---

### Task 5: Add CLI --clean and --force Flags

**Files:**
- Modify: `src/openapi_ts_client/cli.py`
- Test: `tests/test_cli.py`

**Step 1: Write the failing tests**

Add to `tests/test_cli.py`:

```python
class TestCleanForceFlags:
    """Test --clean and --force CLI flags."""

    def test_clean_flag_clears_directory(self, tmp_path: Path):
        """Test that --clean clears the output directory."""
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        (output_dir / "old_file.ts").touch()

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "openapi_ts_client.cli",
                "tests/fixtures/petstore/openapi.json",
                "-o",
                str(output_dir),
                "--clean",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert not (output_dir / "old_file.ts").exists()
        assert (output_dir / "index.ts").exists()

    def test_force_flag_continues_without_clearing(self, tmp_path: Path):
        """Test that --force continues without clearing."""
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        (output_dir / "keep_me.txt").touch()

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "openapi_ts_client.cli",
                "tests/fixtures/petstore/openapi.json",
                "-o",
                str(output_dir),
                "--force",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"stderr: {result.stderr}"
        assert (output_dir / "keep_me.txt").exists()
        assert (output_dir / "index.ts").exists()

    def test_both_flags_error(self, tmp_path: Path):
        """Test that --clean and --force together gives error."""
        output_dir = tmp_path / "output"

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "openapi_ts_client.cli",
                "tests/fixtures/petstore/openapi.json",
                "-o",
                str(output_dir),
                "--clean",
                "--force",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0
        assert "mutually exclusive" in result.stderr.lower() or "error" in result.stderr.lower()

    def test_nonempty_without_flags_error(self, tmp_path: Path):
        """Test that non-empty directory without flags gives error."""
        output_dir = tmp_path / "output"
        output_dir.mkdir()
        (output_dir / "existing.ts").touch()

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
            # Ensure non-interactive (stdin is not a TTY in subprocess)
        )
        assert result.returncode != 0
        assert "not empty" in result.stderr.lower() or "error" in result.stderr.lower()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli.py::TestCleanForceFlags::test_clean_flag_clears_directory -v`
Expected: FAIL (--clean not recognized)

**Step 3: Add arguments to create_parser**

In `src/openapi_ts_client/cli.py`, add to `create_parser()` function:

```python
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clear output directory before generating",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Continue even if output directory is not empty (may overwrite files)",
    )
```

**Step 4: Pass flags to generate_typescript_client**

Update the `main()` function call (around line 257):
```python
            generate_typescript_client(
                spec, client_format, args.output,
                skip_validation=args.no_validate,
                clean=args.clean,
                force=args.force,
            )
```

Also update `generate_from_config()` (around line 214):
```python
        generate_typescript_client(
            spec, client_format, output_path,
            skip_validation=args.no_validate,
            clean=getattr(args, 'clean', False),
            force=getattr(args, 'force', False),
        )
```

**Step 5: Run tests to verify they pass**

Run: `pytest tests/test_cli.py::TestCleanForceFlags -v`
Expected: PASS

**Step 6: Commit**

```bash
git add src/openapi_ts_client/cli.py tests/test_cli.py
git commit -m "feat: add --clean and --force CLI flags"
```

---

### Task 6: Add Interactive TTY Prompt

**Files:**
- Modify: `src/openapi_ts_client/cli.py`
- Test: `tests/test_cli.py`

**Step 1: Write the failing test**

Add to `tests/test_cli.py`:

```python
class TestInteractivePrompt:
    """Test interactive TTY prompt."""

    def test_prompt_function_returns_clean(self, monkeypatch):
        """Test prompt_directory_action returns 'clean' for input '1'."""
        from openapi_ts_client import cli
        monkeypatch.setattr('builtins.input', lambda _: '1')
        result = cli.prompt_directory_action(Path('/tmp/test'), 5)
        assert result == 'clean'

    def test_prompt_function_returns_force(self, monkeypatch):
        """Test prompt_directory_action returns 'force' for input '2'."""
        from openapi_ts_client import cli
        monkeypatch.setattr('builtins.input', lambda _: '2')
        result = cli.prompt_directory_action(Path('/tmp/test'), 5)
        assert result == 'force'

    def test_prompt_function_returns_cancel(self, monkeypatch):
        """Test prompt_directory_action returns 'cancel' for input '3'."""
        from openapi_ts_client import cli
        monkeypatch.setattr('builtins.input', lambda _: '3')
        result = cli.prompt_directory_action(Path('/tmp/test'), 5)
        assert result == 'cancel'
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli.py::TestInteractivePrompt -v`
Expected: FAIL with "has no attribute 'prompt_directory_action'"

**Step 3: Add prompt_directory_action function**

Add to `src/openapi_ts_client/cli.py`:

```python
def prompt_directory_action(path: Path, file_count: int) -> str:
    """Prompt user for action on non-empty directory.

    Args:
        path: The output directory path.
        file_count: Number of non-hidden files in the directory.

    Returns:
        'clean' to clear directory, 'force' to continue, or 'cancel' to abort.
    """
    print(f"\nOutput directory '{path}' is not empty (contains {file_count} files).")
    print("\nHow would you like to proceed?")
    print("  [1] Clear directory and continue")
    print("  [2] Continue without clearing (may overwrite files)")
    print("  [3] Cancel")

    while True:
        choice = input("\nChoice [1/2/3]: ").strip()
        if choice == '1':
            return 'clean'
        elif choice == '2':
            return 'force'
        elif choice == '3':
            return 'cancel'
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
```

**Step 4: Run tests to verify they pass**

Run: `pytest tests/test_cli.py::TestInteractivePrompt -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/cli.py tests/test_cli.py
git commit -m "feat: add prompt_directory_action for interactive mode"
```

---

### Task 7: Integrate Interactive Prompt into CLI

**Files:**
- Modify: `src/openapi_ts_client/cli.py`
- Test: `tests/test_cli.py`

**Step 1: Write the failing test**

Add to `tests/test_cli.py`:

```python
class TestInteractivePrompt:
    # ...existing tests...

    def test_interactive_cancel_exits(self, tmp_path: Path, monkeypatch):
        """Test that cancel choice exits without generating."""
        from openapi_ts_client import cli

        output_dir = tmp_path / "output"
        output_dir.mkdir()
        (output_dir / "existing.ts").touch()

        # Mock isatty to return True
        monkeypatch.setattr('sys.stdin.isatty', lambda: True)
        # Mock prompt to return cancel
        monkeypatch.setattr(cli, 'prompt_directory_action', lambda p, c: 'cancel')

        spec_path = Path.cwd() / "tests/fixtures/petstore/openapi.json"
        result = cli.main([str(spec_path), "-o", str(output_dir)])

        assert result == 1  # Cancelled
        assert (output_dir / "existing.ts").exists()  # Not cleared
        assert not (output_dir / "index.ts").exists()  # Not generated

    def test_interactive_clean_clears_and_generates(self, tmp_path: Path, monkeypatch):
        """Test that clean choice clears directory and generates."""
        from openapi_ts_client import cli

        output_dir = tmp_path / "output"
        output_dir.mkdir()
        (output_dir / "existing.ts").touch()

        monkeypatch.setattr('sys.stdin.isatty', lambda: True)
        monkeypatch.setattr(cli, 'prompt_directory_action', lambda p, c: 'clean')

        spec_path = Path.cwd() / "tests/fixtures/petstore/openapi.json"
        result = cli.main([str(spec_path), "-o", str(output_dir)])

        assert result == 0
        assert not (output_dir / "existing.ts").exists()  # Cleared
        assert (output_dir / "index.ts").exists()  # Generated
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_cli.py::TestInteractivePrompt::test_interactive_cancel_exits -v`
Expected: FAIL (prompt not integrated)

**Step 3: Integrate prompt into main()**

In `src/openapi_ts_client/cli.py`, import at top:
```python
from .exceptions import OutputDirectoryNotEmptyError
from .generator import _get_non_hidden_files
```

Update the `main()` function to handle OutputDirectoryNotEmptyError with interactive prompt. After the `generate_typescript_client` call in the explicit input section, wrap it in a try/except:

```python
            # Generate client
            client_format = get_client_format(args.format)
            try:
                generate_typescript_client(
                    spec, client_format, args.output,
                    skip_validation=args.no_validate,
                    clean=args.clean,
                    force=args.force,
                )
            except OutputDirectoryNotEmptyError as e:
                if sys.stdin.isatty() and not args.quiet:
                    action = prompt_directory_action(e.path, e.file_count)
                    if action == 'cancel':
                        out.info("Cancelled.")
                        return 1
                    elif action == 'clean':
                        generate_typescript_client(
                            spec, client_format, args.output,
                            skip_validation=args.no_validate,
                            clean=True,
                        )
                    else:  # force
                        generate_typescript_client(
                            spec, client_format, args.output,
                            skip_validation=args.no_validate,
                            force=True,
                        )
                else:
                    out.error(str(e))
                    out.error("  Use --clean to clear the directory first, or --force to continue anyway.")
                    return 1
```

Do the same for the `generate_from_config()` function.

**Step 4: Run tests to verify they pass**

Run: `pytest tests/test_cli.py::TestInteractivePrompt -v`
Expected: PASS

**Step 5: Run all CLI tests**

Run: `pytest tests/test_cli.py -v`
Expected: Some existing tests may fail due to non-empty directory errors. Fix by adding `--force` flag or ensuring clean directories.

**Step 6: Fix existing CLI tests if needed**

Review and fix any failing tests.

**Step 7: Commit**

```bash
git add src/openapi_ts_client/cli.py tests/test_cli.py
git commit -m "feat: integrate interactive prompt for non-empty directories"
```

---

### Task 8: Final Integration Test and Cleanup

**Files:**
- Modify: `tests/test_cli.py`
- Modify: `tests/test_generator.py`

**Step 1: Run full test suite**

Run: `pytest -v`
Expected: All tests pass (except pre-existing logging failures)

**Step 2: Fix any remaining test failures**

Review failures, add `force=True` or `--force` where tests use pre-existing directories.

**Step 3: Run ruff for linting**

Run: `ruff check src --fix && ruff format src`
Expected: No errors

**Step 4: Final commit**

```bash
git add -A
git commit -m "test: ensure all tests pass with new directory handling"
```

---

### Task 9: Update __init__.py Exports

**Files:**
- Verify: `src/openapi_ts_client/__init__.py`

**Step 1: Verify exports are complete**

Ensure `OutputDirectoryNotEmptyError` is exported and `__all__` is updated.

**Step 2: Run import test**

```python
python -c "from openapi_ts_client import generate_typescript_client, ClientFormat, OutputDirectoryNotEmptyError; print('OK')"
```
Expected: "OK"

**Step 3: Commit if changes needed**

```bash
git add src/openapi_ts_client/__init__.py
git commit -m "chore: ensure all exports are complete"
```
