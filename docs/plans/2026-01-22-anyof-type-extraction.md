# anyOf Type Extraction Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Extract anyOf schemas with `title` properties as separate empty interface model files to match openapi-generator behavior exactly.

**Architecture:** Create a discovery module that scans the entire OpenAPI spec for titled anyOf schemas, assigns unique type names (with numeric suffixes for duplicates), then integrates with the model generator to produce empty interface files and update type references.

**Tech Stack:** Python, Jinja2 templates, pytest

---

### Task 1: Create anyof_extractor module with discovery function

**Files:**
- Create: `src/openapi_ts_client/generators/angular/anyof_extractor.py`
- Test: `tests/test_anyof_extractor.py`

**Step 1: Write the failing test for discovery**

```python
# tests/test_anyof_extractor.py
"""Tests for anyOf type extraction."""

from openapi_ts_client.generators.angular.anyof_extractor import discover_titled_anyofs


class TestDiscoverTitledAnyofs:
    """Tests for discovering titled anyOf schemas."""

    def test_finds_titled_anyof_in_schema_properties(self):
        """Finds anyOf with title in schema properties."""
        spec = {
            "components": {
                "schemas": {
                    "TestSchema": {
                        "properties": {
                            "score": {
                                "anyOf": [{"type": "number"}, {"type": "string"}],
                                "title": "Score",
                                "description": "A score value",
                            }
                        }
                    }
                }
            }
        }
        discoveries = discover_titled_anyofs(spec)
        assert len(discoveries) == 1
        assert discoveries[0]["title"] == "Score"
        assert discoveries[0]["description"] == "A score value"

    def test_ignores_anyof_without_title(self):
        """Ignores anyOf schemas that lack a title."""
        spec = {
            "components": {
                "schemas": {
                    "TestSchema": {
                        "properties": {
                            "value": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                            }
                        }
                    }
                }
            }
        }
        discoveries = discover_titled_anyofs(spec)
        assert len(discoveries) == 0

    def test_finds_titled_anyof_in_parameters(self):
        """Finds anyOf with title in operation parameters."""
        spec = {
            "paths": {
                "/api/test": {
                    "get": {
                        "parameters": [
                            {
                                "name": "score",
                                "in": "query",
                                "schema": {
                                    "anyOf": [{"type": "number"}, {"type": "null"}],
                                    "title": "Score",
                                },
                            }
                        ]
                    }
                }
            }
        }
        discoveries = discover_titled_anyofs(spec)
        assert len(discoveries) == 1
        assert discoveries[0]["title"] == "Score"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_anyof_extractor.py -v`
Expected: FAIL with "ModuleNotFoundError" or "ImportError"

**Step 3: Write minimal implementation**

```python
# src/openapi_ts_client/generators/angular/anyof_extractor.py
"""Extract anyOf schemas with titles as separate type definitions."""

from typing import Any, Dict, List


def discover_titled_anyofs(spec: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Recursively scan OpenAPI spec for anyOf schemas with title properties.

    Args:
        spec: OpenAPI specification dict

    Returns:
        List of discoveries, each containing:
        - path: JSON path to the schema
        - title: The title value
        - description: Optional description
        - schema: The full anyOf schema
    """
    discoveries: List[Dict[str, Any]] = []
    _scan_for_titled_anyofs(spec, "", discoveries)
    return discoveries


def _scan_for_titled_anyofs(
    obj: Any, path: str, discoveries: List[Dict[str, Any]]
) -> None:
    """Recursively scan object for titled anyOf schemas."""
    if isinstance(obj, dict):
        # Check if this is a titled anyOf
        if "anyOf" in obj and "title" in obj:
            discoveries.append({
                "path": path,
                "title": obj["title"],
                "description": obj.get("description", ""),
                "schema": obj,
            })
        # Recurse into children
        for key, value in obj.items():
            _scan_for_titled_anyofs(value, f"{path}/{key}", discoveries)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            _scan_for_titled_anyofs(item, f"{path}[{i}]", discoveries)
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_anyof_extractor.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generators/angular/anyof_extractor.py tests/test_anyof_extractor.py
git commit -m "feat(angular): add anyof discovery function"
```

