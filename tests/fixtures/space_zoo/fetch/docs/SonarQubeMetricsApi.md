# SonarQubeMetricsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](SonarQubeMetricsApi.md#_delete) | **DELETE** /api/sonarqube-metrics/{pk} | Delete |
| [**clone**](SonarQubeMetricsApi.md#clone) | **POST** /api/sonarqube-metrics/{pk}/clone | Clone |
| [**count**](SonarQubeMetricsApi.md#count) | **GET** /api/sonarqube-metrics/count | Count |
| [**create**](SonarQubeMetricsApi.md#create) | **POST** /api/sonarqube-metrics | Create |
| [**get**](SonarQubeMetricsApi.md#get) | **GET** /api/sonarqube-metrics/{pk} | Get |
| [**listAll**](SonarQubeMetricsApi.md#listall) | **GET** /api/sonarqube-metrics | List All |
| [**update**](SonarQubeMetricsApi.md#update) | **PUT** /api/sonarqube-metrics/{pk} | Update |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  SonarQubeMetricsApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SonarQubeMetricsApi();

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

> WellnessMetricOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  SonarQubeMetricsApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SonarQubeMetricsApi();

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

[**WellnessMetricOut**](WellnessMetricOut.md)

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
  SonarQubeMetricsApi,
} from '';
import type { CountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SonarQubeMetricsApi();

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

> WellnessMetricOut create(wellnessMetricIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  SonarQubeMetricsApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SonarQubeMetricsApi();

  const body = {
    // WellnessMetricIn
    wellnessMetricIn: ...,
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
| **wellnessMetricIn** | [WellnessMetricIn](WellnessMetricIn.md) |  | |

### Return type

[**WellnessMetricOut**](WellnessMetricOut.md)

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

> WellnessMetricOut get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  SonarQubeMetricsApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SonarQubeMetricsApi();

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

[**WellnessMetricOut**](WellnessMetricOut.md)

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

> Array&lt;WellnessMetricOut&gt; listAll(id, metricId, datetime, habitat, linesOfCode, testCoverage, codeDuplication, reliabilityRating, securityRating, securityReviewRating, maintainabilityRating)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  SonarQubeMetricsApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SonarQubeMetricsApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    metricId: metricId_example,
    // string | Filter by exact match (optional)
    datetime: datetime_example,
    // string | Filter by exact match (optional)
    habitat: habitat_example,
    // string | Filter by exact match (optional)
    linesOfCode: linesOfCode_example,
    // string | Filter by exact match (optional)
    testCoverage: testCoverage_example,
    // string | Filter by exact match (optional)
    codeDuplication: codeDuplication_example,
    // string | Filter by exact match (optional)
    reliabilityRating: reliabilityRating_example,
    // string | Filter by exact match (optional)
    securityRating: securityRating_example,
    // string | Filter by exact match (optional)
    securityReviewRating: securityReviewRating_example,
    // string | Filter by exact match (optional)
    maintainabilityRating: maintainabilityRating_example,
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
| **metricId** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **datetime** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **habitat** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **linesOfCode** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **testCoverage** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **codeDuplication** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **reliabilityRating** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **securityRating** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **securityReviewRating** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **maintainabilityRating** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;WellnessMetricOut&gt;**](WellnessMetricOut.md)

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

> WellnessMetricOut update(pk, wellnessMetricIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  SonarQubeMetricsApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SonarQubeMetricsApi();

  const body = {
    // number
    pk: 56,
    // WellnessMetricIn
    wellnessMetricIn: ...,
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
| **wellnessMetricIn** | [WellnessMetricIn](WellnessMetricIn.md) |  | |

### Return type

[**WellnessMetricOut**](WellnessMetricOut.md)

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

