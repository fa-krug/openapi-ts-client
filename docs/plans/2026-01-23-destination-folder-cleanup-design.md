# Destination Folder Cleanup Behavior

## Overview

Add safeguards and options for handling non-empty destination folders during client generation.

## Current Behavior

The generator currently creates/overwrites the output directory without checking if it exists or contains files, which can lead to unexpected file mixing or loss.

## New Behavior

### When destination folder is empty or doesn't exist

Proceed normally (create if needed).

### When destination folder is non-empty (has non-hidden files)

| Context | `--clean` | `--force` | Behavior |
|---------|-----------|-----------|----------|
| CLI (interactive TTY) | no | no | Prompt: Clear / Cancel / Continue without clearing |
| CLI (non-interactive) | no | no | Error with message |
| CLI | yes | - | Clear folder, then generate |
| CLI | - | yes | Continue without clearing (overwrite) |
| Function API | `clean=False` | `force=False` | Raise error |
| Function API | `clean=True` | - | Clear folder, then generate |
| Function API | - | `force=True` | Continue without clearing |

Hidden files (dotfiles like `.gitkeep`, `.gitignore`) are ignored when checking if folder is non-empty.

## Function API Changes

### Signature

```python
def generate_typescript_client(
    openapi_spec: Union[Dict[str, Any], str],
    output_format: ClientFormat = ClientFormat.FETCH,
    output_path: Union[str, Path, None] = None,
    skip_validation: bool = False,
    clean: bool = False,      # NEW: Clear folder before generating
    force: bool = False,      # NEW: Continue even if folder is non-empty
) -> str:
```

### New Error Type

```python
class OutputDirectoryNotEmptyError(Exception):
    """Raised when output directory is not empty and neither clean nor force is set."""
    pass
```

### Behavior Logic

1. If `clean=True` and `force=True`: raise `ValueError` (mutually exclusive)
2. Check if folder exists and has non-hidden files
3. If non-empty:
   - `clean=True` → delete all contents, proceed
   - `force=True` → proceed (files may be overwritten)
   - Both `False` → raise `OutputDirectoryNotEmptyError`

## CLI Changes

### New Arguments

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

### Interactive Prompt

When TTY detected, folder non-empty, no flags:

```
Output directory './generated' is not empty (contains 12 files).

How would you like to proceed?
  [1] Clear directory and continue
  [2] Continue without clearing (may overwrite files)
  [3] Cancel

Choice [1/2/3]:
```

### Non-Interactive Error Message

```
Error: Output directory './generated' is not empty (contains 12 files).
  Use --clean to clear the directory first, or --force to continue anyway.
```

### TTY Detection

Use `sys.stdin.isatty()` to determine if we can prompt interactively.

## Implementation Details

### New Helper Functions (generator.py)

```python
def _get_non_hidden_files(directory: Path) -> list[Path]:
    """Return list of non-hidden files/dirs in directory."""

def _clear_directory(directory: Path, logger) -> None:
    """Remove all contents of directory (but not the directory itself)."""

def _check_output_directory(
    path: Path,
    clean: bool,
    force: bool,
    logger
) -> None:
    """Check output directory and handle non-empty case."""
```

### CLI Helper (cli.py)

```python
def prompt_directory_action(path: Path, file_count: int) -> str:
    """Prompt user for action on non-empty directory.

    Returns: 'clean', 'force', or 'cancel'
    """
```

### Files to Modify

- `src/openapi_ts_client/generator.py` - add parameters, helpers, error class
- `src/openapi_ts_client/cli.py` - add flags, interactive prompt, error handling
- `src/openapi_ts_client/__init__.py` - export `OutputDirectoryNotEmptyError`

## Testing Strategy

### Unit Tests (test_generator.py)

- Empty folder → proceeds normally
- Non-empty folder, no flags → raises `OutputDirectoryNotEmptyError`
- Non-empty folder, `clean=True` → clears and proceeds
- Non-empty folder, `force=True` → proceeds without clearing
- Both `clean=True` and `force=True` → raises `ValueError`
- Folder with only dotfiles → treated as empty

### CLI Tests (test_cli.py)

- `--clean` flag clears directory
- `--force` flag continues without clearing
- Both flags together → error
- Non-interactive mode without flags → exit code + error message