---

### Task 2: Add name assignment with duplicate handling

**Files:**
- Modify: `src/openapi_ts_client/generators/angular/anyof_extractor.py`
- Modify: `tests/test_anyof_extractor.py`

**Step 1: Write the failing test for name assignment**

```python
# Add to tests/test_anyof_extractor.py
from openapi_ts_client.generators.angular.anyof_extractor import (
    discover_titled_anyofs,
    assign_type_names,
)


class TestAssignTypeNames:
    """Tests for assigning unique type names."""

    def test_converts_title_to_pascal_case(self):
        """Converts space-separated titles to PascalCase."""
        discoveries = [
            {"path": "/a", "title": "Code Duplication", "description": "", "schema": {}},
        ]
        registry = assign_type_names(discoveries, set())
        assert registry["/a"]["type_name"] == "CodeDuplication"

    def test_assigns_numeric_suffix_for_duplicates(self):
        """Second occurrence of same title gets numeric suffix."""
        discoveries = [
            {"path": "/a", "title": "Score", "description": "", "schema": {}},
            {"path": "/b", "title": "Score", "description": "", "schema": {}},
            {"path": "/c", "title": "Score", "description": "", "schema": {}},
        ]
        registry = assign_type_names(discoveries, set())
        assert registry["/a"]["type_name"] == "Score"
        assert registry["/b"]["type_name"] == "Score1"
        assert registry["/c"]["type_name"] == "Score2"

    def test_conflict_with_existing_schema_gets_suffix(self):
        """Title conflicting with existing schema name gets suffix."""
        discoveries = [
            {"path": "/a", "title": "User", "description": "", "schema": {}},
        ]
        existing_schemas = {"User"}
        registry = assign_type_names(discoveries, existing_schemas)
        assert registry["/a"]["type_name"] == "User1"

    def test_deterministic_ordering_by_path(self):
        """Assignments are deterministic based on path sorting."""
        discoveries = [
            {"path": "/z/prop", "title": "Score", "description": "", "schema": {}},
            {"path": "/a/prop", "title": "Score", "description": "", "schema": {}},
        ]
        registry = assign_type_names(discoveries, set())
        # /a comes before /z alphabetically
        assert registry["/a/prop"]["type_name"] == "Score"
        assert registry["/z/prop"]["type_name"] == "Score1"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_anyof_extractor.py::TestAssignTypeNames -v`
Expected: FAIL with "ImportError" or "cannot import name 'assign_type_names'"

**Step 3: Write minimal implementation**

```python
# Add to src/openapi_ts_client/generators/angular/anyof_extractor.py

def assign_type_names(
    discoveries: List[Dict[str, Any]], existing_schemas: set
) -> Dict[str, Dict[str, Any]]:
    """
    Assign unique type names to discovered titled anyOf schemas.

    Args:
        discoveries: List from discover_titled_anyofs()
        existing_schemas: Set of schema names already defined in components/schemas

    Returns:
        Registry mapping path -> {type_name, title, description, schema}
    """
    # Sort by path for deterministic ordering
    sorted_discoveries = sorted(discoveries, key=lambda d: d["path"])

    # Track used names (include existing schemas)
    used_names: set = set(existing_schemas)
    registry: Dict[str, Dict[str, Any]] = {}

    for discovery in sorted_discoveries:
        base_name = _title_to_pascal_case(discovery["title"])
        type_name = _get_unique_name(base_name, used_names)
        used_names.add(type_name)

        registry[discovery["path"]] = {
            "type_name": type_name,
            "title": discovery["title"],
            "description": discovery["description"],
            "schema": discovery["schema"],
        }

    return registry


def _title_to_pascal_case(title: str) -> str:
    """Convert a title like 'Code Duplication' to 'CodeDuplication'."""
    return "".join(word.capitalize() for word in title.split())


def _get_unique_name(base_name: str, used_names: set) -> str:
    """Get a unique name, adding numeric suffix if needed."""
    if base_name not in used_names:
        return base_name

    counter = 1
    while f"{base_name}{counter}" in used_names:
        counter += 1
    return f"{base_name}{counter}"
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_anyof_extractor.py::TestAssignTypeNames -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generators/angular/anyof_extractor.py tests/test_anyof_extractor.py
git commit -m "feat(angular): add name assignment with duplicate handling"
```

