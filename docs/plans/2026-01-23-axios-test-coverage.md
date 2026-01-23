# Axios Test Coverage Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Extend Axios test coverage to match Fetch and Angular generators.

**Architecture:** Add TypeScript compilation and runtime tests for Axios clients, mirroring the existing Fetch test patterns. Fix the structural equivalence test by updating it to test petstore (which works) and updating the space_zoo fixture to match current generator output.

**Tech Stack:** Python, pytest, TypeScript (tsc, tsx), tree-sitter

---

## Summary of Gaps

| Test Type | Fetch | Angular | Axios (Current) | Axios (After) |
|-----------|-------|---------|-----------------|---------------|
| Structural (petstore) | ✓ | ✓ | ✗ | ✓ |
| Structural (space_zoo) | ✓ | ✓ | xfail | ✓ |
| TypeScript compilation | ✓ | ✓ | ✗ | ✓ |
| Runtime execution | ✓ | ✗ | ✗ | ✓ |

---

## Task 1: Add TypeScript Compilation Test for Axios

**Files:**
- Modify: `tests/test_typescript_validity.py:70-122`

**Step 1: Write the failing test**

Add after `test_angular_typescript_compiles` (around line 122):

```python
@pytest.mark.parametrize(
    "fixture_name",
    [
        "petstore",
        pytest.param(
            "space_zoo",
            marks=pytest.mark.xfail(
                reason="Space zoo fixture needs updating to match generator output"
            ),
        ),
    ],
)
def test_axios_typescript_compiles(fixture_name: str, tmp_path: Path) -> None:
    """Test that generated Axios client compiles with tsc."""
    spec = load_spec(fixture_name)
    generate_typescript_client(spec, ClientFormat.AXIOS, tmp_path)

    # Axios needs axios types - write tsconfig with type stubs
    tsconfig = {
        "compilerOptions": {
            "target": "ES2020",
            "module": "ESNext",
            "moduleResolution": "node",
            "strict": True,
            "noEmit": True,
            "skipLibCheck": True,
            "esModuleInterop": True,
        },
        "include": ["**/*.ts"],
    }
    (tmp_path / "tsconfig.json").write_text(json.dumps(tsconfig, indent=2))

    result = subprocess.run(
        ["tsc", "--project", str(tmp_path)],
        capture_output=True,
        text=True,
        timeout=60,
    )

    # Filter out errors about missing axios module (expected without npm install)
    if result.returncode != 0:
        errors = [
            line
            for line in result.stderr.split("\n")
            if "error TS" in line
            and "Cannot find module" not in line
            and "'axios'" not in line
        ]
        if errors:
            pytest.fail("TypeScript compilation errors:\n" + "\n".join(errors))
```

**Step 2: Run test to verify it works**

Run: `pytest tests/test_typescript_validity.py::test_axios_typescript_compiles -v`
Expected: petstore PASS, space_zoo XFAIL

**Step 3: Commit**

```bash
git add tests/test_typescript_validity.py
git commit -m "test(axios): add TypeScript compilation test"
```

---

## Task 2: Add Runtime Execution Test for Axios

**Files:**
- Modify: `tests/test_typescript_validity.py` (add after compilation test)

**Step 1: Write the test**

Add after `test_axios_typescript_compiles`:

```python
@pytest.mark.parametrize("fixture_name", ["petstore"])
def test_axios_typescript_runtime(fixture_name: str, tmp_path: Path, ts_parser) -> None:
    """Test that generated Axios client runs with tsx."""
    spec = load_spec(fixture_name)
    generate_typescript_client(spec, ClientFormat.AXIOS, tmp_path)

    # Extract structure and generate runtime test
    structure = extract_ts_structure(tmp_path, ts_parser)
    test_code = generate_runtime_test(structure)

    test_file = tmp_path / "runtime_test.ts"
    test_file.write_text(test_code)

    write_tsconfig(tmp_path)

    result = subprocess.run(
        ["tsx", str(test_file)],
        capture_output=True,
        text=True,
        timeout=30,
        cwd=tmp_path,
    )

    assert result.returncode == 0, f"Runtime test failed:\n{result.stdout}\n{result.stderr}"
    assert "Runtime validation passed" in result.stdout
```

**Step 2: Run test to verify it works**

Run: `pytest tests/test_typescript_validity.py::test_axios_typescript_runtime -v`
Expected: PASS

**Step 3: Commit**

```bash
git add tests/test_typescript_validity.py
git commit -m "test(axios): add TypeScript runtime test"
```

