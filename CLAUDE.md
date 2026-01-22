# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Development Commands

```bash
# Install in development mode (with dev dependencies)
pip install -e ".[dev]"

# Lint and format
ruff check src --fix
ruff format src

# Setup pre-commit hooks
pre-commit install

# Run the package (example usage)
python -c "from openapi_ts_client import generate_typescript_client, ClientFormat; print(generate_typescript_client({'openapi': '3.0.0', 'info': {'title': 'Test', 'version': '1.0'}, 'paths': {}}))"
```

## Architecture

This is a Python package (`openapi-ts-client`) that generates TypeScript clients from OpenAPI specifications. Uses src-layout packaging.

### Core Components

- **`src/openapi_ts_client/generator.py`**: Main entry point. Contains `generate_typescript_client()` which validates specs and coordinates generation. Generation logic is intentionally NOT implemented (placeholder only).

- **`src/openapi_ts_client/enums.py`**: `ClientFormat` enum with FETCH (default), REACT, and ANGULAR options.

- **`src/openapi_ts_client/logging_config.py`**: Verbose logging setup. All operations log with timestamps, module/function/line info.

### Key Design Decisions

- Accepts both OpenAPI 2.0 (`swagger` field) and 3.x (`openapi` field) specifications
- Input can be dict or JSON string
- Very verbose logging is intentional - logs every validation step, path resolution, and spec detail
- The actual TypeScript generation is a placeholder - only validation and logging are implemented

## Critical Rules

- **NEVER modify files in `tests/fixtures/`** - These are the ultimate reference for expected output. Tests compare generated code against these fixtures. If tests fail, fix the generator, not the fixtures.

- **ALWAYS generate to a temp folder** - When testing generator output manually, ALWAYS use a temporary directory (e.g., `/tmp/test_output` or Python's `tempfile`). NEVER generate output to the project root directory, as this will pollute the working directory with generated files.