---

### Task 3: Add registry creation entry point

**Files:**
- Modify: `src/openapi_ts_client/generators/angular/anyof_extractor.py`
- Modify: `tests/test_anyof_extractor.py`

**Step 1: Write the failing test**

```python
# Add to tests/test_anyof_extractor.py
from openapi_ts_client.generators.angular.anyof_extractor import (
    discover_titled_anyofs,
    assign_type_names,
    create_extraction_registry,
)


class TestCreateExtractionRegistry:
    """Tests for the main entry point."""

    def test_creates_registry_from_spec(self):
        """Creates complete registry from OpenAPI spec."""
        spec = {
            "components": {
                "schemas": {
                    "ExistingSchema": {"type": "object"},
                    "TestSchema": {
                        "properties": {
                            "score": {
                                "anyOf": [{"type": "number"}],
                                "title": "Score",
                            }
                        }
                    },
                }
            }
        }
        registry = create_extraction_registry(spec)
        # Should have one entry for the titled anyOf
        assert len(registry) == 1
        path = "/components/schemas/TestSchema/properties/score"
        assert path in registry
        assert registry[path]["type_name"] == "Score"

    def test_returns_empty_for_spec_without_titled_anyofs(self):
        """Returns empty registry when no titled anyOf schemas exist."""
        spec = {"components": {"schemas": {}}}
        registry = create_extraction_registry(spec)
        assert registry == {}
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_anyof_extractor.py::TestCreateExtractionRegistry -v`
Expected: FAIL with "ImportError"

**Step 3: Write minimal implementation**

```python
# Add to src/openapi_ts_client/generators/angular/anyof_extractor.py

def create_extraction_registry(spec: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Main entry point: discover titled anyOf schemas and assign type names.

    Args:
        spec: OpenAPI specification dict

    Returns:
        Registry mapping JSON path -> {type_name, title, description, schema}
    """
    discoveries = discover_titled_anyofs(spec)
    if not discoveries:
        return {}

    existing_schemas = set(spec.get("components", {}).get("schemas", {}).keys())
    return assign_type_names(discoveries, existing_schemas)
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_anyof_extractor.py::TestCreateExtractionRegistry -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generators/angular/anyof_extractor.py tests/test_anyof_extractor.py
git commit -m "feat(angular): add create_extraction_registry entry point"
```

---

### Task 4: Create empty interface template for extracted types

**Files:**
- Create: `src/openapi_ts_client/templates/angular/extracted_type.ts.j2`
- Test: Manual inspection (template file)

**Step 1: Write the template file**

The template must match the fixture format exactly (note the specific whitespace):

```jinja2
{# src/openapi_ts_client/templates/angular/extracted_type.ts.j2 #}
/**
 * {{ api_title }}
 *
 * {{ 'Contact: ' + contact_email if contact_email else '' }}
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

{% if description %}
/**
 * {{ description }}
 */
{% endif %}
export interface {{ interface_name }} {
}

```

**Step 2: Verify template exists**

Run: `ls -la src/openapi_ts_client/templates/angular/extracted_type.ts.j2`
Expected: File exists

**Step 3: Commit**

```bash
git add src/openapi_ts_client/templates/angular/extracted_type.ts.j2
git commit -m "feat(angular): add extracted type template"
```

