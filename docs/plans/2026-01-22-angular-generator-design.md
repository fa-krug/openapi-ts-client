# Angular TypeScript Client Generator Design

## Overview

Implement TypeScript generation for Angular format, producing Angular services and TypeScript interfaces from OpenAPI 3.x specifications. The reference implementation is `tests/fixtures/space_zoo/angular/`.

## Package Structure

```
src/openapi_ts_client/
├── __init__.py                    # Export public API
├── enums.py                       # ClientFormat enum (existing)
├── logging_config.py              # Verbose logging (existing)
├── generator.py                   # Main entry point (existing, updated)
├── utils/
│   ├── __init__.py
│   ├── naming.py                  # Naming convention utilities
│   └── openapi.py                 # OpenAPI parsing/resolution using openapi-core
├── generators/
│   └── angular/
│       ├── __init__.py
│       ├── generator.py           # Angular generation orchestrator
│       ├── models.py              # Schema → TypeScript interfaces
│       ├── services.py            # Paths/tags → Angular services
│       └── type_mapper.py         # OpenAPI types → TypeScript types
└── templates/
    └── angular/
        ├── index.ts.j2
        ├── api.module.ts.j2
        ├── provide-api.ts.j2
        ├── configuration.ts.j2
        ├── api.base.service.ts.j2
        ├── variables.ts.j2
        ├── encoder.ts.j2
        ├── param.ts.j2
        ├── query.params.ts.j2
        ├── model.ts.j2            # Individual model template
        ├── models.ts.j2           # Barrel export for models
        ├── service.ts.j2          # Individual service template
        └── api.ts.j2              # Barrel export for services
```

## Dependencies

- `jinja2` - Template rendering
- `openapi-core` - Spec validation and `$ref` resolution

