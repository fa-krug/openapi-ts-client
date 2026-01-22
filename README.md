# openapi-ts-client

Generate TypeScript clients from OpenAPI specifications (2.0/Swagger and 3.x).

## Installation

```bash
pip install openapi-ts-client
```

Or install from source:

```bash
pip install -e .
```

## Usage

### Basic Usage

```python
from openapi_ts_client import generate_typescript_client, ClientFormat

# Load your OpenAPI specification (3.x example)
spec = {
    "openapi": "3.0.0",
    "info": {
        "title": "My API",
        "version": "1.0.0"
    },
    "paths": {
        "/users": {
            "get": {
                "summary": "Get all users",
                "responses": {
                    "200": {
                        "description": "Success"
                    }
                }
            }
        }
    }
}

# Generate TypeScript client with default settings (Fetch API, current directory)
result = generate_typescript_client(spec)
print(result)
```

### OpenAPI 2.0 (Swagger) Example

```python
from openapi_ts_client import generate_typescript_client

# OpenAPI 2.0 specs use "swagger" instead of "openapi"
spec = {
    "swagger": "2.0",
    "info": {
        "title": "My API",
        "version": "1.0.0"
    },
    "paths": {}
}

result = generate_typescript_client(spec)
```

### Using JSON String Input

```python
from openapi_ts_client import generate_typescript_client

# Load spec from a JSON file
with open("openapi.json", "r") as f:
    json_string = f.read()

result = generate_typescript_client(json_string)
```

### Custom Output Format

The package supports three output formats:

- `ClientFormat.FETCH` (default) - Native Fetch API client
- `ClientFormat.REACT` - React-optimized client with hooks
- `ClientFormat.ANGULAR` - Angular-optimized client with services

```python
from openapi_ts_client import generate_typescript_client, ClientFormat

# Generate a React client
result = generate_typescript_client(
    spec,
    output_format=ClientFormat.REACT
)

# Generate an Angular client
result = generate_typescript_client(
    spec,
    output_format=ClientFormat.ANGULAR
)
```

### Custom Output Path

```python
from openapi_ts_client import generate_typescript_client

# Output to a specific directory
result = generate_typescript_client(
    spec,
    output_path="./generated/api-client"
)
```

### Full Example

```python
from openapi_ts_client import generate_typescript_client, ClientFormat

# Load your OpenAPI spec
with open("api-spec.json", "r") as f:
    spec = f.read()

# Generate a React client in a specific directory
result = generate_typescript_client(
    openapi_spec=spec,
    output_format=ClientFormat.REACT,
    output_path="./src/api"
)

print(result)
```

## API Reference

### `generate_typescript_client(openapi_spec, output_format=ClientFormat.FETCH, output_path=".")`

Generate a TypeScript client from an OpenAPI specification.

**Parameters:**

- `openapi_spec` (dict | str): The OpenAPI specification as a dictionary or JSON string. Supports both OpenAPI 2.0 (Swagger) and OpenAPI 3.x.
- `output_format` (ClientFormat, optional): The output client format. Defaults to `ClientFormat.FETCH`
- `output_path` (str | Path, optional): The output directory path. Defaults to current directory `"."`

**Returns:**

- `str`: A status message indicating the result of the generation process

**Raises:**

- `ValueError`: If the specification is not a valid OpenAPI spec
- `TypeError`: If `openapi_spec` is neither a dict nor a string

### `ClientFormat` Enum

- `ClientFormat.FETCH` - Generate a client using the native Fetch API
- `ClientFormat.REACT` - Generate a client optimized for React applications
- `ClientFormat.ANGULAR` - Generate a client optimized for Angular applications

## Supported OpenAPI Versions

- OpenAPI 2.0 (Swagger)
- OpenAPI 3.0.x
- OpenAPI 3.1.x

## Requirements

- Python 3.8+

## License

MIT License