---

### Task 5: Add function to generate extracted type files

**Files:**
- Modify: `src/openapi_ts_client/generators/angular/models.py`
- Create: `tests/test_extracted_types.py`

**Step 1: Write the failing test**

```python
# tests/test_extracted_types.py
"""Tests for extracted type file generation."""

from pathlib import Path

from openapi_ts_client.generators.angular.models import generate_extracted_type_file


class TestGenerateExtractedTypeFile:
    """Tests for generating extracted type files."""

    def test_generates_empty_interface(self, tmp_path: Path):
        """Generates empty interface file for extracted type."""
        output_dir = tmp_path / "model"
        output_dir.mkdir()

        generate_extracted_type_file(
            type_name="Score",
            description="",
            output_dir=output_dir,
            api_title="Test API",
            contact_email="",
        )

        output_file = output_dir / "score.ts"
        assert output_file.exists()
        content = output_file.read_text()
        assert "export interface Score {" in content

    def test_includes_description_as_jsdoc(self, tmp_path: Path):
        """Includes description as JSDoc comment when provided."""
        output_dir = tmp_path / "model"
        output_dir.mkdir()

        generate_extracted_type_file(
            type_name="CodeDuplication",
            description="Percentage of code duplications in main branch",
            output_dir=output_dir,
            api_title="Test API",
            contact_email="",
        )

        output_file = output_dir / "codeDuplication.ts"
        content = output_file.read_text()
        assert "Percentage of code duplications in main branch" in content
        assert "export interface CodeDuplication {" in content
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_extracted_types.py -v`
Expected: FAIL with "ImportError" or "cannot import name 'generate_extracted_type_file'"

**Step 3: Write minimal implementation**

```python
# Add to src/openapi_ts_client/generators/angular/models.py

def generate_extracted_type_file(
    type_name: str,
    description: str,
    output_dir: Path,
    api_title: str,
    contact_email: str,
) -> str:
    """
    Generate an empty interface file for an extracted anyOf type.

    Args:
        type_name: PascalCase type name (e.g., "Score", "CodeDuplication")
        description: Optional description for JSDoc
        output_dir: Directory to write the file
        api_title: API title for header
        contact_email: Contact email for header

    Returns:
        Filename without extension (for barrel export)
    """
    env = _create_jinja_env()
    template = env.get_template("extracted_type.ts.j2")

    content = template.render(
        api_title=api_title,
        contact_email=contact_email,
        interface_name=type_name,
        description=description,
    )

    filename = schema_to_filename(type_name)
    filename_without_ext = filename[:-3]

    output_file = output_dir / filename
    output_file.write_text(content)

    return filename_without_ext
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_extracted_types.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generators/angular/models.py tests/test_extracted_types.py
git commit -m "feat(angular): add generate_extracted_type_file function"
```

---

### Task 6: Integrate extraction into model generation

**Files:**
- Modify: `src/openapi_ts_client/generators/angular/models.py`

**Step 1: Write the failing test**

```python
# Add to tests/test_extracted_types.py
import json
from pathlib import Path

from openapi_ts_client.generators.angular.models import generate_models


class TestGenerateModelsWithExtraction:
    """Tests for model generation with anyOf extraction."""

    def test_generates_extracted_type_files(self, tmp_path: Path):
        """Generates separate files for titled anyOf schemas."""
        spec = {
            "info": {"title": "Test API"},
            "components": {
                "schemas": {
                    "TestSchema": {
                        "properties": {
                            "score": {
                                "anyOf": [{"type": "number"}, {"type": "string"}],
                                "title": "Score",
                                "description": "A score value",
                            }
                        }
                    }
                }
            },
        }

        generate_models(spec, tmp_path)

        # Should generate both testSchema.ts and score.ts
        assert (tmp_path / "testSchema.ts").exists()
        assert (tmp_path / "score.ts").exists()

        # score.ts should be an empty interface with description
        score_content = (tmp_path / "score.ts").read_text()
        assert "export interface Score {" in score_content
        assert "A score value" in score_content

    def test_extracted_types_in_barrel_export(self, tmp_path: Path):
        """Extracted types are included in models.ts barrel export."""
        spec = {
            "info": {"title": "Test API"},
            "components": {
                "schemas": {
                    "TestSchema": {
                        "properties": {
                            "score": {
                                "anyOf": [{"type": "number"}],
                                "title": "Score",
                            }
                        }
                    }
                }
            },
        }

        generate_models(spec, tmp_path)

        barrel = (tmp_path / "models.ts").read_text()
        assert "export * from './score';" in barrel
        assert "export * from './testSchema';" in barrel
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_extracted_types.py::TestGenerateModelsWithExtraction -v`
Expected: FAIL (score.ts not generated)

