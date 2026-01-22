"""Shared utilities for OpenAPI TypeScript client generation."""

from .naming import (
    TYPESCRIPT_RESERVED_WORDS,
    operation_id_to_method_name,
    schema_to_filename,
    tag_to_service_filename,
    tag_to_service_name,
)
from .openapi import load_and_resolve_spec

__all__ = [
    "TYPESCRIPT_RESERVED_WORDS",
    "operation_id_to_method_name",
    "schema_to_filename",
    "tag_to_service_filename",
    "tag_to_service_name",
    "load_and_resolve_spec",
]
