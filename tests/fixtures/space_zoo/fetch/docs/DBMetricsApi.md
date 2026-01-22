# DBMetricsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](DBMetricsApi.md#_delete) | **DELETE** /api/db-metrics/{pk} | Delete |
| [**clone**](DBMetricsApi.md#clone) | **POST** /api/db-metrics/{pk}/clone | Clone |
| [**count**](DBMetricsApi.md#count) | **GET** /api/db-metrics/count | Count |
| [**create**](DBMetricsApi.md#create) | **POST** /api/db-metrics | Create |
| [**get**](DBMetricsApi.md#get) | **GET** /api/db-metrics/{pk} | Get |
| [**listAll**](DBMetricsApi.md#listall) | **GET** /api/db-metrics | List All |
| [**update**](DBMetricsApi.md#update) | **PUT** /api/db-metrics/{pk} | Update |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  DBMetricsApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DBMetricsApi();

  const body = {
    // number
    pk: 56,
  } satisfies DeleteRequest;

  try {
    const data = await api._delete(body);
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


## clone

> NutritionMetricOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  DBMetricsApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DBMetricsApi();

  const body = {
    // number
    pk: 56,
  } satisfies CloneRequest;

  try {
    const data = await api.clone(body);
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

[**NutritionMetricOut**](NutritionMetricOut.md)

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


## count

> number count()

Count

Count all feeding records.

### Example

```ts
import {
  Configuration,
  DBMetricsApi,
} from '';
import type { CountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DBMetricsApi();

  try {
    const data = await api.count();
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


## create

> NutritionMetricOut create(nutritionMetricIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  DBMetricsApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DBMetricsApi();

  const body = {
    // NutritionMetricIn
    nutritionMetricIn: ...,
  } satisfies CreateRequest;

  try {
    const data = await api.create(body);
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
| **nutritionMetricIn** | [NutritionMetricIn](NutritionMetricIn.md) |  | |

### Return type

[**NutritionMetricOut**](NutritionMetricOut.md)

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


## get

> NutritionMetricOut get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  DBMetricsApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DBMetricsApi();

  const body = {
    // number
    pk: 56,
  } satisfies GetRequest;

  try {
    const data = await api.get(body);
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

[**NutritionMetricOut**](NutritionMetricOut.md)

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


## listAll

> Array&lt;NutritionMetricOut&gt; listAll(id, spanId, start, end, timespanNs, type, name, statement, httpMetric)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  DBMetricsApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DBMetricsApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    spanId: spanId_example,
    // string | Filter by exact match (optional)
    start: start_example,
    // string | Filter by exact match (optional)
    end: end_example,
    // string | Filter by exact match (optional)
    timespanNs: timespanNs_example,
    // string | Filter by exact match (optional)
    type: type_example,
    // string | Filter by exact match (optional)
    name: name_example,
    // string | Filter by exact match (optional)
    statement: statement_example,
    // string | Filter by exact match (optional)
    httpMetric: httpMetric_example,
  } satisfies ListAllRequest;

  try {
    const data = await api.listAll(body);
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
| **spanId** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **start** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **end** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **timespanNs** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **type** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **name** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **statement** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **httpMetric** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;NutritionMetricOut&gt;**](NutritionMetricOut.md)

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


## update

> NutritionMetricOut update(pk, nutritionMetricIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  DBMetricsApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DBMetricsApi();

  const body = {
    // number
    pk: 56,
    // NutritionMetricIn
    nutritionMetricIn: ...,
  } satisfies UpdateRequest;

  try {
    const data = await api.update(body);
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
| **nutritionMetricIn** | [NutritionMetricIn](NutritionMetricIn.md) |  | |

### Return type

[**NutritionMetricOut**](NutritionMetricOut.md)

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