**Step 3: Modify generate_all_models to integrate extraction**

```python
# Modify generate_models in src/openapi_ts_client/generators/angular/models.py

from .anyof_extractor import create_extraction_registry


def generate_models(spec: Dict[str, Any], output_dir: Path) -> None:
    """
    Generate all model files from an OpenAPI spec.

    Args:
        spec: OpenAPI specification dict
        output_dir: Directory to write model files to
    """
    api_title = spec.get("info", {}).get("title", "")
    contact_email = spec.get("info", {}).get("contact", {}).get("email", "")
    schemas = spec.get("components", {}).get("schemas", {})

    # Create extraction registry for titled anyOf schemas
    registry = create_extraction_registry(spec)

    generate_all_models(schemas, output_dir, api_title, contact_email, registry)


def generate_all_models(
    schemas: Dict[str, Any],
    output_dir: Path,
    api_title: str,
    contact_email: str,
    registry: Dict[str, Dict[str, Any]] = None,
) -> None:
    """
    Generate all model files from schemas.

    Args:
        schemas: OpenAPI schemas dict
        output_dir: Directory to write model files to
        api_title: API title for header comments
        contact_email: Contact email for header comments
        registry: Optional extraction registry for titled anyOf schemas
    """
    if registry is None:
        registry = {}

    env = _create_jinja_env()

    # Add the schema_to_filename_filter to the environment
    def _schema_to_filename_filter(name: str) -> str:
        """Jinja2 filter to convert schema name to filename without .ts extension."""
        filename = schema_to_filename(name)
        return filename[:-3] if filename.endswith(".ts") else filename

    env.filters["schema_to_filename_filter"] = _schema_to_filename_filter

    model_filenames = []

    # Generate extracted type files first
    generated_types = set()
    for path, info in registry.items():
        type_name = info["type_name"]
        if type_name not in generated_types:
            filename = generate_extracted_type_file(
                type_name=type_name,
                description=info["description"],
                output_dir=output_dir,
                api_title=api_title,
                contact_email=contact_email,
            )
            model_filenames.append(filename)
            generated_types.add(type_name)

    # Generate schema model files
    for schema_name, schema in schemas.items():
        content = _generate_model_file(
            env, schema_name, schema, api_title, contact_email
        )

        filename = schema_to_filename(schema_name)
        filename_without_ext = filename[:-3]

        model_filenames.append(filename_without_ext)

        output_file = output_dir / filename
        output_file.write_text(content)

    # Generate barrel export (models.ts)
    barrel_template = env.get_template("models.ts.j2")
    barrel_content = barrel_template.render(
        model_filenames=sorted(model_filenames)
    )
    (output_dir / "models.ts").write_text(barrel_content)
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_extracted_types.py::TestGenerateModelsWithExtraction -v`
Expected: PASS

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generators/angular/models.py
git commit -m "feat(angular): integrate anyOf extraction into model generation"
```

---

### Task 7: Update type mapper to use extraction registry

**Files:**
- Modify: `src/openapi_ts_client/generators/angular/type_mapper.py`
- Modify: `tests/test_type_mapper.py`

**Step 1: Write the failing test**

```python
# Add to tests/test_type_mapper.py

