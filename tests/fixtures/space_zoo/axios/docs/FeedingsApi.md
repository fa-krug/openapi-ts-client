# FeedingsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/feedings/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/feedings/{pk}/duplicate | Clone|
|[**count**](#count) | **GET** /api/feedings/count | Count|
|[**create**](#create) | **POST** /api/feedings | Create|
|[**decreaseAction**](#decreaseaction) | **PUT** /api/feedings/{pk}/decrease-portion | Decrease Action|
|[**extendAction**](#extendaction) | **PUT** /api/feedings/{pk}/extend-schedule | Extend Action|
|[**get**](#get) | **GET** /api/feedings/{pk} | Get|
|[**increaseAction**](#increaseaction) | **PUT** /api/feedings/{pk}/increase-portion | Increase Action|
|[**listAll**](#listall) | **GET** /api/feedings | List All|
|[**update**](#update) | **PUT** /api/feedings/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    FeedingsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeedingsApi(configuration);

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
> FeedingOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    FeedingsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeedingsApi(configuration);

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

**FeedingOut**

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
    FeedingsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeedingsApi(configuration);

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
> FeedingOut create(feedingIn)

Create a new feeding schedule.

### Example

```typescript
import {
    FeedingsApi,
    Configuration,
    FeedingIn
} from './api';

const configuration = new Configuration();
const apiInstance = new FeedingsApi(configuration);

let feedingIn: FeedingIn; //

const { status, data } = await apiInstance.create(
    feedingIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **feedingIn** | **FeedingIn**|  | |


### Return type

**FeedingOut**

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

# **decreaseAction**
> FeedingOut decreaseAction()

Decrease portion size for feeding.

### Example

```typescript
import {
    FeedingsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeedingsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.decreaseAction(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**FeedingOut**

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

# **extendAction**
> FeedingOut extendAction()

Extend feeding schedule duration.

### Example

```typescript
import {
    FeedingsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeedingsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.extendAction(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**FeedingOut**

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

# **get**
> FeedingOut get()

Get a feeding record.

### Example

```typescript
import {
    FeedingsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeedingsApi(configuration);

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

**FeedingOut**

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

# **increaseAction**
> FeedingOut increaseAction()

Increase portion size for feeding.

### Example

```typescript
import {
    FeedingsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeedingsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.increaseAction(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**FeedingOut**

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
> Array<FeedingOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    FeedingsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new FeedingsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let value: string; //Filter by exact match (optional) (default to undefined)
let keeper: string; //Filter by exact match (optional) (default to undefined)
let creature: string; //Filter by exact match (optional) (default to undefined)
let priority: string; //Filter by exact match (optional) (default to undefined)
let start: string; //Filter by exact match (optional) (default to undefined)
let end: string; //Filter by exact match (optional) (default to undefined)
let habitat: string; //Filter by exact match (optional) (default to undefined)
let administered: boolean; //Filter by exact match (optional) (default to undefined)
let feedingDate: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    value,
    keeper,
    creature,
    priority,
    start,
    end,
    habitat,
    administered,
    feedingDate
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **value** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **keeper** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **creature** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **priority** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **start** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **end** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **habitat** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **administered** | [**boolean**] | Filter by exact match | (optional) defaults to undefined|
| **feedingDate** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<FeedingOut>**

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
> FeedingOut update(feedingIn)

Update a feeding schedule.

### Example

```typescript
import {
    FeedingsApi,
    Configuration,
    FeedingIn
} from './api';

const configuration = new Configuration();
const apiInstance = new FeedingsApi(configuration);

let pk: number; // (default to undefined)
let feedingIn: FeedingIn; //

const { status, data } = await apiInstance.update(
    pk,
    feedingIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **feedingIn** | **FeedingIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**FeedingOut**

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

