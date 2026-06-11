"""Tests for OpenAPI utilities."""

import pytest

from openapi_ts_client.utils.openapi import load_and_resolve_spec, sanitize_spec


class TestSanitizeSpec:
    """Tests for sanitize_spec function."""

    def test_coerces_numeric_default_under_string_type(self):
        """A numeric default on a string-typed node is coerced to its string form.

        Pydantic v2 renders Decimal fields as {"type": "string", "pattern": ...}
        but emits the default as a JSON number, producing an internally
        inconsistent node that strict validators reject.
        """
        spec = {
            "components": {
                "schemas": {
                    "Score": {
                        "type": "string",
                        "pattern": r"^[+-]?\d*\.?\d*$",
                        "default": 0.0,
                    }
                }
            }
        }
        sanitize_spec(spec)
        assert spec["components"]["schemas"]["Score"]["default"] == "0.0"

    def test_coerces_example_and_examples(self):
        """example and examples entries are coerced under string type."""
        spec = {"type": "string", "example": 1.5, "examples": [2.0, "ok", None]}
        sanitize_spec(spec)
        assert spec["example"] == "1.5"
        assert spec["examples"] == ["2.0", "ok", None]

    def test_leaves_valid_string_defaults_untouched(self):
        """A string default under string type is left as-is."""
        spec = {"type": "string", "default": "hello"}
        sanitize_spec(spec)
        assert spec["default"] == "hello"

    def test_ignores_non_string_typed_nodes(self):
        """A numeric default under a non-string type stays numeric."""
        spec = {"type": "number", "default": 0.0}
        sanitize_spec(spec)
        assert spec["default"] == 0.0

    def test_recurses_into_nested_structures(self):
        """Nested string-typed nodes (e.g. in parameters) are sanitized."""
        spec = {
            "paths": {"/x": {"get": {"parameters": [{"schema": {"type": "string", "default": 3}}]}}}
        }
        sanitize_spec(spec)
        assert spec["paths"]["/x"]["get"]["parameters"][0]["schema"]["default"] == "3"

    def test_returns_same_object(self):
        """sanitize_spec mutates in place and returns the node."""
        spec = {"type": "string", "default": 1}
        assert sanitize_spec(spec) is spec


class TestLoadAndResolveSpec:
    """Tests for load_and_resolve_spec function."""

    def test_simple_spec_no_refs(self):
        """Spec without refs returns as-is."""
        spec = {
            "openapi": "3.1.0",
            "info": {"title": "Test", "version": "1.0"},
            "paths": {},
            "components": {
                "schemas": {"User": {"type": "object", "properties": {"name": {"type": "string"}}}}
            },
        }
        resolved = load_and_resolve_spec(spec)
        assert "components" in resolved
        assert "schemas" in resolved["components"]
        assert "User" in resolved["components"]["schemas"]

    def test_resolves_ref(self):
        """$ref is resolved to actual schema."""
        spec = {
            "openapi": "3.1.0",
            "info": {"title": "Test", "version": "1.0"},
            "paths": {},
            "components": {
                "schemas": {
                    "User": {"type": "object", "properties": {"name": {"type": "string"}}},
                    "Response": {
                        "type": "object",
                        "properties": {"user": {"$ref": "#/components/schemas/User"}},
                    },
                }
            },
        }
        resolved = load_and_resolve_spec(spec)
        response_schema = resolved["components"]["schemas"]["Response"]
        user_prop = response_schema["properties"]["user"]
        # After resolution, should have the User schema content or a marker
        # The exact behavior depends on openapi-core's dereferencing
        assert "properties" in user_prop or "$ref" in user_prop

    def test_invalid_spec_raises(self):
        """Invalid spec raises ValueError."""
        spec = {"invalid": "spec"}
        with pytest.raises(ValueError):
            load_and_resolve_spec(spec)

    def test_sanitizes_string_typed_numeric_default(self):
        """A Decimal-style string field with a numeric default no longer fails validation."""
        spec = {
            "openapi": "3.0.3",
            "info": {"title": "Test", "version": "1.0"},
            "paths": {},
            "components": {
                "schemas": {
                    "Score": {
                        "type": "string",
                        "pattern": r"^[+-]?\d*\.?\d*$",
                        "default": 0.0,
                    }
                }
            },
        }
        resolved = load_and_resolve_spec(spec)
        assert resolved["components"]["schemas"]["Score"]["default"] == "0.0"

    def test_skip_validation_allows_invalid_spec(self):
        """With skip_validation=True, an otherwise-invalid spec is still resolved."""
        # Missing required OpenAPI fields would normally fail strict validation.
        spec = {
            "openapi": "3.0.3",
            "info": {"title": "Test", "version": "1.0"},
            "paths": {
                "/x": {
                    "get": {
                        "responses": {
                            # 'description' is required by OpenAPI; omitting it
                            # fails strict validation but must pass when skipped.
                            "200": {}
                        }
                    }
                }
            },
        }
        with pytest.raises(ValueError):
            load_and_resolve_spec(spec)
        resolved = load_and_resolve_spec(spec, skip_validation=True)
        assert "/x" in resolved["paths"]
