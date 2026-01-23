# CarePlansApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**plansClone**](#plansclone) | **POST** /api/care-plans/{pk}/duplicate | Clone|
|[**plansCount**](#planscount) | **GET** /api/care-plans/count | Count|
|[**plansCreate**](#planscreate) | **POST** /api/care-plans | Create|
|[**plansDelete**](#plansdelete) | **DELETE** /api/care-plans/{pk} | Delete|
|[**plansGet**](#plansget) | **GET** /api/care-plans/{pk} | Get|
|[**plansListAll**](#planslistall) | **GET** /api/care-plans | List All|
|[**plansListNames**](#planslistnames) | **GET** /api/care-plans/names | List Names|
|[**plansUpdate**](#plansupdate) | **PUT** /api/care-plans/{pk} | Update|

# **plansClone**
> CarePlanOut plansClone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    CarePlansApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new CarePlansApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.plansClone(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**CarePlanOut**

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

# **plansCount**
> number plansCount()

Count all feeding records.

### Example

```typescript
import {
    CarePlansApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new CarePlansApi(configuration);

const { status, data } = await apiInstance.plansCount();
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

# **plansCreate**
> CarePlanOut plansCreate(carePlanIn)

Create a new feeding schedule.

### Example

```typescript
import {
    CarePlansApi,
    Configuration,
    CarePlanIn
} from './api';

const configuration = new Configuration();
const apiInstance = new CarePlansApi(configuration);

let carePlanIn: CarePlanIn; //

const { status, data } = await apiInstance.plansCreate(
    carePlanIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **carePlanIn** | **CarePlanIn**|  | |


### Return type

**CarePlanOut**

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

# **plansDelete**
> plansDelete()

Remove a feeding schedule.

### Example

```typescript
import {
    CarePlansApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new CarePlansApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.plansDelete(
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

# **plansGet**
> CarePlanOut plansGet()

Get a feeding record.

### Example

```typescript
import {
    CarePlansApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new CarePlansApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.plansGet(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**CarePlanOut**

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

# **plansListAll**
> Array<CarePlanOut> plansListAll()

List all feeding schedules.

### Example

```typescript
import {
    CarePlansApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new CarePlansApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)
let content: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.plansListAll(
    id,
    name,
    content
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **content** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<CarePlanOut>**

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

# **plansListNames**
> Array<CarePlanNames> plansListNames()

List all names.

### Example

```typescript
import {
    CarePlansApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new CarePlansApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)
let content: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.plansListNames(
    id,
    name,
    content
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **content** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<CarePlanNames>**

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

# **plansUpdate**
> CarePlanOut plansUpdate(carePlanIn)

Update a feeding schedule.

### Example

```typescript
import {
    CarePlansApi,
    Configuration,
    CarePlanIn
} from './api';

const configuration = new Configuration();
const apiInstance = new CarePlansApi(configuration);

let pk: number; // (default to undefined)
let carePlanIn: CarePlanIn; //

const { status, data } = await apiInstance.plansUpdate(
    pk,
    carePlanIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **carePlanIn** | **CarePlanIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**CarePlanOut**

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

