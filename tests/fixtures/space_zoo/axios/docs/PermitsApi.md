# PermitsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/permits/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/permits/{pk}/duplicate | Clone|
|[**count**](#count) | **GET** /api/permits/count | Count|
|[**create**](#create) | **POST** /api/permits | Create|
|[**get**](#get) | **GET** /api/permits/{pk} | Get|
|[**listAll**](#listall) | **GET** /api/permits | List All|
|[**update**](#update) | **PUT** /api/permits/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    PermitsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new PermitsApi(configuration);

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
> PermitOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    PermitsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new PermitsApi(configuration);

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

**PermitOut**

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
    PermitsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new PermitsApi(configuration);

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
> PermitOut create(permitIn)

Create a new feeding schedule.

### Example

```typescript
import {
    PermitsApi,
    Configuration,
    PermitIn
} from './api';

const configuration = new Configuration();
const apiInstance = new PermitsApi(configuration);

let permitIn: PermitIn; //

const { status, data } = await apiInstance.create(
    permitIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **permitIn** | **PermitIn**|  | |


### Return type

**PermitOut**

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
> PermitOut get()

Get a feeding record.

### Example

```typescript
import {
    PermitsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new PermitsApi(configuration);

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

**PermitOut**

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
> Array<PermitOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    PermitsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new PermitsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)
let allowed: boolean; //Filter by exact match (optional) (default to undefined)
let riskScore: string; //Filter by exact match (optional) (default to undefined)
let sourceUrl: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    name,
    allowed,
    riskScore,
    sourceUrl
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **allowed** | [**boolean**] | Filter by exact match | (optional) defaults to undefined|
| **riskScore** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **sourceUrl** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<PermitOut>**

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
> PermitOut update(permitIn)

Update a feeding schedule.

### Example

```typescript
import {
    PermitsApi,
    Configuration,
    PermitIn
} from './api';

const configuration = new Configuration();
const apiInstance = new PermitsApi(configuration);

let pk: number; // (default to undefined)
let permitIn: PermitIn; //

const { status, data } = await apiInstance.update(
    pk,
    permitIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **permitIn** | **PermitIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**PermitOut**

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

