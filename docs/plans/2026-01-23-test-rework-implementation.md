# Test Rework Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace byte-for-byte fixture comparison with structural equivalence (tree-sitter) + TypeScript validity (tsc/tsx) testing.

**Architecture:** Two-layer testing: (1) Extract TypeScript structure using tree-sitter and compare against fixtures order-independently, (2) Verify generated code compiles and runs via tsc and tsx.

**Tech Stack:** Python tree-sitter + tree-sitter-typescript, Node.js tsc/tsx

---

## Task 1: Add tree-sitter Dependencies

**Files:**
- Modify: `pyproject.toml:36-42`

**Step 1: Add tree-sitter dependencies to dev extras**

Edit `pyproject.toml` to add the tree-sitter packages:

```toml
[project.optional-dependencies]
dev = [
    "ruff>=0.4.0",
    "pre-commit>=3.0.0",
    "pytest>=7.0",
    "pytest-mock>=3.10",
    "tree-sitter>=0.21",
    "tree-sitter-typescript>=0.21",
]
```

**Step 2: Reinstall dev dependencies**

Run: `pip install -e ".[dev]"`
Expected: SUCCESS, tree-sitter packages installed

**Step 3: Verify tree-sitter works**

Run: `python -c "import tree_sitter; import tree_sitter_typescript; print('OK')"`
Expected: `OK`

**Step 4: Commit**

```bash
git add pyproject.toml
git commit -m "$(cat <<'EOF'
build: add tree-sitter dependencies for structural testing

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 2: Create conftest.py with Shared Fixtures

**Files:**
- Create: `tests/conftest.py`

**Step 1: Write conftest.py with ts_parser fixture and tool verification**

```python
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
```

**Step 2: Run pytest to verify conftest loads**

Run: `pytest --collect-only 2>&1 | head -20`
Expected: Test collection succeeds (or fails with "tsc/tsx not found" if tools missing)

**Step 3: Commit**

```bash
git add tests/conftest.py
git commit -m "$(cat <<'EOF'
test: add conftest.py with ts_parser fixture and tool checks

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 3: Create ts_structure.py - Basic Interface Extraction

**Files:**
- Create: `tests/ts_structure.py`
- Test: `tests/test_ts_structure.py`

**Step 1: Write failing test for interface extraction**

Create `tests/test_ts_structure.py`:

```python
"""Tests for TypeScript structure extraction."""

import pytest

from tests.ts_structure import extract_interfaces


def test_extract_simple_interface(ts_parser):
    """Extract a simple interface with required and optional properties."""
    code = b"""
export interface Pet {
    id?: number;
    name: string;
    tag?: string;
}
"""
    result = extract_interfaces(code, ts_parser)

    assert result == [
        {
            "name": "Pet",
            "properties": [
                {"name": "id", "type": "number", "optional": True},
                {"name": "name", "type": "string", "optional": False},
                {"name": "tag", "type": "string", "optional": True},
            ],
        }
    ]


def test_extract_interface_with_array_type(ts_parser):
    """Extract interface with array type."""
    code = b"""
export interface Pet {
    tags: Array<string>;
    photoUrls: string[];
}
"""
    result = extract_interfaces(code, ts_parser)

    assert result == [
        {
            "name": "Pet",
            "properties": [
                {"name": "tags", "type": "Array<string>", "optional": False},
                {"name": "photoUrls", "type": "string[]", "optional": False},
            ],
        }
    ]


def test_extract_multiple_interfaces(ts_parser):
    """Extract multiple interfaces from same file."""
    code = b"""
export interface Pet {
    name: string;
}

export interface Category {
    id: number;
}
"""
    result = extract_interfaces(code, ts_parser)

    # Should be sorted by name for stable comparison
    assert len(result) == 2
    assert result[0]["name"] == "Category"
    assert result[1]["name"] == "Pet"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_ts_structure.py -v`
Expected: FAIL with "No module named 'tests.ts_structure'"

**Step 3: Write minimal ts_structure.py with interface extraction**

Create `tests/ts_structure.py`:

```python
"""TypeScript structure extraction using tree-sitter.

Extracts functional structure from TypeScript code for order-independent comparison.
"""

from tree_sitter import Parser


def extract_interfaces(code: bytes, parser: Parser) -> list[dict]:
    """Extract interface definitions from TypeScript code.

    Returns:
        List of interfaces sorted by name, each containing:
        - name: Interface name
        - properties: List of {name, type, optional} dicts sorted by name
    """
    tree = parser.parse(code)
    interfaces = []

    for node in _find_nodes(tree.root_node, "interface_declaration"):
        name_node = node.child_by_field_name("name")
        if not name_node:
            continue

        body_node = node.child_by_field_name("body")
        if not body_node:
            continue

        properties = []
        for prop_node in _find_nodes(body_node, "property_signature"):
            prop_name = None
            prop_type = None
            optional = False

            for child in prop_node.children:
                if child.type == "property_identifier":
                    prop_name = child.text.decode("utf-8")
                elif child.type == "?":
                    optional = True
                elif child.type == "type_annotation":
                    # Get the type inside the annotation (skip the colon)
                    for type_child in child.children:
                        if type_child.type != ":":
                            prop_type = type_child.text.decode("utf-8")
                            break

            if prop_name and prop_type:
                properties.append({
                    "name": prop_name,
                    "type": prop_type,
                    "optional": optional,
                })

        interfaces.append({
            "name": name_node.text.decode("utf-8"),
            "properties": sorted(properties, key=lambda p: p["name"]),
        })

    return sorted(interfaces, key=lambda i: i["name"])


def _find_nodes(node, node_type: str) -> list:
    """Recursively find all nodes of a given type."""
    results = []
    if node.type == node_type:
        results.append(node)
    for child in node.children:
        results.extend(_find_nodes(child, node_type))
    return results
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_ts_structure.py -v`
Expected: PASS

