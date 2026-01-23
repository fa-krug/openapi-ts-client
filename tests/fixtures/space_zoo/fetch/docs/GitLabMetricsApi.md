# GitLabMetricsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](GitLabMetricsApi.md#_delete) | **DELETE** /api/gitlab-metrics/{pk} | Delete |
| [**clone**](GitLabMetricsApi.md#clone) | **POST** /api/gitlab-metrics/{pk}/clone | Clone |
| [**count**](GitLabMetricsApi.md#count) | **GET** /api/gitlab-metrics/count | Count |
| [**create**](GitLabMetricsApi.md#create) | **POST** /api/gitlab-metrics | Create |
| [**get**](GitLabMetricsApi.md#get) | **GET** /api/gitlab-metrics/{pk} | Get |
| [**listAll**](GitLabMetricsApi.md#listall) | **GET** /api/gitlab-metrics | List All |
| [**update**](GitLabMetricsApi.md#update) | **PUT** /api/gitlab-metrics/{pk} | Update |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  GitLabMetricsApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabMetricsApi();

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

> MigrationMetricOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  GitLabMetricsApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabMetricsApi();

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

[**MigrationMetricOut**](MigrationMetricOut.md)

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
  GitLabMetricsApi,
} from '';
import type { CountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabMetricsApi();

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

> MigrationMetricOut create(migrationMetricIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  GitLabMetricsApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabMetricsApi();

  const body = {
    // MigrationMetricIn
    migrationMetricIn: ...,
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
| **migrationMetricIn** | [MigrationMetricIn](MigrationMetricIn.md) |  | |

### Return type

[**MigrationMetricOut**](MigrationMetricOut.md)

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

> MigrationMetricOut get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  GitLabMetricsApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabMetricsApi();

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

[**MigrationMetricOut**](MigrationMetricOut.md)

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

> Array&lt;MigrationMetricOut&gt; listAll(id, metricId, datetime, habitat, lastCommit, commits, lastRelease, openIssues, closedIssues, featureIssues, closedFeatureIssues, bugIssues, closedBugIssues, bugTtl, doingTime, reviewTime, codeQuality)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  GitLabMetricsApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabMetricsApi();

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
    lastCommit: lastCommit_example,
    // string | Filter by exact match (optional)
    commits: commits_example,
    // string | Filter by exact match (optional)
    lastRelease: lastRelease_example,
    // string | Filter by exact match (optional)
    openIssues: openIssues_example,
    // string | Filter by exact match (optional)
    closedIssues: closedIssues_example,
    // string | Filter by exact match (optional)
    featureIssues: featureIssues_example,
    // string | Filter by exact match (optional)
    closedFeatureIssues: closedFeatureIssues_example,
    // string | Filter by exact match (optional)
    bugIssues: bugIssues_example,
    // string | Filter by exact match (optional)
    closedBugIssues: closedBugIssues_example,
    // string | Filter by exact match (optional)
    bugTtl: bugTtl_example,
    // string | Filter by exact match (optional)
    doingTime: doingTime_example,
    // string | Filter by exact match (optional)
    reviewTime: reviewTime_example,
    // string | Filter by exact match (optional)
    codeQuality: codeQuality_example,
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
| **lastCommit** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **commits** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **lastRelease** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **openIssues** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **closedIssues** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **featureIssues** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **closedFeatureIssues** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **bugIssues** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **closedBugIssues** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **bugTtl** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **doingTime** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **reviewTime** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **codeQuality** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;MigrationMetricOut&gt;**](MigrationMetricOut.md)

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

> MigrationMetricOut update(pk, migrationMetricIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  GitLabMetricsApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabMetricsApi();

  const body = {
    // number
    pk: 56,
    // MigrationMetricIn
    migrationMetricIn: ...,
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
| **migrationMetricIn** | [MigrationMetricIn](MigrationMetricIn.md) |  | |

### Return type

[**MigrationMetricOut**](MigrationMetricOut.md)

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

