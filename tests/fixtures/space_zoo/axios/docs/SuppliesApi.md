# SuppliesApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/supplies/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/supplies/{pk}/duplicate | Clone|
|[**count**](#count) | **GET** /api/supplies/count | Count|
|[**create**](#create) | **POST** /api/supplies | Create|
|[**get**](#get) | **GET** /api/supplies/{pk} | Get|
|[**listAll**](#listall) | **GET** /api/supplies | List All|
|[**update**](#update) | **PUT** /api/supplies/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    SuppliesApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SuppliesApi(configuration);

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
> SupplyOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    SuppliesApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SuppliesApi(configuration);

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

**SupplyOut**

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
    SuppliesApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SuppliesApi(configuration);

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
> SupplyOut create(supplyIn)

Create a new feeding schedule.

### Example

```typescript
import {
    SuppliesApi,
    Configuration,
    SupplyIn
} from './api';

const configuration = new Configuration();
const apiInstance = new SuppliesApi(configuration);

let supplyIn: SupplyIn; //

const { status, data } = await apiInstance.create(
    supplyIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **supplyIn** | **SupplyIn**|  | |


### Return type

**SupplyOut**

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
> SupplyDetails get()

Get a feeding record.

### Example

```typescript
import {
    SuppliesApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SuppliesApi(configuration);

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

**SupplyDetails**

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
> Array<SupplyOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    SuppliesApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new SuppliesApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let purl: string; //Filter by exact match (optional) (default to undefined)
let _package: string; //Filter by exact match (optional) (default to undefined)
let version: string; //Filter by exact match (optional) (default to undefined)
let image: string; //Filter by exact match (optional) (default to undefined)
let bomRef: string; //Filter by exact match (optional) (default to undefined)
let type: string; //Filter by exact match (optional) (default to undefined)
let author: string; //Filter by exact match (optional) (default to undefined)
let riskScore: string; //Filter by exact match (optional) (default to undefined)
let riskDetails: string; //Filter by exact match (optional) (default to undefined)
let licenses: Array<number>; // (optional) (default to undefined)
let dependsOn: Array<number>; // (optional) (default to undefined)
let tags: Array<number>; // (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    purl,
    _package,
    version,
    image,
    bomRef,
    type,
    author,
    riskScore,
    riskDetails,
    licenses,
    dependsOn,
    tags
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **purl** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **_package** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **version** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **image** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **bomRef** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **type** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **author** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **riskScore** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **riskDetails** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **licenses** | **Array&lt;number&gt;** |  | (optional) defaults to undefined|
| **dependsOn** | **Array&lt;number&gt;** |  | (optional) defaults to undefined|
| **tags** | **Array&lt;number&gt;** |  | (optional) defaults to undefined|


### Return type

**Array<SupplyOut>**

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
> SupplyOut update(supplyIn)

Update a feeding schedule.

### Example

```typescript
import {
    SuppliesApi,
    Configuration,
    SupplyIn
} from './api';

const configuration = new Configuration();
const apiInstance = new SuppliesApi(configuration);

let pk: number; // (default to undefined)
let supplyIn: SupplyIn; //

const { status, data } = await apiInstance.update(
    pk,
    supplyIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **supplyIn** | **SupplyIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**SupplyOut**

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