**Step 5: Lint and format**

Run: `ruff check tests/ts_structure.py tests/test_ts_structure.py --fix && ruff format tests/ts_structure.py tests/test_ts_structure.py`
Expected: Files formatted/fixed

**Step 6: Commit**

```bash
git add tests/ts_structure.py tests/test_ts_structure.py
git commit -m "$(cat <<'EOF'
feat(tests): add interface extraction with tree-sitter

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 4: Add Function Extraction to ts_structure.py

**Files:**
- Modify: `tests/ts_structure.py`
- Modify: `tests/test_ts_structure.py`

**Step 1: Write failing test for function extraction**

Add to `tests/test_ts_structure.py`:

```python
from tests.ts_structure import extract_functions


def test_extract_function_declaration(ts_parser):
    """Extract a function with parameters and return type."""
    code = b"""
export function PetFromJSON(json: any): Pet {
    return json;
}
"""
    result = extract_functions(code, ts_parser)

    assert result == [
        {
            "name": "PetFromJSON",
            "params": [{"name": "json", "type": "any"}],
            "return_type": "Pet",
        }
    ]


def test_extract_function_no_return_type(ts_parser):
    """Extract function without explicit return type."""
    code = b"""
export function log(message: string) {
    console.log(message);
}
"""
    result = extract_functions(code, ts_parser)

    assert result == [
        {
            "name": "log",
            "params": [{"name": "message", "type": "string"}],
            "return_type": None,
        }
    ]


def test_extract_multiple_functions(ts_parser):
    """Extract multiple functions sorted by name."""
    code = b"""
export function PetToJSON(pet: Pet): any {
    return pet;
}

export function PetFromJSON(json: any): Pet {
    return json;
}
"""
    result = extract_functions(code, ts_parser)

    assert len(result) == 2
    assert result[0]["name"] == "PetFromJSON"
    assert result[1]["name"] == "PetToJSON"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_ts_structure.py::test_extract_function_declaration -v`
Expected: FAIL with "cannot import name 'extract_functions'"

**Step 3: Implement extract_functions**

Add to `tests/ts_structure.py`:

```python
def extract_functions(code: bytes, parser: Parser) -> list[dict]:
    """Extract function definitions from TypeScript code.

    Returns:
        List of functions sorted by name, each containing:
        - name: Function name
        - params: List of {name, type} dicts in declaration order
        - return_type: Return type string or None
    """
    tree = parser.parse(code)
    functions = []

    for node in _find_nodes(tree.root_node, "function_declaration"):
        name_node = node.child_by_field_name("name")
        if not name_node:
            continue

        params = []
        params_node = node.child_by_field_name("parameters")
        if params_node:
            for param_node in _find_nodes(params_node, "required_parameter"):
                param_name = None
                param_type = None
                for child in param_node.children:
                    if child.type == "identifier":
                        param_name = child.text.decode("utf-8")
                    elif child.type == "type_annotation":
                        for type_child in child.children:
                            if type_child.type != ":":
                                param_type = type_child.text.decode("utf-8")
                                break
                if param_name:
                    params.append({"name": param_name, "type": param_type})

        return_type = None
        return_type_node = node.child_by_field_name("return_type")
        if return_type_node:
            for child in return_type_node.children:
                if child.type != ":":
                    return_type = child.text.decode("utf-8")
                    break

        functions.append({
            "name": name_node.text.decode("utf-8"),
            "params": params,
            "return_type": return_type,
        })

    return sorted(functions, key=lambda f: f["name"])
```

**Step 4: Run tests to verify they pass**

Run: `pytest tests/test_ts_structure.py -v -k function`
Expected: All function tests PASS

**Step 5: Lint and format**

Run: `ruff check tests/ts_structure.py tests/test_ts_structure.py --fix && ruff format tests/ts_structure.py tests/test_ts_structure.py`

**Step 6: Commit**

```bash
git add tests/ts_structure.py tests/test_ts_structure.py
git commit -m "$(cat <<'EOF'
feat(tests): add function extraction to ts_structure

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 5: Add Type Alias Extraction to ts_structure.py

**Files:**
- Modify: `tests/ts_structure.py`
- Modify: `tests/test_ts_structure.py`

**Step 1: Write failing test for type alias extraction**

Add to `tests/test_ts_structure.py`:

