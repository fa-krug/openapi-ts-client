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
