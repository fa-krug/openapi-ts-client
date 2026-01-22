"""Tests for TypeScript type mapper."""

from openapi_ts_client.generators.angular.type_mapper import map_openapi_type


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
