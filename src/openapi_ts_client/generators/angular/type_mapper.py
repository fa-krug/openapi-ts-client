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

    # Handle object with additionalProperties (map types)
    if schema_type == "object" and "additionalProperties" in schema:
        additional_props = schema["additionalProperties"]
        if additional_props and isinstance(additional_props, dict):
            value_type, value_imports = map_openapi_type_with_imports(additional_props)
            imports.update(value_imports)
            return f"{{ [key: string]: {value_type}; }}", imports

    # Handle enum types (string or integer with enum values)
    if "enum" in schema:
        enum_values = schema["enum"]
        if schema_type == "string":
            # String enum - create union of string literals
            return " | ".join(f"'{v}'" for v in enum_values), imports
        elif schema_type in ("integer", "number"):
            # Numeric enum - create union of number literals
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
