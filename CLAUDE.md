# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`openapi-ts-client` is a Python package that generates TypeScript API clients from OpenAPI 3.x specifications. It uses Jinja2 templates and supports three output formats: Fetch, Axios, and Angular.

## Build and Development Commands

```bash
# Install in development mode (with dev dependencies)
pip install -e ".[dev]"

# Run tests
pytest

# Run a specific test file
pytest tests/test_generator.py -v

# Lint and format
ruff check src --fix
ruff format src

# Setup pre-commit hooks
pre-commit install

# Quick test of the generator
python -c "from openapi_ts_client import generate_typescript_client, ClientFormat; print(generate_typescript_client({'openapi': '3.0.0', 'info': {'title': 'Test', 'version': '1.0'}, 'paths': {}}))"
```

## Architecture

Uses src-layout packaging (`src/openapi_ts_client/`).

### Core Components

```
src/openapi_ts_client/
├── __init__.py              # Package exports: generate_typescript_client, ClientFormat
├── generator.py             # Main entry point, validates specs, dispatches to format generators
├── enums.py                 # ClientFormat enum (FETCH, AXIOS, ANGULAR)
├── logging_config.py        # Verbose logging setup
├── generators/
│   ├── fetch/               # Fetch API client generator
│   │   ├── generator.py     # generate_fetch_client()
│   │   ├── apis.py          # API class generation
│   │   ├── models.py        # Model/interface generation
│   │   ├── runtime.py       # Runtime utilities generation
│   │   └── docs.py          # Documentation generation
│   ├── axios/               # Axios client generator
│   │   ├── generator.py     # generate_axios_client()
│   │   ├── api.py           # API class generation
│   │   ├── base.py          # Base class generation
│   │   ├── common.py        # Common utilities
│   │   ├── configuration.py # Configuration class
│   │   └── docs.py          # Documentation generation
│   ├── angular/             # Angular client generator
│   │   ├── generator.py     # generate_angular_client()
│   │   ├── services.py      # Angular service generation
│   │   ├── models.py        # Model generation
│   │   ├── infrastructure.py# Module/config generation
│   │   ├── type_mapper.py   # OpenAPI to TypeScript type mapping
│   │   └── anyof_extractor.py # anyOf/oneOf handling
│   └── shared/              # Shared utilities across generators
│       ├── type_mapper.py   # Common type mapping logic
│       └── anyof_extractor.py # Shared anyOf extraction
├── templates/               # Jinja2 templates (if used)
└── utils/
    ├── naming.py            # Naming conventions (camelCase, PascalCase)
    └── openapi.py           # OpenAPI spec utilities
```

### Data Flow

1. `generate_typescript_client()` receives spec (dict or JSON string)
2. Validates spec structure (version, info, paths)
3. Dispatches to format-specific generator based on `ClientFormat`
4. Format generator creates output directory structure
5. Generates TypeScript files (APIs, models, runtime/config)

### Generated Output Structures

**Fetch:**
```
output/
├── index.ts, runtime.ts
├── apis/     # PetApi.ts, StoreApi.ts, etc.
└── models/   # Pet.ts, Order.ts, etc.
```

**Axios:**
```
output/
├── index.ts, api.ts, base.ts, common.ts, configuration.ts
```

**Angular:**
```
output/
├── index.ts, api.module.ts, api.base.service.ts, configuration.ts
├── api/      # pet.service.ts, store.service.ts, etc.
└── model/    # pet.ts, order.ts, etc.
```

## Testing

Tests are in `tests/` and compare generated output against fixtures.

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_fetch_generator.py -v
```

### Test Fixtures

Located in `tests/fixtures/`. Contains reference OpenAPI specs and expected outputs:

```
tests/fixtures/
├── petstore/
│   ├── openapi.json    # Petstore OpenAPI spec
│   ├── fetch/          # Expected Fetch output
│   ├── axios/          # Expected Axios output
│   └── angular/        # Expected Angular output
└── space_zoo/
    ├── openapi.json    # Space Zoo OpenAPI spec (larger/complex)
    ├── fetch/
    ├── axios/
    └── angular/
```

## Critical Rules

### Fixture Files Are Sacred

**NEVER modify files in `tests/fixtures/`** - These are the ultimate reference for expected output. Tests compare generated code against these fixtures. If tests fail, fix the generator, not the fixtures.

### Use Temp Directories

**ALWAYS generate to a temp folder** when testing manually:
```python
import tempfile
with tempfile.TemporaryDirectory() as tmpdir:
    generate_typescript_client(spec, output_path=tmpdir)
```

NEVER generate output to the project root directory.

### Key Design Decisions

- Accepts OpenAPI 3.x specifications (`openapi` field)
- Input can be dict or JSON string
- Verbose logging is intentional - helps debug generation issues
- Each format generator is self-contained with its own templates/logic
- Type mapping handles OpenAPI types → TypeScript types
- anyOf/oneOf extraction creates union types

## Dependencies

**Runtime:**
- `jinja2>=3.1.0` - Template engine
- `openapi-core>=0.19.0` - OpenAPI validation

**Dev:**
- `ruff` - Linting and formatting
- `pytest` - Testing
- `pre-commit` - Git hooks
- `tree-sitter`, `tree-sitter-typescript` - TypeScript parsing for tests

## Common Tasks

### Adding Support for New OpenAPI Feature

1. Update type mapper in relevant generator(s)
2. Update model/API generation logic
3. Add test case with fixture
4. Run tests to verify

### Debugging Generation Issues

Enable verbose logging (already on by default). Check:
- Spec validation in `generator.py`
- Type mapping in `generators/*/type_mapper.py`
- Template rendering in format-specific generators

### Regenerating Fixtures

If intentionally changing output format:
1. Generate to temp directory
2. Verify output is correct
3. Copy to fixture directory
4. Run tests to confirm
