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