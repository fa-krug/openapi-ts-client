# Fetch Client Generator Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement a Fetch-based TypeScript client generator that passes all fixture tests against `tests/fixtures/space_zoo/fetch/`.

**Architecture:** Create a new `generators/fetch/` module mirroring the Angular generator structure, with shared utilities extracted to `generators/shared/`. Uses Jinja2 templates for all TypeScript output.

**Tech Stack:** Python 3.13, Jinja2, pytest

---

## Task 1: Create Shared Utilities Module

**Files:**
- Create: `src/openapi_ts_client/generators/shared/__init__.py`
- Create: `src/openapi_ts_client/generators/shared/type_mapper.py`
- Create: `src/openapi_ts_client/generators/shared/anyof_extractor.py`
- Modify: `src/openapi_ts_client/generators/angular/models.py`
- Modify: `src/openapi_ts_client/generators/angular/services.py`
- Modify: `src/openapi_ts_client/generators/angular/type_mapper.py`

**Step 1: Create shared module directory**

```bash
mkdir -p src/openapi_ts_client/generators/shared
```

**Step 2: Create shared __init__.py**

Create `src/openapi_ts_client/generators/shared/__init__.py`:
```python
"""Shared utilities for TypeScript client generators."""

from .type_mapper import map_openapi_type, map_openapi_type_with_imports
from .anyof_extractor import create_extraction_registry

__all__ = [
    "map_openapi_type",
    "map_openapi_type_with_imports",
    "create_extraction_registry",
]
```

**Step 3: Copy type_mapper to shared**

```bash
cp src/openapi_ts_client/generators/angular/type_mapper.py src/openapi_ts_client/generators/shared/type_mapper.py
```

**Step 4: Copy anyof_extractor to shared**

```bash
cp src/openapi_ts_client/generators/angular/anyof_extractor.py src/openapi_ts_client/generators/shared/anyof_extractor.py
```

**Step 5: Update Angular imports to use shared utilities**

In `src/openapi_ts_client/generators/angular/models.py`, change:
```python
from .anyof_extractor import create_extraction_registry
from .type_mapper import map_openapi_type_with_imports
```
to:
```python
from openapi_ts_client.generators.shared import create_extraction_registry, map_openapi_type_with_imports
```

In `src/openapi_ts_client/generators/angular/services.py`, change:
```python
from openapi_ts_client.generators.angular.type_mapper import map_openapi_type_with_imports
```
to:
```python
from openapi_ts_client.generators.shared import map_openapi_type_with_imports
```

**Step 6: Update Angular type_mapper.py to re-export from shared**

Replace `src/openapi_ts_client/generators/angular/type_mapper.py` contents:
```python
"""Angular type mapper - re-exports from shared for backwards compatibility."""

from openapi_ts_client.generators.shared.type_mapper import (
    map_openapi_type,
    map_openapi_type_with_imports,
)

__all__ = ["map_openapi_type", "map_openapi_type_with_imports"]
```

**Step 7: Update Angular anyof_extractor.py to re-export from shared**

Replace `src/openapi_ts_client/generators/angular/anyof_extractor.py` contents:
```python
"""Angular anyof extractor - re-exports from shared for backwards compatibility."""

from openapi_ts_client.generators.shared.anyof_extractor import (
    create_extraction_registry,
)

__all__ = ["create_extraction_registry"]
```

**Step 8: Run tests to verify no regressions**

```bash
pytest tests/ -v
```

Expected: All 132 tests pass.

**Step 9: Commit**

```bash
git add src/openapi_ts_client/generators/shared/ src/openapi_ts_client/generators/angular/
git commit -m "refactor: extract shared utilities from angular generator

Move type_mapper.py and anyof_extractor.py to generators/shared/
for reuse by fetch generator. Angular imports updated to use
shared module with backwards-compatible re-exports.

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>"
```

---

## Task 2: Create Fetch Generator Module Structure

**Files:**
- Create: `src/openapi_ts_client/generators/fetch/__init__.py`
- Create: `src/openapi_ts_client/generators/fetch/generator.py`
- Create: `src/openapi_ts_client/templates/fetch/` directory

**Step 1: Create fetch module directory**

```bash
mkdir -p src/openapi_ts_client/generators/fetch
mkdir -p src/openapi_ts_client/templates/fetch
```

**Step 2: Create fetch __init__.py**

