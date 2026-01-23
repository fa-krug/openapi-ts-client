# AuditFieldsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**criteriaClone**](#criteriaclone) | **POST** /api/audit-fields/{pk}/clone | Clone|
|[**criteriaCreate**](#criteriacreate) | **POST** /api/audit-fields | Create|
|[**criteriaDelete**](#criteriadelete) | **DELETE** /api/audit-fields/{pk} | Delete|
|[**criteriaGet**](#criteriaget) | **GET** /api/audit-fields/{pk} | Get|
|[**criteriaListAll**](#criterialistall) | **GET** /api/audit-fields | List All|
|[**criteriaUpdate**](#criteriaupdate) | **PUT** /api/audit-fields/{pk} | Update|

# **criteriaClone**
> InspectionCriteriaIn criteriaClone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    AuditFieldsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AuditFieldsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.criteriaClone(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**InspectionCriteriaIn**

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

# **criteriaCreate**
> InspectionCriteriaOut criteriaCreate(inspectionCriteriaIn)

Create a new feeding schedule.

### Example

```typescript
import {
    AuditFieldsApi,
    Configuration,
    InspectionCriteriaIn
} from './api';

const configuration = new Configuration();
const apiInstance = new AuditFieldsApi(configuration);

let inspectionCriteriaIn: InspectionCriteriaIn; //

const { status, data } = await apiInstance.criteriaCreate(
    inspectionCriteriaIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **inspectionCriteriaIn** | **InspectionCriteriaIn**|  | |


### Return type

**InspectionCriteriaOut**

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

# **criteriaDelete**
> criteriaDelete()

Remove a feeding schedule.

### Example

```typescript
import {
    AuditFieldsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AuditFieldsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.criteriaDelete(
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

# **criteriaGet**
> InspectionCriteriaOut criteriaGet()

Get a feeding record.

### Example

```typescript
import {
    AuditFieldsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AuditFieldsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.criteriaGet(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**InspectionCriteriaOut**

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

# **criteriaListAll**
> Array<InspectionCriteriaOut> criteriaListAll()

List all feeding schedules.

### Example

```typescript
import {
    AuditFieldsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new AuditFieldsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let text: string; //Filter by exact match (optional) (default to undefined)
let audit: string; //Filter by exact match (optional) (default to undefined)
let type: string; //Filter by exact match (optional) (default to undefined)
let kwargs: string; //Filter by exact match (optional) (default to undefined)
let info: string; //Filter by exact match (optional) (default to undefined)
let value: string; //Filter by exact match (optional) (default to undefined)
let score: string; //Filter by exact match (optional) (default to undefined)
let section: string; //Filter by exact match (optional) (default to undefined)
let visible: boolean; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.criteriaListAll(
    id,
    text,
    audit,
    type,
    kwargs,
    info,
    value,
    score,
    section,
    visible
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **text** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **audit** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **type** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **kwargs** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **info** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **value** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **score** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **section** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **visible** | [**boolean**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<InspectionCriteriaOut>**

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

# **criteriaUpdate**
> InspectionCriteriaOut criteriaUpdate(inspectionCriteriaIn)

Update a feeding schedule.

### Example

```typescript
import {
    AuditFieldsApi,
    Configuration,
    InspectionCriteriaIn
} from './api';

const configuration = new Configuration();
const apiInstance = new AuditFieldsApi(configuration);

let pk: number; // (default to undefined)
let inspectionCriteriaIn: InspectionCriteriaIn; //

const { status, data } = await apiInstance.criteriaUpdate(
    pk,
    inspectionCriteriaIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **inspectionCriteriaIn** | **InspectionCriteriaIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**InspectionCriteriaOut**

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

