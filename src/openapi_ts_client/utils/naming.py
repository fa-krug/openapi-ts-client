"""Naming convention utilities for TypeScript generation."""


def schema_to_filename(schema_name: str) -> str:
    """
    Convert OpenAPI schema name to TypeScript filename.

    Examples:
        FeedingOut -> feedingOut.ts
        HTTPMetrics -> hTTPMetrics.ts
        Score -> score.ts
    """
    if not schema_name:
        return ".ts"

    # Lowercase first character only
    filename = (
        schema_name[0].lower() + schema_name[1:] if len(schema_name) > 1 else schema_name.lower()
    )

    return f"{filename}.ts"
