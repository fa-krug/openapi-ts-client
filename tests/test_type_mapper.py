"""Tests for TypeScript type mapper."""

from openapi_ts_client.generators.angular.type_mapper import (
    map_openapi_type,
    map_openapi_type_with_imports,
)


class TestMapOpenapiTypeBasic:
    """Tests for basic OpenAPI to TypeScript type mapping."""

    def test_string_type(self):
        """string -> string"""
        schema = {"type": "string"}
        assert map_openapi_type(schema) == "string"

    def test_integer_type(self):
        """integer -> number"""
        schema = {"type": "integer"}
        assert map_openapi_type(schema) == "number"

    def test_number_type(self):
        """number -> number"""
        schema = {"type": "number"}
        assert map_openapi_type(schema) == "number"

    def test_boolean_type(self):
        """boolean -> boolean"""
        schema = {"type": "boolean"}
        assert map_openapi_type(schema) == "boolean"

    def test_object_type_no_properties(self):
        """object without properties -> object"""
        schema = {"type": "object"}
        assert map_openapi_type(schema) == "object"

    def test_string_with_format(self):
        """string with format still returns string."""
        schema = {"type": "string", "format": "date-time"}
        assert map_openapi_type(schema) == "string"


class TestMapOpenapiTypeArrays:
    """Tests for array type mapping."""

    def test_array_of_strings(self):
        """Array of strings."""
        schema = {"type": "array", "items": {"type": "string"}}
        assert map_openapi_type(schema) == "Array<string>"

    def test_array_of_integers(self):
        """Array of integers."""
        schema = {"type": "array", "items": {"type": "integer"}}
        assert map_openapi_type(schema) == "Array<number>"

    def test_array_of_refs(self):
        """Array of schema references."""
        schema = {"type": "array", "items": {"$ref": "#/components/schemas/User"}}
        result, imports = map_openapi_type_with_imports(schema)
        assert result == "Array<User>"
        assert "User" in imports


class TestMapOpenapiTypeRefs:
    """Tests for $ref type mapping."""

    def test_simple_ref(self):
        """$ref extracts schema name."""
        schema = {"$ref": "#/components/schemas/FeedingOut"}
        result, imports = map_openapi_type_with_imports(schema)
        assert result == "FeedingOut"
        assert "FeedingOut" in imports

    def test_nested_ref(self):
        """Nested $ref in properties."""
        schema = {"$ref": "#/components/schemas/BiomeTypeIn"}
        result, imports = map_openapi_type_with_imports(schema)
        assert result == "BiomeTypeIn"
        assert "BiomeTypeIn" in imports