Create `src/openapi_ts_client/generators/fetch/__init__.py`:
```python
"""Fetch TypeScript client generator."""

from .generator import generate_fetch_client

__all__ = ["generate_fetch_client"]
```

**Step 3: Create generator.py stub**

Create `src/openapi_ts_client/generators/fetch/generator.py`:
```python
"""Fetch TypeScript client generator orchestrator."""

from pathlib import Path
from typing import Any, Dict

from openapi_ts_client.logging_config import get_logger
from openapi_ts_client.utils.openapi import load_and_resolve_spec


def generate_fetch_client(
    spec: Dict[str, Any],
    output_path: Path,
) -> None:
    """
    Generate complete Fetch TypeScript client.

    Args:
        spec: OpenAPI specification dictionary
        output_path: Directory to write generated files
    """
    logger = get_logger("fetch.generator")

    logger.info("Starting Fetch client generation")

    # Resolve all $refs
    resolved_spec = load_and_resolve_spec(spec)

    # Create output directories
    output_path.mkdir(parents=True, exist_ok=True)
    (output_path / "models").mkdir(exist_ok=True)
    (output_path / "apis").mkdir(exist_ok=True)
    (output_path / "docs").mkdir(exist_ok=True)

    # TODO: Generate runtime.ts
    # TODO: Generate models
    # TODO: Generate APIs
    # TODO: Generate docs
    # TODO: Generate barrel exports

    logger.info("Fetch client generation complete")
```

**Step 4: Run tests to verify module imports work**

```bash
python -c "from openapi_ts_client.generators.fetch import generate_fetch_client; print('OK')"
```

Expected: "OK"

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generators/fetch/ src/openapi_ts_client/templates/fetch/
git commit -m "feat(fetch): add fetch generator module structure

