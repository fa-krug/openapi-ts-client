# CLI Design

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a command-line interface to openapi-ts-client, enabling use as both a library and a CLI tool.

**Tech Stack:** Python, argparse (stdlib only - no new dependencies)

---

## Command Interface

**Command name:** `openapi-ts-client`

**Basic usage:**
```bash
openapi-ts-client <input> [options]
```

**Input sources (positional argument):**
- File path: `openapi-ts-client ./openapi.json`
- URL: `openapi-ts-client https://api.example.com/openapi.json`
- Stdin: `cat openapi.json | openapi-ts-client -`

**Options:**
```
-f, --format FORMAT    Output format: fetch, axios, angular (default: fetch)
-o, --output DIR       Output directory (default: ./generated)
-c, --config FILE      Config file path (default: looks for openapi-ts-client.json)
    --no-validate      Skip OpenAPI spec validation
-q, --quiet            Suppress all output except errors
-v, --verbose          Show detailed progress
    --version          Show version and exit
    --help             Show help and exit
```

---

## Config File

**File name:** `openapi-ts-client.json`

**Discovery:** CLI looks for config in current directory. Override with `--config path/to/config.json`.

**Structure - multiple clients:**
```json
{
  "clients": [
    {
      "input": "./specs/users-api.json",
      "format": "fetch",
      "output": "./src/api/users"
    },
    {
      "input": "https://api.example.com/orders/openapi.json",
      "format": "axios",
      "output": "./src/api/orders"
    }
  ]
}
```

**Single client shorthand:**
```json
{
  "input": "./openapi.json",
  "format": "axios",
  "output": "./generated"
}
```

**Behavior:**
- Running `openapi-ts-client` with no arguments uses config file if present
- Running `openapi-ts-client <input>` ignores config file (explicit input wins)
- Command-line options override config values when both are present
- Progress shows each client being generated when using config

---

## Output and Progress

**Default output (no flags):**
```
Generating fetch client...
✓ Generated 12 models
✓ Generated 5 API classes
✓ Output: ./generated
```

**Quiet mode (`-q`):**
No output unless errors occur.

**Verbose mode (`-v`):**
```
Generating fetch client...
  Reading spec from ./openapi.json
  Validating OpenAPI 3.0.0 specification
  API: Petstore API v1.0.0
  Processing 12 schemas...
    → Pet
    → Order
    → User
    ...
  Processing 5 API tags...
    → PetApi (8 operations)
    → StoreApi (4 operations)
    → UserApi (6 operations)
  Writing output to ./generated
✓ Generated 12 models
✓ Generated 5 API classes
✓ Output: ./generated
```

**Multi-client config output:**
```
Generating 2 clients...

[1/2] users-api → ./src/api/users (fetch)
✓ Generated 8 models, 3 API classes

[2/2] orders-api → ./src/api/orders (axios)
✓ Generated 5 models, 2 API classes

Done.
```

---

## Error Handling

**Exit codes:**
- `0` - Success
- `1` - General error (invalid spec, generation failure)
- `2` - Invalid arguments or config

**Error examples:**
```
Error: File not found: ./missing.json
```
```
Error: Failed to fetch URL: https://example.com/spec.json
  Connection timeout
```
```
Error: No input provided and no config file found
  Usage: openapi-ts-client <input> [options]
```
```
Error: Invalid OpenAPI specification
  Missing required 'info.title' field
```
```
Error: Invalid config file: openapi-ts-client.json
  'clients' must be an array
```

---

## Implementation

**New file:** `src/openapi_ts_client/cli.py`

Contains:
- Argument parsing with argparse
- Config file loading and validation
- Input resolution (file/URL/stdin)
- Progress output handling
- Error formatting

**Entry point in `pyproject.toml`:**
```toml
[project.scripts]
openapi-ts-client = "openapi_ts_client.cli:main"
```

**Dependencies:** None added. Uses stdlib only:
- `argparse` - argument parsing
- `urllib.request` - URL fetching
- `json` - config/spec parsing
- `sys.stdin` - stdin reading

**Module structure:**
```
src/openapi_ts_client/
├── cli.py              # NEW: CLI entry point
├── __init__.py         # unchanged (library API)
├── generator.py        # unchanged
└── ...
```

---

## Testing

**Unit tests** (`tests/test_cli.py`):
- Argument parsing (all flags and combinations)
- Config file parsing and validation
- Input resolution (file path, URL detection, stdin detection)
- Error message formatting

**Integration tests** (`tests/test_cli_integration.py`):
- End-to-end: file input → generated output
- End-to-end: config file with multiple clients
- URL fetching (mocked)
- Stdin input
- Error scenarios (missing file, invalid spec, bad config)

**Manual test cases:**
```bash
# Basic usage
openapi-ts-client tests/fixtures/petstore/openapi.json

# With options
openapi-ts-client tests/fixtures/petstore/openapi.json -f axios -o ./tmp

# Config file
echo '{"clients":[{"input":"./tests/fixtures/petstore/openapi.json"}]}' > openapi-ts-client.json
openapi-ts-client

# Stdin
cat tests/fixtures/petstore/openapi.json | openapi-ts-client -

# Verbose
openapi-ts-client tests/fixtures/petstore/openapi.json -v
```

---

## Implementation Tasks

### Task 1: Create CLI module with argument parsing
- Create `src/openapi_ts_client/cli.py`
- Implement `main()` function with argparse
- Add entry point to `pyproject.toml`
- Test: `openapi-ts-client --help` and `openapi-ts-client --version`

### Task 2: Implement file input
- Read spec from file path
- Handle file not found errors
- Test with petstore fixture

### Task 3: Implement URL input
- Detect URL vs file path
- Fetch spec from URL using urllib
- Handle network errors

### Task 4: Implement stdin input
- Detect `-` as stdin marker
- Read spec from stdin
- Handle empty stdin

### Task 5: Implement config file support
- Load `openapi-ts-client.json` from current directory
- Support `--config` flag for custom path
- Parse single client and multi-client formats
- Validate config structure

### Task 6: Implement output formatting
- Default progress output
- Quiet mode (`-q`)
- Verbose mode (`-v`)
- Multi-client progress

### Task 7: Implement --no-validate flag
- Pass validation skip flag to generator
- Update generator to accept skip flag

### Task 8: Add unit tests
- Create `tests/test_cli.py`
- Test argument parsing
- Test config parsing
- Test input detection

### Task 9: Add integration tests
- Create `tests/test_cli_integration.py`
- Test end-to-end generation
- Test error scenarios
