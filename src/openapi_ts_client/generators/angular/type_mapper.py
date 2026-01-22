"""Map OpenAPI types to TypeScript types."""

from typing import Any, Dict


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
