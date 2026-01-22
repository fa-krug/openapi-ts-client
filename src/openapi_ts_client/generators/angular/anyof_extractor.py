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