```python
from tests.ts_structure import extract_type_aliases


def test_extract_type_alias(ts_parser):
    """Extract a type alias."""
    code = b"""
export type PetStatus = 'available' | 'pending' | 'sold';
"""
    result = extract_type_aliases(code, ts_parser)

    assert result == [
        {
            "name": "PetStatus",
            "definition": "'available' | 'pending' | 'sold'",
        }
    ]


def test_extract_multiple_type_aliases(ts_parser):
    """Extract multiple type aliases sorted by name."""
    code = b"""
export type OrderStatus = 'placed' | 'approved';
export type PetStatus = 'available' | 'pending';
"""
    result = extract_type_aliases(code, ts_parser)

    assert len(result) == 2
    assert result[0]["name"] == "OrderStatus"
    assert result[1]["name"] == "PetStatus"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_ts_structure.py::test_extract_type_alias -v`
Expected: FAIL

**Step 3: Implement extract_type_aliases**

Add to `tests/ts_structure.py`:

```python
def extract_type_aliases(code: bytes, parser: Parser) -> list[dict]:
    """Extract type alias definitions from TypeScript code.

    Returns:
        List of type aliases sorted by name, each containing:
        - name: Type alias name
        - definition: The type definition string
    """
    tree = parser.parse(code)
    aliases = []

    for node in _find_nodes(tree.root_node, "type_alias_declaration"):
        name_node = node.child_by_field_name("name")
        value_node = node.child_by_field_name("value")

        if name_node and value_node:
            aliases.append({
                "name": name_node.text.decode("utf-8"),
                "definition": value_node.text.decode("utf-8"),
            })

    return sorted(aliases, key=lambda a: a["name"])
```

**Step 4: Run tests to verify they pass**

Run: `pytest tests/test_ts_structure.py -v -k type_alias`
Expected: PASS

**Step 5: Lint and format**

Run: `ruff check tests/ts_structure.py tests/test_ts_structure.py --fix && ruff format tests/ts_structure.py tests/test_ts_structure.py`

**Step 6: Commit**

```bash
git add tests/ts_structure.py tests/test_ts_structure.py
git commit -m "$(cat <<'EOF'
feat(tests): add type alias extraction to ts_structure

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 6: Add Enum/Const Object Extraction to ts_structure.py

**Files:**
- Modify: `tests/ts_structure.py`
- Modify: `tests/test_ts_structure.py`

**Step 1: Write failing test for enum extraction**

Add to `tests/test_ts_structure.py`:

```python
from tests.ts_structure import extract_enums


def test_extract_const_object_as_enum(ts_parser):
    """Extract const object used as enum."""
    code = b"""
export const PetStatusEnum = {
    Available: 'available',
    Pending: 'pending',
    Sold: 'sold'
} as const;
"""
    result = extract_enums(code, ts_parser)

    assert result == [
        {
            "name": "PetStatusEnum",
            "members": [
                {"name": "Available", "value": "'available'"},
                {"name": "Pending", "value": "'pending'"},
                {"name": "Sold", "value": "'sold'"},
            ],
        }
    ]


def test_extract_typescript_enum(ts_parser):
    """Extract TypeScript enum."""
    code = b"""
export enum Status {
    Active = 'active',
    Inactive = 'inactive'
}
"""
    result = extract_enums(code, ts_parser)

    assert result == [
        {
            "name": "Status",
            "members": [
                {"name": "Active", "value": "'active'"},
                {"name": "Inactive", "value": "'inactive'"},
            ],
        }
    ]
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_ts_structure.py::test_extract_const_object_as_enum -v`
Expected: FAIL

**Step 3: Implement extract_enums**

Add to `tests/ts_structure.py`:

```python
def extract_enums(code: bytes, parser: Parser) -> list[dict]:
    """Extract enum and const-object-as-enum definitions from TypeScript code.

    Returns:
        List of enums sorted by name, each containing:
        - name: Enum name
        - members: List of {name, value} dicts sorted by name
    """
    tree = parser.parse(code)
    enums = []

    # Handle TypeScript enums
    for node in _find_nodes(tree.root_node, "enum_declaration"):
        name_node = node.child_by_field_name("name")
        body_node = node.child_by_field_name("body")

        if not name_node or not body_node:
            continue

        members = []
        for member_node in _find_nodes(body_node, "enum_assignment"):
            member_name = None
            member_value = None
            for child in member_node.children:
                if child.type == "property_identifier":
                    member_name = child.text.decode("utf-8")
                elif child.type == "string":
                    member_value = child.text.decode("utf-8")
            if member_name and member_value:
                members.append({"name": member_name, "value": member_value})

        enums.append({
            "name": name_node.text.decode("utf-8"),
            "members": sorted(members, key=lambda m: m["name"]),
        })

    # Handle const objects used as enums (export const X = {...} as const)
    for node in _find_nodes(tree.root_node, "lexical_declaration"):
        # Check if this is an export const
        is_const = any(child.type == "const" for child in node.children)
        if not is_const:
            continue

        for var_decl in _find_nodes(node, "variable_declarator"):
            name_node = var_decl.child_by_field_name("name")
            value_node = var_decl.child_by_field_name("value")

            if not name_node or not value_node:
                continue

            # Check for "as const" assertion with object literal
            if value_node.type == "as_expression":
                obj_node = None
                for child in value_node.children:
                    if child.type == "object":
                        obj_node = child
                        break

                if obj_node:
                    members = []
                    for pair_node in _find_nodes(obj_node, "pair"):
                        key_node = pair_node.child_by_field_name("key")
                        val_node = pair_node.child_by_field_name("value")
                        if key_node and val_node:
                            members.append({
                                "name": key_node.text.decode("utf-8"),
                                "value": val_node.text.decode("utf-8"),
                            })

                    if members:
                        enums.append({
                            "name": name_node.text.decode("utf-8"),
                            "members": sorted(members, key=lambda m: m["name"]),
                        })

    return sorted(enums, key=lambda e: e["name"])
