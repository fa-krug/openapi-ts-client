# SonarQubeMetricsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/sonarqube-metrics/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/sonarqube-metrics/{pk}/clone | Clone|
|[**count**](#count) | **GET** /api/sonarqube-metrics/count | Count|
|[**create**](#create) | **POST** /api/sonarqube-metrics | Create|
|[**get**](#get) | **GET** /api/sonarqube-metrics/{pk} | Get|
|[**listAll**](#listall) | **GET** /api/sonarqube-metrics | List All|
|[**update**](#update) | **PUT** /api/sonarqube-metrics/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    SonarQubeMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeMetricsApi(configuration);

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
> WellnessMetricOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    SonarQubeMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeMetricsApi(configuration);

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

**WellnessMetricOut**

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
    SonarQubeMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeMetricsApi(configuration);

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
> WellnessMetricOut create(wellnessMetricIn)

Create a new feeding schedule.

### Example

```typescript
import {
    SonarQubeMetricsApi,
    Configuration,
    WellnessMetricIn
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeMetricsApi(configuration);

let wellnessMetricIn: WellnessMetricIn; //

const { status, data } = await apiInstance.create(
    wellnessMetricIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **wellnessMetricIn** | **WellnessMetricIn**|  | |


### Return type

**WellnessMetricOut**

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
> WellnessMetricOut get()

Get a feeding record.

### Example

```typescript
import {
    SonarQubeMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeMetricsApi(configuration);

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

**WellnessMetricOut**

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
> Array<WellnessMetricOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    SonarQubeMetricsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeMetricsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let metricId: string; //Filter by exact match (optional) (default to undefined)
let datetime: string; //Filter by exact match (optional) (default to undefined)
let habitat: string; //Filter by exact match (optional) (default to undefined)
let linesOfCode: string; //Filter by exact match (optional) (default to undefined)
let testCoverage: string; //Filter by exact match (optional) (default to undefined)
let codeDuplication: string; //Filter by exact match (optional) (default to undefined)
let reliabilityRating: string; //Filter by exact match (optional) (default to undefined)
let securityRating: string; //Filter by exact match (optional) (default to undefined)
let securityReviewRating: string; //Filter by exact match (optional) (default to undefined)
let maintainabilityRating: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    metricId,
    datetime,
    habitat,
    linesOfCode,
    testCoverage,
    codeDuplication,
    reliabilityRating,
    securityRating,
    securityReviewRating,
    maintainabilityRating
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **metricId** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **datetime** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **habitat** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **linesOfCode** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **testCoverage** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **codeDuplication** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **reliabilityRating** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **securityRating** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **securityReviewRating** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **maintainabilityRating** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<WellnessMetricOut>**

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
> WellnessMetricOut update(wellnessMetricIn)

Update a feeding schedule.

### Example

```typescript
import {
    SonarQubeMetricsApi,
    Configuration,
    WellnessMetricIn
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeMetricsApi(configuration);

let pk: number; // (default to undefined)
let wellnessMetricIn: WellnessMetricIn; //

const { status, data } = await apiInstance.update(
    pk,
    wellnessMetricIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **wellnessMetricIn** | **WellnessMetricIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**WellnessMetricOut**

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

