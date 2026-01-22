# CarePlansApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**plansClone**](CarePlansApi.md#plansclone) | **POST** /api/care-plans/{pk}/duplicate | Clone |
| [**plansCount**](CarePlansApi.md#planscount) | **GET** /api/care-plans/count | Count |
| [**plansCreate**](CarePlansApi.md#planscreate) | **POST** /api/care-plans | Create |
| [**plansDelete**](CarePlansApi.md#plansdelete) | **DELETE** /api/care-plans/{pk} | Delete |
| [**plansGet**](CarePlansApi.md#plansget) | **GET** /api/care-plans/{pk} | Get |
| [**plansListAll**](CarePlansApi.md#planslistall) | **GET** /api/care-plans | List All |
| [**plansListNames**](CarePlansApi.md#planslistnames) | **GET** /api/care-plans/names | List Names |
| [**plansUpdate**](CarePlansApi.md#plansupdate) | **PUT** /api/care-plans/{pk} | Update |



## plansClone

> CarePlanOut plansClone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  CarePlansApi,
} from '';
import type { PlansCloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new CarePlansApi();

  const body = {
    // number
    pk: 56,
  } satisfies PlansCloneRequest;

  try {
    const data = await api.plansClone(body);
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

[**CarePlanOut**](CarePlanOut.md)

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


## plansCount

> number plansCount()

Count

Count all feeding records.

### Example

```ts
import {
  Configuration,
  CarePlansApi,
} from '';
import type { PlansCountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new CarePlansApi();

  try {
    const data = await api.plansCount();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**number**

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


## plansCreate

> CarePlanOut plansCreate(carePlanIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  CarePlansApi,
} from '';
import type { PlansCreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new CarePlansApi();

  const body = {
    // CarePlanIn
    carePlanIn: ...,
  } satisfies PlansCreateRequest;

  try {
    const data = await api.plansCreate(body);
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
| **carePlanIn** | [CarePlanIn](CarePlanIn.md) |  | |

### Return type

[**CarePlanOut**](CarePlanOut.md)

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


## plansDelete

> plansDelete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  CarePlansApi,
} from '';
import type { PlansDeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new CarePlansApi();

  const body = {
    // number
    pk: 56,
  } satisfies PlansDeleteRequest;

  try {
    const data = await api.plansDelete(body);
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


## plansGet

> CarePlanOut plansGet(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  CarePlansApi,
} from '';
import type { PlansGetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new CarePlansApi();

  const body = {
    // number
    pk: 56,
  } satisfies PlansGetRequest;

  try {
    const data = await api.plansGet(body);
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

[**CarePlanOut**](CarePlanOut.md)

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


## plansListAll

> Array&lt;CarePlanOut&gt; plansListAll(id, name, content)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  CarePlansApi,
} from '';
import type { PlansListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new CarePlansApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    name: name_example,
    // string | Filter by exact match (optional)
    content: content_example,
  } satisfies PlansListAllRequest;

  try {
    const data = await api.plansListAll(body);
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
| **name** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **content** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;CarePlanOut&gt;**](CarePlanOut.md)

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


## plansListNames

> Array&lt;CarePlanNames&gt; plansListNames(id, name, content)

List Names

List all names.

### Example

```ts
import {
  Configuration,
  CarePlansApi,
} from '';
import type { PlansListNamesRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new CarePlansApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    name: name_example,
    // string | Filter by exact match (optional)
    content: content_example,
  } satisfies PlansListNamesRequest;

  try {
    const data = await api.plansListNames(body);
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
| **name** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **content** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;CarePlanNames&gt;**](CarePlanNames.md)

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


## plansUpdate

> CarePlanOut plansUpdate(pk, carePlanIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  CarePlansApi,
} from '';
import type { PlansUpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new CarePlansApi();

  const body = {
    // number
    pk: 56,
    // CarePlanIn
    carePlanIn: ...,
  } satisfies PlansUpdateRequest;

  try {
    const data = await api.plansUpdate(body);
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
| **carePlanIn** | [CarePlanIn](CarePlanIn.md) |  | |

### Return type

[**CarePlanOut**](CarePlanOut.md)

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

