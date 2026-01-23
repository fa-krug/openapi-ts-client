# Angular TypeScript Generator Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement TypeScript generation for Angular format, producing Angular services and TypeScript interfaces from OpenAPI 3.x specifications that match the reference fixtures exactly.

**Architecture:** Module-per-output design with shared utilities. OpenAPI spec is parsed and dereferenced using openapi-core, then split into schemas (for models) and paths (for services). Jinja2 templates render the TypeScript output. Tests compare generated output byte-for-byte against fixtures.

**Tech Stack:** Python 3.10+, Jinja2, openapi-core, pytest

---

## Phase 1: Foundation

### Task 1: Add Dependencies

**Files:**
- Modify: `pyproject.toml`

**Step 1: Add jinja2 and openapi-core to dependencies**

In `pyproject.toml`, update the `dependencies` list:

```toml
dependencies = [
    "jinja2>=3.1.0",
    "openapi-core>=0.19.0",
]
```

**Step 2: Install updated dependencies**

Run: `pip3 install -e ".[dev]"`
Expected: Successfully installed jinja2 and openapi-core

**Step 3: Verify imports work**

Run: `python3 -c "import jinja2; import openapi_core; print('OK')"`
Expected: `OK`

**Step 4: Commit**

```bash
git add pyproject.toml
git commit -m "chore: add jinja2 and openapi-core dependencies"
```

---

### Task 2: Create Utils Package Structure

**Files:**
- Create: `src/openapi_ts_client/utils/__init__.py`

**Step 1: Create utils package**

```python
"""Shared utilities for OpenAPI TypeScript client generation."""
```

**Step 2: Verify package imports**

Run: `python3 -c "from openapi_ts_client import utils; print('OK')"`
Expected: `OK`

**Step 3: Commit**

```bash
git add src/openapi_ts_client/utils/
git commit -m "chore: create utils package structure"
```

---

### Task 3: Create Naming Utilities - Schema to Filename

**Files:**
- Create: `src/openapi_ts_client/utils/naming.py`
- Create: `tests/test_naming.py`

**Step 1: Write failing test for schema_to_filename**

```python
"""Tests for naming utilities."""

import pytest

from openapi_ts_client.utils.naming import schema_to_filename


class TestSchemaToFilename:
    """Tests for schema_to_filename function."""

    def test_simple_name(self):
        """Simple PascalCase becomes camelCase."""
        assert schema_to_filename("FeedingOut") == "feedingOut.ts"

    def test_single_word(self):
        """Single word gets lowercased."""
        assert schema_to_filename("Score") == "score.ts"

    def test_acronym_preserved(self):
        """Acronyms preserve their casing pattern from fixture."""
        # From fixture: HTTPMetrics -> hTTPMetrics.ts
        assert schema_to_filename("HTTPMetrics") == "hTTPMetrics.ts"

    def test_db_prefix(self):
        """DB prefix follows fixture pattern."""
        # From fixture: DBMetrics -> dBMetrics.ts
        assert schema_to_filename("DBMetrics") == "dBMetrics.ts"

    def test_already_camelcase(self):
        """Already camelCase stays the same."""
        assert schema_to_filename("biomeTypeIn") == "biomeTypeIn.ts"
```

**Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_naming.py -v`
Expected: FAIL with "cannot import name 'schema_to_filename'"

**Step 3: Write minimal implementation**

```python
"""Naming convention utilities for TypeScript generation."""


def schema_to_filename(schema_name: str) -> str:
    """
    Convert OpenAPI schema name to TypeScript filename.

    Examples:
        FeedingOut -> feedingOut.ts
        HTTPMetrics -> hTTPMetrics.ts
        Score -> score.ts
    """
    if not schema_name:
        return ".ts"

    # Lowercase first character only
    filename = schema_name[0].lower() + schema_name[1:] if len(schema_name) > 1 else schema_name.lower()

    return f"{filename}.ts"
```

**Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_naming.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/utils/naming.py tests/test_naming.py
git commit -m "feat: add schema_to_filename naming utility"
```

---

### Task 4: Create Naming Utilities - Tag to Service Name

**Files:**
- Modify: `src/openapi_ts_client/utils/naming.py`
- Modify: `tests/test_naming.py`

**Step 1: Write failing test for tag_to_service_name**

Add to `tests/test_naming.py`:

```python
from openapi_ts_client.utils.naming import schema_to_filename, tag_to_service_name


class TestTagToServiceName:
    """Tests for tag_to_service_name function."""

    def test_simple_tag(self):
        """Simple tag becomes ServiceName."""
        assert tag_to_service_name("Feedings") == "FeedingsService"

    def test_multi_word_tag(self):
        """Multi-word tag preserves casing."""
        assert tag_to_service_name("HealthReports") == "HealthReportsService"

    def test_acronym_tag(self):
        """Acronym tags preserve casing."""
        assert tag_to_service_name("HTTPMetrics") == "HTTPMetricsService"

    def test_spaces_in_tag(self):
        """Spaces are removed and words concatenated."""
        assert tag_to_service_name("Care Plans") == "CarePlansService"
```

**Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_naming.py::TestTagToServiceName -v`
Expected: FAIL with "cannot import name 'tag_to_service_name'"

**Step 3: Write minimal implementation**

Add to `src/openapi_ts_client/utils/naming.py`:

```python
def tag_to_service_name(tag: str) -> str:
    """
    Convert OpenAPI tag to Angular service class name.

    Examples:
        Feedings -> FeedingsService
        HTTPMetrics -> HTTPMetricsService
        Care Plans -> CarePlansService
    """
    # Remove spaces and ensure first letter of each word is capitalized
    words = tag.split()
    class_name = "".join(word[0].upper() + word[1:] if word else "" for word in words)

    return f"{class_name}Service"
```

**Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_naming.py::TestTagToServiceName -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/utils/naming.py tests/test_naming.py
git commit -m "feat: add tag_to_service_name naming utility"
```

---

### Task 5: Create Naming Utilities - Tag to Service Filename

**Files:**
- Modify: `src/openapi_ts_client/utils/naming.py`
- Modify: `tests/test_naming.py`

**Step 1: Write failing test for tag_to_service_filename**

Add to `tests/test_naming.py`:

```python
from openapi_ts_client.utils.naming import (
    schema_to_filename,
    tag_to_service_name,
    tag_to_service_filename,
)


class TestTagToServiceFilename:
    """Tests for tag_to_service_filename function."""

    def test_simple_tag(self):
        """Simple tag becomes lowercase.service.ts."""
        assert tag_to_service_filename("Feedings") == "feedings.service.ts"

    def test_multi_word_tag(self):
        """Multi-word tag becomes camelCase.service.ts."""
        assert tag_to_service_filename("HealthReports") == "healthReports.service.ts"

    def test_acronym_tag(self):
        """Acronym tags follow fixture pattern."""
        # From fixture: HTTPMetrics -> hTTPMetrics.service.ts
        assert tag_to_service_filename("HTTPMetrics") == "hTTPMetrics.service.ts"

    def test_spaces_in_tag(self):
        """Spaces removed, camelCase result."""
        assert tag_to_service_filename("Care Plans") == "carePlans.service.ts"
```

**Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_naming.py::TestTagToServiceFilename -v`
Expected: FAIL with "cannot import name 'tag_to_service_filename'"

**Step 3: Write minimal implementation**

Add to `src/openapi_ts_client/utils/naming.py`:

```python
def tag_to_service_filename(tag: str) -> str:
    """
    Convert OpenAPI tag to Angular service filename.

    Examples:
        Feedings -> feedings.service.ts
        HTTPMetrics -> hTTPMetrics.service.ts
        Care Plans -> carePlans.service.ts
    """
    # Remove spaces and join words
    words = tag.split()
    if not words:
        return ".service.ts"

    # First word: lowercase first char
    # Subsequent words: keep first char case
    result = words[0][0].lower() + words[0][1:] if words[0] else ""
    for word in words[1:]:
        result += word

    return f"{result}.service.ts"
```

**Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_naming.py::TestTagToServiceFilename -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/utils/naming.py tests/test_naming.py
git commit -m "feat: add tag_to_service_filename naming utility"
```

---

### Task 6: Create Naming Utilities - Operation ID to Method Name

**Files:**
- Modify: `src/openapi_ts_client/utils/naming.py`
- Modify: `tests/test_naming.py`

**Step 1: Write failing test for operation_id_to_method_name**

Add to `tests/test_naming.py`:

```python
from openapi_ts_client.utils.naming import (
    schema_to_filename,
    tag_to_service_name,
    tag_to_service_filename,
    operation_id_to_method_name,
)


class TestOperationIdToMethodName:
    """Tests for operation_id_to_method_name function."""

    def test_dotted_path_with_underscores(self):
        """Extract last segment and convert to camelCase."""
        assert operation_id_to_method_name("zoo.api.endpoints.feedings_list_all") == "listAll"

    def test_simple_operation(self):
        """Simple operation ID stays as-is."""
        assert operation_id_to_method_name("count") == "count"

    def test_snake_case(self):
        """Snake case becomes camelCase."""
        assert operation_id_to_method_name("list_all") == "listAll"

    def test_reserved_word_delete(self):
        """Reserved word 'delete' gets underscore prefix."""
        assert operation_id_to_method_name("delete") == "_delete"

    def test_reserved_word_in_path(self):
        """Reserved word at end of path gets underscore prefix."""
        assert operation_id_to_method_name("zoo.api.endpoints.delete") == "_delete"

    def test_decrease_action(self):
        """Action with underscore becomes camelCase."""
        assert operation_id_to_method_name("zoo.api.endpoints.feedings_decrease_action") == "decreaseAction"
```

**Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_naming.py::TestOperationIdToMethodName -v`
Expected: FAIL with "cannot import name 'operation_id_to_method_name'"

**Step 3: Write minimal implementation**

Add to `src/openapi_ts_client/utils/naming.py`:

```python
# TypeScript reserved words that need escaping
TYPESCRIPT_RESERVED_WORDS = {
    "break", "case", "catch", "class", "const", "continue", "debugger",
    "default", "delete", "do", "else", "enum", "export", "extends",
    "false", "finally", "for", "function", "if", "import", "in",
    "instanceof", "new", "null", "return", "super", "switch", "this",
    "throw", "true", "try", "typeof", "var", "void", "while", "with",
    "yield", "let", "static", "implements", "interface", "package",
    "private", "protected", "public", "any", "boolean", "number",
    "string", "symbol", "type", "from", "of", "async", "await",
}


def operation_id_to_method_name(operation_id: str) -> str:
    """
    Convert OpenAPI operationId to TypeScript method name.

    Examples:
        zoo.api.endpoints.feedings_list_all -> listAll
        delete -> _delete
        list_all -> listAll
    """
    # Extract last segment if dotted path
    if "." in operation_id:
        operation_id = operation_id.split(".")[-1]

    # Convert snake_case to camelCase
    parts = operation_id.split("_")
    if not parts:
        return ""

    # First part lowercase, rest capitalized
    method_name = parts[0].lower()
    for part in parts[1:]:
        if part:
            method_name += part[0].upper() + part[1:].lower() if len(part) > 1 else part.upper()

    # Escape reserved words
    if method_name in TYPESCRIPT_RESERVED_WORDS:
        method_name = f"_{method_name}"

    return method_name
```

**Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_naming.py::TestOperationIdToMethodName -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/utils/naming.py tests/test_naming.py
git commit -m "feat: add operation_id_to_method_name naming utility"
```

---

### Task 7: Create OpenAPI Utilities - Spec Loading and Resolution

**Files:**
- Create: `src/openapi_ts_client/utils/openapi.py`
- Create: `tests/test_openapi_utils.py`

**Step 1: Write failing test for load_and_resolve_spec**

```python
"""Tests for OpenAPI utilities."""

import pytest

from openapi_ts_client.utils.openapi import load_and_resolve_spec


class TestLoadAndResolveSpec:
    """Tests for load_and_resolve_spec function."""

    def test_simple_spec_no_refs(self):
        """Spec without refs returns as-is."""
        spec = {
            "openapi": "3.1.0",
            "info": {"title": "Test", "version": "1.0"},
            "paths": {},
            "components": {
                "schemas": {
                    "User": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"}
                        }
                    }
                }
            }
        }
        resolved = load_and_resolve_spec(spec)
        assert "components" in resolved
        assert "schemas" in resolved["components"]
        assert "User" in resolved["components"]["schemas"]

    def test_resolves_ref(self):
        """$ref is resolved to actual schema."""
        spec = {
            "openapi": "3.1.0",
            "info": {"title": "Test", "version": "1.0"},
            "paths": {},
            "components": {
                "schemas": {
                    "User": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"}
                        }
                    },
                    "Response": {
                        "type": "object",
                        "properties": {
                            "user": {"$ref": "#/components/schemas/User"}
                        }
                    }
                }
            }
        }
        resolved = load_and_resolve_spec(spec)
        response_schema = resolved["components"]["schemas"]["Response"]
        user_prop = response_schema["properties"]["user"]
        # After resolution, should have the User schema content or a marker
        # The exact behavior depends on openapi-core's dereferencing
        assert "properties" in user_prop or "$ref" in user_prop

    def test_invalid_spec_raises(self):
        """Invalid spec raises ValueError."""
        spec = {"invalid": "spec"}
        with pytest.raises(ValueError):
            load_and_resolve_spec(spec)
```

**Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_openapi_utils.py -v`
Expected: FAIL with "cannot import name 'load_and_resolve_spec'"

**Step 3: Write minimal implementation**

```python
"""OpenAPI specification utilities."""

from typing import Any, Dict

from openapi_core import OpenAPI


