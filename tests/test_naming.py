"""Tests for naming utilities."""

from openapi_ts_client.utils.naming import schema_to_filename


class TestSchemaToFilename:
    """Tests for schema_to_filename function."""

    def test_simple_name(self):
        """Simple PascalCase becomes camelCase."""
        assert schema_to_filename("FeedingOut") == "feedingOut.ts"

    def test_single_word(self):
        """Single word gets lowercased."""
        assert schema_to_filename("Score") == "score.ts"

    def test_acronym_preserved(self):
        """Acronyms preserve their casing pattern from fixture."""
        # From fixture: HTTPMetrics -> hTTPMetrics.ts
        assert schema_to_filename("HTTPMetrics") == "hTTPMetrics.ts"

    def test_db_prefix(self):
        """DB prefix follows fixture pattern."""
        # From fixture: DBMetrics -> dBMetrics.ts
        assert schema_to_filename("DBMetrics") == "dBMetrics.ts"

    def test_already_camelcase(self):
        """Already camelCase stays the same."""
        assert schema_to_filename("biomeTypeIn") == "biomeTypeIn.ts"