Create generators/fetch/ module with stub orchestrator.
Create templates/fetch/ directory for Jinja2 templates.

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>"
```

---

## Task 3: Implement runtime.ts Generation

**Files:**
- Create: `src/openapi_ts_client/templates/fetch/runtime.ts.j2`
- Create: `src/openapi_ts_client/generators/fetch/runtime.py`
- Modify: `src/openapi_ts_client/generators/fetch/generator.py`

**Step 1: Create runtime.ts.j2 template**

Copy the fixture file and add template variables at the top:

Create `src/openapi_ts_client/templates/fetch/runtime.ts.j2` with content from `tests/fixtures/space_zoo/fetch/runtime.ts`, replacing lines 3-13:
```jinja2
/* tslint:disable */
/* eslint-disable */
/**
 * {{ api_title }}
 * {{ api_description }}
 *
 * The version of the OpenAPI document: {{ api_version }}
 * {% if contact_email %}Contact: {{ contact_email }}{% endif %}
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
```

And replace line 16:
```jinja2
export const BASE_PATH = "{{ base_path }}".replace(/\/+$/, "");
```

**Step 2: Create runtime.py module**

Create `src/openapi_ts_client/generators/fetch/runtime.py`:
```python
"""Generate Fetch runtime.ts file."""

from pathlib import Path

from jinja2 import Environment, PackageLoader


def _create_jinja_env() -> Environment:
    """Create Jinja2 environment for fetch templates."""
    return Environment(
        loader=PackageLoader("openapi_ts_client", "templates/fetch"),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )


def generate_runtime(
    output_path: Path,
    api_title: str,
    api_description: str,
    api_version: str,
    base_path: str,
    contact_email: str = "",
) -> None:
    """
    Generate runtime.ts file.

    Args:
        output_path: Directory to write runtime.ts
        api_title: API title from spec
        api_description: API description from spec
        api_version: API version from spec
        base_path: Base URL from spec servers
        contact_email: Contact email from spec
    """
    env = _create_jinja_env()
    template = env.get_template("runtime.ts.j2")

    content = template.render(
        api_title=api_title,
        api_description=api_description,
        api_version=api_version,
        base_path=base_path,
        contact_email=contact_email,
    )

    (output_path / "runtime.ts").write_text(content)
```

**Step 3: Update generator.py to use runtime generation**

Update `src/openapi_ts_client/generators/fetch/generator.py`:
```python
"""Fetch TypeScript client generator orchestrator."""

from pathlib import Path
from typing import Any, Dict

from openapi_ts_client.logging_config import get_logger
from openapi_ts_client.utils.openapi import load_and_resolve_spec
from .runtime import generate_runtime


def generate_fetch_client(
    spec: Dict[str, Any],
    output_path: Path,
) -> None:
    """
    Generate complete Fetch TypeScript client.

    Args:
        spec: OpenAPI specification dictionary
        output_path: Directory to write generated files
    """
    logger = get_logger("fetch.generator")

    logger.info("Starting Fetch client generation")

    # Resolve all $refs
    resolved_spec = load_and_resolve_spec(spec)

    # Extract metadata
    info = resolved_spec.get("info", {})
    api_title = info.get("title", "API")
    api_description = info.get("description", "")
    api_version = info.get("version", "")
    contact = info.get("contact", {})
    contact_email = contact.get("email", "")

    # Extract base path from servers
    servers = resolved_spec.get("servers", [])
    base_path = servers[0].get("url", "http://localhost") if servers else "http://localhost"

    # Create output directories
    output_path.mkdir(parents=True, exist_ok=True)
    (output_path / "models").mkdir(exist_ok=True)
    (output_path / "apis").mkdir(exist_ok=True)
    (output_path / "docs").mkdir(exist_ok=True)

    # Generate runtime.ts
    logger.info("Generating runtime.ts...")
    generate_runtime(
        output_path,
        api_title=api_title,
        api_description=api_description,
        api_version=api_version,
        base_path=base_path,
        contact_email=contact_email,
    )

    # TODO: Generate models
    # TODO: Generate APIs
    # TODO: Generate docs
    # TODO: Generate barrel exports

    logger.info("Fetch client generation complete")
```

**Step 4: Test runtime generation manually**

```bash
python -c "
import json
import tempfile
from pathlib import Path
from openapi_ts_client.generators.fetch import generate_fetch_client

spec = json.load(open('tests/fixtures/space_zoo/openapi.json'))
with tempfile.TemporaryDirectory() as tmpdir:
    generate_fetch_client(spec, Path(tmpdir))
    runtime = Path(tmpdir) / 'runtime.ts'
    print('Generated:', runtime.exists())
    print('First 5 lines:')
    for line in runtime.read_text().split('\n')[:5]:
        print(line)
"
```

Expected: Shows generated runtime.ts with correct header.

**Step 5: Commit**

```bash
git add src/openapi_ts_client/generators/fetch/runtime.py src/openapi_ts_client/templates/fetch/runtime.ts.j2 src/openapi_ts_client/generators/fetch/generator.py
git commit -m "feat(fetch): implement runtime.ts generation

Add Jinja2 template for runtime.ts with configurable header.
Wire up runtime generation in fetch generator orchestrator.

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>"
```

---

## Task 4: Implement Model Generation (Part 1 - Basic Interface)

**Files:**
- Create: `src/openapi_ts_client/templates/fetch/model.ts.j2`
- Create: `src/openapi_ts_client/generators/fetch/models.py`
- Create: `tests/test_fetch_models.py`

**Step 1: Write failing test for basic model generation**

Create `tests/test_fetch_models.py`:
```python
"""Tests for fetch model generation."""

import pytest


def test_generate_simple_model_interface():
    """Test generating a simple model interface."""
    from openapi_ts_client.generators.fetch.models import generate_model_content

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
        },
        "required": ["name"],
    }

    content = generate_model_content(
        schema_name="SimpleModel",
        schema=schema,
        api_title="Test API",
        api_version="1.0.0",
        registry={},
    )

    assert "export interface SimpleModel" in content
    assert "id?: number" in content
    assert "name: string" in content
```

**Step 2: Run test to verify it fails**

```bash
pytest tests/test_fetch_models.py::test_generate_simple_model_interface -v
```

Expected: FAIL with "cannot import name 'generate_model_content'"

**Step 3: Create model.ts.j2 template**

Create `src/openapi_ts_client/templates/fetch/model.ts.j2`:
```jinja2
/* tslint:disable */
/* eslint-disable */
/**
 * {{ api_title }}
 * {{ api_description }}
 *
 * The version of the OpenAPI document: {{ api_version }}
 * {% if contact_email %}Contact: {{ contact_email }}{% endif %}
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
{% for import_name in type_imports %}
import type { {{ import_name }} } from './{{ import_name }}';
import {
    {{ import_name }}FromJSON,
    {{ import_name }}FromJSONTyped,
    {{ import_name }}ToJSON,
    {{ import_name }}ToJSONTyped,
} from './{{ import_name }}';
{% endfor %}
/**
 * {% if description %}{{ description }}{% endif %}
 * @export
 * @interface {{ interface_name }}
 */
