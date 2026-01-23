# SonarQubeProjectsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/sonarqube-projects/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/sonarqube-projects/{pk}/clone | Clone|
|[**create**](#create) | **POST** /api/sonarqube-projects | Create|
|[**get**](#get) | **GET** /api/sonarqube-projects/{pk} | Get|
|[**listAll**](#listall) | **GET** /api/sonarqube-projects | List All|
|[**update**](#update) | **PUT** /api/sonarqube-projects/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    SonarQubeProjectsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeProjectsApi(configuration);

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
> BiomeTypeOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    SonarQubeProjectsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeProjectsApi(configuration);

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

**BiomeTypeOut**

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
> BiomeTypeOut create(biomeTypeIn)

Create a new feeding schedule.

### Example

```typescript
import {
    SonarQubeProjectsApi,
    Configuration,
    BiomeTypeIn
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeProjectsApi(configuration);

let biomeTypeIn: BiomeTypeIn; //

const { status, data } = await apiInstance.create(
    biomeTypeIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **biomeTypeIn** | **BiomeTypeIn**|  | |


### Return type

**BiomeTypeOut**

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
> BiomeTypeOut get()

Get a feeding record.

### Example

```typescript
import {
    SonarQubeProjectsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeProjectsApi(configuration);

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

**BiomeTypeOut**

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
> Array<BiomeTypeOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    SonarQubeProjectsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeProjectsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let biomeCode: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)
let habitat: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    biomeCode,
    name,
    habitat
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **biomeCode** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **habitat** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<BiomeTypeOut>**

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
> BiomeTypeOut update(biomeTypeIn)

Update a feeding schedule.

### Example

```typescript
import {
    SonarQubeProjectsApi,
    Configuration,
    BiomeTypeIn
} from './api';

const configuration = new Configuration();
const apiInstance = new SonarQubeProjectsApi(configuration);

let pk: number; // (default to undefined)
let biomeTypeIn: BiomeTypeIn; //

const { status, data } = await apiInstance.update(
    pk,
    biomeTypeIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **biomeTypeIn** | **BiomeTypeIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**BiomeTypeOut**

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

