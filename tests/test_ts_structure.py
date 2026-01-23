"""Tests for TypeScript structure extraction."""

from tests.ts_structure import extract_functions, extract_interfaces


def test_extract_simple_interface(ts_parser):
    """Extract a simple interface with required and optional properties."""
    code = b"""
export interface Pet {
    id?: number;
    name: string;
    tag?: string;
}
"""
    result = extract_interfaces(code, ts_parser)

    assert result == [
        {
            "name": "Pet",
            "properties": [
                {"name": "id", "type": "number", "optional": True},
                {"name": "name", "type": "string", "optional": False},
                {"name": "tag", "type": "string", "optional": True},
            ],
        }
    ]


def test_extract_interface_with_array_type(ts_parser):
    """Extract interface with array type."""
    code = b"""
export interface Pet {
    tags: Array<string>;
    photoUrls: string[];
}
"""
    result = extract_interfaces(code, ts_parser)

    assert result == [
        {
            "name": "Pet",
            "properties": [
                {"name": "photoUrls", "type": "string[]", "optional": False},
                {"name": "tags", "type": "Array<string>", "optional": False},
            ],
        }
    ]


def test_extract_multiple_interfaces(ts_parser):
    """Extract multiple interfaces from same file."""
    code = b"""
export interface Pet {
    name: string;
}

export interface Category {
    id: number;
}
"""
    result = extract_interfaces(code, ts_parser)

    # Should be sorted by name for stable comparison
    assert len(result) == 2
    assert result[0]["name"] == "Category"
    assert result[1]["name"] == "Pet"


def test_extract_function_declaration(ts_parser):
    """Extract a function with parameters and return type."""
    code = b"""
export function PetFromJSON(json: any): Pet {
    return json;
}
"""
    result = extract_functions(code, ts_parser)

    assert result == [
        {
            "name": "PetFromJSON",
            "params": [{"name": "json", "type": "any"}],
            "return_type": "Pet",
        }
    ]


def test_extract_function_no_return_type(ts_parser):
    """Extract function without explicit return type."""
    code = b"""
export function log(message: string) {
    console.log(message);
}
"""
    result = extract_functions(code, ts_parser)

    assert result == [
        {
            "name": "log",
            "params": [{"name": "message", "type": "string"}],
            "return_type": None,
        }
    ]


def test_extract_multiple_functions(ts_parser):
    """Extract multiple functions sorted by name."""
    code = b"""
export function PetToJSON(pet: Pet): any {
    return pet;
}

export function PetFromJSON(json: any): Pet {
    return json;
}
"""
    result = extract_functions(code, ts_parser)

    assert len(result) == 2
    assert result[0]["name"] == "PetFromJSON"
    assert result[1]["name"] == "PetToJSON"