class TestMapOpenapiTypeWithRegistry:
    """Tests for type mapping with extraction registry."""

    def test_titled_anyof_uses_extracted_type(self):
        """Titled anyOf returns extracted type name from registry."""
        schema = {
            "anyOf": [{"type": "number"}, {"type": "string"}],
            "title": "Score",
        }
        registry = {
            "test/path": {
                "type_name": "Score",
                "title": "Score",
                "description": "",
                "schema": schema,
            }
        }
        # Need to pass registry and match by schema identity
        result, imports = map_openapi_type_with_imports(schema, registry)
        assert result == "Score"
        assert "Score" in imports

    def test_untitled_anyof_still_inlines(self):
        """anyOf without title still produces inline union."""
        schema = {
            "anyOf": [{"type": "string"}, {"type": "null"}],
        }
        result, imports = map_openapi_type_with_imports(schema, {})
        assert result == "string | null"
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_type_mapper.py::TestMapOpenapiTypeWithRegistry -v`
Expected: FAIL (TypeError about registry parameter)

**Step 3: Modify type_mapper to accept registry**

```python
# Modify src/openapi_ts_client/generators/angular/type_mapper.py

"""Map OpenAPI types to TypeScript types."""

from typing import Any, Dict, Optional, Set, Tuple


def map_openapi_type(
    schema: Dict[str, Any], registry: Optional[Dict[str, Dict[str, Any]]] = None
) -> str:
    """
    Map an OpenAPI schema to a TypeScript type string.

    Args:
        schema: OpenAPI schema object
        registry: Optional extraction registry for titled anyOf lookups

    Returns:
        TypeScript type string
    """
    result, _ = map_openapi_type_with_imports(schema, registry)
    return result


def map_openapi_type_with_imports(
    schema: Dict[str, Any], registry: Optional[Dict[str, Dict[str, Any]]] = None
) -> Tuple[str, Set[str]]:
    """
    Map an OpenAPI schema to a TypeScript type string, tracking imports.

    Args:
        schema: OpenAPI schema object
        registry: Optional extraction registry for titled anyOf lookups

    Returns:
        Tuple of (TypeScript type string, set of required imports)
    """
    if registry is None:
        registry = {}

    imports: Set[str] = set()

    if not schema:
        return "any", imports

    # Handle $ref
    if "$ref" in schema:
        ref = schema["$ref"]
        type_name = ref.split("/")[-1]
        imports.add(type_name)
        return type_name, imports

    # Handle anyOf (commonly used for nullable types)
    if "anyOf" in schema:
        # Check if this is a titled anyOf that should use extracted type
        if "title" in schema:
            type_name = _lookup_extracted_type(schema, registry)
            if type_name:
                imports.add(type_name)
                return type_name, imports

        # Fall back to inline union
        types = []
        for sub_schema in schema["anyOf"]:
            if sub_schema.get("type") == "null":
                types.append("null")
            else:
                sub_type, sub_imports = map_openapi_type_with_imports(sub_schema, registry)
                types.append(sub_type)
                imports.update(sub_imports)
        return " | ".join(types), imports

    schema_type = schema.get("type")

    # Handle arrays
    if schema_type == "array":
        items = schema.get("items", {})
        item_type, item_imports = map_openapi_type_with_imports(items, registry)
        imports.update(item_imports)
        return f"Array<{item_type}>", imports

    # Handle object with additionalProperties (map types)
    if schema_type == "object" and "additionalProperties" in schema:
        additional_props = schema["additionalProperties"]
        if additional_props and isinstance(additional_props, dict):
            value_type, value_imports = map_openapi_type_with_imports(additional_props, registry)
            imports.update(value_imports)
            return f"{{ [key: string]: {value_type}; }}", imports

    # Handle enum types (string or integer with enum values)
    if "enum" in schema:
        enum_values = schema["enum"]
        if schema_type == "string":
            return " | ".join(f"'{v}'" for v in enum_values), imports
        elif schema_type in ("integer", "number"):
            return " | ".join(str(v) for v in enum_values), imports

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


