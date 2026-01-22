"""Main generator module for creating TypeScript clients from OpenAPI 2.0 specifications."""

import json
import os
from pathlib import Path
from typing import Any, Dict, Union

from .enums import ClientFormat
from .logging_config import get_logger, setup_logging

# Initialize logger with verbose output
logger = setup_logging()


def generate_typescript_client(
    openapi_spec: Union[Dict[str, Any], str],
    output_format: ClientFormat = ClientFormat.FETCH,
    output_path: Union[str, Path] = ".",
) -> str:
    """
    Generate a TypeScript client from an OpenAPI 2.0 specification.

    This function takes an OpenAPI 2.0 (Swagger) specification and generates
    a TypeScript client based on the specified output format.

    Args:
        openapi_spec: The OpenAPI 2.0 specification. Can be provided as:
            - A dictionary containing the parsed JSON specification
            - A JSON string containing the specification
        output_format: The format of the generated TypeScript client.
            Defaults to ClientFormat.FETCH. Options are:
            - ClientFormat.FETCH: Native Fetch API client
            - ClientFormat.REACT: React-optimized client with hooks
            - ClientFormat.ANGULAR: Angular-optimized client with services
        output_path: The directory path where the generated client will be written.
            Defaults to the current directory (".").

    Returns:
        A status message indicating the result of the generation process.

    Raises:
        ValueError: If the provided specification is not valid OpenAPI 2.0.
        TypeError: If the openapi_spec parameter is neither a dict nor a string.

    Example:
        >>> from openapi_ts_client import generate_typescript_client, ClientFormat
        >>> spec = {"swagger": "2.0", "info": {"title": "My API", "version": "1.0"}, "paths": {}}
        >>> result = generate_typescript_client(spec, ClientFormat.REACT, "./output")
        >>> print(result)
    """
    func_logger = get_logger("generator")

    func_logger.info("=" * 80)
    func_logger.info("Starting TypeScript client generation")
    func_logger.info("=" * 80)

    # Log input parameters
    func_logger.debug(f"Input parameter 'output_format': {output_format}")
    func_logger.debug(f"Input parameter 'output_format' type: {type(output_format)}")
    func_logger.debug(f"Input parameter 'output_path': {output_path}")
    func_logger.debug(f"Input parameter 'output_path' type: {type(output_path)}")
    func_logger.debug(f"Input parameter 'openapi_spec' type: {type(openapi_spec)}")

    # Parse the OpenAPI spec if it's a string
    func_logger.info("Processing OpenAPI specification input")
    if isinstance(openapi_spec, str):
        func_logger.debug("OpenAPI spec provided as string, attempting to parse as JSON")
        func_logger.debug(f"String length: {len(openapi_spec)} characters")
        try:
            parsed_spec = json.loads(openapi_spec)
            func_logger.info("Successfully parsed OpenAPI spec from JSON string")
            func_logger.debug(f"Parsed spec keys: {list(parsed_spec.keys())}")
        except json.JSONDecodeError as e:
            func_logger.error(f"Failed to parse OpenAPI spec as JSON: {e}")
            func_logger.error(f"JSON error at line {e.lineno}, column {e.colno}")
            func_logger.error(f"Error message: {e.msg}")
            raise ValueError(f"Invalid JSON in openapi_spec: {e}") from e
    elif isinstance(openapi_spec, dict):
        func_logger.debug("OpenAPI spec provided as dictionary")
        func_logger.debug(f"Dictionary keys: {list(openapi_spec.keys())}")
        parsed_spec = openapi_spec
    else:
        func_logger.error(f"Invalid type for openapi_spec: {type(openapi_spec)}")
        func_logger.error("Expected dict or str, got something else")
        raise TypeError(
            f"openapi_spec must be a dict or JSON string, got {type(openapi_spec).__name__}"
        )

    # Validate OpenAPI 2.0 specification
    func_logger.info("Validating OpenAPI 2.0 specification")
    _validate_openapi_spec(parsed_spec, func_logger)

    # Resolve and validate output path
    func_logger.info("Resolving output path")
    resolved_output_path = _resolve_output_path(output_path, func_logger)

    # Log specification details
    func_logger.info("Extracting specification metadata")
    _log_spec_details(parsed_spec, func_logger)

    # Log generation configuration
    func_logger.info("-" * 60)
    func_logger.info("Generation Configuration Summary")
    func_logger.info("-" * 60)
    func_logger.info(f"  Output Format: {output_format.value}")
    func_logger.info(f"  Output Path: {resolved_output_path}")
    func_logger.info(f"  API Title: {parsed_spec.get('info', {}).get('title', 'Unknown')}")
    func_logger.info(f"  API Version: {parsed_spec.get('info', {}).get('version', 'Unknown')}")
    func_logger.info("-" * 60)

    # Placeholder for actual generation logic
    func_logger.warning("=" * 80)
    func_logger.warning("CLIENT GENERATION LOGIC NOT IMPLEMENTED")
    func_logger.warning("This is a placeholder. The actual TypeScript client generation")
    func_logger.warning("logic needs to be implemented in this function.")
    func_logger.warning("=" * 80)

    # Build status message
    api_title = parsed_spec.get("info", {}).get("title", "Unknown API")
    api_version = parsed_spec.get("info", {}).get("version", "Unknown")
    paths_count = len(parsed_spec.get("paths", {}))

    status_message = (
        f"TypeScript client generation initiated for '{api_title}' v{api_version}. "
        f"Format: {output_format.value}, Output: {resolved_output_path}, "
        f"Paths to process: {paths_count}. "
        f"NOTE: Generation logic not yet implemented."
    )

    func_logger.info("=" * 80)
    func_logger.info("Generation process completed")
    func_logger.info(f"Status: {status_message}")
    func_logger.info("=" * 80)

    return status_message


