# FeatureMetricsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](FeatureMetricsApi.md#_delete) | **DELETE** /api/feature-metrics/{pk} | Delete |
| [**clone**](FeatureMetricsApi.md#clone) | **POST** /api/feature-metrics/{pk}/clone | Clone |
| [**count**](FeatureMetricsApi.md#count) | **GET** /api/feature-metrics/count | Count |
| [**create**](FeatureMetricsApi.md#create) | **POST** /api/feature-metrics | Create |
| [**get**](FeatureMetricsApi.md#get) | **GET** /api/feature-metrics/{pk} | Get |
| [**listAll**](FeatureMetricsApi.md#listall) | **GET** /api/feature-metrics | List All |
| [**update**](FeatureMetricsApi.md#update) | **PUT** /api/feature-metrics/{pk} | Update |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  FeatureMetricsApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeatureMetricsApi();

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

> BehaviorMetricOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  FeatureMetricsApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeatureMetricsApi();

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

[**BehaviorMetricOut**](BehaviorMetricOut.md)

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
  FeatureMetricsApi,
} from '';
import type { CountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeatureMetricsApi();

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

> BehaviorMetricOut create(behaviorMetricIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  FeatureMetricsApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeatureMetricsApi();

  const body = {
    // BehaviorMetricIn
    behaviorMetricIn: ...,
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
| **behaviorMetricIn** | [BehaviorMetricIn](BehaviorMetricIn.md) |  | |

### Return type

[**BehaviorMetricOut**](BehaviorMetricOut.md)

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

> BehaviorMetricOut get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  FeatureMetricsApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeatureMetricsApi();

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

[**BehaviorMetricOut**](BehaviorMetricOut.md)

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

> Array&lt;BehaviorMetricOut&gt; listAll(id, spanId, start, end, timespanNs, httpMetric, name, value, details, createdBy, message, state)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  FeatureMetricsApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeatureMetricsApi();

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
    httpMetric: httpMetric_example,
    // string | Filter by exact match (optional)
    name: name_example,
    // string | Filter by exact match (optional)
    value: value_example,
    // string | Filter by exact match (optional)
    details: details_example,
    // string | Filter by exact match (optional)
    createdBy: createdBy_example,
    // string | Filter by exact match (optional)
    message: message_example,
    // string | Filter by exact match (optional)
    state: state_example,
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
| **httpMetric** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **name** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **value** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **details** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **createdBy** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **message** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **state** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;BehaviorMetricOut&gt;**](BehaviorMetricOut.md)

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

> BehaviorMetricOut update(pk, behaviorMetricIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  FeatureMetricsApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeatureMetricsApi();

  const body = {
    // number
    pk: 56,
    // BehaviorMetricIn
    behaviorMetricIn: ...,
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
| **behaviorMetricIn** | [BehaviorMetricIn](BehaviorMetricIn.md) |  | |

### Return type

[**BehaviorMetricOut**](BehaviorMetricOut.md)

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

