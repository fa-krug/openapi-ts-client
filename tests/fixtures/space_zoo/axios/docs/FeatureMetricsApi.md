# FeatureMetricsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/feature-metrics/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/feature-metrics/{pk}/clone | Clone|
|[**count**](#count) | **GET** /api/feature-metrics/count | Count|
|[**create**](#create) | **POST** /api/feature-metrics | Create|
|[**get**](#get) | **GET** /api/feature-metrics/{pk} | Get|
|[**listAll**](#listall) | **GET** /api/feature-metrics | List All|
|[**update**](#update) | **PUT** /api/feature-metrics/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    FeatureMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeatureMetricsApi(configuration);

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
> BehaviorMetricOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    FeatureMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeatureMetricsApi(configuration);

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

**BehaviorMetricOut**

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
    FeatureMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeatureMetricsApi(configuration);

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
> BehaviorMetricOut create(behaviorMetricIn)

Create a new feeding schedule.

### Example

```typescript
import {
    FeatureMetricsApi,
    Configuration,
    BehaviorMetricIn
} from './api';

const configuration = new Configuration();
const apiInstance = new FeatureMetricsApi(configuration);

let behaviorMetricIn: BehaviorMetricIn; //

const { status, data } = await apiInstance.create(
    behaviorMetricIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **behaviorMetricIn** | **BehaviorMetricIn**|  | |


### Return type

**BehaviorMetricOut**

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
> BehaviorMetricOut get()

Get a feeding record.

### Example

```typescript
import {
    FeatureMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeatureMetricsApi(configuration);

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

**BehaviorMetricOut**

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
> Array<BehaviorMetricOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    FeatureMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeatureMetricsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let spanId: string; //Filter by exact match (optional) (default to undefined)
let start: string; //Filter by exact match (optional) (default to undefined)
let end: string; //Filter by exact match (optional) (default to undefined)
let timespanNs: string; //Filter by exact match (optional) (default to undefined)
let httpMetric: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)
let value: string; //Filter by exact match (optional) (default to undefined)
let details: string; //Filter by exact match (optional) (default to undefined)
let createdBy: string; //Filter by exact match (optional) (default to undefined)
let message: string; //Filter by exact match (optional) (default to undefined)
let state: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    spanId,
    start,
    end,
    timespanNs,
    httpMetric,
    name,
    value,
    details,
    createdBy,
    message,
    state
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **spanId** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **start** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **end** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **timespanNs** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **httpMetric** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **value** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **details** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **createdBy** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **message** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **state** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<BehaviorMetricOut>**

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
> BehaviorMetricOut update(behaviorMetricIn)

Update a feeding schedule.

### Example

```typescript
import {
    FeatureMetricsApi,
    Configuration,
    BehaviorMetricIn
} from './api';

const configuration = new Configuration();
const apiInstance = new FeatureMetricsApi(configuration);

let pk: number; // (default to undefined)
let behaviorMetricIn: BehaviorMetricIn; //

const { status, data } = await apiInstance.update(
    pk,
    behaviorMetricIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **behaviorMetricIn** | **BehaviorMetricIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**BehaviorMetricOut**

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

