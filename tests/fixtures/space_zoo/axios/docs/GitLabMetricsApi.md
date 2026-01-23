# GitLabMetricsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/gitlab-metrics/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/gitlab-metrics/{pk}/clone | Clone|
|[**count**](#count) | **GET** /api/gitlab-metrics/count | Count|
|[**create**](#create) | **POST** /api/gitlab-metrics | Create|
|[**get**](#get) | **GET** /api/gitlab-metrics/{pk} | Get|
|[**listAll**](#listall) | **GET** /api/gitlab-metrics | List All|
|[**update**](#update) | **PUT** /api/gitlab-metrics/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    GitLabMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabMetricsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance._delete(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone**
> MigrationMetricOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    GitLabMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabMetricsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.clone(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**MigrationMetricOut**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count**
> number count()

Count all feeding records.

### Example

```typescript
import {
    GitLabMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabMetricsApi(configuration);

const { status, data } = await apiInstance.count();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**number**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> MigrationMetricOut create(migrationMetricIn)

Create a new feeding schedule.

### Example

```typescript
import {
    GitLabMetricsApi,
    Configuration,
    MigrationMetricIn
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabMetricsApi(configuration);

let migrationMetricIn: MigrationMetricIn; //

const { status, data } = await apiInstance.create(
    migrationMetricIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **migrationMetricIn** | **MigrationMetricIn**|  | |


### Return type

**MigrationMetricOut**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> MigrationMetricOut get()

Get a feeding record.

### Example

```typescript
import {
    GitLabMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabMetricsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.get(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**MigrationMetricOut**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listAll**
> Array<MigrationMetricOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    GitLabMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabMetricsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let metricId: string; //Filter by exact match (optional) (default to undefined)
let datetime: string; //Filter by exact match (optional) (default to undefined)
let habitat: string; //Filter by exact match (optional) (default to undefined)
let lastCommit: string; //Filter by exact match (optional) (default to undefined)
let commits: string; //Filter by exact match (optional) (default to undefined)
let lastRelease: string; //Filter by exact match (optional) (default to undefined)
let openIssues: string; //Filter by exact match (optional) (default to undefined)
let closedIssues: string; //Filter by exact match (optional) (default to undefined)
let featureIssues: string; //Filter by exact match (optional) (default to undefined)
let closedFeatureIssues: string; //Filter by exact match (optional) (default to undefined)
let bugIssues: string; //Filter by exact match (optional) (default to undefined)
let closedBugIssues: string; //Filter by exact match (optional) (default to undefined)
let bugTtl: string; //Filter by exact match (optional) (default to undefined)
let doingTime: string; //Filter by exact match (optional) (default to undefined)
let reviewTime: string; //Filter by exact match (optional) (default to undefined)
let codeQuality: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    metricId,
    datetime,
    habitat,
    lastCommit,
    commits,
    lastRelease,
    openIssues,
    closedIssues,
    featureIssues,
    closedFeatureIssues,
    bugIssues,
    closedBugIssues,
    bugTtl,
    doingTime,
    reviewTime,
    codeQuality
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **metricId** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **datetime** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **habitat** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **lastCommit** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **commits** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **lastRelease** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **openIssues** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **closedIssues** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **featureIssues** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **closedFeatureIssues** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **bugIssues** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **closedBugIssues** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **bugTtl** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **doingTime** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **reviewTime** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **codeQuality** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<MigrationMetricOut>**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> MigrationMetricOut update(migrationMetricIn)

Update a feeding schedule.

### Example

```typescript
import {
    GitLabMetricsApi,
    Configuration,
    MigrationMetricIn
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabMetricsApi(configuration);

let pk: number; // (default to undefined)
let migrationMetricIn: MigrationMetricIn; //

const { status, data } = await apiInstance.update(
    pk,
    migrationMetricIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **migrationMetricIn** | **MigrationMetricIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**MigrationMetricOut**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