def _validate_openapi_spec(spec: Dict[str, Any], func_logger) -> None:
    """
    Validate that the specification is a valid OpenAPI 2.0 document.

    Args:
        spec: The parsed OpenAPI specification dictionary.
        func_logger: Logger instance for verbose output.

    Raises:
        ValueError: If the specification is not valid OpenAPI 2.0.
    """
    func_logger.debug("Checking for 'swagger' field in specification")

    # Check for swagger version field
    swagger_version = spec.get("swagger")
    func_logger.debug(f"Found swagger version: {swagger_version}")

    if swagger_version is None:
        func_logger.error("Missing 'swagger' field in specification")
        func_logger.error("This field is required for OpenAPI 2.0 (Swagger) specifications")
        func_logger.debug(f"Available top-level keys: {list(spec.keys())}")

        # Check if it might be OpenAPI 3.x
        if "openapi" in spec:
            openapi_version = spec.get("openapi")
            func_logger.error(f"Found 'openapi' field with version {openapi_version}")
            func_logger.error("This appears to be an OpenAPI 3.x specification")
            raise ValueError(
                f"OpenAPI 3.x specifications are not supported. "
                f"Found version: {openapi_version}. Please provide an OpenAPI 2.0 (Swagger) specification."
            )

        raise ValueError(
            "Invalid OpenAPI specification: missing 'swagger' field. "
            "Please provide a valid OpenAPI 2.0 (Swagger) specification."
        )

    # Validate swagger version is 2.0
    func_logger.debug(f"Validating swagger version: {swagger_version}")
    if swagger_version != "2.0":
        func_logger.error(f"Unsupported swagger version: {swagger_version}")
        func_logger.error("Only OpenAPI 2.0 (Swagger 2.0) is supported")
        raise ValueError(
            f"Unsupported swagger version: {swagger_version}. "
            f"Only version '2.0' is supported."
        )

    func_logger.info("Swagger version validated: 2.0")

    # Check for required 'info' field
    func_logger.debug("Checking for required 'info' field")
    if "info" not in spec:
        func_logger.error("Missing required 'info' field in specification")
        raise ValueError("Invalid OpenAPI specification: missing required 'info' field.")

    info = spec["info"]
    func_logger.debug(f"Info field contents: {info}")

    # Check for required 'title' in info
    if "title" not in info:
        func_logger.error("Missing required 'title' field in info object")
        raise ValueError("Invalid OpenAPI specification: missing required 'info.title' field.")

    func_logger.info(f"API title found: {info['title']}")

    # Check for required 'version' in info
    if "version" not in info:
        func_logger.error("Missing required 'version' field in info object")
        raise ValueError("Invalid OpenAPI specification: missing required 'info.version' field.")

    func_logger.info(f"API version found: {info['version']}")

    # Check for 'paths' field (optional but log if missing)
    func_logger.debug("Checking for 'paths' field")
    if "paths" not in spec:
        func_logger.warning("No 'paths' field found in specification")
        func_logger.warning("The generated client may have no API methods")
    else:
        paths_count = len(spec["paths"])
        func_logger.info(f"Found {paths_count} path(s) in specification")

    func_logger.info("OpenAPI 2.0 specification validation completed successfully")