export interface {{ interface_name }} {
{% for prop in properties %}
    /**
     * {% if prop.description %}{{ prop.description }}{% endif %}
     * @type {{ '{' }}{{ prop.ts_type }}{{ '}' }}
     * @memberof {{ interface_name }}
     */
    {{ prop.name }}{% if not prop.required %}?{% endif %}: {{ prop.ts_type }};
{% endfor %}
}

/**
 * Check if a given object implements the {{ interface_name }} interface.
 */
export function instanceOf{{ interface_name }}(value: object): value is {{ interface_name }} {
{% if required_properties %}
{% for prop in required_properties %}
    if (!('{{ prop.json_name }}' in value) || value['{{ prop.json_name }}'] === undefined) return false;
{% endfor %}
{% endif %}
    return true;
}

export function {{ interface_name }}FromJSON(json: any): {{ interface_name }} {
    return {{ interface_name }}FromJSONTyped(json, false);
}

export function {{ interface_name }}FromJSONTyped(json: any, ignoreDiscriminator: boolean): {{ interface_name }} {
    if (json == null) {
        return json;
    }
    return {
        {% for prop in properties %}
        '{{ prop.name }}': {{ prop.from_json_expr }},
        {% endfor %}
    };
}

export function {{ interface_name }}ToJSON(json: any): {{ interface_name }} {
    return {{ interface_name }}ToJSONTyped(json, false);
}

export function {{ interface_name }}ToJSONTyped(value?: {{ interface_name }} | null, ignoreDiscriminator: boolean = false): any {
    if (value == null) {
        return value;
    }

    return {
        {% for prop in properties %}
        '{{ prop.json_name }}': {{ prop.to_json_expr }},
        {% endfor %}
    };
}
```

**Step 4: Create models.py module**

Create `src/openapi_ts_client/generators/fetch/models.py`:
```python
"""Generate Fetch TypeScript model files from OpenAPI schemas."""

import re
from pathlib import Path
from typing import Any, Dict, List, Set

from jinja2 import Environment, PackageLoader

from openapi_ts_client.generators.shared import map_openapi_type_with_imports
from openapi_ts_client.utils import schema_to_filename


def _create_jinja_env() -> Environment:
    """Create Jinja2 environment for fetch templates."""
    return Environment(
        loader=PackageLoader("openapi_ts_client", "templates/fetch"),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )


def _to_camel_case(name: str) -> str:
    """Convert snake_case to camelCase."""
    parts = re.split(r"[_-]", name)
    if not parts:
        return name
    return parts[0] + "".join(word.title() for word in parts[1:])


def _get_property_info(
    prop_name: str,
    prop_schema: Dict[str, Any],
    required_props: List[str],
    registry: Dict[str, Dict[str, Any]],
) -> Dict[str, Any]:
    """Get property information for template rendering."""
    ts_type, imports = map_openapi_type_with_imports(prop_schema, registry)
    is_required = prop_name in required_props

    # Convert snake_case JSON name to camelCase TypeScript name
    ts_name = _to_camel_case(prop_name)

    # Determine if this is a date type
    schema_type = prop_schema.get("type")
    schema_format = prop_schema.get("format")
    is_date = schema_type == "string" and schema_format in ("date", "date-time")
    is_date_only = schema_format == "date"

    # Check for nullable
    is_nullable = False
    if "anyOf" in prop_schema:
        is_nullable = any(s.get("type") == "null" for s in prop_schema["anyOf"])

    # Build FromJSON expression
    if is_nullable or not is_required:
        if is_date:
            from_json = f"json['{prop_name}'] == null ? undefined : (new Date(json['{prop_name}']))"
        elif imports:
            # Nested type
            nested_type = list(imports)[0]
            from_json = f"json['{prop_name}'] == null ? undefined : {nested_type}FromJSON(json['{prop_name}'])"
        else:
            from_json = f"json['{prop_name}'] == null ? undefined : json['{prop_name}']"
    else:
        if is_date:
            from_json = f"(new Date(json['{prop_name}']))"
        elif imports:
            nested_type = list(imports)[0]
            from_json = f"{nested_type}FromJSON(json['{prop_name}'])"
        else:
            from_json = f"json['{prop_name}']"

    # Build ToJSON expression
    if is_date:
        if is_nullable or not is_required:
            if is_date_only:
                to_json = f"value['{ts_name}'] == null ? value['{ts_name}'] : value['{ts_name}'].toISOString().substring(0,10)"
            else:
                to_json = f"value['{ts_name}'] == null ? value['{ts_name}'] : value['{ts_name}'].toISOString()"
        else:
            if is_date_only:
                to_json = f"value['{ts_name}'].toISOString().substring(0,10)"
            else:
                to_json = f"value['{ts_name}'].toISOString()"
    elif imports:
        nested_type = list(imports)[0]
        to_json = f"{nested_type}ToJSON(value['{ts_name}'])"
    else:
        to_json = f"value['{ts_name}']"

    # Handle type with nullable
    display_type = ts_type
    if is_nullable and "| null" not in ts_type:
        display_type = f"{ts_type} | null"

    return {
        "name": ts_name,
        "json_name": prop_name,
        "ts_type": display_type,
        "required": is_required,
        "description": prop_schema.get("description", ""),
        "imports": imports,
        "from_json_expr": from_json,
        "to_json_expr": to_json,
    }