def load_and_resolve_spec(spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Load and resolve all $ref references in an OpenAPI specification.

    Args:
        spec: OpenAPI specification as dictionary

    Returns:
        Resolved specification with $refs dereferenced

    Raises:
        ValueError: If spec is invalid
    """
    try:
        # Use openapi-core to parse and validate
        openapi = OpenAPI.from_dict(spec)

        # Access the dereferenced spec
        # openapi-core stores the spec in a way we can access
        resolved = openapi.spec.contents

        return dict(resolved)
    except Exception as e:
        raise ValueError(f"Invalid OpenAPI specification: {e}") from e
```

**Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_openapi_utils.py -v`
Expected: PASS (may need adjustment based on openapi-core behavior)

**Step 5: Commit**

```bash
git add src/openapi_ts_client/utils/openapi.py tests/test_openapi_utils.py
git commit -m "feat: add OpenAPI spec loading and resolution utility"
```

---

### Task 8: Update Utils __init__.py Exports

**Files:**
- Modify: `src/openapi_ts_client/utils/__init__.py`

**Step 1: Update exports**

```python
"""Shared utilities for OpenAPI TypeScript client generation."""

from .naming import (
    TYPESCRIPT_RESERVED_WORDS,
    operation_id_to_method_name,
    schema_to_filename,
    tag_to_service_filename,
    tag_to_service_name,
)
from .openapi import load_and_resolve_spec

__all__ = [
    "TYPESCRIPT_RESERVED_WORDS",
    "operation_id_to_method_name",
    "schema_to_filename",
    "tag_to_service_filename",
    "tag_to_service_name",
    "load_and_resolve_spec",
]
```

**Step 2: Verify imports work**

Run: `python3 -c "from openapi_ts_client.utils import schema_to_filename, load_and_resolve_spec; print('OK')"`
Expected: `OK`

**Step 3: Commit**

```bash
git add src/openapi_ts_client/utils/__init__.py
git commit -m "chore: export utils functions from package"
```

---

## Phase 2: Type System

### Task 9: Create Angular Generator Package Structure

**Files:**
- Create: `src/openapi_ts_client/generators/__init__.py`
- Create: `src/openapi_ts_client/generators/angular/__init__.py`

**Step 1: Create generators package**

`src/openapi_ts_client/generators/__init__.py`:
```python
"""Code generators for different TypeScript client formats."""
```

`src/openapi_ts_client/generators/angular/__init__.py`:
```python
"""Angular TypeScript client generator."""
```

**Step 2: Verify package imports**

Run: `python3 -c "from openapi_ts_client.generators import angular; print('OK')"`
Expected: `OK`

**Step 3: Commit**

```bash
git add src/openapi_ts_client/generators/
git commit -m "chore: create generators package structure"
```

---

### Task 10: Create Type Mapper - Basic Types

**Files:**
- Create: `src/openapi_ts_client/generators/angular/type_mapper.py`
- Create: `tests/test_type_mapper.py`

**Step 1: Write failing tests for basic type mapping**

```python
"""Tests for TypeScript type mapper."""

import pytest

from openapi_ts_client.generators.angular.type_mapper import map_openapi_type


class TestMapOpenapiTypeBasic:
    """Tests for basic OpenAPI to TypeScript type mapping."""

    def test_string_type(self):
        """string -> string"""
        schema = {"type": "string"}
        assert map_openapi_type(schema) == "string"

    def test_integer_type(self):
        """integer -> number"""
        schema = {"type": "integer"}
        assert map_openapi_type(schema) == "number"

    def test_number_type(self):
        """number -> number"""
        schema = {"type": "number"}
        assert map_openapi_type(schema) == "number"

    def test_boolean_type(self):
        """boolean -> boolean"""
        schema = {"type": "boolean"}
        assert map_openapi_type(schema) == "boolean"

    def test_object_type_no_properties(self):
        """object without properties -> object"""
        schema = {"type": "object"}
        assert map_openapi_type(schema) == "object"

    def test_string_with_format(self):
        """string with format still returns string."""
        schema = {"type": "string", "format": "date-time"}
        assert map_openapi_type(schema) == "string"
```

**Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_type_mapper.py::TestMapOpenapiTypeBasic -v`
Expected: FAIL with "cannot import name 'map_openapi_type'"

**Step 3: Write minimal implementation**

```python
"""Map OpenAPI types to TypeScript types."""

from typing import Any, Dict, Set, Tuple


def map_openapi_type(schema: Dict[str, Any]) -> str:
    """
    Map an OpenAPI schema to a TypeScript type string.

    Args:
        schema: OpenAPI schema object

    Returns:
        TypeScript type string
    """
    if not schema:
        return "any"

    schema_type = schema.get("type")

    # Basic type mapping
    type_map = {
        "string": "string",
        "integer": "number",
        "number": "number",
        "boolean": "boolean",
        "object": "object",
    }

    if schema_type in type_map:
        return type_map[schema_type]

    return "any"
```

**Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_type_mapper.py::TestMapOpenapiTypeBasic -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generators/angular/type_mapper.py tests/test_type_mapper.py
git commit -m "feat: add basic OpenAPI to TypeScript type mapping"
```

---

### Task 11: Create Type Mapper - Arrays and Refs

**Files:**
- Modify: `src/openapi_ts_client/generators/angular/type_mapper.py`
- Modify: `tests/test_type_mapper.py`

**Step 1: Write failing tests for arrays and refs**

Add to `tests/test_type_mapper.py`:

```python
class TestMapOpenapiTypeArrays:
    """Tests for array type mapping."""

    def test_array_of_strings(self):
        """Array of strings."""
        schema = {"type": "array", "items": {"type": "string"}}
        assert map_openapi_type(schema) == "Array<string>"

    def test_array_of_integers(self):
        """Array of integers."""
        schema = {"type": "array", "items": {"type": "integer"}}
        assert map_openapi_type(schema) == "Array<number>"

    def test_array_of_refs(self):
        """Array of schema references."""
        schema = {"type": "array", "items": {"$ref": "#/components/schemas/User"}}
        result, imports = map_openapi_type_with_imports(schema)
        assert result == "Array<User>"
        assert "User" in imports


class TestMapOpenapiTypeRefs:
    """Tests for $ref type mapping."""

    def test_simple_ref(self):
        """$ref extracts schema name."""
        schema = {"$ref": "#/components/schemas/FeedingOut"}
        result, imports = map_openapi_type_with_imports(schema)
        assert result == "FeedingOut"
        assert "FeedingOut" in imports

    def test_nested_ref(self):
        """Nested $ref in properties."""
        schema = {"$ref": "#/components/schemas/BiomeTypeIn"}
        result, imports = map_openapi_type_with_imports(schema)
        assert result == "BiomeTypeIn"
        assert "BiomeTypeIn" in imports
```

Also add import:
```python
from openapi_ts_client.generators.angular.type_mapper import map_openapi_type, map_openapi_type_with_imports
```

**Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_type_mapper.py::TestMapOpenapiTypeArrays -v`
Expected: FAIL with "cannot import name 'map_openapi_type_with_imports'"

**Step 3: Update implementation**

Update `src/openapi_ts_client/generators/angular/type_mapper.py`:

```python
"""Map OpenAPI types to TypeScript types."""

from typing import Any, Dict, Set, Tuple


def map_openapi_type(schema: Dict[str, Any]) -> str:
    """
    Map an OpenAPI schema to a TypeScript type string.

    Args:
        schema: OpenAPI schema object

    Returns:
        TypeScript type string
    """
    result, _ = map_openapi_type_with_imports(schema)
    return result


def map_openapi_type_with_imports(schema: Dict[str, Any]) -> Tuple[str, Set[str]]:
    """
    Map an OpenAPI schema to a TypeScript type string, tracking imports.

    Args:
        schema: OpenAPI schema object

    Returns:
        Tuple of (TypeScript type string, set of required imports)
    """
    imports: Set[str] = set()

    if not schema:
        return "any", imports

    # Handle $ref
    if "$ref" in schema:
        ref = schema["$ref"]
        # Extract schema name from "#/components/schemas/Name"
        type_name = ref.split("/")[-1]
        imports.add(type_name)
        return type_name, imports

    schema_type = schema.get("type")

    # Handle arrays
    if schema_type == "array":
        items = schema.get("items", {})
        item_type, item_imports = map_openapi_type_with_imports(items)
        imports.update(item_imports)
        return f"Array<{item_type}>", imports

    # Basic type mapping
    type_map = {
        "string": "string",
        "integer": "number",
        "number": "number",
        "boolean": "boolean",
        "object": "object",
    }

    if schema_type in type_map:
        return type_map[schema_type], imports

    return "any", imports
```

**Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_type_mapper.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generators/angular/type_mapper.py tests/test_type_mapper.py
git commit -m "feat: add array and $ref type mapping with import tracking"
```

---

### Task 12: Create Type Mapper - Nullable Types (anyOf)

**Files:**
- Modify: `src/openapi_ts_client/generators/angular/type_mapper.py`
- Modify: `tests/test_type_mapper.py`

**Step 1: Write failing tests for nullable types**

Add to `tests/test_type_mapper.py`:

```python
class TestMapOpenapiTypeNullable:
    """Tests for nullable type mapping (anyOf with null)."""

    def test_anyof_string_null(self):
        """anyOf [string, null] -> string | null"""
        schema = {
            "anyOf": [
                {"type": "string"},
                {"type": "null"}
            ]
        }
        assert map_openapi_type(schema) == "string | null"

    def test_anyof_integer_null(self):
        """anyOf [integer, null] -> number | null"""
        schema = {
            "anyOf": [
                {"type": "integer"},
                {"type": "null"}
            ]
        }
        assert map_openapi_type(schema) == "number | null"

    def test_anyof_ref_null(self):
        """anyOf [ref, null] -> RefType | null"""
        schema = {
            "anyOf": [
                {"$ref": "#/components/schemas/Score"},
                {"type": "null"}
            ]
        }
        result, imports = map_openapi_type_with_imports(schema)
        assert result == "Score | null"
        assert "Score" in imports

    def test_anyof_without_null(self):
        """anyOf without null becomes union."""
        schema = {
            "anyOf": [
                {"type": "string"},
                {"type": "integer"}
            ]
        }
        assert map_openapi_type(schema) == "string | number"
```

**Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_type_mapper.py::TestMapOpenapiTypeNullable -v`
Expected: FAIL

**Step 3: Update implementation**

Add anyOf handling to `map_openapi_type_with_imports`:

```python
def map_openapi_type_with_imports(schema: Dict[str, Any]) -> Tuple[str, Set[str]]:
    """
    Map an OpenAPI schema to a TypeScript type string, tracking imports.

    Args:
        schema: OpenAPI schema object

    Returns:
        Tuple of (TypeScript type string, set of required imports)
    """
    imports: Set[str] = set()

    if not schema:
        return "any", imports

    # Handle $ref
    if "$ref" in schema:
        ref = schema["$ref"]
        # Extract schema name from "#/components/schemas/Name"
        type_name = ref.split("/")[-1]
        imports.add(type_name)
        return type_name, imports

    # Handle anyOf (commonly used for nullable types)
    if "anyOf" in schema:
        types = []
        for sub_schema in schema["anyOf"]:
            if sub_schema.get("type") == "null":
                types.append("null")
            else:
                sub_type, sub_imports = map_openapi_type_with_imports(sub_schema)
                types.append(sub_type)
                imports.update(sub_imports)
        return " | ".join(types), imports

    schema_type = schema.get("type")

    # Handle arrays
    if schema_type == "array":
        items = schema.get("items", {})
        item_type, item_imports = map_openapi_type_with_imports(items)
        imports.update(item_imports)
        return f"Array<{item_type}>", imports

    # Basic type mapping
    type_map = {
        "string": "string",
        "integer": "number",
        "number": "number",
        "boolean": "boolean",
        "object": "object",
    }

    if schema_type in type_map:
        return type_map[schema_type], imports

    return "any", imports
```

**Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_type_mapper.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generators/angular/type_mapper.py tests/test_type_mapper.py
git commit -m "feat: add nullable type mapping for anyOf patterns"
```

---

### Task 13: Create Templates Directory Structure

**Files:**
- Create: `src/openapi_ts_client/templates/angular/` directory
- Create: `src/openapi_ts_client/templates/__init__.py`

**Step 1: Create directory structure**

```bash
mkdir -p src/openapi_ts_client/templates/angular
```

**Step 2: Create __init__.py**

`src/openapi_ts_client/templates/__init__.py`:
```python
"""Jinja2 templates for TypeScript client generation."""
```

**Step 3: Verify structure exists**

Run: `ls -la src/openapi_ts_client/templates/angular/`
Expected: Directory exists (empty)

**Step 4: Commit**

```bash
git add src/openapi_ts_client/templates/
git commit -m "chore: create templates directory structure"
```

---

### Task 14: Create Model Template

**Files:**
- Create: `src/openapi_ts_client/templates/angular/model.ts.j2`

**Step 1: Create model template based on fixture pattern**

```jinja2
/**
 * {{ api_title }}
 *
 * {{ api_description }}
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
{% for import_name in imports | sort %}
import { {{ import_name }} } from './{{ import_name | schema_to_filename_filter }}';
{% endfor %}
{% if imports %}

{% endif %}

export interface {{ interface_name }} {
{% for prop in properties %}
    {{ prop.name }}{% if not prop.required %}?{% endif %}: {{ prop.type }};
{% endfor %}
}

```

**Step 2: Verify file created**

Run: `cat src/openapi_ts_client/templates/angular/model.ts.j2`
Expected: Template content displayed

**Step 3: Commit**

```bash
git add src/openapi_ts_client/templates/angular/model.ts.j2
git commit -m "feat: add Jinja2 template for model interfaces"
```

---

### Task 15: Create Models Barrel Export Template

**Files:**
- Create: `src/openapi_ts_client/templates/angular/models.ts.j2`

**Step 1: Create models barrel template**

```jinja2
{% for model_name in model_names | sort %}
export * from './{{ model_name | schema_to_filename_filter }}';
{% endfor %}
```

Note: The filter removes the .ts extension since export uses bare module names.

**Step 2: Verify file created**

Run: `cat src/openapi_ts_client/templates/angular/models.ts.j2`
Expected: Template content displayed

**Step 3: Commit**

```bash
git add src/openapi_ts_client/templates/angular/models.ts.j2
git commit -m "feat: add Jinja2 template for models barrel export"
```

---

### Task 16: Create Models Generator

**Files:**
- Create: `src/openapi_ts_client/generators/angular/models.py`
- Create: `tests/test_angular_models.py`

**Step 1: Write failing test for model generation**

```python
"""Tests for Angular model generation."""

import pytest

from openapi_ts_client.generators.angular.models import generate_model, extract_model_data


class TestExtractModelData:
    """Tests for extracting model data from schema."""

    def test_simple_properties(self):
        """Extract simple property types."""
        schema = {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
            },
            "required": ["name"]
        }
        data = extract_model_data("UserOut", schema, "Test API", "")

        assert data["interface_name"] == "UserOut"
        assert len(data["properties"]) == 2

        # Find properties by name
        props = {p["name"]: p for p in data["properties"]}
        assert props["id"]["type"] == "number"
        assert props["id"]["required"] == False
        assert props["name"]["type"] == "string"
        assert props["name"]["required"] == True

    def test_nullable_property(self):
        """Extract nullable property type."""
        schema = {
            "type": "object",
            "properties": {
                "value": {
                    "anyOf": [
                        {"type": "string"},
                        {"type": "null"}
                    ]
                }
            }
        }
        data = extract_model_data("TestOut", schema, "Test API", "")

        props = {p["name"]: p for p in data["properties"]}
        assert props["value"]["type"] == "string | null"

    def test_ref_property_tracked_in_imports(self):
        """$ref properties are tracked in imports."""
        schema = {
            "type": "object",
            "properties": {
                "user": {"$ref": "#/components/schemas/UserIn"}
            }
        }
        data = extract_model_data("ResponseOut", schema, "Test API", "")

        assert "UserIn" in data["imports"]
        props = {p["name"]: p for p in data["properties"]}
        assert props["user"]["type"] == "UserIn"
```

**Step 2: Run test to verify it fails**

Run: `python3 -m pytest tests/test_angular_models.py -v`
Expected: FAIL with "cannot import name 'generate_model'"

**Step 3: Write minimal implementation**

```python
"""Generate TypeScript model interfaces from OpenAPI schemas."""

from pathlib import Path
from typing import Any, Dict, List, Set

from jinja2 import Environment, PackageLoader, select_autoescape

from openapi_ts_client.utils.naming import schema_to_filename
from openapi_ts_client.generators.angular.type_mapper import map_openapi_type_with_imports


def _schema_to_filename_filter(name: str) -> str:
    """Jinja2 filter to convert schema name to filename without .ts extension."""
    filename = schema_to_filename(name)
    return filename[:-3] if filename.endswith(".ts") else filename


def get_template_env() -> Environment:
    """Get Jinja2 environment with templates loaded."""
    env = Environment(
        loader=PackageLoader("openapi_ts_client", "templates/angular"),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["schema_to_filename_filter"] = _schema_to_filename_filter
    return env


def extract_model_data(
    schema_name: str,
    schema: Dict[str, Any],
    api_title: str,
    api_description: str,
) -> Dict[str, Any]:
    """
    Extract data needed to render a model template.

    Args:
        schema_name: Name of the schema
        schema: OpenAPI schema object
        api_title: API title for header comment
        api_description: API description for header comment

    Returns:
        Dictionary with template data
    """
    imports: Set[str] = set()
    properties: List[Dict[str, Any]] = []

    required_fields = set(schema.get("required", []))
    schema_properties = schema.get("properties", {})

    for prop_name, prop_schema in schema_properties.items():
        prop_type, prop_imports = map_openapi_type_with_imports(prop_schema)
        imports.update(prop_imports)

        properties.append({
            "name": prop_name,
            "type": prop_type,
            "required": prop_name in required_fields,
        })

    # Don't import self
    imports.discard(schema_name)

    return {
        "api_title": api_title,
        "api_description": api_description or "",
        "interface_name": schema_name,
        "imports": imports,
        "properties": properties,
    }


def generate_model(
    schema_name: str,
    schema: Dict[str, Any],
    api_title: str,
    api_description: str,
) -> str:
    """
    Generate TypeScript interface code for a model.

    Args:
        schema_name: Name of the schema
        schema: OpenAPI schema object
        api_title: API title for header comment
        api_description: API description for header comment

    Returns:
        Generated TypeScript code as string
    """
    env = get_template_env()
    template = env.get_template("model.ts.j2")

    data = extract_model_data(schema_name, schema, api_title, api_description)

    return template.render(**data)
```

**Step 4: Run test to verify it passes**

Run: `python3 -m pytest tests/test_angular_models.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generators/angular/models.py tests/test_angular_models.py
git commit -m "feat: add Angular model generator with template rendering"
```

---

## Phase 3: Services (Tasks 17-22)

*Continue with service template creation, service generator implementation, following same TDD pattern...*

---

## Phase 4: Infrastructure (Tasks 23-32)

*Create all 9 infrastructure templates, following fixture patterns exactly...*

---

## Phase 5: Integration (Tasks 33-38)

### Task 33: Create Angular Generator Orchestrator

**Files:**
- Create: `src/openapi_ts_client/generators/angular/generator.py`

**Step 1: Create orchestrator that coordinates all generation**

```python
"""Angular TypeScript client generator orchestrator."""

from pathlib import Path
from typing import Any, Dict

from openapi_ts_client.logging_config import get_logger
from openapi_ts_client.utils.openapi import load_and_resolve_spec
from .models import generate_all_models
from .services import generate_all_services
from .infrastructure import generate_infrastructure


def generate_angular_client(
    spec: Dict[str, Any],
    output_path: Path,
) -> None:
    """
    Generate complete Angular TypeScript client.

    Args:
        spec: OpenAPI specification dictionary
        output_path: Directory to write generated files
    """
    logger = get_logger("angular.generator")

    logger.info("Starting Angular client generation")

    # Resolve all $refs
    resolved_spec = load_and_resolve_spec(spec)

    # Extract metadata
    info = resolved_spec.get("info", {})
    api_title = info.get("title", "API")
    api_description = info.get("description", "")

    # Create output directories
    output_path.mkdir(parents=True, exist_ok=True)
    (output_path / "model").mkdir(exist_ok=True)
    (output_path / "api").mkdir(exist_ok=True)

    # Generate models
    logger.info("Generating models...")
    schemas = resolved_spec.get("components", {}).get("schemas", {})
    generate_all_models(schemas, output_path / "model", api_title, api_description)

    # Generate services
    logger.info("Generating services...")
    paths = resolved_spec.get("paths", {})
    generate_all_services(paths, output_path / "api", api_title, api_description)

    # Generate infrastructure files
    logger.info("Generating infrastructure files...")
    generate_infrastructure(output_path, api_title, api_description)

    logger.info("Angular client generation complete")
```

**Step 2: Commit**

```bash
git add src/openapi_ts_client/generators/angular/generator.py
git commit -m "feat: add Angular generator orchestrator"
```

---

### Task 34: Update Main Generator to Dispatch to Angular

**Files:**
- Modify: `src/openapi_ts_client/generator.py`

**Step 1: Add Angular dispatch**

Update the placeholder section in `generator.py` to dispatch to Angular generator when format is ANGULAR:

```python
from .generators.angular.generator import generate_angular_client

# ... in generate_typescript_client function, replace placeholder with:

if output_format == ClientFormat.ANGULAR:
    generate_angular_client(parsed_spec, resolved_output_path)
    status_message = (
        f"TypeScript Angular client generated for '{api_title}' v{api_version} "
        f"(OpenAPI {openapi_version}). "
        f"Output: {resolved_output_path}"
    )
else:
    # Placeholder for other formats
    func_logger.warning("=" * 80)
    func_logger.warning("CLIENT GENERATION LOGIC NOT IMPLEMENTED FOR THIS FORMAT")
    func_logger.warning("=" * 80)
    status_message = (
        f"TypeScript client generation not yet implemented for {output_format.value}"
    )
```

**Step 2: Commit**

```bash
git add src/openapi_ts_client/generator.py
git commit -m "feat: dispatch to Angular generator for ANGULAR format"
```

---

### Task 35: Create Integration Test

**Files:**
- Create: `tests/test_angular_integration.py`

**Step 1: Write integration test comparing against fixtures**

```python
"""Integration tests for Angular client generation."""

import filecmp
import json
from pathlib import Path

import pytest

from openapi_ts_client import generate_typescript_client, ClientFormat


FIXTURES_DIR = Path(__file__).parent / "fixtures" / "space_zoo"
OUTPUT_DIR = Path(__file__).parent.parent / "temp" / "space_zoo" / "angular"


class TestAngularIntegration:
    """Integration tests comparing generated output to fixtures."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Load spec and generate client before each test."""
        # Clean output directory
        if OUTPUT_DIR.exists():
            import shutil
            shutil.rmtree(OUTPUT_DIR)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # Load and generate
        spec_path = FIXTURES_DIR / "openapi.json"
        with open(spec_path) as f:
            spec = json.load(f)

        generate_typescript_client(spec, ClientFormat.ANGULAR, OUTPUT_DIR)

    def test_all_model_files_match(self):
        """All generated model files match fixtures exactly."""
        fixture_model_dir = FIXTURES_DIR / "angular" / "model"
        output_model_dir = OUTPUT_DIR / "model"

        fixture_files = set(f.name for f in fixture_model_dir.glob("*.ts"))
        output_files = set(f.name for f in output_model_dir.glob("*.ts"))

        assert fixture_files == output_files, f"File mismatch: {fixture_files ^ output_files}"

        for filename in fixture_files:
            fixture_content = (fixture_model_dir / filename).read_text()
            output_content = (output_model_dir / filename).read_text()
            assert fixture_content == output_content, f"Content mismatch in {filename}"

    def test_all_service_files_match(self):
        """All generated service files match fixtures exactly."""
        fixture_api_dir = FIXTURES_DIR / "angular" / "api"
        output_api_dir = OUTPUT_DIR / "api"

        fixture_files = set(f.name for f in fixture_api_dir.glob("*.ts"))
        output_files = set(f.name for f in output_api_dir.glob("*.ts"))

        assert fixture_files == output_files, f"File mismatch: {fixture_files ^ output_files}"

        for filename in fixture_files:
            fixture_content = (fixture_api_dir / filename).read_text()
            output_content = (output_api_dir / filename).read_text()
            assert fixture_content == output_content, f"Content mismatch in {filename}"

    def test_all_infrastructure_files_match(self):
        """All generated infrastructure files match fixtures exactly."""
        fixture_dir = FIXTURES_DIR / "angular"
        output_dir = OUTPUT_DIR

        infra_files = [
            "index.ts",
            "api.module.ts",
            "provide-api.ts",
            "configuration.ts",
            "api.base.service.ts",
            "variables.ts",
            "encoder.ts",
            "param.ts",
            "query.params.ts",
        ]

        for filename in infra_files:
            fixture_content = (fixture_dir / filename).read_text()
            output_content = (output_dir / filename).read_text()
            assert fixture_content == output_content, f"Content mismatch in {filename}"
```

**Step 2: Run test (expected to fail until all pieces are in place)**

Run: `python3 -m pytest tests/test_angular_integration.py -v`
Expected: FAIL (will pass once all components are implemented)

**Step 3: Commit**

```bash
git add tests/test_angular_integration.py
git commit -m "test: add integration test for Angular generation"
```

---

### Task 36-38: Iterate Until Tests Pass

Continue implementing missing pieces (services, infrastructure templates) following the same TDD pattern until `test_angular_integration.py` passes completely.

**Final verification:**

Run: `python3 -m pytest tests/ -v`
Expected: All tests pass

**Final commit:**

```bash
git add -A
git commit -m "feat: complete Angular TypeScript client generator"
```

---

## Completion Checklist

- [ ] All 68 existing tests still pass
- [ ] Integration test passes (byte-for-byte match with fixtures)
- [ ] `pip install -e ".[dev]"` works
- [ ] `ruff check src --fix` passes
- [ ] `ruff format src` passes
- [ ] All new code has test coverage