def _lookup_extracted_type(
    schema: Dict[str, Any], registry: Dict[str, Dict[str, Any]]
) -> Optional[str]:
    """
    Look up extracted type name for a schema in the registry.

    Matches by schema object identity (same dict instance).

    Args:
        schema: The schema to look up
        registry: The extraction registry

    Returns:
        Type name if found, None otherwise
    """
    for info in registry.values():
        if info["schema"] is schema:
            return info["type_name"]
    return None
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_type_mapper.py::TestMapOpenapiTypeWithRegistry -v`
Expected: PASS

**Step 5: Run all type mapper tests to ensure no regression**

Run: `pytest tests/test_type_mapper.py -v`
Expected: All PASS

**Step 6: Commit**

```bash
git add src/openapi_ts_client/generators/angular/type_mapper.py tests/test_type_mapper.py
git commit -m "feat(angular): update type mapper to use extraction registry"
```

---

### Task 8: Pass registry through model generation

**Files:**
- Modify: `src/openapi_ts_client/generators/angular/models.py`

**Step 1: Write the failing test**

```python
# Add to tests/test_extracted_types.py

class TestModelPropertyReferences:
    """Tests for model properties referencing extracted types."""

    def test_property_references_extracted_type(self, tmp_path: Path):
        """Property with titled anyOf references the extracted type."""
        spec = {
            "info": {"title": "Test API"},
            "components": {
                "schemas": {
                    "TestSchema": {
                        "properties": {
                            "score": {
                                "anyOf": [{"type": "number"}, {"type": "string"}],
                                "title": "Score",
                            }
                        }
                    }
                }
            },
        }

        generate_models(spec, tmp_path)

        # testSchema.ts should reference Score, not inline number | string
        content = (tmp_path / "testSchema.ts").read_text()
        assert "score?: Score;" in content
        assert "import { Score } from './score';" in content
        assert "number | string" not in content
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_extracted_types.py::TestModelPropertyReferences -v`
Expected: FAIL (property still inlines as `number | string`)

**Step 3: Modify _get_property_info to accept registry**

```python
# Modify src/openapi_ts_client/generators/angular/models.py

