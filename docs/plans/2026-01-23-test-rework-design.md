# Test Rework: Structural Equivalence + TypeScript Validity

## Overview

Replace byte-for-byte fixture comparison with two-layer testing:

1. **Structural equivalence** - Verify generated code has the same functional structure as fixtures (interfaces, functions, enums, etc.) using tree-sitter
2. **Validity verification** - Prove generated code compiles and runs (tsc + tsx runtime tests)

### Goals

- Less strict: Don't care about whitespace, newlines, ordering, formatting
- More strict: Verify generated TypeScript actually compiles and works at runtime

## Test Structure

```
tests/
├── conftest.py                      # Shared fixtures: ts_parser, generated_client
├── ts_structure.py                  # Tree-sitter extraction logic
├── test_structural_equivalence.py   # Compare generated vs fixture structure
├── test_typescript_validity.py      # tsc compilation + tsx runtime tests
├── fixtures/                        # Keep existing fixtures (unchanged)
└── (other existing tests unchanged)
```

### Files to Delete

- `tests/test_fixture_comparison.py` - Replaced by new tests

## Structural Equivalence Testing

### What We Extract and Compare

| Element | What we capture |
|---------|-----------------|
| Interfaces | Name, property names, property types, optionality |
| Type aliases | Name, definition |
| Functions | Name, parameter names/types, return type |
| Enums/const objects | Name, member names, member values |
| Classes | Name, property names/types, method signatures |
| Exports | What's exported (names only) |

### What We Ignore

- Whitespace, newlines, indentation
- Order of declarations within a file
- Order of properties within an interface
- Order of imports
- Comment content (JSDoc descriptions)
- Blank lines in function bodies

### Extraction Logic

```python
def extract_ts_structure(directory: Path, parser: Parser) -> dict:
    """Extract functional structure from all .ts files in directory.

    Returns:
        {
            "models/Pet.ts": {
                "interfaces": [
                    {"name": "Pet", "properties": [
                        {"name": "id", "type": "number", "optional": True},
                        {"name": "name", "type": "string", "optional": False},
                    ]}
                ],
                "functions": [
                    {"name": "PetFromJSON", "params": [{"name": "json", "type": "any"}], "return_type": "Pet"}
                ],
                "enums": [
                    {"name": "PetStatusEnum", "members": [
                        {"name": "Available", "value": "'available'"},
                    ]}
                ],
                "exports": ["Pet", "PetFromJSON", "PetToJSON", "PetStatusEnum"]
            }
        }
    """
```

### Comparison Logic

```python
def test_structural_equivalence(fixture_name, client_format, tmp_path, ts_parser):
    # Generate client to temp dir
    spec = load_spec(fixture_name)
    generate_typescript_client(spec, client_format, tmp_path)

    # Extract structure from both
    fixture_dir = FIXTURES_DIR / fixture_name / client_format.value
    expected_structure = extract_ts_structure(fixture_dir, ts_parser)
    actual_structure = extract_ts_structure(tmp_path, ts_parser)

    # Compare (order-independent - all lists sorted by name)
    assert actual_structure == expected_structure
```

## TypeScript Validity Testing

### Phase 1: Compilation (tsc)

- Run `tsc --noEmit` on generated code
- Proves all types resolve, imports work, no syntax errors
- Uses a minimal `tsconfig.json` we generate

```python
def test_typescript_compiles(generated_path: Path):
    # Write minimal tsconfig.json
    tsconfig = {
        "compilerOptions": {
            "target": "ES2020",
            "module": "ESNext",
            "moduleResolution": "node",
            "strict": True,
            "noEmit": True,
            "skipLibCheck": True
        },
        "include": ["**/*.ts"]
    }
    (generated_path / "tsconfig.json").write_text(json.dumps(tsconfig))

    # Run tsc
    result = subprocess.run(
        ["tsc", "--project", str(generated_path)],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"TypeScript compilation failed:\n{result.stderr}"
```

### Phase 2: Runtime (tsx)

Auto-generate a test file that exercises the generated code:

```typescript
// Auto-generated test file

// 1. Import all models
import { Pet, Category, Tag, PetStatusEnum } from './models';

// 2. Instantiate each interface (with required fields)
const pet: Pet = { name: 'Fido', photoUrls: [] };

// 3. Call conversion functions
import { PetFromJSON, PetToJSON } from './models';
const json = PetToJSON(pet);
const roundtrip = PetFromJSON(json);

// 4. Verify enum values exist
console.assert(PetStatusEnum.Available === 'available');

// 5. Instantiate API classes (without calling endpoints)
import { PetApi, Configuration } from './apis';
const config = new Configuration({ basePath: 'http://localhost' });
const api = new PetApi(config);

console.log('Runtime validation passed');
```

```python
def test_typescript_runtime(generated_path: Path, extracted_structure: dict):
    # Generate test file based on extracted structure
    test_code = generate_runtime_test(extracted_structure)
    test_file = generated_path / "runtime_test.ts"
    test_file.write_text(test_code)

    # Run with tsx
    result = subprocess.run(
        ["tsx", str(test_file)],
        capture_output=True, text=True,
        cwd=generated_path
    )
    assert result.returncode == 0, f"Runtime test failed:\n{result.stderr}"
```

## Dependencies

### Python (add to pyproject.toml)

```toml
[project.optional-dependencies]
dev = [
    # ... existing deps ...
    "tree-sitter>=0.21",
    "tree-sitter-typescript>=0.21",
]
```

### Node.js (required, tests fail if missing)

- `tsc` - TypeScript compiler
- `tsx` - TypeScript execute

```python
# conftest.py
def pytest_configure(config):
    """Verify required tools are available."""
    import shutil

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
```

## Test Configuration

```python
# conftest.py

@pytest.fixture(scope="session")
def ts_parser():
    """Shared tree-sitter TypeScript parser."""
    import tree_sitter_typescript as ts_typescript
    from tree_sitter import Language, Parser

    parser = Parser()
    parser.language = Language(ts_typescript.language_typescript())
    return parser

@pytest.fixture
def generated_fetch_client(request, tmp_path):
    """Generate Fetch client and return path."""
    fixture_name = request.param
    spec = load_spec(fixture_name)
    generate_typescript_client(spec, ClientFormat.FETCH, tmp_path)
    return tmp_path

@pytest.fixture
def generated_angular_client(request, tmp_path):
    """Generate Angular client and return path."""
    fixture_name = request.param
    spec = load_spec(fixture_name)
    generate_typescript_client(spec, ClientFormat.ANGULAR, tmp_path)
    return tmp_path
```

## File Summary

### Create

| File | Lines (est.) | Purpose |
|------|--------------|---------|
| `tests/ts_structure.py` | ~200 | Tree-sitter extraction logic |
| `tests/test_structural_equivalence.py` | ~100 | Structure comparison tests |
| `tests/test_typescript_validity.py` | ~150 | Compilation + runtime tests |

### Modify

| File | Change |
|------|--------|
| `tests/conftest.py` | Add ts_parser fixture, tool verification |
| `pyproject.toml` | Add tree-sitter dependencies |

### Delete

| File | Reason |
|------|--------|
| `tests/test_fixture_comparison.py` | Replaced by new tests |

### Unchanged

- `tests/fixtures/**` - Keep as source of truth
- All other existing tests