def generate_model_content(
    schema_name: str,
    schema: Dict[str, Any],
    api_title: str,
    api_version: str,
    registry: Dict[str, Dict[str, Any]],
    api_description: str = "",
    contact_email: str = "",
) -> str:
    """
    Generate content for a single model file.

    Args:
        schema_name: Name of the schema (e.g., "FeedingOut")
        schema: The schema definition
        api_title: API title for the header
        api_version: API version for the header
        registry: Extraction registry for titled anyOf schemas
        api_description: API description for the header
        contact_email: Contact email for the header

    Returns:
        Generated TypeScript content
    """
    env = _create_jinja_env()
    template = env.get_template("model.ts.j2")

    properties = schema.get("properties", {})
    required_props = schema.get("required", [])

    # Build property info list
    prop_infos = []
    all_imports: Set[str] = set()
    required_properties = []

    for prop_name, prop_schema in properties.items():
        info = _get_property_info(prop_name, prop_schema, required_props, registry)
        prop_infos.append(info)
        all_imports.update(info["imports"])
        if info["required"]:
            required_properties.append(info)

    # Sort imports
    sorted_imports = sorted(all_imports)

    return template.render(
        api_title=api_title,
        api_description=api_description,
        api_version=api_version,
        contact_email=contact_email,
        interface_name=schema_name,
        description=schema.get("description", ""),
        type_imports=sorted_imports,
        properties=prop_infos,
        required_properties=required_properties,
    )
```

**Step 5: Run test to verify it passes**

```bash
pytest tests/test_fetch_models.py::test_generate_simple_model_interface -v
```

Expected: PASS

**Step 6: Commit**

```bash
git add src/openapi_ts_client/generators/fetch/models.py src/openapi_ts_client/templates/fetch/model.ts.j2 tests/test_fetch_models.py
git commit -m "feat(fetch): implement basic model generation