def _get_property_info(
    prop_name: str,
    prop_schema: Dict[str, Any],
    required_props: List[str],
    interface_name: str,
    registry: Dict[str, Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get property information for template rendering.

    Args:
        prop_name: The property name
        prop_schema: The property schema
        required_props: List of required property names
        interface_name: Name of the parent interface (for enum type references)
        registry: Optional extraction registry for titled anyOf lookups

    Returns:
        Dict with name, type, required status, and enum info
    """
    if registry is None:
        registry = {}

    enum_values = prop_schema.get("enum")
    description = prop_schema.get("description", "")

    if enum_values:
        # Enum property - type references the namespace
        enum_name = prop_name[0].upper() + prop_name[1:] + "Enum"
        ts_type = f"{interface_name}.{enum_name}"
        imports = set()

        return {
            "name": prop_name,
            "type": ts_type,
            "required": prop_name in required_props,
            "imports": imports,
            "description": description,
            "is_enum": True,
            "enum_name": enum_name,
            "enum_values": enum_values,
        }

    # Non-enum property - pass registry for titled anyOf lookups
    ts_type, imports = map_openapi_type_with_imports(prop_schema, registry)
    return {
        "name": prop_name,
        "type": ts_type,
        "required": prop_name in required_props,
        "imports": imports,
        "description": description,
        "is_enum": False,
        "enum_name": None,
        "enum_values": None,
    }
```

**Step 4: Modify _generate_model_file to pass registry**

```python
# Modify _generate_model_file in src/openapi_ts_client/generators/angular/models.py

def _generate_model_file(
    env: Environment,
    schema_name: str,
    schema: Dict[str, Any],
    api_title: str,
    contact_email: str,
    registry: Dict[str, Dict[str, Any]] = None,
) -> str:
    """
    Generate a single model file content.

    Args:
        env: Jinja2 environment
        schema_name: Name of the schema (e.g., "FeedingOut")
        schema: The schema definition
        api_title: API title for the header
        contact_email: Contact email for the header
        registry: Optional extraction registry for titled anyOf lookups

    Returns:
        Generated TypeScript content
    """
    if registry is None:
        registry = {}

    template = env.get_template("model.ts.j2")

    properties = schema.get("properties", {})
    required_props = schema.get("required", [])

    # Build property info list preserving schema order
    prop_infos = []
    all_imports = set()
    enums = []

    for prop_name, prop_schema in properties.items():
        info = _get_property_info(
            prop_name, prop_schema, required_props, schema_name, registry
        )
        prop_infos.append(info)
        all_imports.update(info["imports"])

        if info["is_enum"]:
            enums.append({
                "name": info["enum_name"],
                "enum_values": info["enum_values"],
            })

    # Sort imports alphabetically
    sorted_imports = sorted(all_imports)

    return template.render(
        api_title=api_title,
        contact_email=contact_email,
        interface_name=schema_name,
        imports=sorted_imports,
        properties=prop_infos,
        enums=enums,
    )
```

**Step 5: Update generate_all_models to pass registry to _generate_model_file**

```python
# In generate_all_models, change the call to _generate_model_file:

    # Generate schema model files
    for schema_name, schema in schemas.items():
        content = _generate_model_file(
            env, schema_name, schema, api_title, contact_email, registry
        )
        # ... rest unchanged
```

**Step 6: Run test to verify it passes**

Run: `pytest tests/test_extracted_types.py::TestModelPropertyReferences -v`
Expected: PASS

**Step 7: Commit**

```bash
git add src/openapi_ts_client/generators/angular/models.py
git commit -m "feat(angular): pass registry through model generation"
```

---

### Task 9: Run fixture comparison test

**Files:**
- None (verification only)

**Step 1: Run the space_zoo fixture comparison test**

Run: `pytest tests/test_fixture_comparison.py::test_angular_generation_matches_fixture[space_zoo] -v`

**Step 2: Analyze any failures**

If test fails with "Missing files", check which of the 9 files are still missing.
If test fails with "MISMATCH", examine the diff to understand what's different.

**Step 3: Iterate if needed**

If there are failures, create additional tasks to address them. Common issues:
- Whitespace differences in template
- Import ordering differences
- Description formatting differences

**Step 4: Commit once tests pass**

```bash
git add -A
git commit -m "fix(angular): ensure fixture comparison passes"
```

---

### Task 10: Run full test suite

**Files:**
- None (verification only)

**Step 1: Run all tests**

Run: `pytest -v`
Expected: All PASS

**Step 2: Run linting**

Run: `ruff check src tests --fix && ruff format src tests`

**Step 3: Final commit**

```bash
git add -A
git commit -m "chore: lint and format"
```

---

## Summary

This plan implements anyOf type extraction in 10 tasks:

1. **Discovery function** - Scan spec for titled anyOf schemas
2. **Name assignment** - Handle duplicates with numeric suffixes
3. **Registry entry point** - Main API for extraction
4. **Template** - Empty interface Jinja2 template
5. **File generation** - Generate extracted type files
6. **Integration** - Hook into model generation
7. **Type mapper** - Use registry for type resolution
8. **Registry threading** - Pass registry through generation
9. **Fixture verification** - Ensure space_zoo matches
10. **Full test suite** - Final verification

Each task is self-contained with TDD approach: failing test → implementation → passing test → commit.
