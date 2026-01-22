"""Enums for the openapi-ts-client package."""

from enum import Enum


class ClientFormat(Enum):
    """
    Enum representing the output client format for TypeScript client generation.

    Attributes:
        FETCH: Generate a client using the native Fetch API (default).
        REACT: Generate a client optimized for React applications with hooks.
        ANGULAR: Generate a client optimized for Angular applications with services.
    """

    FETCH = "fetch"
    REACT = "react"
    ANGULAR = "angular"

    def __str__(self) -> str:
        """Return the string value of the enum."""
        return self.value