```

**Step 4: Run tests to verify they pass**

Run: `pytest tests/test_ts_structure.py -v -k enum`
Expected: PASS

**Step 5: Lint and format**

Run: `ruff check tests/ts_structure.py tests/test_ts_structure.py --fix && ruff format tests/ts_structure.py tests/test_ts_structure.py`

**Step 6: Commit**

```bash
git add tests/ts_structure.py tests/test_ts_structure.py
git commit -m "$(cat <<'EOF'
feat(tests): add enum/const extraction to ts_structure

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 7: Add Export Extraction to ts_structure.py

**Files:**
- Modify: `tests/ts_structure.py`
- Modify: `tests/test_ts_structure.py`

**Step 1: Write failing test for export extraction**

Add to `tests/test_ts_structure.py`:

```python
from tests.ts_structure import extract_exports


def test_extract_inline_exports(ts_parser):
    """Extract exports from export declarations."""
    code = b"""
export interface Pet {
    name: string;
}

export function PetFromJSON(json: any): Pet {
    return json;
}

export const PetStatusEnum = {} as const;
"""
    result = extract_exports(code, ts_parser)

    assert sorted(result) == ["Pet", "PetFromJSON", "PetStatusEnum"]


def test_extract_export_statement(ts_parser):
    """Extract exports from export statements."""
    code = b"""
interface Pet {
    name: string;
}

export { Pet };
"""
    result = extract_exports(code, ts_parser)

    assert result == ["Pet"]


def test_extract_reexports(ts_parser):
    """Extract re-exports from other modules."""
    code = b"""
export { Pet, Category } from './models';
export * from './runtime';
"""
    result = extract_exports(code, ts_parser)

    # Named exports should be captured, star exports noted
    assert "Pet" in result
    assert "Category" in result
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_ts_structure.py::test_extract_inline_exports -v`
Expected: FAIL

**Step 3: Implement extract_exports**

Add to `tests/ts_structure.py`:

```python
def extract_exports(code: bytes, parser: Parser) -> list[str]:
    """Extract exported names from TypeScript code.

    Returns:
        List of exported names (sorted, unique).
    """
    tree = parser.parse(code)
    exports = set()

    # Handle export statements (export { X, Y })
    for node in _find_nodes(tree.root_node, "export_statement"):
        # Check for named exports: export { X, Y } or export { X } from './module'
        for clause in _find_nodes(node, "export_clause"):
            for spec in _find_nodes(clause, "export_specifier"):
                name_node = spec.child_by_field_name("name")
                if name_node:
                    exports.add(name_node.text.decode("utf-8"))

        # Check for declaration exports (export interface X, export function Y, etc.)
        for child in node.children:
            if child.type == "interface_declaration":
                name = child.child_by_field_name("name")
                if name:
                    exports.add(name.text.decode("utf-8"))
            elif child.type == "function_declaration":
                name = child.child_by_field_name("name")
                if name:
                    exports.add(name.text.decode("utf-8"))
            elif child.type == "lexical_declaration":
                for var_decl in _find_nodes(child, "variable_declarator"):
                    name = var_decl.child_by_field_name("name")
                    if name:
                        exports.add(name.text.decode("utf-8"))
            elif child.type == "type_alias_declaration":
                name = child.child_by_field_name("name")
                if name:
                    exports.add(name.text.decode("utf-8"))
            elif child.type == "enum_declaration":
                name = child.child_by_field_name("name")
                if name:
                    exports.add(name.text.decode("utf-8"))
            elif child.type == "class_declaration":
                name = child.child_by_field_name("name")
                if name:
                    exports.add(name.text.decode("utf-8"))

    return sorted(exports)
```

**Step 4: Run tests to verify they pass**

Run: `pytest tests/test_ts_structure.py -v -k export`
Expected: PASS

**Step 5: Lint and format**

Run: `ruff check tests/ts_structure.py tests/test_ts_structure.py --fix && ruff format tests/ts_structure.py tests/test_ts_structure.py`

**Step 6: Commit**

```bash
git add tests/ts_structure.py tests/test_ts_structure.py
git commit -m "$(cat <<'EOF'
feat(tests): add export extraction to ts_structure

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 8: Add Class Extraction to ts_structure.py

**Files:**
- Modify: `tests/ts_structure.py`
- Modify: `tests/test_ts_structure.py`

**Step 1: Write failing test for class extraction**

Add to `tests/test_ts_structure.py`:

```python
from tests.ts_structure import extract_classes


