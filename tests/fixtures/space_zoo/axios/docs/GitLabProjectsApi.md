# GitLabProjectsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/gitlab-projects/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/gitlab-projects/{pk}/clone | Clone|
|[**create**](#create) | **POST** /api/gitlab-projects | Create|
|[**get**](#get) | **GET** /api/gitlab-projects/{pk} | Get|
|[**listAll**](#listall) | **GET** /api/gitlab-projects | List All|
|[**update**](#update) | **PUT** /api/gitlab-projects/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    GitLabProjectsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabProjectsApi(configuration);

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
> OriginPlanetOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    GitLabProjectsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabProjectsApi(configuration);

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

**OriginPlanetOut**

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
> OriginPlanetOut create(originPlanetIn)

Create a new feeding schedule.

### Example

```typescript
import {
    GitLabProjectsApi,
    Configuration,
    OriginPlanetIn
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabProjectsApi(configuration);

let originPlanetIn: OriginPlanetIn; //

const { status, data } = await apiInstance.create(
    originPlanetIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **originPlanetIn** | **OriginPlanetIn**|  | |


### Return type

**OriginPlanetOut**

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
> OriginPlanetOut get()

Get a feeding record.

### Example

```typescript
import {
    GitLabProjectsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabProjectsApi(configuration);

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

**OriginPlanetOut**

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
> Array<OriginPlanetOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    GitLabProjectsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabProjectsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)
let habitat: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    name,
    habitat
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **habitat** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<OriginPlanetOut>**

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
> OriginPlanetOut update(originPlanetIn)

Update a feeding schedule.

### Example

```typescript
import {
    GitLabProjectsApi,
    Configuration,
    OriginPlanetIn
} from './api';

const configuration = new Configuration();
const apiInstance = new GitLabProjectsApi(configuration);

let pk: number; // (default to undefined)
let originPlanetIn: OriginPlanetIn; //

const { status, data } = await apiInstance.update(
    pk,
    originPlanetIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **originPlanetIn** | **OriginPlanetIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**OriginPlanetOut**

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

