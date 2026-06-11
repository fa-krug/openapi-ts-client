"""OpenAPI specification utilities."""

import json
from typing import Any, Dict

from openapi_core import Config, OpenAPI


def sanitize_spec(node: Any) -> Any:
    """Coerce schema literals whose value doesn't match their declared type.

    Django Ninja (via Pydantic v2) renders ``Decimal`` model fields as
    ``{"type": "string", "pattern": ...}`` because decimals are serialized as
    strings to preserve precision. The field's ``default``/``example`` is,
    however, emitted as a JSON *number* (e.g. ``0.0``), yielding a node that is
    internally inconsistent::

        {"type": "string", "pattern": "...", "default": 0.0}

    Strict OpenAPI validators (openapi-core / openapi-spec-validator) reject
    this with "0.0 is not of type 'string'". Because the serialized value really
    is a string, we coerce these literals to their string form, which makes the
    schema *correct*, not merely valid.

    The walk is recursive and covers ``components.schemas``, ``paths``,
    parameters, and nested ``anyOf``/``allOf``/``items``/``properties`` — anywhere
    a string-typed node can appear. The node is mutated in place and returned.

    Args:
        node: An OpenAPI specification (or any sub-node of one).

    Returns:
        The same node, with inconsistent string literals coerced.
    """
    if isinstance(node, dict):
        if node.get("type") == "string":
            for key in ("default", "example"):
                value = node.get(key)
                if value is not None and not isinstance(value, str):
                    node[key] = str(value)
            examples = node.get("examples")
            if isinstance(examples, list):
                node["examples"] = [
                    str(v) if v is not None and not isinstance(v, str) else v for v in examples
                ]
        for value in node.values():
            sanitize_spec(value)
    elif isinstance(node, list):
        for item in node:
            sanitize_spec(item)
    return node


def _normalize_spec(spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize an OpenAPI specification to ensure all dictionary keys are strings.

    Django Ninja's get_openapi_schema() returns integer keys for HTTP status codes
    (e.g., 200, 404) instead of string keys ("200", "404"). The OpenAPI specification
    requires these to be strings, and jsonschema validation fails with integer keys.

    This function performs a JSON round-trip to convert all keys to strings,
    which is the standard behavior when serializing to JSON.

    Args:
        spec: OpenAPI specification dictionary (may contain integer keys)

    Returns:
        Normalized specification with all keys as strings
    """
    return json.loads(json.dumps(spec))


def load_and_resolve_spec(spec: Dict[str, Any], skip_validation: bool = False) -> Dict[str, Any]:
    """
    Load and resolve all $ref references in an OpenAPI specification.

    Args:
        spec: OpenAPI specification as dictionary
        skip_validation: If True, construct the spec without running strict
            OpenAPI validation. openapi-core validates by default even when only
            $ref resolution is wanted, so this is the only way to honor a
            caller's ``skip_validation`` request on the resolution path.

    Returns:
        Resolved specification with $refs dereferenced

    Raises:
        ValueError: If spec is invalid
    """
    try:
        # Normalize the spec to ensure all keys are strings
        # This handles Django Ninja which uses integer keys for status codes
        normalized_spec = _normalize_spec(spec)

        # Coerce literals whose value doesn't match their declared type
        # (e.g. Pydantic Decimal fields: string type with a numeric default).
        sanitize_spec(normalized_spec)

        # Use openapi-core to parse (and, unless skipped, validate). Passing
        # spec_validator_cls=None disables validation while still resolving refs.
        config = Config(spec_validator_cls=None) if skip_validation else None
        openapi = OpenAPI.from_dict(normalized_spec, config)

        # Access the spec contents
        resolved = openapi.spec.read_value()

        return dict(resolved)
    except Exception as e:
        raise ValueError(f"Invalid OpenAPI specification: {e}") from e
