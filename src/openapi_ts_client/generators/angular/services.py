"""Generate Angular service classes from OpenAPI paths."""

import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from jinja2 import Environment, PackageLoader, select_autoescape

from openapi_ts_client.utils.naming import (
    operation_id_to_method_name,
    schema_to_filename,
    tag_to_service_filename,
    tag_to_service_name,
)
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


def _extract_path_params(path: str) -> List[str]:
    """Extract path parameter names from a path template."""
    return re.findall(r'\{(\w+)\}', path)


def _get_typescript_type_for_param(param: Dict[str, Any]) -> Tuple[str, Set[str]]:
    """Get TypeScript type for a parameter schema."""
    schema = param.get("schema", {})

    # Handle anyOf patterns (nullable types)
    if "anyOf" in schema:
        non_null_types = [s for s in schema["anyOf"] if s.get("type") != "null"]
        if non_null_types:
            return map_openapi_type_with_imports(non_null_types[0])

    return map_openapi_type_with_imports(schema)


def _build_path_template(path: str, path_params: List[Dict[str, Any]]) -> str:
    """Build the path template string for the service method."""
    result = path

    for param in path_params:
        name = param["name"]
        schema = param.get("schema", {})
        data_type = "number" if schema.get("type") in ("integer", "number") else "string"
        data_format = schema.get("format")

        # Replace {name} with template expression
        placeholder = f'{{{name}}}'
        replacement = (
            f'${{this.configuration.encodeParam({{name: "{name}", value: {name}, '
            f'in: "path", style: "simple", explode: false, '
            f'dataType: "{data_type}", dataFormat: {repr(data_format) if data_format else "undefined"}}})}}'
        )
        result = result.replace(placeholder, replacement)

    return result


def _extract_response_type(operation: Dict[str, Any]) -> Tuple[str, Set[str]]:
    """Extract the response type from operation responses."""
    responses = operation.get("responses", {})

    # Look for 200 or 201 response
    for status in ["200", "201"]:
        if status in responses:
            response = responses[status]
            content = response.get("content", {})

            if "application/json" in content:
                schema = content["application/json"].get("schema", {})
                return map_openapi_type_with_imports(schema)

    return "any", set()


def _extract_request_body_type(operation: Dict[str, Any]) -> Tuple[Optional[str], Optional[str], Set[str]]:
    """Extract request body parameter name and type."""
    request_body = operation.get("requestBody", {})
    content = request_body.get("content", {})

    if "application/json" in content:
        schema = content["application/json"].get("schema", {})

        if "$ref" in schema:
            type_name = schema["$ref"].split("/")[-1]
            # Convert to camelCase for parameter name
            param_name = type_name[0].lower() + type_name[1:]
            return param_name, type_name, {type_name}

    return None, None, set()


def _extract_accept_types(operation: Dict[str, Any]) -> List[str]:
    """Extract Accept content types from responses."""
    responses = operation.get("responses", {})

    for status in ["200", "201"]:
        if status in responses:
            response = responses[status]
            content = response.get("content", {})
            return list(content.keys())

    return []


