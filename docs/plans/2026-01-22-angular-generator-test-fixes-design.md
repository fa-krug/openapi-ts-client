# Angular Generator Test Fixes - Design Document

**Date:** 2026-01-22
**Status:** Approved
**Goal:** Fix all content differences and missing files so Angular generator tests pass

## Problem Statement

The Angular generator produces output that differs from the OpenAPI Generator fixtures in two ways:
1. **Missing 6 files** - metadata and documentation files
2. **Content mismatches in 19+ files** - formatting, enums, method naming, security, etc.

## Issue Categories

### Category A: Template/Formatting Issues
1. Missing trailing newlines in all generated files
2. Header comment shows full description instead of `Contact: email`
3. Extra blank line in `model/models.ts`

### Category B: Missing Feature - Enum Generation
4. Enums not generated for properties with `enum` keyword
5. Missing JSDoc comments for enum properties

### Category C: Service Generation Issues
6. Wrong basePath - `http://localhost` instead of `servers[0].url`
7. Method names not properly derived from operationId
8. Methods in wrong order
9. Missing security credential initialization in `configuration.ts`
10. Missing security header injection in service methods
11. Content-Type handling incomplete

### Category D: Missing Files
12. 6 missing files: `.gitignore`, `.openapi-generator-ignore`, `.openapi-generator/FILES`, `.openapi-generator/VERSION`, `README.md`, `git_push.sh`

## Implementation Phases

### Phase 1: Foundational Fixes (Template Infrastructure)

**1.1 Missing Trailing Newlines**
- Ensure all 13 template files end with exactly one `\n`
- Files: all `.j2` templates in `templates/angular/`

**1.2 Header Comment Format**
- Extract `info.contact.email` from OpenAPI spec
- Pass `contact_email` to all templates
- Update templates to use `Contact: {{ contact_email }}` format
- Files: `generator.py`, `models.py`, `services.py`, `infrastructure.py`, `model.ts.j2`, `service.ts.j2`, `api.base.service.ts.j2`

### Phase 2: Model Generation Enhancements

**2.1 Enum Generation**
- Detect `enum` keyword in schema properties
- Generate TypeScript namespace with enum pattern:
  ```typescript
  export namespace Order {
      export const StatusEnum = {
          Placed: 'placed',
          Approved: 'approved',
          Delivered: 'delivered'
      } as const;
      export type StatusEnum = typeof StatusEnum[keyof typeof StatusEnum];
  }
  ```
- Update property type to `ModelName.EnumName`
- Files: `models.py`, `model.ts.j2`, `type_mapper.py`

**2.2 Enum JSDoc Comments**
- Extract `description` from enum properties
- Add JSDoc comment above property
- Files: `models.py`, `model.ts.j2`

**2.3 Fix models.ts Barrel**
- Remove extra blank line at end
- File: `models.ts.j2`

### Phase 3: Service Generation Fixes

**3.1 basePath Extraction**
- Extract from `servers[0].url` in OpenAPI spec
- Pass to `api.base.service.ts.j2` template
- Files: `generator.py`, `infrastructure.py`, `api.base.service.ts.j2`

**3.2 Method Name Derivation**
- Fix `operation_id_to_method_name()` to handle simple operationIds
- `addPet` should stay `addPet`, not become `addpet`
- Only apply dotted-path logic when operationId contains dots
- File: `utils/naming.py`

**3.3 Method Ordering**
- Sort methods alphabetically by method name
- File: `services.py`

**3.4 Security Credential Initialization**
- Extract `securitySchemes` from OpenAPI spec
- Generate credential initializers in `configuration.ts`
- Files: `generator.py`, `infrastructure.py`, `configuration.ts.j2`

**3.5 Security Header Injection**
- Check operation's `security` requirements
- Add `addCredentialToHeaders()` calls for oauth2/apiKey schemes
- Files: `services.py`, `service.ts.j2`

**3.6 Content-Type Handling**
- Include all content types from `requestBody.content`
- Not just `application/json`
- File: `services.py`

### Phase 4: Missing Files

**4.1 Static Files**
Create new templates:
- `.gitignore.j2` - node_modules, dist, typings, wwwroot/*.js
- `.openapi-generator-ignore.j2` - standard ignore file comments
- `git_push.sh.j2` - shell script for git operations
- `.openapi-generator/VERSION.j2` - contains `7.19.0`

**4.2 Dynamic Files**
- `README.md.j2` - uses `api_title`, `api_description`, `api_version`
- `.openapi-generator/FILES` - generated list of all output files (no template, generated in Python)

**4.3 Infrastructure Update**
- Add generation of all 6 files to `infrastructure.py`
- Create `.openapi-generator/` directory
- File: `infrastructure.py`

## Files to Modify

### Python Files
| File | Changes |
|------|---------|
| `generators/angular/generator.py` | Extract contact_email, servers, security_schemes; pass to sub-generators |
| `generators/angular/models.py` | Enum handling, contact_email, property descriptions |
| `generators/angular/services.py` | Method ordering, security headers, content types |
| `generators/angular/infrastructure.py` | basePath, missing files generation, security init |
| `generators/angular/type_mapper.py` | Enum type support |
| `utils/naming.py` | Fix operation_id_to_method_name() |

### Templates to Modify
| Template | Changes |
|----------|---------|
| `model.ts.j2` | Contact header, enum namespace, property JSDoc |
| `models.ts.j2` | Remove extra blank line |
| `service.ts.j2` | Contact header, security headers |
| `api.base.service.ts.j2` | Contact header, dynamic basePath |
| `configuration.ts.j2` | Security credential initialization |
| All templates | Ensure trailing newline |

### Templates to Add
| Template | Purpose |
|----------|---------|
| `.gitignore.j2` | Git ignore patterns |
| `.openapi-generator-ignore.j2` | Generator ignore patterns |
| `git_push.sh.j2` | Git push helper script |
| `VERSION.j2` | Generator version |
| `README.md.j2` | Package documentation |

## Success Criteria

- `pytest tests/test_fixture_comparison.py` passes for both petstore and space_zoo fixtures
- No missing files
- Byte-for-byte match with fixtures

## Notes

- Fixtures are the source of truth (per CLAUDE.md)
- Do not modify fixture files
- All changes must be to generator code and templates
