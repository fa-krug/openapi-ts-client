# EnclosuresApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/docker-images/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/docker-images/{pk}/clone | Clone|
|[**count**](#count) | **GET** /api/docker-images/count | Count|
|[**create**](#create) | **POST** /api/docker-images | Create|
|[**get**](#get) | **GET** /api/docker-images/{pk} | Get|
|[**listAll**](#listall) | **GET** /api/docker-images | List All|
|[**update**](#update) | **PUT** /api/docker-images/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    EnclosuresApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new EnclosuresApi(configuration);

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
> EnclosureOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    EnclosuresApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new EnclosuresApi(configuration);

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

**EnclosureOut**

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
    EnclosuresApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new EnclosuresApi(configuration);

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
> EnclosureOut create(enclosureIn)

Create a new feeding schedule.

### Example

```typescript
import {
    EnclosuresApi,
    Configuration,
    EnclosureIn
} from './api';

const configuration = new Configuration();
const apiInstance = new EnclosuresApi(configuration);

let enclosureIn: EnclosureIn; //

const { status, data } = await apiInstance.create(
    enclosureIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **enclosureIn** | **EnclosureIn**|  | |


### Return type

**EnclosureOut**

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
> EnclosureOut get()

Get a feeding record.

### Example

```typescript
import {
    EnclosuresApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new EnclosuresApi(configuration);

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

**EnclosureOut**

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
> Array<EnclosureOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    EnclosuresApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new EnclosuresApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)
let timestamp: string; //Filter by exact match (optional) (default to undefined)
let habitat: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    name,
    timestamp,
    habitat
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **timestamp** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **habitat** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<EnclosureOut>**

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
> EnclosureOut update(enclosureIn)

Update a feeding schedule.

### Example

```typescript
import {
    EnclosuresApi,
    Configuration,
    EnclosureIn
} from './api';

const configuration = new Configuration();
const apiInstance = new EnclosuresApi(configuration);

let pk: number; // (default to undefined)
let enclosureIn: EnclosureIn; //

const { status, data } = await apiInstance.update(
    pk,
    enclosureIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **enclosureIn** | **EnclosureIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**EnclosureOut**

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

