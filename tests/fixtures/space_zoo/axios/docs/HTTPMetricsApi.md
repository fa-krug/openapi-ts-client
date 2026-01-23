# HTTPMetricsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/http-metrics/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/http-metrics/{pk}/clone | Clone|
|[**count**](#count) | **GET** /api/http-metrics/count | Count|
|[**create**](#create) | **POST** /api/http-metrics | Create|
|[**get**](#get) | **GET** /api/http-metrics/{pk} | Get|
|[**listAll**](#listall) | **GET** /api/http-metrics | List All|
|[**update**](#update) | **PUT** /api/http-metrics/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    HTTPMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HTTPMetricsApi(configuration);

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
> EnvironmentReadingOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    HTTPMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HTTPMetricsApi(configuration);

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

**EnvironmentReadingOut**

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
    HTTPMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HTTPMetricsApi(configuration);

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
> EnvironmentReadingOut create(environmentReadingIn)

Create a new feeding schedule.

### Example

```typescript
import {
    HTTPMetricsApi,
    Configuration,
    EnvironmentReadingIn
} from './api';

const configuration = new Configuration();
const apiInstance = new HTTPMetricsApi(configuration);

let environmentReadingIn: EnvironmentReadingIn; //

const { status, data } = await apiInstance.create(
    environmentReadingIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **environmentReadingIn** | **EnvironmentReadingIn**|  | |


### Return type

**EnvironmentReadingOut**

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
> EnvironmentReadingOut get()

Get a feeding record.

### Example

```typescript
import {
    HTTPMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HTTPMetricsApi(configuration);

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

**EnvironmentReadingOut**

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
> Array<EnvironmentReadingOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    HTTPMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HTTPMetricsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let spanId: string; //Filter by exact match (optional) (default to undefined)
let start: string; //Filter by exact match (optional) (default to undefined)
let end: string; //Filter by exact match (optional) (default to undefined)
let timespanNs: string; //Filter by exact match (optional) (default to undefined)
let habitat: string; //Filter by exact match (optional) (default to undefined)
let url: string; //Filter by exact match (optional) (default to undefined)
let method: string; //Filter by exact match (optional) (default to undefined)
let version: string; //Filter by exact match (optional) (default to undefined)
let statusCode: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    spanId,
    start,
    end,
    timespanNs,
    habitat,
    url,
    method,
    version,
    statusCode
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
| **habitat** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **url** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **method** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **version** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **statusCode** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<EnvironmentReadingOut>**

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
> EnvironmentReadingOut update(environmentReadingIn)

Update a feeding schedule.

### Example

```typescript
import {
    HTTPMetricsApi,
    Configuration,
    EnvironmentReadingIn
} from './api';

const configuration = new Configuration();
const apiInstance = new HTTPMetricsApi(configuration);

let pk: number; // (default to undefined)
let environmentReadingIn: EnvironmentReadingIn; //

const { status, data } = await apiInstance.update(
    pk,
    environmentReadingIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **environmentReadingIn** | **EnvironmentReadingIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**EnvironmentReadingOut**

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