## Data Flow

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────────┐
│  OpenAPI Spec   │────▶│  utils/openapi   │────▶│  Resolved Spec      │
│  (JSON dict)    │     │  (openapi-core)  │     │  (refs dereferenced)│
└─────────────────┘     └──────────────────┘     └──────────┬──────────┘
                                                            │
                        ┌───────────────────────────────────┴──────────┐
                        ▼                                              ▼
              ┌─────────────────┐                           ┌─────────────────┐
              │ Extract Schemas │                           │ Extract Paths   │
              │ (components/    │                           │ (group by tags) │
              │  schemas)       │                           │                 │
              └────────┬────────┘                           └────────┬────────┘
                       ▼                                              ▼
              ┌─────────────────┐                           ┌─────────────────┐
              │ models.py       │                           │ services.py     │
              │ + type_mapper   │                           │ + type_mapper   │
              └────────┬────────┘                           └────────┬────────┘
                       ▼                                              ▼
              ┌─────────────────┐                           ┌─────────────────┐
              │ model.ts.j2     │                           │ service.ts.j2   │
              │ templates       │                           │ templates       │
              └────────┬────────┘                           └────────┬────────┘
                       │                                              │
                       └──────────────┬───────────────────────────────┘
                                      ▼
                        ┌─────────────────────────┐
                        │  Write to output_path/  │
                        │  ├── model/*.ts         │
                        │  ├── api/*.ts           │
                        │  └── *.ts (infra)       │
                        └─────────────────────────┘
```

1. `utils/openapi.py` validates and resolves all `$ref` using openapi-core
2. Resolved spec is split: schemas go to `models.py`, paths go to `services.py`
3. Both use `type_mapper.py` for consistent OpenAPI→TypeScript type conversion
4. Jinja2 templates render the final TypeScript
5. Files written to disk in the Angular client structure

## Type Mapping

| OpenAPI | TypeScript |
|---------|------------|
| `type: "string"` | `string` |
| `type: "integer"` | `number` |
| `type: "number"` | `number` |
| `type: "boolean"` | `boolean` |
| `type: "object"` (no properties) | `object` |
| `type: "array", items: X` | `Array<X>` |
| `$ref: "#/components/schemas/Foo"` | `Foo` (+ import) |
| `anyOf: [{type: X}, {type: "null"}]` | `X \| null` |
| `type: "string", format: "date-time"` | `string` |

### Nullability rules

- `anyOf [type, null]` → `type | null`
- Property in `required` array → no `?` suffix
- Property not in `required` → `?` optional marker

### Import tracking

- When a property references another schema, track it
- Generate import statements at top of model file
- Use relative imports: `import { Foo } from './foo';`

## Naming Conventions

### Schema name → filename
- `FeedingOut` → `feedingOut.ts` (camelCase)
- `HTTPMetrics` → `hTTPMetrics.ts` (preserve acronym casing from fixture)

### Schema name → interface name
- Keep as-is: `FeedingOut` → `FeedingOut`

### Tag → service class name
- `Feedings` → `FeedingsService`
- `HTTPMetrics` → `HTTPMetricsService`

### Tag → service filename
- `Feedings` → `feedings.service.ts`
- `HTTPMetrics` → `hTTPMetrics.service.ts`

### Operation ID → method name
- `zoo.api.endpoints.feedings_list_all` → `listAll`
- Extract last segment, convert `snake_case` to `camelCase`
- Handle reserved words: `delete` → `_delete`

### Reserved TypeScript words to escape
```python
RESERVED = {'delete', 'class', 'function', 'import', 'export', ...}
```

## Service Generation

### Method overloads
Every operation gets 3 TypeScript overloads + implementation:
```typescript
public listAll(..., observe?: 'body'): Observable<Array<FeedingOut>>;
public listAll(..., observe?: 'response'): Observable<HttpResponse<Array<FeedingOut>>>;
public listAll(..., observe?: 'events'): Observable<HttpEvent<Array<FeedingOut>>>;
public listAll(..., observe: any = 'body'): Observable<any> {
    // implementation
}
```

### Parameter handling
- Path params: `{pk}` → method argument, encoded via `this.configuration.encodeParam()`
- Query params: Added to `OpenApiHttpParams` with `QueryParamStyle.Form`
- Body params: Passed to `httpClient.request()` as `body`
- Required params: Null check with thrown error

### Grouping by tag
- Endpoints tagged `Feedings` → `FeedingsService`
- All methods for that tag in one service class
- Service inherits from `BaseService`

### Response types
- `200` response schema determines return type
- Array responses: `Array<ModelName>`
- No content: `any`

## Testing Strategy

### Test structure
```
tests/
├── test_angular_generator.py      # Integration tests
├── test_type_mapper.py            # Unit tests for type mapping
├── test_naming.py                 # Unit tests for naming utils
├── test_openapi_utils.py          # Unit tests for ref resolution
└── fixtures/
    └── space_zoo/                 # Reference (DO NOT MODIFY)
        ├── openapi.json
        └── angular/
```

### Generated output location
```
project_root/
├── temp/                          # .gitignored
│   └── space_zoo/
│       └── angular/               # Generated output for inspection
```

### Integration test approach
1. Load `space_zoo/openapi.json`
2. Generate Angular client to `temp/space_zoo/angular/`
3. Compare each generated file against `tests/fixtures/space_zoo/angular/` byte-for-byte
4. Fail on any difference, showing a diff

### Test fixtures rule (from CLAUDE.md)
- Never modify files in `tests/fixtures/`
- If tests fail, fix the generator, not the fixtures

## Key Decisions

- **OpenAPI 3.x only** - No OpenAPI 2.0 (Swagger) support
- **Fail-fast error handling** - Raise exceptions with clear messages
- **Pre-resolve all $ref** - Dereference before generation
- **Verbose logging** - Use existing logging setup
- **Exact file comparison** - Tests must match fixtures byte-for-byte

## Implementation Order

### Phase 1: Foundation
1. Add `jinja2` and `openapi-core` to dependencies
2. Create `utils/naming.py` with naming utilities
3. Create `utils/openapi.py` with spec loading and ref resolution
4. Add `temp/` to `.gitignore`

### Phase 2: Type System
5. Create `generators/angular/type_mapper.py`
6. Create model templates (`model.ts.j2`, `models.ts.j2`)
7. Create `generators/angular/models.py`

### Phase 3: Services
8. Create service template (`service.ts.j2`, `api.ts.j2`)
9. Create `generators/angular/services.py`

### Phase 4: Infrastructure
10. Create infrastructure templates (9 files)
11. Create `generators/angular/generator.py` (orchestrator)

### Phase 5: Integration
12. Update main `generator.py` to dispatch to Angular generator
13. Write integration tests comparing against fixtures
14. Iterate until tests pass
