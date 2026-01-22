"""Tests for anyOf type extraction."""

from openapi_ts_client.generators.angular.anyof_extractor import discover_titled_anyofs


class TestDiscoverTitledAnyofs:
    """Tests for discovering titled anyOf schemas."""

    def test_finds_titled_anyof_in_schema_properties(self):
        """Finds anyOf with title in schema properties."""
        spec = {
            "components": {
                "schemas": {
                    "TestSchema": {
                        "properties": {
                            "score": {
                                "anyOf": [{"type": "number"}, {"type": "string"}],
                                "title": "Score",
                                "description": "A score value",
                            }
                        }
                    }
                }
            }
        }
        discoveries = discover_titled_anyofs(spec)
        assert len(discoveries) == 1
        assert discoveries[0]["title"] == "Score"
        assert discoveries[0]["description"] == "A score value"

    def test_ignores_anyof_without_title(self):
        """Ignores anyOf schemas that lack a title."""
        spec = {
            "components": {
                "schemas": {
                    "TestSchema": {
                        "properties": {
                            "value": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                            }
                        }
                    }
                }
            }
        }
        discoveries = discover_titled_anyofs(spec)
        assert len(discoveries) == 0

    def test_finds_titled_anyof_in_parameters(self):
        """Finds anyOf with title in operation parameters."""
        spec = {
            "paths": {
                "/api/test": {
                    "get": {
                        "parameters": [
                            {
                                "name": "score",
                                "in": "query",
                                "schema": {
                                    "anyOf": [{"type": "number"}, {"type": "null"}],
                                    "title": "Score",
                                },
                            }
                        ]
                    }
                }
            }
        }
        discoveries = discover_titled_anyofs(spec)
        assert len(discoveries) == 1
        assert discoveries[0]["title"] == "Score"
