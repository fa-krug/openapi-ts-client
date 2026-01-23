# HTTPMetricsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](HTTPMetricsApi.md#_delete) | **DELETE** /api/http-metrics/{pk} | Delete |
| [**clone**](HTTPMetricsApi.md#clone) | **POST** /api/http-metrics/{pk}/clone | Clone |
| [**count**](HTTPMetricsApi.md#count) | **GET** /api/http-metrics/count | Count |
| [**create**](HTTPMetricsApi.md#create) | **POST** /api/http-metrics | Create |
| [**get**](HTTPMetricsApi.md#get) | **GET** /api/http-metrics/{pk} | Get |
| [**listAll**](HTTPMetricsApi.md#listall) | **GET** /api/http-metrics | List All |
| [**update**](HTTPMetricsApi.md#update) | **PUT** /api/http-metrics/{pk} | Update |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  HTTPMetricsApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HTTPMetricsApi();

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

> EnvironmentReadingOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  HTTPMetricsApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HTTPMetricsApi();

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

[**EnvironmentReadingOut**](EnvironmentReadingOut.md)

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
  HTTPMetricsApi,
} from '';
import type { CountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HTTPMetricsApi();

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

> EnvironmentReadingOut create(environmentReadingIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  HTTPMetricsApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HTTPMetricsApi();

  const body = {
    // EnvironmentReadingIn
    environmentReadingIn: ...,
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
| **environmentReadingIn** | [EnvironmentReadingIn](EnvironmentReadingIn.md) |  | |

### Return type

[**EnvironmentReadingOut**](EnvironmentReadingOut.md)

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

> EnvironmentReadingOut get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  HTTPMetricsApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HTTPMetricsApi();

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

[**EnvironmentReadingOut**](EnvironmentReadingOut.md)

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

> Array&lt;EnvironmentReadingOut&gt; listAll(id, spanId, start, end, timespanNs, habitat, url, method, version, statusCode)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  HTTPMetricsApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HTTPMetricsApi();

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
    habitat: habitat_example,
    // string | Filter by exact match (optional)
    url: url_example,
    // string | Filter by exact match (optional)
    method: method_example,
    // string | Filter by exact match (optional)
    version: version_example,
    // string | Filter by exact match (optional)
    statusCode: statusCode_example,
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
| **habitat** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **url** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **method** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **version** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **statusCode** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;EnvironmentReadingOut&gt;**](EnvironmentReadingOut.md)

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

> EnvironmentReadingOut update(pk, environmentReadingIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  HTTPMetricsApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HTTPMetricsApi();

  const body = {
    // number
    pk: 56,
    // EnvironmentReadingIn
    environmentReadingIn: ...,
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
| **environmentReadingIn** | [EnvironmentReadingIn](EnvironmentReadingIn.md) |  | |

### Return type

[**EnvironmentReadingOut**](EnvironmentReadingOut.md)

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

