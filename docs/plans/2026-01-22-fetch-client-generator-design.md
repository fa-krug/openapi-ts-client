# Fetch Client Generator Design

## Overview

Implement a Fetch-based TypeScript client generator for OpenAPI specifications. The fetch client uses native browser Fetch API with Promises, generating type-safe API classes with serialization/deserialization functions.

## Output Structure

```
output/
├── runtime.ts              # Infrastructure: Configuration, BaseAPI, middleware, errors
├── index.ts                # Barrel export for runtime, apis, models
├── models/
│   ├── index.ts            # Barrel export for all models
│   └── *.ts                # One file per schema with interface + serialization
├── apis/
│   ├── index.ts            # Barrel export for all API classes
│   └── *Api.ts             # One class per OpenAPI tag
└── docs/
    └── *.md                # Markdown documentation per model
```

## Module Organization

```
src/openapi_ts_client/
├── generators/
│   ├── shared/                    # Shared utilities (NEW)
│   │   ├── __init__.py
│   │   ├── type_mapper.py         # Moved from angular/
│   │   └── anyof_extractor.py     # Moved from angular/
│   ├── angular/                   # Existing, updated imports
│   └── fetch/                     # NEW
│       ├── __init__.py
│       ├── generator.py           # Orchestrator
│       ├── models.py              # Model + serialization generation
│       ├── apis.py                # API class generation
│       ├── docs.py                # Markdown doc generation
│       └── runtime.py             # runtime.ts template renderer
├── templates/
│   ├── angular/                   # Existing
│   └── fetch/                     # NEW
│       ├── runtime.ts.j2
│       ├── model.ts.j2
│       ├── api.ts.j2
│       ├── doc.md.j2
│       ├── models_index.ts.j2
│       └── apis_index.ts.j2
```

## Model Generation

Each model file generates:

1. **Interface** with JSDoc comments (`@export`, `@interface`, `@type`, `@memberof`)
2. **`instanceOf{Model}`** - Type guard checking required properties
3. **`{Model}FromJSON`** / **`{Model}FromJSONTyped`** - Deserialize from JSON
4. **`{Model}ToJSON`** / **`{Model}ToJSONTyped`** - Serialize to JSON

### Property Mapping Rules

| OpenAPI | JSON Key | TypeScript Property |
|---------|----------|---------------------|
| `habitat_id` | `habitat_id` | `habitatId` |
| `feedingDate` | `feedingDate` | `feedingDate` |

### Type Conversions

| OpenAPI Type | FromJSON | ToJSON |
|--------------|----------|--------|
| `string` (date) | `new Date(json['field'])` | `.toISOString().substring(0,10)` |
| `string` (date-time) | `new Date(json['field'])` | `.toISOString()` |
| Nested object | `{Type}FromJSON(json['field'])` | `{Type}ToJSON(value['field'])` |
| Array of objects | `json['field'].map({Type}FromJSON)` | `value['field'].map({Type}ToJSON)` |

### Imports

- Always import `mapValues` from `../runtime`
- Import nested types: both `type` import and serialization functions

```typescript
import { mapValues } from '../runtime';
import type { LastInspection } from './LastInspection';
import {
    LastInspectionFromJSON,
    LastInspectionFromJSONTyped,
    LastInspectionToJSON,
    LastInspectionToJSONTyped,
} from './LastInspection';
```

## API Generation

### Class Structure

- One class per OpenAPI tag, extending `BaseAPI`
- Request interfaces for methods with parameters
- Two methods per operation: `methodRaw()` and `method()`

### Method Pattern

```typescript
// Raw method returns ApiResponse wrapper
async getRaw(params: GetRequest, initOverrides?): Promise<ApiResponse<ModelOut>> {
    // 1. Validate required params
    if (params['pk'] == null) {
        throw new RequiredError('pk', 'Required parameter "pk" was null...');
    }

    // 2. Build query parameters
    const queryParameters: any = {};
    if (params['name'] != null) {
        queryParameters['name'] = params['name'];
    }

    // 3. Build headers
    const headerParameters: HTTPHeaders = {};
    headerParameters['Content-Type'] = 'application/json';  // for POST/PUT

    // 4. Build URL path
    let urlPath = `/api/items/{pk}`;
    urlPath = urlPath.replace(`{${"pk"}}`, encodeURIComponent(String(params['pk'])));

    // 5. Make request
    const response = await this.request({
        path: urlPath,
        method: 'GET',
        headers: headerParameters,
        query: queryParameters,
        body: ModelInToJSON(params['modelIn']),  // for POST/PUT
    }, initOverrides);

    // 6. Return typed response
    return new JSONApiResponse(response, (jsonValue) => ModelOutFromJSON(jsonValue));
}

// Convenience method unwraps the response
async get(params: GetRequest, initOverrides?): Promise<ModelOut> {
    const response = await this.getRaw(params, initOverrides);
    return await response.value();
}
```

### Response Handling

| Response Type | Return Pattern |
|---------------|----------------|
| Object | `JSONApiResponse(response, (json) => ModelFromJSON(json))` |
| Array | `JSONApiResponse(response, (json) => json.map(ModelFromJSON))` |
| Void | `VoidApiResponse(response)` |
| Primitive | `JSONApiResponse<number>(response)` or `TextApiResponse` |

## Runtime Generation

The `runtime.ts` file is a Jinja2 template with minimal variables:

- `api_title` - From spec `info.title`
- `api_description` - From spec `info.description`
- `api_version` - From spec `info.version`
- `base_path` - From spec `servers[0].url` (default: `http://localhost`)

The file contains ~430 lines of infrastructure:
- `Configuration` class with auth, headers, middleware support
- `BaseAPI` class with request/response handling
- Error classes: `ResponseError`, `FetchError`, `RequiredError`
- Type definitions: `HTTPMethod`, `HTTPHeaders`, `HTTPQuery`, `HTTPBody`
- Response wrappers: `JSONApiResponse`, `VoidApiResponse`, `BlobApiResponse`, `TextApiResponse`
- Utilities: `querystring`, `exists`, `mapValues`, `canConsumeForm`
- Middleware interface with `pre`, `post`, `onError` hooks

## Documentation Generation

One markdown file per model:

```markdown
# ModelName

## Properties

Name | Type
------------ | -------------
`id` | number
`name` | string

## Example

\`\`\`typescript
import type { ModelName } from ''

const example = {
  "id": null,
  "name": null,
} satisfies ModelName
\`\`\`

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) ...
```

## Integration

Update main `generator.py`:

```python
def generate_typescript_client(spec, output_path, client_format):
    if client_format == ClientFormat.ANGULAR:
        generate_angular_client(spec, output_path)
    elif client_format == ClientFormat.FETCH:
        generate_fetch_client(spec, output_path)
    elif client_format == ClientFormat.AXIOS:
        logger.warning("AXIOS format not yet implemented")
```

## Testing

- Generate against `tests/fixtures/space_zoo/openapi.json`
- Compare byte-for-byte against `tests/fixtures/space_zoo/fetch/`
- Follow existing test patterns

**Critical rule:** Never modify fixtures. If tests fail, fix the generator.

## Implementation Order

1. Create `generators/shared/` and move utilities
2. Update Angular imports
3. Create `generators/fetch/` module structure
4. Create Jinja2 templates in `templates/fetch/`
5. Implement `runtime.py` (simplest)
6. Implement `models.py` with serialization
7. Implement `apis.py` with request/response handling
8. Implement `docs.py` for markdown
9. Implement `generator.py` orchestrator
10. Wire up to main generator
11. Run tests and iterate until fixtures match