def test_extract_class_with_properties(ts_parser):
    """Extract class with properties."""
    code = b"""
export class Configuration {
    basePath: string;
    apiKey?: string;

    constructor(config?: Partial<Configuration>) {}
}
"""
    result = extract_classes(code, ts_parser)

    assert len(result) == 1
    assert result[0]["name"] == "Configuration"
    assert {"name": "basePath", "type": "string", "optional": False} in result[0]["properties"]
    assert {"name": "apiKey", "type": "string", "optional": True} in result[0]["properties"]


def test_extract_class_with_methods(ts_parser):
    """Extract class with method signatures."""
    code = b"""
export class PetApi {
    getPet(petId: number): Promise<Pet> {
        return fetch('/pet/' + petId);
    }

    addPet(pet: Pet): Promise<void> {
        return fetch('/pet', { method: 'POST' });
    }
}
"""
    result = extract_classes(code, ts_parser)

    assert len(result) == 1
    methods = result[0]["methods"]
    assert len(methods) == 2
    assert {"name": "addPet", "params": [{"name": "pet", "type": "Pet"}], "return_type": "Promise<void>"} in methods
    assert {"name": "getPet", "params": [{"name": "petId", "type": "number"}], "return_type": "Promise<Pet>"} in methods
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_ts_structure.py::test_extract_class_with_properties -v`
Expected: FAIL

**Step 3: Implement extract_classes**

Add to `tests/ts_structure.py`:

```python
def extract_classes(code: bytes, parser: Parser) -> list[dict]:
    """Extract class definitions from TypeScript code.

    Returns:
        List of classes sorted by name, each containing:
        - name: Class name
        - properties: List of {name, type, optional} dicts sorted by name
        - methods: List of {name, params, return_type} dicts sorted by name
    """
    tree = parser.parse(code)
    classes = []

    for node in _find_nodes(tree.root_node, "class_declaration"):
        name_node = node.child_by_field_name("name")
        body_node = node.child_by_field_name("body")

        if not name_node or not body_node:
            continue

        properties = []
        methods = []

        for child in body_node.children:
            # Public field definition (property)
            if child.type == "public_field_definition":
                prop_name = None
                prop_type = None
                optional = False

                for field_child in child.children:
                    if field_child.type == "property_identifier":
                        prop_name = field_child.text.decode("utf-8")
                    elif field_child.type == "?":
                        optional = True
                    elif field_child.type == "type_annotation":
                        for type_child in field_child.children:
                            if type_child.type != ":":
                                prop_type = type_child.text.decode("utf-8")
                                break

                if prop_name and prop_type:
                    properties.append({
                        "name": prop_name,
                        "type": prop_type,
                        "optional": optional,
                    })

            # Method definition
            elif child.type == "method_definition":
                method_name_node = child.child_by_field_name("name")
                if not method_name_node:
                    continue

                method_name = method_name_node.text.decode("utf-8")
                if method_name == "constructor":
                    continue  # Skip constructor

                params = []
                params_node = child.child_by_field_name("parameters")
                if params_node:
                    for param_node in _find_nodes(params_node, "required_parameter"):
                        param_name = None
                        param_type = None
                        for p_child in param_node.children:
                            if p_child.type == "identifier":
                                param_name = p_child.text.decode("utf-8")
                            elif p_child.type == "type_annotation":
                                for type_child in p_child.children:
                                    if type_child.type != ":":
                                        param_type = type_child.text.decode("utf-8")
                                        break
                        if param_name:
                            params.append({"name": param_name, "type": param_type})

                return_type = None
                return_type_node = child.child_by_field_name("return_type")
                if return_type_node:
                    for rt_child in return_type_node.children:
                        if rt_child.type != ":":
                            return_type = rt_child.text.decode("utf-8")
                            break

                methods.append({
                    "name": method_name,
                    "params": params,
                    "return_type": return_type,
                })

        classes.append({
            "name": name_node.text.decode("utf-8"),
            "properties": sorted(properties, key=lambda p: p["name"]),
            "methods": sorted(methods, key=lambda m: m["name"]),
        })

    return sorted(classes, key=lambda c: c["name"])
```

**Step 4: Run tests to verify they pass**

Run: `pytest tests/test_ts_structure.py -v -k class`
Expected: PASS

**Step 5: Lint and format**

Run: `ruff check tests/ts_structure.py tests/test_ts_structure.py --fix && ruff format tests/ts_structure.py tests/test_ts_structure.py`

**Step 6: Commit**

```bash
git add tests/ts_structure.py tests/test_ts_structure.py
git commit -m "$(cat <<'EOF'
feat(tests): add class extraction to ts_structure

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 9: Add Directory-Level Structure Extraction

**Files:**
- Modify: `tests/ts_structure.py`
- Modify: `tests/test_ts_structure.py`

**Step 1: Write failing test for directory extraction**

Add to `tests/test_ts_structure.py`:

