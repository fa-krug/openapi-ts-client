# DBMetricsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/db-metrics/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/db-metrics/{pk}/clone | Clone|
|[**count**](#count) | **GET** /api/db-metrics/count | Count|
|[**create**](#create) | **POST** /api/db-metrics | Create|
|[**get**](#get) | **GET** /api/db-metrics/{pk} | Get|
|[**listAll**](#listall) | **GET** /api/db-metrics | List All|
|[**update**](#update) | **PUT** /api/db-metrics/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    DBMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new DBMetricsApi(configuration);

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
> NutritionMetricOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    DBMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new DBMetricsApi(configuration);

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

**NutritionMetricOut**

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
    DBMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new DBMetricsApi(configuration);

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
> NutritionMetricOut create(nutritionMetricIn)

Create a new feeding schedule.

### Example

```typescript
import {
    DBMetricsApi,
    Configuration,
    NutritionMetricIn
} from './api';

const configuration = new Configuration();
const apiInstance = new DBMetricsApi(configuration);

let nutritionMetricIn: NutritionMetricIn; //

const { status, data } = await apiInstance.create(
    nutritionMetricIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **nutritionMetricIn** | **NutritionMetricIn**|  | |


### Return type

**NutritionMetricOut**

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
> NutritionMetricOut get()

Get a feeding record.

### Example

```typescript
import {
    DBMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new DBMetricsApi(configuration);

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

**NutritionMetricOut**

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
> Array<NutritionMetricOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    DBMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new DBMetricsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let spanId: string; //Filter by exact match (optional) (default to undefined)
let start: string; //Filter by exact match (optional) (default to undefined)
let end: string; //Filter by exact match (optional) (default to undefined)
let timespanNs: string; //Filter by exact match (optional) (default to undefined)
let type: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)
let statement: string; //Filter by exact match (optional) (default to undefined)
let httpMetric: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    spanId,
    start,
    end,
    timespanNs,
    type,
    name,
    statement,
    httpMetric
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
| **type** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **statement** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **httpMetric** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<NutritionMetricOut>**

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
> NutritionMetricOut update(nutritionMetricIn)

Update a feeding schedule.

### Example

```typescript
import {
    DBMetricsApi,
    Configuration,
    NutritionMetricIn
} from './api';

const configuration = new Configuration();
const apiInstance = new DBMetricsApi(configuration);

let pk: number; // (default to undefined)
let nutritionMetricIn: NutritionMetricIn; //

const { status, data } = await apiInstance.update(
    pk,
    nutritionMetricIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **nutritionMetricIn** | **NutritionMetricIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**NutritionMetricOut**

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

