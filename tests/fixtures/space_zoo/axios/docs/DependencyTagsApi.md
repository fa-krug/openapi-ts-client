# DependencyTagsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/dependency-tags/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/dependency-tags/{pk}/clone | Clone|
|[**count**](#count) | **GET** /api/dependency-tags/count | Count|
|[**create**](#create) | **POST** /api/dependency-tags | Create|
|[**get**](#get) | **GET** /api/dependency-tags/{pk} | Get|
|[**listAll**](#listall) | **GET** /api/dependency-tags | List All|
|[**listNames**](#listnames) | **GET** /api/dependency-tags/names | List Names|
|[**update**](#update) | **PUT** /api/dependency-tags/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    DependencyTagsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new DependencyTagsApi(configuration);

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
> SupplyCategoryOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    DependencyTagsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new DependencyTagsApi(configuration);

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

**SupplyCategoryOut**

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
    DependencyTagsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new DependencyTagsApi(configuration);

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
> SupplyCategoryOut create(supplyCategoryIn)

Create a new feeding schedule.

### Example

```typescript
import {
    DependencyTagsApi,
    Configuration,
    SupplyCategoryIn
} from './api';

const configuration = new Configuration();
const apiInstance = new DependencyTagsApi(configuration);

let supplyCategoryIn: SupplyCategoryIn; //

const { status, data } = await apiInstance.create(
    supplyCategoryIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **supplyCategoryIn** | **SupplyCategoryIn**|  | |


### Return type

**SupplyCategoryOut**

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
> SupplyCategoryOut get()

Get a feeding record.

### Example

```typescript
import {
    DependencyTagsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new DependencyTagsApi(configuration);

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

**SupplyCategoryOut**

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
> Array<SupplyCategoryOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    DependencyTagsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new DependencyTagsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    name
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<SupplyCategoryOut>**

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

# **listNames**
> Array<SupplyCategoryNames> listNames()

List all names.

### Example

```typescript
import {
    DependencyTagsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new DependencyTagsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listNames(
    id,
    name
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<SupplyCategoryNames>**

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
> SupplyCategoryOut update(supplyCategoryIn)

Update a feeding schedule.

### Example

```typescript
import {
    DependencyTagsApi,
    Configuration,
    SupplyCategoryIn
} from './api';

const configuration = new Configuration();
const apiInstance = new DependencyTagsApi(configuration);

let pk: number; // (default to undefined)
let supplyCategoryIn: SupplyCategoryIn; //

const { status, data } = await apiInstance.update(
    pk,
    supplyCategoryIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **supplyCategoryIn** | **SupplyCategoryIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**SupplyCategoryOut**

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