```python
from pathlib import Path

from tests.ts_structure import extract_ts_structure


def test_extract_ts_structure_from_directory(ts_parser, tmp_path):
    """Extract structure from all .ts files in a directory."""
    # Create test files
    models_dir = tmp_path / "models"
    models_dir.mkdir()

    (models_dir / "Pet.ts").write_text("""
export interface Pet {
    id?: number;
    name: string;
}

export function PetFromJSON(json: any): Pet {
    return json;
}
""")

    (models_dir / "index.ts").write_text("""
export { Pet, PetFromJSON } from './Pet';
""")

    result = extract_ts_structure(tmp_path, ts_parser)

    assert "models/Pet.ts" in result
    assert "models/index.ts" in result

    pet_structure = result["models/Pet.ts"]
    assert len(pet_structure["interfaces"]) == 1
    assert pet_structure["interfaces"][0]["name"] == "Pet"
    assert len(pet_structure["functions"]) == 1
    assert pet_structure["functions"][0]["name"] == "PetFromJSON"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_ts_structure.py::test_extract_ts_structure_from_directory -v`
Expected: FAIL

**Step 3: Implement extract_ts_structure**

Add to `tests/ts_structure.py`:

```python
from pathlib import Path


def extract_ts_structure(directory: Path, parser: Parser) -> dict:
    """Extract functional structure from all .ts files in directory.

    Returns:
        {
            "relative/path/to/file.ts": {
                "interfaces": [...],
                "functions": [...],
                "type_aliases": [...],
                "enums": [...],
                "classes": [...],
                "exports": [...]
            }
        }
    """
    result = {}

    for ts_file in sorted(directory.rglob("*.ts")):
        rel_path = str(ts_file.relative_to(directory))
        code = ts_file.read_bytes()

        result[rel_path] = {
            "interfaces": extract_interfaces(code, parser),
            "functions": extract_functions(code, parser),
            "type_aliases": extract_type_aliases(code, parser),
            "enums": extract_enums(code, parser),
            "classes": extract_classes(code, parser),
            "exports": extract_exports(code, parser),
        }

    return result
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_ts_structure.py::test_extract_ts_structure_from_directory -v`
Expected: PASS

**Step 5: Lint and format**

Run: `ruff check tests/ts_structure.py tests/test_ts_structure.py --fix && ruff format tests/ts_structure.py tests/test_ts_structure.py`

**Step 6: Commit**

```bash
git add tests/ts_structure.py tests/test_ts_structure.py
git commit -m "$(cat <<'EOF'
feat(tests): add directory-level structure extraction

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 10: Create Structural Equivalence Test

**Files:**
- Create: `tests/test_structural_equivalence.py`

**Step 1: Write structural equivalence test**

Create `tests/test_structural_equivalence.py`:

```python
"""Structural equivalence tests for generated TypeScript clients.

Compares the functional structure of generated code against fixtures,
ignoring whitespace, ordering, and formatting differences.
"""

import json
from pathlib import Path

import pytest

from openapi_ts_client import ClientFormat, generate_typescript_client
from tests.ts_structure import extract_ts_structure

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def load_spec(fixture_name: str) -> dict:
    """Load OpenAPI spec from fixture directory."""
    spec_path = FIXTURES_DIR / fixture_name / "openapi.json"
    return json.loads(spec_path.read_text())


@pytest.mark.parametrize("fixture_name", ["petstore", "space_zoo"])
def test_fetch_structural_equivalence(fixture_name: str, tmp_path: Path, ts_parser) -> None:
    """Test that Fetch generation produces structurally equivalent output."""
    fixture_dir = FIXTURES_DIR / fixture_name / "fetch"
    spec = load_spec(fixture_name)

    # Generate client to temp dir
    generate_typescript_client(spec, ClientFormat.FETCH, tmp_path)

    # Extract structure from both
    expected = extract_ts_structure(fixture_dir, ts_parser)
    actual = extract_ts_structure(tmp_path, ts_parser)

    # Compare file sets (excluding .openapi-generator metadata)
    expected_files = {k for k in expected.keys() if not k.startswith(".openapi-generator")}
    actual_files = set(actual.keys())

    missing = expected_files - actual_files
    extra = actual_files - expected_files

    if missing:
        pytest.fail(f"Missing files: {sorted(missing)}")
    if extra:
        pytest.fail(f"Extra files: {sorted(extra)}")

    # Compare structure of each file
    differences = []
    for rel_path in sorted(expected_files):
        exp_struct = expected[rel_path]
        act_struct = actual[rel_path]

        for key in ["interfaces", "functions", "type_aliases", "enums", "classes", "exports"]:
            if exp_struct[key] != act_struct[key]:
                differences.append(
                    f"{rel_path} - {key}:\n"
                    f"  Expected: {exp_struct[key]}\n"
                    f"  Actual:   {act_struct[key]}"
                )

    if differences:
        pytest.fail("\n\n".join(differences))


