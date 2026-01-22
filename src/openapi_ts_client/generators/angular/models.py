"""Generate Angular TypeScript model files from OpenAPI schemas."""

from pathlib import Path
from typing import Any, Dict, List

from jinja2 import Environment, PackageLoader

from openapi_ts_client.utils import schema_to_filename
from .type_mapper import map_openapi_type_with_imports


def _lower_first(s: str) -> str:
    """Convert first character to lowercase."""
    if not s:
        return s
    return s[0].lower() + s[1:]


def _create_jinja_env() -> Environment:
    """Create Jinja2 environment with custom filters."""
    env = Environment(
        loader=PackageLoader("openapi_ts_client", "templates/angular"),
        keep_trailing_newline=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["lower_first"] = _lower_first
    return env


def _get_property_info(
    prop_name: str,
    prop_schema: Dict[str, Any],
    required_props: List[str],
    interface_name: str,
) -> Dict[str, Any]:
    """
    Get property information for template rendering.

    Args:
        prop_name: The property name
        prop_schema: The property schema
        required_props: List of required property names
        interface_name: Name of the parent interface (for enum type references)

    Returns:
        Dict with name, type, required status, and enum info
    """
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

    # Non-enum property
    ts_type, imports = map_openapi_type_with_imports(prop_schema)
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


def _generate_model_file(
    env: Environment,
    schema_name: str,
    schema: Dict[str, Any],
    api_title: str,
    contact_email: str,
) -> str:
    """
    Generate a single model file content.

    Args:
        env: Jinja2 environment
        schema_name: Name of the schema (e.g., "FeedingOut")
        schema: The schema definition
        api_title: API title for the header
        contact_email: Contact email for the header

    Returns:
        Generated TypeScript content
    """
    template = env.get_template("model.ts.j2")

    properties = schema.get("properties", {})
    required_props = schema.get("required", [])

    # Build property info list preserving schema order
    prop_infos = []
    all_imports = set()
    enums = []

    for prop_name, prop_schema in properties.items():
        info = _get_property_info(prop_name, prop_schema, required_props, schema_name)
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

    generate_all_models(schemas, output_dir, api_title, contact_email)


def generate_all_models(
    schemas: Dict[str, Any],
    output_dir: Path,
    api_title: str,
    contact_email: str,
) -> None:
    """
    Generate all model files from schemas.

    Args:
        schemas: OpenAPI schemas dict
        output_dir: Directory to write model files to
        api_title: API title for header comments
        contact_email: Contact email for header comments
    """
    env = _create_jinja_env()

    # Add the schema_to_filename_filter to the environment
    def _schema_to_filename_filter(name: str) -> str:
        """Jinja2 filter to convert schema name to filename without .ts extension."""
        filename = schema_to_filename(name)
        return filename[:-3] if filename.endswith(".ts") else filename

    env.filters["schema_to_filename_filter"] = _schema_to_filename_filter

    model_filenames = []

    for schema_name, schema in schemas.items():
        # Generate model file
        content = _generate_model_file(
            env, schema_name, schema, api_title, contact_email
        )

        # Get filename (without .ts extension for barrel export)
        filename = schema_to_filename(schema_name)
        filename_without_ext = filename[:-3]  # Remove .ts

        model_filenames.append(filename_without_ext)

        # Write file
        output_file = output_dir / filename
        output_file.write_text(content)

    # Generate barrel export (models.ts)
    barrel_template = env.get_template("models.ts.j2")
    barrel_content = barrel_template.render(
        model_filenames=sorted(model_filenames)
    )
    (output_dir / "models.ts").write_text(barrel_content)
