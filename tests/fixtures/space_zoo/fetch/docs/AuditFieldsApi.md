# AuditFieldsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**criteriaClone**](AuditFieldsApi.md#criteriaclone) | **POST** /api/audit-fields/{pk}/clone | Clone |
| [**criteriaCreate**](AuditFieldsApi.md#criteriacreate) | **POST** /api/audit-fields | Create |
| [**criteriaDelete**](AuditFieldsApi.md#criteriadelete) | **DELETE** /api/audit-fields/{pk} | Delete |
| [**criteriaGet**](AuditFieldsApi.md#criteriaget) | **GET** /api/audit-fields/{pk} | Get |
| [**criteriaListAll**](AuditFieldsApi.md#criterialistall) | **GET** /api/audit-fields | List All |
| [**criteriaUpdate**](AuditFieldsApi.md#criteriaupdate) | **PUT** /api/audit-fields/{pk} | Update |



## criteriaClone

> InspectionCriteriaIn criteriaClone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  AuditFieldsApi,
} from '';
import type { CriteriaCloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new AuditFieldsApi();

  const body = {
    // number
    pk: 56,
  } satisfies CriteriaCloneRequest;

  try {
    const data = await api.criteriaClone(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |

### Return type

[**InspectionCriteriaIn**](InspectionCriteriaIn.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## criteriaCreate

> InspectionCriteriaOut criteriaCreate(inspectionCriteriaIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  AuditFieldsApi,
} from '';
import type { CriteriaCreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new AuditFieldsApi();

  const body = {
    // InspectionCriteriaIn
    inspectionCriteriaIn: ...,
  } satisfies CriteriaCreateRequest;

  try {
    const data = await api.criteriaCreate(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **inspectionCriteriaIn** | [InspectionCriteriaIn](InspectionCriteriaIn.md) |  | |

### Return type

[**InspectionCriteriaOut**](InspectionCriteriaOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## criteriaDelete

> criteriaDelete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  AuditFieldsApi,
} from '';
import type { CriteriaDeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new AuditFieldsApi();

  const body = {
    // number
    pk: 56,
  } satisfies CriteriaDeleteRequest;

  try {
    const data = await api.criteriaDelete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## criteriaGet

> InspectionCriteriaOut criteriaGet(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  AuditFieldsApi,
} from '';
import type { CriteriaGetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new AuditFieldsApi();

  const body = {
    // number
    pk: 56,
  } satisfies CriteriaGetRequest;

  try {
    const data = await api.criteriaGet(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |

### Return type

[**InspectionCriteriaOut**](InspectionCriteriaOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## criteriaListAll

> Array&lt;InspectionCriteriaOut&gt; criteriaListAll(id, text, audit, type, kwargs, info, value, score, section, visible)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  AuditFieldsApi,
} from '';
import type { CriteriaListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new AuditFieldsApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    text: text_example,
    // string | Filter by exact match (optional)
    audit: audit_example,
    // string | Filter by exact match (optional)
    type: type_example,
    // string | Filter by exact match (optional)
    kwargs: kwargs_example,
    // string | Filter by exact match (optional)
    info: info_example,
    // string | Filter by exact match (optional)
    value: value_example,
    // string | Filter by exact match (optional)
    score: score_example,
    // string | Filter by exact match (optional)
    section: section_example,
    // boolean | Filter by exact match (optional)
    visible: true,
  } satisfies CriteriaListAllRequest;

  try {
    const data = await api.criteriaListAll(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **text** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **audit** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **type** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **kwargs** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **info** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **value** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **score** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **section** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **visible** | `boolean` | Filter by exact match | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;InspectionCriteriaOut&gt;**](InspectionCriteriaOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## criteriaUpdate

> InspectionCriteriaOut criteriaUpdate(pk, inspectionCriteriaIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  AuditFieldsApi,
} from '';
import type { CriteriaUpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new AuditFieldsApi();

  const body = {
    // number
    pk: 56,
    // InspectionCriteriaIn
    inspectionCriteriaIn: ...,
  } satisfies CriteriaUpdateRequest;

  try {
    const data = await api.criteriaUpdate(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |
| **inspectionCriteriaIn** | [InspectionCriteriaIn](InspectionCriteriaIn.md) |  | |

### Return type

[**InspectionCriteriaOut**](InspectionCriteriaOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