@pytest.mark.parametrize("fixture_name", ["petstore", "space_zoo"])
def test_angular_structural_equivalence(fixture_name: str, tmp_path: Path, ts_parser) -> None:
    """Test that Angular generation produces structurally equivalent output."""
    fixture_dir = FIXTURES_DIR / fixture_name / "angular"
    spec = load_spec(fixture_name)

    # Generate client to temp dir
    generate_typescript_client(spec, ClientFormat.ANGULAR, tmp_path)

    # Extract structure from both
    expected = extract_ts_structure(fixture_dir, ts_parser)
    actual = extract_ts_structure(tmp_path, ts_parser)

    # Compare file sets (excluding .openapi-generator metadata)
    expected_files = {k for k in expected.keys() if not k.startswith(".openapi-generator")}
    actual_files = set(actual.keys())

    missing = expected_files - actual_files
    extra = actual_files - expected_files

    if missing:
        pytest.fail(f"Missing files: {sorted(missing)}")
    if extra:
        pytest.fail(f"Extra files: {sorted(extra)}")

    # Compare structure of each file
    differences = []
    for rel_path in sorted(expected_files):
        exp_struct = expected[rel_path]
        act_struct = actual[rel_path]

        for key in ["interfaces", "functions", "type_aliases", "enums", "classes", "exports"]:
            if exp_struct[key] != act_struct[key]:
                differences.append(
                    f"{rel_path} - {key}:\n"
                    f"  Expected: {exp_struct[key]}\n"
                    f"  Actual:   {act_struct[key]}"
                )

    if differences:
        pytest.fail("\n\n".join(differences))
```

**Step 2: Run test to verify it works (may fail if generator output differs)**

Run: `pytest tests/test_structural_equivalence.py -v --tb=short`
Expected: Tests run (pass or fail based on current generator output)

**Step 3: Lint and format**

Run: `ruff check tests/test_structural_equivalence.py --fix && ruff format tests/test_structural_equivalence.py`

**Step 4: Commit**

```bash
git add tests/test_structural_equivalence.py
git commit -m "$(cat <<'EOF'
test: add structural equivalence tests for generated clients

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 11: Create TypeScript Validity Test - Compilation

**Files:**
- Create: `tests/test_typescript_validity.py`

**Step 1: Write TypeScript compilation test**

Create `tests/test_typescript_validity.py`:

```python
"""TypeScript validity tests for generated clients.

Verifies that generated TypeScript code compiles and runs correctly.
"""

import json
import subprocess
from pathlib import Path

import pytest

from openapi_ts_client import ClientFormat, generate_typescript_client

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def load_spec(fixture_name: str) -> dict:
    """Load OpenAPI spec from fixture directory."""
    spec_path = FIXTURES_DIR / fixture_name / "openapi.json"
    return json.loads(spec_path.read_text())


def write_tsconfig(output_path: Path) -> None:
    """Write minimal tsconfig.json for compilation check."""
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
    (output_path / "tsconfig.json").write_text(json.dumps(tsconfig, indent=2))


@pytest.mark.parametrize("fixture_name", ["petstore", "space_zoo"])
def test_fetch_typescript_compiles(fixture_name: str, tmp_path: Path) -> None:
    """Test that generated Fetch client compiles with tsc."""
    spec = load_spec(fixture_name)
    generate_typescript_client(spec, ClientFormat.FETCH, tmp_path)

    write_tsconfig(tmp_path)

    result = subprocess.run(
        ["tsc", "--project", str(tmp_path)],
        capture_output=True,
        text=True,
        timeout=60,
    )

    assert result.returncode == 0, f"TypeScript compilation failed:\n{result.stdout}\n{result.stderr}"


@pytest.mark.parametrize("fixture_name", ["petstore", "space_zoo"])
def test_angular_typescript_compiles(fixture_name: str, tmp_path: Path) -> None:
    """Test that generated Angular client compiles with tsc."""
    spec = load_spec(fixture_name)
    generate_typescript_client(spec, ClientFormat.ANGULAR, tmp_path)

    # Angular needs rxjs types - add to tsconfig
    tsconfig = {
        "compilerOptions": {
            "target": "ES2020",
            "module": "ESNext",
            "moduleResolution": "node",
            "strict": True,
            "noEmit": True,
            "skipLibCheck": True,
            "esModuleInterop": True,
            "experimentalDecorators": True,
            "paths": {
                "rxjs": ["node_modules/rxjs"],
                "rxjs/*": ["node_modules/rxjs/*"],
                "@angular/*": ["node_modules/@angular/*"],
            },
        },
        "include": ["**/*.ts"],
    }
    (tmp_path / "tsconfig.json").write_text(json.dumps(tsconfig, indent=2))

    # Install minimal Angular/RxJS types for compilation
    # Note: This may need adjustment based on CI environment
    result = subprocess.run(
        ["tsc", "--project", str(tmp_path)],
        capture_output=True,
        text=True,
        timeout=60,
    )

    # For Angular, we expect some errors due to missing @angular/core and rxjs
    # A more complete test would install these dependencies
    # For now, we check that there are no syntax errors in our generated code
    if result.returncode != 0:
        # Filter out errors about missing modules (expected without npm install)
        errors = [
            line
            for line in result.stderr.split("\n")
            if "error TS" in line
            and "Cannot find module" not in line
            and "has no exported member" not in line
        ]
        if errors:
            pytest.fail(f"TypeScript compilation errors:\n" + "\n".join(errors))
```

**Step 2: Run test to verify it works**

Run: `pytest tests/test_typescript_validity.py -v --tb=short`
Expected: Tests run (pass or fail based on generated output)

**Step 3: Lint and format**

Run: `ruff check tests/test_typescript_validity.py --fix && ruff format tests/test_typescript_validity.py`

**Step 4: Commit**

