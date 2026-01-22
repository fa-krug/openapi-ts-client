"""Tests for the enums module."""

import pytest

from openapi_ts_client import ClientFormat


class TestClientFormat:
    """Tests for the ClientFormat enum."""

    def test_fetch_value(self):
        """Test that FETCH has correct value."""
        assert ClientFormat.FETCH.value == "fetch"

    def test_react_value(self):
        """Test that REACT has correct value."""
        assert ClientFormat.REACT.value == "react"

    def test_angular_value(self):
        """Test that ANGULAR has correct value."""
        assert ClientFormat.ANGULAR.value == "angular"

    def test_str_fetch(self):
        """Test string representation of FETCH."""
        assert str(ClientFormat.FETCH) == "fetch"

    def test_str_react(self):
        """Test string representation of REACT."""
        assert str(ClientFormat.REACT) == "react"

    def test_str_angular(self):
        """Test string representation of ANGULAR."""
        assert str(ClientFormat.ANGULAR) == "angular"

    def test_all_values(self):
        """Test that all expected values exist."""
        values = [e.value for e in ClientFormat]
        assert "fetch" in values
        assert "react" in values
        assert "angular" in values
        assert len(values) == 3

    def test_enum_membership(self):
        """Test enum membership checks."""
        assert ClientFormat.FETCH in ClientFormat
        assert ClientFormat.REACT in ClientFormat
        assert ClientFormat.ANGULAR in ClientFormat

    def test_enum_comparison(self):
        """Test that enum members are equal to themselves."""
        assert ClientFormat.FETCH == ClientFormat.FETCH
        assert ClientFormat.REACT == ClientFormat.REACT
        assert ClientFormat.ANGULAR == ClientFormat.ANGULAR

    def test_enum_inequality(self):
        """Test that different enum members are not equal."""
        assert ClientFormat.FETCH != ClientFormat.REACT
        assert ClientFormat.REACT != ClientFormat.ANGULAR
        assert ClientFormat.ANGULAR != ClientFormat.FETCH

    def test_from_value(self):
        """Test creating enum from value."""
        assert ClientFormat("fetch") == ClientFormat.FETCH
        assert ClientFormat("react") == ClientFormat.REACT
        assert ClientFormat("angular") == ClientFormat.ANGULAR

    def test_invalid_value_raises(self):
        """Test that invalid value raises ValueError."""
        with pytest.raises(ValueError):
            ClientFormat("invalid")