Add model.ts.j2 template and models.py with generate_model_content.
Includes interface, instanceOf, FromJSON, and ToJSON functions.

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>"
```

---

## Task 5: Implement Model Generation (Part 2 - Full Model Generation)

**Files:**
- Modify: `src/openapi_ts_client/generators/fetch/models.py`
- Create: `src/openapi_ts_client/templates/fetch/models_index.ts.j2`
- Modify: `src/openapi_ts_client/generators/fetch/generator.py`

**Step 1: Add generate_models function to models.py**

Add to `src/openapi_ts_client/generators/fetch/models.py`:
```python
def generate_models(
    spec: Dict[str, Any],
    output_dir: Path,
    api_title: str,
    api_version: str,
    api_description: str = "",
    contact_email: str = "",
) -> List[str]:
    """
    Generate all model files from an OpenAPI spec.

    Args:
        spec: OpenAPI specification dict
        output_dir: Directory to write model files to
        api_title: API title for headers
        api_version: API version for headers
        api_description: API description for headers
        contact_email: Contact email for headers

    Returns:
        List of generated model filenames (without extension)
    """
    from openapi_ts_client.generators.shared import create_extraction_registry

    schemas = spec.get("components", {}).get("schemas", {})
    registry = create_extraction_registry(spec)
    env = _create_jinja_env()

    model_filenames = []

    # Generate extracted type files first
    generated_types = set()
    for _path, info in registry.items():
        type_name = info["type_name"]
        if type_name not in generated_types:
            content = _generate_extracted_type_content(
                type_name=type_name,
                description=info["description"],
                api_title=api_title,
                api_version=api_version,
                api_description=api_description,
                contact_email=contact_email,
            )
            filename = schema_to_filename(type_name)
            (output_dir / filename).write_text(content)
            model_filenames.append(filename[:-3])  # Remove .ts
            generated_types.add(type_name)

    # Generate schema model files
    for schema_name, schema in schemas.items():
        content = generate_model_content(
            schema_name=schema_name,
            schema=schema,
            api_title=api_title,
            api_version=api_version,
            registry=registry,
            api_description=api_description,
            contact_email=contact_email,
        )
        filename = schema_to_filename(schema_name)
        (output_dir / filename).write_text(content)
        model_filenames.append(filename[:-3])

    # Generate barrel export
    barrel_template = env.get_template("models_index.ts.j2")
    barrel_content = barrel_template.render(model_filenames=sorted(model_filenames))
    (output_dir / "index.ts").write_text(barrel_content)

    return model_filenames


def _generate_extracted_type_content(
    type_name: str,
    description: str,
    api_title: str,
    api_version: str,
    api_description: str = "",
    contact_email: str = "",
) -> str:
    """Generate an empty interface file for an extracted anyOf type."""
    env = _create_jinja_env()
    template = env.get_template("extracted_type.ts.j2")

    return template.render(
        api_title=api_title,
        api_description=api_description,
        api_version=api_version,
        contact_email=contact_email,
        interface_name=type_name,
        description=description,
    )
```

**Step 2: Create models_index.ts.j2 template**

Create `src/openapi_ts_client/templates/fetch/models_index.ts.j2`:
```jinja2
/* tslint:disable */
/* eslint-disable */
{% for filename in model_filenames %}
export * from './{{ filename }}';
{% endfor %}
```

**Step 3: Create extracted_type.ts.j2 template**

Create `src/openapi_ts_client/templates/fetch/extracted_type.ts.j2`:
```jinja2
/* tslint:disable */
/* eslint-disable */
/**
 * {{ api_title }}
 * {{ api_description }}
 *
 * The version of the OpenAPI document: {{ api_version }}
 * {% if contact_email %}Contact: {{ contact_email }}{% endif %}
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
/**
 * {% if description %}{{ description }}{% endif %}
 * @export
 * @interface {{ interface_name }}
 */
export interface {{ interface_name }} {
}

/**
 * Check if a given object implements the {{ interface_name }} interface.
 */
export function instanceOf{{ interface_name }}(value: object): value is {{ interface_name }} {
    return true;
}

export function {{ interface_name }}FromJSON(json: any): {{ interface_name }} {
    return {{ interface_name }}FromJSONTyped(json, false);
}

export function {{ interface_name }}FromJSONTyped(json: any, ignoreDiscriminator: boolean): {{ interface_name }} {
    return json;
}

export function {{ interface_name }}ToJSON(json: any): {{ interface_name }} {
    return {{ interface_name }}ToJSONTyped(json, false);
}

export function {{ interface_name }}ToJSONTyped(value?: {{ interface_name }} | null, ignoreDiscriminator: boolean = false): any {
    return value;
}
```

**Step 4: Update generator.py to use model generation**

Update `src/openapi_ts_client/generators/fetch/generator.py` to add model generation:
```python
from .models import generate_models

# In generate_fetch_client, after runtime generation:
    # Generate models
    logger.info("Generating models...")
    generate_models(
        spec=resolved_spec,
        output_dir=output_path / "models",
        api_title=api_title,
        api_version=api_version,
        api_description=api_description,
        contact_email=contact_email,
    )
```

**Step 5: Run test generation and compare one model**

```bash
python -c "
import json
import tempfile
from pathlib import Path
from openapi_ts_client.generators.fetch import generate_fetch_client

