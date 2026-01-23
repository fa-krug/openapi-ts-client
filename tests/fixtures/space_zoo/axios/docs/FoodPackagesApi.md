# FoodPackagesApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/food-packages/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/food-packages/{pk}/duplicate | Clone|
|[**count**](#count) | **GET** /api/food-packages/count | Count|
|[**create**](#create) | **POST** /api/food-packages | Create|
|[**get**](#get) | **GET** /api/food-packages/{pk} | Get|
|[**listAll**](#listall) | **GET** /api/food-packages | List All|
|[**update**](#update) | **PUT** /api/food-packages/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    FoodPackagesApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FoodPackagesApi(configuration);

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
> FoodPackageOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    FoodPackagesApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FoodPackagesApi(configuration);

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

**FoodPackageOut**

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
    FoodPackagesApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FoodPackagesApi(configuration);

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
> FoodPackageOut create(foodPackageIn)

Create a new feeding schedule.

### Example

```typescript
import {
    FoodPackagesApi,
    Configuration,
    FoodPackageIn
} from './api';

const configuration = new Configuration();
const apiInstance = new FoodPackagesApi(configuration);

let foodPackageIn: FoodPackageIn; //

const { status, data } = await apiInstance.create(
    foodPackageIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **foodPackageIn** | **FoodPackageIn**|  | |


### Return type

**FoodPackageOut**

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
> FoodPackageOut get()

Get a feeding record.

### Example

```typescript
import {
    FoodPackagesApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FoodPackagesApi(configuration);

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

**FoodPackageOut**

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
> Array<FoodPackageOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    FoodPackagesApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FoodPackagesApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)
let allowedSpecifier: string; //Filter by exact match (optional) (default to undefined)
let latestVersion: string; //Filter by exact match (optional) (default to undefined)
let hidden: boolean; //Filter by exact match (optional) (default to undefined)
let allowed: boolean; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    name,
    allowedSpecifier,
    latestVersion,
    hidden,
    allowed
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **allowedSpecifier** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **latestVersion** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **hidden** | [**boolean**] | Filter by exact match | (optional) defaults to undefined|
| **allowed** | [**boolean**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<FoodPackageOut>**

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
> FoodPackageOut update(foodPackageIn)

Update a feeding schedule.

### Example

```typescript
import {
    FoodPackagesApi,
    Configuration,
    FoodPackageIn
} from './api';

const configuration = new Configuration();
const apiInstance = new FoodPackagesApi(configuration);

let pk: number; // (default to undefined)
let foodPackageIn: FoodPackageIn; //

const { status, data } = await apiInstance.update(
    pk,
    foodPackageIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **foodPackageIn** | **FoodPackageIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**FoodPackageOut**

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