def extract_service_data(
    tag: str,
    operations: List[Dict[str, Any]],
    api_title: str,
    contact_email: str,
) -> Dict[str, Any]:
    """
    Extract data needed to render a service template.

    Args:
        tag: The OpenAPI tag name
        operations: List of operations for this tag
        api_title: API title for header comment
        contact_email: Contact email for header comment

    Returns:
        Dictionary with template data
    """
    model_imports: Set[str] = set()
    methods: List[Dict[str, Any]] = []

    for op in operations:
        path = op["path"]
        http_method = op["http_method"]
        operation = op["operation"]

        operation_id = operation.get("operationId", "")
        method_name = operation_id_to_method_name(operation_id)
        summary = operation.get("summary", "")
        description = operation.get("description", "")

        # Extract parameters
        parameters = operation.get("parameters", [])
        path_params = [p for p in parameters if p.get("in") == "path"]
        query_params = [p for p in parameters if p.get("in") == "query"]

        # Build required params list (path params are always required)
        required_params = []
        for p in path_params:
            ts_type, imports = _get_typescript_type_for_param(p)
            model_imports.update(imports)
            required_params.append({
                "name": p["name"],
                "type": ts_type,
                "description": p.get("description", ""),
            })

        # Handle request body
        body_param_name, body_param_type, body_imports = _extract_request_body_type(operation)
        model_imports.update(body_imports)

        if body_param_name:
            required_params.append({
                "name": body_param_name,
                "type": body_param_type,
                "description": "",
            })

        # Extract response type
        return_type, return_imports = _extract_response_type(operation)
        model_imports.update(return_imports)

        # Build path template
        path_template = _build_path_template(path, path_params)

        # Build accept types
        accept_list = _extract_accept_types(operation)
        if accept_list:
            accept_types = "'" + "' | '".join(accept_list) + "'"
        else:
            accept_types = "undefined"

        # Build parameter signatures
        all_params = []

        # Path parameters first
        for p in path_params:
            ts_type, _ = _get_typescript_type_for_param(p)
            all_params.append({"name": p["name"], "type": ts_type, "required": True, "description": p.get("description", "")})

        # Request body next
        if body_param_name:
            all_params.append({"name": body_param_name, "type": body_param_type, "required": True, "description": ""})

        # Query parameters last (optional)
        for p in query_params:
            ts_type, imports = _get_typescript_type_for_param(p)
            model_imports.update(imports)
            all_params.append({
                "name": p["name"],
                "type": ts_type,
                "required": p.get("required", False),
                "description": p.get("description", ""),
            })

        # Build signature strings
        sig_parts = []
        for p in all_params:
            optional = "?" if not p["required"] else ""
            sig_parts.append(f"{p['name']}{optional}: {p['type']}")

        params_signature = ", ".join(sig_parts)
        if params_signature:
            params_signature += ", "

        # Query params for method
        query_param_data = []
        for p in query_params:
            ts_type, _ = _get_typescript_type_for_param(p)
            query_param_data.append({
                "name": p["name"],
                "type": ts_type,
            })

        methods.append({
            "method_name": method_name,
            "summary": summary,
            "description": description,
            "http_method": http_method,
            "path": path,
            "path_template": path_template,
            "parameters": all_params,
            "required_params": required_params,
            "query_params": query_param_data,
            "has_body": body_param_name is not None,
            "body_param_name": body_param_name,
            "return_type": return_type,
            "accept_types": accept_types,
            "accept_list": accept_list,
            "params_signature_body": params_signature,
            "params_signature_response": params_signature,
            "params_signature_events": params_signature,
            "params_signature_impl": params_signature,
        })

    return {
        "api_title": api_title,
        "contact_email": contact_email,
        "service_name": tag_to_service_name(tag),
        "model_imports": model_imports,
        "methods": methods,
    }


def generate_service(
    tag: str,
    operations: List[Dict[str, Any]],
    api_title: str,
    contact_email: str,
) -> str:
    """
    Generate TypeScript service code for a tag.

    Args:
        tag: The OpenAPI tag name
        operations: List of operations for this tag
        api_title: API title for header comment
        contact_email: Contact email for header comment

    Returns:
        Generated TypeScript code as string
    """
    env = get_template_env()
    template = env.get_template("service.ts.j2")

    data = extract_service_data(tag, operations, api_title, contact_email)

    return template.render(**data)


def group_operations_by_tag(paths: Dict[str, Any]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Group path operations by their tags.

    Args:
        paths: OpenAPI paths object

    Returns:
        Dictionary mapping tag names to list of operations
    """
    tag_operations: Dict[str, List[Dict[str, Any]]] = {}

    for path, path_item in paths.items():
        for method in ["get", "post", "put", "delete", "patch", "options", "head"]:
            if method in path_item:
                operation = path_item[method]
                tags = operation.get("tags", ["default"])

                for tag in tags:
                    if tag not in tag_operations:
                        tag_operations[tag] = []

                    tag_operations[tag].append({
                        "path": path,
                        "http_method": method,
                        "operation": operation,
                    })

    return tag_operations


def generate_all_services(
    paths: Dict[str, Any],
    output_path: Path,
    api_title: str,
    contact_email: str,
) -> List[str]:
    """
    Generate all service files from OpenAPI paths.

    Args:
        paths: OpenAPI paths object
        output_path: Directory to write service files
        api_title: API title for header comments
        contact_email: Contact email for header comments

    Returns:
        List of generated service class names
    """
    env = get_template_env()
    service_names = []

    tag_operations = group_operations_by_tag(paths)

    for tag, operations in sorted(tag_operations.items()):
        service_name = tag_to_service_name(tag)
        service_names.append(service_name)

        content = generate_service(tag, operations, api_title, contact_email)
        filename = tag_to_service_filename(tag)
        (output_path / filename).write_text(content)

    # Generate barrel export (api.ts)
    api_template = env.get_template("api.ts.j2")
    api_content = api_template.render(
        services=[
            {
                "name": tag_to_service_name(tag),
                "filename": tag_to_service_filename(tag)[:-3],  # Remove .ts
            }
            for tag in sorted(tag_operations.keys())
        ]
    )
    (output_path / "api.ts").write_text(api_content)

    return service_names
