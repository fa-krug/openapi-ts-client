"""
openapi-ts-client: Generate TypeScript clients from OpenAPI 2.0 specifications.

This package provides utilities to generate TypeScript API clients from
OpenAPI 2.0 (Swagger) specifications. It supports multiple output formats
including Fetch API, React hooks, and Angular services.

Example usage:
    >>> from openapi_ts_client import generate_typescript_client, ClientFormat
    >>>
    >>> # Using a dictionary spec
    >>> spec = {
    ...     "swagger": "2.0",
    ...     "info": {"title": "My API", "version": "1.0.0"},
    ...     "paths": {}
    ... }
    >>> result = generate_typescript_client(spec)
    >>> print(result)
    >>>
    >>> # With custom format and output path
    >>> result = generate_typescript_client(
    ...     spec,
    ...     output_format=ClientFormat.REACT,
    ...     output_path="./generated"
    ... )
"""

from .enums import ClientFormat
from .generator import generate_typescript_client

__version__ = "0.1.0"
__author__ = "openapi-ts-client contributors"
__all__ = [
    "generate_typescript_client",
    "ClientFormat",
    "__version__",
]