def _resolve_output_path(output_path: Union[str, Path], func_logger) -> Path:
    """
    Resolve and validate the output path.

    Args:
        output_path: The output path as string or Path object.
        func_logger: Logger instance for verbose output.

    Returns:
        The resolved absolute Path object.
    """
    func_logger.debug(f"Input output_path: {output_path}")
    func_logger.debug(f"Input output_path type: {type(output_path)}")

    # Convert to Path object
    if isinstance(output_path, str):
        func_logger.debug("Converting string path to Path object")
        path = Path(output_path)
    else:
        path = output_path

    func_logger.debug(f"Path object created: {path}")

    # Resolve to absolute path
    func_logger.debug("Resolving to absolute path")
    absolute_path = path.resolve()
    func_logger.debug(f"Absolute path: {absolute_path}")

    # Check if path exists
    func_logger.debug(f"Checking if path exists: {absolute_path}")
    if absolute_path.exists():
        func_logger.info(f"Output path exists: {absolute_path}")
        func_logger.debug(f"Path is directory: {absolute_path.is_dir()}")
        func_logger.debug(f"Path is file: {absolute_path.is_file()}")

        if absolute_path.is_file():
            func_logger.warning(f"Output path is a file, not a directory: {absolute_path}")
    else:
        func_logger.warning(f"Output path does not exist: {absolute_path}")
        func_logger.info("Directory will need to be created during generation")

    # Log path components
    func_logger.debug(f"Path parts: {absolute_path.parts}")
    func_logger.debug(f"Path parent: {absolute_path.parent}")
    func_logger.debug(f"Path name: {absolute_path.name}")

    # Check write permissions on parent directory
    parent = absolute_path if absolute_path.is_dir() else absolute_path.parent
    if parent.exists():
        func_logger.debug(f"Checking write permissions on: {parent}")
        is_writable = os.access(parent, os.W_OK)
        func_logger.debug(f"Directory is writable: {is_writable}")
        if not is_writable:
            func_logger.warning(f"Directory may not be writable: {parent}")

    func_logger.info(f"Resolved output path: {absolute_path}")
    return absolute_path


def _log_spec_details(spec: Dict[str, Any], func_logger) -> None:
    """
    Log detailed information about the OpenAPI specification.

    Args:
        spec: The parsed OpenAPI specification dictionary.
        func_logger: Logger instance for verbose output.
    """
    func_logger.debug("-" * 40)
    func_logger.debug("OpenAPI Specification Details")
    func_logger.debug("-" * 40)

    # Info section
    info = spec.get("info", {})
    func_logger.debug(f"  Title: {info.get('title', 'N/A')}")
    func_logger.debug(f"  Version: {info.get('version', 'N/A')}")
    func_logger.debug(f"  Description: {info.get('description', 'N/A')[:100] if info.get('description') else 'N/A'}")

    # Host and basePath
    func_logger.debug(f"  Host: {spec.get('host', 'N/A')}")
    func_logger.debug(f"  Base Path: {spec.get('basePath', 'N/A')}")

    # Schemes
    schemes = spec.get("schemes", [])
    func_logger.debug(f"  Schemes: {', '.join(schemes) if schemes else 'N/A'}")

    # Consumes and produces
    consumes = spec.get("consumes", [])
    produces = spec.get("produces", [])
    func_logger.debug(f"  Consumes: {', '.join(consumes) if consumes else 'N/A'}")
    func_logger.debug(f"  Produces: {', '.join(produces) if produces else 'N/A'}")

    # Paths summary
    paths = spec.get("paths", {})
    func_logger.debug(f"  Total Paths: {len(paths)}")

    if paths:
        func_logger.debug("  Path endpoints:")
        for path_name, path_item in paths.items():
            methods = [m.upper() for m in path_item.keys() if m in ["get", "post", "put", "delete", "patch", "options", "head"]]
            func_logger.debug(f"    {path_name}: {', '.join(methods)}")

    # Definitions (models)
    definitions = spec.get("definitions", {})
    func_logger.debug(f"  Total Definitions (Models): {len(definitions)}")
    if definitions:
        func_logger.debug(f"  Model names: {', '.join(list(definitions.keys())[:10])}")
        if len(definitions) > 10:
            func_logger.debug(f"    ... and {len(definitions) - 10} more")

    # Security definitions
    security_defs = spec.get("securityDefinitions", {})
    func_logger.debug(f"  Security Definitions: {len(security_defs)}")
    if security_defs:
        for sec_name, sec_def in security_defs.items():
            func_logger.debug(f"    {sec_name}: {sec_def.get('type', 'unknown')}")

    # Tags
    tags = spec.get("tags", [])
    func_logger.debug(f"  Tags: {len(tags)}")
    if tags:
        tag_names = [t.get("name", "unnamed") for t in tags]
        func_logger.debug(f"  Tag names: {', '.join(tag_names)}")

    func_logger.debug("-" * 40)