spec = json.load(open('tests/fixtures/space_zoo/openapi.json'))
with tempfile.TemporaryDirectory() as tmpdir:
    generate_fetch_client(spec, Path(tmpdir))
    print('Models generated:', len(list((Path(tmpdir) / 'models').glob('*.ts'))))
"
```

**Step 6: Commit**

```bash
git add src/openapi_ts_client/generators/fetch/models.py src/openapi_ts_client/generators/fetch/generator.py src/openapi_ts_client/templates/fetch/*.j2
git commit -m "feat(fetch): implement full model generation

Add generate_models function, extracted type generation,
and models index barrel export.

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>"
```

---

## Task 6: Implement API Generation

**Files:**
- Create: `src/openapi_ts_client/templates/fetch/api.ts.j2`
- Create: `src/openapi_ts_client/templates/fetch/apis_index.ts.j2`
- Create: `src/openapi_ts_client/generators/fetch/apis.py`
- Modify: `src/openapi_ts_client/generators/fetch/generator.py`

**Step 1: Create api.ts.j2 template**

Create `src/openapi_ts_client/templates/fetch/api.ts.j2` based on the fixture patterns observed in `FeedingsApi.ts`.

**Step 2: Create apis_index.ts.j2 template**

Create `src/openapi_ts_client/templates/fetch/apis_index.ts.j2`:
```jinja2
/* tslint:disable */
/* eslint-disable */
{% for api_name in api_names %}
export * from './{{ api_name }}';
{% endfor %}
```

**Step 3: Create apis.py module**

Create `src/openapi_ts_client/generators/fetch/apis.py` with logic to:
- Group operations by tag
- Generate request interfaces for each method
- Generate API class with raw and convenience methods
- Handle parameter validation, query building, path substitution

**Step 4: Wire up to generator.py**

**Step 5: Test and iterate against fixtures**

**Step 6: Commit**

---

## Task 7: Implement Documentation Generation

**Files:**
- Create: `src/openapi_ts_client/templates/fetch/doc.md.j2`
- Create: `src/openapi_ts_client/generators/fetch/docs.py`
- Modify: `src/openapi_ts_client/generators/fetch/generator.py`

**Step 1: Create doc.md.j2 template**

Based on the fixture `docs/EnclosureOut.md`.

**Step 2: Create docs.py module**

**Step 3: Wire up to generator.py**

**Step 4: Test against fixtures**

**Step 5: Commit**

---

## Task 8: Implement Root index.ts and Wire to Main Generator

**Files:**
- Create: `src/openapi_ts_client/templates/fetch/index.ts.j2`
- Modify: `src/openapi_ts_client/generators/fetch/generator.py`
- Modify: `src/openapi_ts_client/generator.py`

**Step 1: Create index.ts.j2 template**

```jinja2
/* tslint:disable */
/* eslint-disable */
export * from './runtime';
export * from './apis/index';
export * from './models/index';
```

**Step 2: Generate index.ts in generator.py**

**Step 3: Wire fetch generator to main generator.py**

Update `src/openapi_ts_client/generator.py` to call `generate_fetch_client` when format is FETCH.

**Step 4: Run full fixture comparison tests**

**Step 5: Commit**

---

## Task 9: Fix Fixture Comparison Failures

**Files:** Various, based on test failures

**Step 1: Run fixture comparison test**

```bash
pytest tests/test_fixture_comparison.py -v
```

**Step 2: Identify differences**

For each failing comparison, diff the generated file against the fixture to identify:
- Whitespace issues
- Property ordering
- Missing/extra content
- Incorrect type mappings

**Step 3: Fix template or generation logic**

**Step 4: Re-run tests until all pass**

**Step 5: Commit fixes**

---

## Task 10: Final Verification and Cleanup

**Step 1: Run full test suite**

```bash
pytest tests/ -v
```

Expected: All tests pass.

**Step 2: Run linting**

```bash
ruff check src --fix
ruff format src
```

**Step 3: Final commit**

```bash
git add .
git commit -m "feat(fetch): complete fetch client generator

All fixture comparison tests passing.
Fetch client generator fully implemented with:
- runtime.ts generation
- Model generation with serialization
- API class generation
- Documentation generation
- Barrel exports

Generated with [Claude Code](https://claude.ai/code)
via [Happy](https://happy.engineering)

Co-Authored-By: Claude <noreply@anthropic.com>
Co-Authored-By: Happy <yesreply@happy.engineering>"
```
