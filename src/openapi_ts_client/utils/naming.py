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


def tag_to_service_name(tag: str) -> str:
    """
    Convert OpenAPI tag to Angular service class name.

    Examples:
        Feedings -> FeedingsService
        HTTPMetrics -> HTTPMetricsService
        Care Plans -> CarePlansService
    """
    # Remove spaces and ensure first letter of each word is capitalized
    words = tag.split()
    class_name = "".join(word[0].upper() + word[1:] if word else "" for word in words)

    return f"{class_name}Service"


def tag_to_service_filename(tag: str) -> str:
    """
    Convert OpenAPI tag to Angular service filename.

    Examples:
        Feedings -> feedings.service.ts
        HTTPMetrics -> hTTPMetrics.service.ts
        Care Plans -> carePlans.service.ts
    """
    # Remove spaces and join words
    words = tag.split()
    if not words:
        return ".service.ts"

    # First word: lowercase first char
    # Subsequent words: keep first char case
    result = words[0][0].lower() + words[0][1:] if words[0] else ""
    for word in words[1:]:
        result += word

    return f"{result}.service.ts"