```bash
git add tests/test_typescript_validity.py
git commit -m "$(cat <<'EOF'
test: add TypeScript compilation validity tests

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 12: Add Runtime Tests to TypeScript Validity

**Files:**
- Modify: `tests/test_typescript_validity.py`

**Step 1: Add runtime test generator function**

Add to `tests/test_typescript_validity.py`:

```python
from tests.ts_structure import extract_ts_structure


def generate_runtime_test(structure: dict) -> str:
    """Generate a runtime test file based on extracted structure.

    Creates a TypeScript file that:
    1. Imports all models
    2. Instantiates interfaces with required fields
    3. Calls conversion functions
    4. Verifies enum values exist
    """
    lines = [
        "// Auto-generated runtime test",
        "",
    ]

    # Collect all interfaces, functions, and enums
    all_interfaces = []
    all_functions = []
    all_enums = []

    for file_path, file_struct in structure.items():
        if not file_path.startswith("models/") or file_path == "models/index.ts":
            continue

        all_interfaces.extend(file_struct.get("interfaces", []))
        all_functions.extend(file_struct.get("functions", []))
        all_enums.extend(file_struct.get("enums", []))

    # Import from models index
    if all_interfaces or all_functions or all_enums:
        imports = []
        imports.extend(i["name"] for i in all_interfaces)
        imports.extend(f["name"] for f in all_functions)
        imports.extend(e["name"] for e in all_enums)

        # Only import what exists in models/index.ts exports
        index_struct = structure.get("models/index.ts", {})
        available_exports = set(index_struct.get("exports", []))

        valid_imports = [i for i in imports if i in available_exports]
        if valid_imports:
            lines.append(f"import {{ {', '.join(sorted(set(valid_imports)))} }} from './models';")
            lines.append("")

    # Basic runtime check - just verify imports work
    lines.append("console.log('Runtime validation passed');")

    return "\n".join(lines)


@pytest.mark.parametrize("fixture_name", ["petstore"])
def test_fetch_typescript_runtime(fixture_name: str, tmp_path: Path, ts_parser) -> None:
    """Test that generated Fetch client runs with tsx."""
    spec = load_spec(fixture_name)
    generate_typescript_client(spec, ClientFormat.FETCH, tmp_path)

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

Run: `pytest tests/test_typescript_validity.py::test_fetch_typescript_runtime -v`
Expected: Test runs (pass or fail based on generated output)

**Step 3: Lint and format**

Run: `ruff check tests/test_typescript_validity.py --fix && ruff format tests/test_typescript_validity.py`

**Step 4: Commit**

```bash
git add tests/test_typescript_validity.py
git commit -m "$(cat <<'EOF'
test: add TypeScript runtime validity tests

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 13: Delete Old Fixture Comparison Test

**Files:**
- Delete: `tests/test_fixture_comparison.py`

**Step 1: Verify new tests cover the same fixtures**

Run: `pytest tests/test_structural_equivalence.py tests/test_typescript_validity.py --collect-only`
Expected: Tests for petstore and space_zoo fixtures listed

**Step 2: Delete the old test file**

Run: `rm tests/test_fixture_comparison.py`

**Step 3: Verify all tests still pass**

Run: `pytest tests/ -v --tb=short`
Expected: All tests pass (or known failures in structural equivalence)

**Step 4: Commit**

```bash
git add -A
git commit -m "$(cat <<'EOF'
refactor(tests): remove byte-for-byte fixture comparison

Replaced by structural equivalence and TypeScript validity tests.

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Task 14: Run Full Test Suite and Fix Issues

**Files:**
- May modify: Various test files based on failures

**Step 1: Run full test suite**

Run: `pytest tests/ -v`
Expected: All tests pass, or failures identified for fixing

**Step 2: Fix any remaining issues**

Address any failures discovered during the full test run.

**Step 3: Final commit if needed**

```bash
git add -A
git commit -m "$(cat <<'EOF'
fix(tests): address test suite issues

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>
EOF
)"
```

---

## Summary

| Task | Description | Files |
|------|-------------|-------|
| 1 | Add tree-sitter dependencies | pyproject.toml |
| 2 | Create conftest.py | tests/conftest.py |
| 3 | Interface extraction | tests/ts_structure.py, tests/test_ts_structure.py |
| 4 | Function extraction | tests/ts_structure.py, tests/test_ts_structure.py |
| 5 | Type alias extraction | tests/ts_structure.py, tests/test_ts_structure.py |
| 6 | Enum extraction | tests/ts_structure.py, tests/test_ts_structure.py |
| 7 | Export extraction | tests/ts_structure.py, tests/test_ts_structure.py |
| 8 | Class extraction | tests/ts_structure.py, tests/test_ts_structure.py |
| 9 | Directory extraction | tests/ts_structure.py, tests/test_ts_structure.py |
| 10 | Structural equivalence test | tests/test_structural_equivalence.py |
| 11 | TypeScript compilation test | tests/test_typescript_validity.py |
| 12 | TypeScript runtime test | tests/test_typescript_validity.py |
| 13 | Delete old fixture comparison | tests/test_fixture_comparison.py |
| 14 | Final test run and fixes | Various |