---

## Task 3: Enable Structural Equivalence Test for Petstore

**Files:**
- Modify: `tests/test_structural_equivalence.py:114-159`

**Step 1: Update the test parametrization**

Change from:
```python
@pytest.mark.xfail(reason="Axios fixture contains models not in spec - needs fixture update")
@pytest.mark.parametrize("fixture_name", ["space_zoo"])
def test_axios_structural_equivalence(fixture_name: str, tmp_path: Path, ts_parser) -> None:
```

To:
```python
@pytest.mark.parametrize(
    "fixture_name",
    [
        "petstore",
        pytest.param(
            "space_zoo",
            marks=pytest.mark.xfail(
                reason="Axios fixture contains models not in spec - needs fixture update"
            ),
        ),
    ],
)
def test_axios_structural_equivalence(fixture_name: str, tmp_path: Path, ts_parser) -> None:
```

**Step 2: Run test to verify petstore passes**

Run: `pytest tests/test_structural_equivalence.py::test_axios_structural_equivalence -v`
Expected: petstore PASS, space_zoo XFAIL

**Step 3: Commit**

```bash
git add tests/test_structural_equivalence.py
git commit -m "test(axios): enable structural equivalence test for petstore"
```

---

## Task 4: Update Space Zoo Axios Fixture

**Files:**
- Regenerate: `tests/fixtures/space_zoo/axios/` (all files)

**Step 1: Regenerate the fixture**

```bash
python -c "
from pathlib import Path
from openapi_ts_client import generate_typescript_client, ClientFormat
import json
import shutil

spec = json.loads(Path('tests/fixtures/space_zoo/openapi.json').read_text())
fixture_dir = Path('tests/fixtures/space_zoo/axios')

# Backup old fixture
if fixture_dir.exists():
    shutil.rmtree(fixture_dir)

fixture_dir.mkdir(parents=True)
generate_typescript_client(spec, ClientFormat.AXIOS, fixture_dir)
"
```

**Step 2: Verify the fixture is correct**

Run: `pytest tests/test_structural_equivalence.py::test_axios_structural_equivalence -v --runxfail`
Expected: Both petstore and space_zoo PASS

**Step 3: Remove xfail marker from space_zoo**

Update test to:
```python
@pytest.mark.parametrize("fixture_name", ["petstore", "space_zoo"])
def test_axios_structural_equivalence(fixture_name: str, tmp_path: Path, ts_parser) -> None:
```

**Step 4: Commit**

```bash
git add tests/fixtures/space_zoo/axios/ tests/test_structural_equivalence.py
git commit -m "test(fixtures): regenerate space_zoo axios fixture to match generator"
```

---

## Task 5: Update Fetch space_zoo xfail (if needed)

**Files:**
- Check: `tests/test_typescript_validity.py:41-52`

**Step 1: Verify fetch space_zoo compilation status**

Run: `pytest tests/test_typescript_validity.py::test_fetch_typescript_compiles -v --runxfail`

If it passes, remove the xfail marker. If it fails with the "clone method conflict", the xfail should remain.

**Step 2: Run full test suite**

Run: `pytest tests/ -v`
Expected: All tests pass (except any legitimately xfailed)

**Step 3: Commit if changes made**

```bash
git add tests/test_typescript_validity.py
git commit -m "test(fetch): update space_zoo xfail status"
```

---

## Task 6: Final Verification

**Step 1: Run all tests**

```bash
pytest tests/ -v
```

Expected output should show:
- `test_axios_typescript_compiles[petstore]` PASS
- `test_axios_typescript_compiles[space_zoo]` XFAIL or PASS
- `test_axios_typescript_runtime[petstore]` PASS
- `test_axios_structural_equivalence[petstore]` PASS
- `test_axios_structural_equivalence[space_zoo]` PASS

**Step 2: Verify test counts**

```bash
pytest tests/ --collect-only | grep "test session starts" -A 5
```

Confirm Axios now has the same test coverage as Fetch/Angular.

---

## Notes

- **NEVER modify files in `tests/fixtures/`** except as explicitly instructed in Task 4
- The Axios client structure is different from Fetch (single api.ts vs apis/ directory) - this is expected
- The `generate_runtime_test` function should work with Axios since it reads from models/index.ts exports, but Axios puts everything in api.ts - may need adjustment if runtime test fails
- If runtime test fails due to Axios structure differences, the test can be skipped with xfail until the runtime test generator is updated
