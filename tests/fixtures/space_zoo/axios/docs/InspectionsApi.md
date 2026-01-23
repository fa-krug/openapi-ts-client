# InspectionsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/inspections/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/inspections/{pk}/duplicate | Clone|
|[**countActive**](#countactive) | **GET** /api/audits/count-active | Count Active|
|[**countArchived**](#countarchived) | **GET** /api/audits/count-archived | Count Archived|
|[**create**](#create) | **POST** /api/inspections | Create|
|[**get**](#get) | **GET** /api/inspections/{pk} | Get|
|[**getAuditChart**](#getauditchart) | **GET** /api/audits/{pk}/chart | Get Audit Chart|
|[**getAuditScores**](#getauditscores) | **GET** /api/audits/{pk}/scores | Get Audit Scores|
|[**listAll**](#listall) | **GET** /api/inspections | List All|
|[**listAuditActions**](#listauditactions) | **GET** /api/audits/{pk}/actions | List Audit Actions|
|[**listAuditChanges**](#listauditchanges) | **GET** /api/inspections/{pk}/changes | List Audit Changes|
|[**listAuditFields**](#listauditfields) | **GET** /api/audits/{pk}/fields | List Audit Fields|
|[**listAuditProblems**](#listauditproblems) | **GET** /api/inspections/{pk}/issues | List Audit Problems|
|[**listNames**](#listnames) | **GET** /api/audits/names | List Names|
|[**update**](#update) | **PUT** /api/inspections/{pk} | Update|
|[**updateAuditFields**](#updateauditfields) | **PUT** /api/audits/{pk}/fields | Update Audit Fields|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

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
> InspectionOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

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

**InspectionOut**

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

# **countActive**
> number countActive()

Count all active entries.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

const { status, data } = await apiInstance.countActive();
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

# **countArchived**
> number countArchived()

Count all archived entries.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

const { status, data } = await apiInstance.countArchived();
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
> InspectionOut create(inspectionIn)

Create a new feeding schedule.

### Example

```typescript
import {
    InspectionsApi,
    Configuration,
    InspectionIn
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

let inspectionIn: InspectionIn; //

const { status, data } = await apiInstance.create(
    inspectionIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **inspectionIn** | **InspectionIn**|  | |


### Return type

**InspectionOut**

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
> InspectionOut get()

Get a feeding record.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

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

**InspectionOut**

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

# **getAuditChart**
> ResultSchema getAuditChart()

Get graph data for an audit.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

let pk: number; // (default to undefined)
let simplify: boolean; // (optional) (default to false)

const { status, data } = await apiInstance.getAuditChart(
    pk,
    simplify
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|
| **simplify** | [**boolean**] |  | (optional) defaults to false|


### Return type

**ResultSchema**

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

# **getAuditScores**
> { [key: string]: number; } getAuditScores()

Get score data for an audit.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

let pk: number; // (default to undefined)
let simplify: boolean; // (optional) (default to false)

const { status, data } = await apiInstance.getAuditScores(
    pk,
    simplify
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|
| **simplify** | [**boolean**] |  | (optional) defaults to false|


### Return type

**{ [key: string]: number; }**

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
> Array<InspectionOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)
let template: string; //Filter by exact match (optional) (default to undefined)
let habitat: string; //Filter by exact match (optional) (default to undefined)
let lastAudit: string; //Filter by exact match (optional) (default to undefined)
let content: string; //Filter by exact match (optional) (default to undefined)
let version: string; //Filter by exact match (optional) (default to undefined)
let status: string; //Filter by exact match (optional) (default to undefined)
let score: string; //Filter by exact match (optional) (default to undefined)
let archived: boolean; //Filter by exact match (optional) (default to undefined)
let start: string; //Filter by exact match (optional) (default to undefined)
let end: string; //Filter by exact match (optional) (default to undefined)
let summary: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    name,
    template,
    habitat,
    lastAudit,
    content,
    version,
    status,
    score,
    archived,
    start,
    end,
    summary
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **template** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **habitat** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **lastAudit** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **content** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **version** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **status** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **score** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **archived** | [**boolean**] | Filter by exact match | (optional) defaults to undefined|
| **start** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **end** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **summary** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<InspectionOut>**

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

# **listAuditActions**
> Array<FeedingOut> listAuditActions()

List all actions for an audit.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

let pk: number; // (default to undefined)
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

const { status, data } = await apiInstance.listAuditActions(
    pk,
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
| **pk** | [**number**] |  | defaults to undefined|
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

# **listAuditChanges**
> Array<InspectionChange> listAuditChanges()

List all changes for an audit.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.listAuditChanges(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**Array<InspectionChange>**

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

# **listAuditFields**
> Array<InspectionCriteriaOut> listAuditFields()

List all fields for an audit.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.listAuditFields(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


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

# **listAuditProblems**
> Array<InspectionIssue> listAuditProblems()

List all problems for an audit.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.listAuditProblems(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**Array<InspectionIssue>**

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
> Array<InspectionNames> listNames()

List all names.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)
let template: string; //Filter by exact match (optional) (default to undefined)
let habitat: string; //Filter by exact match (optional) (default to undefined)
let lastAudit: string; //Filter by exact match (optional) (default to undefined)
let content: string; //Filter by exact match (optional) (default to undefined)
let version: string; //Filter by exact match (optional) (default to undefined)
let status: string; //Filter by exact match (optional) (default to undefined)
let score: string; //Filter by exact match (optional) (default to undefined)
let archived: boolean; //Filter by exact match (optional) (default to undefined)
let start: string; //Filter by exact match (optional) (default to undefined)
let end: string; //Filter by exact match (optional) (default to undefined)
let summary: string; //Filter by exact match (optional) (default to undefined)

const { status, data } = await apiInstance.listNames(
    id,
    name,
    template,
    habitat,
    lastAudit,
    content,
    version,
    status,
    score,
    archived,
    start,
    end,
    summary
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **template** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **habitat** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **lastAudit** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **content** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **version** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **status** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **score** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **archived** | [**boolean**] | Filter by exact match | (optional) defaults to undefined|
| **start** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **end** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **summary** | [**string**] | Filter by exact match | (optional) defaults to undefined|


### Return type

**Array<InspectionNames>**

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
> InspectionOut update(inspectionIn)

Update a feeding schedule.

### Example

```typescript
import {
    InspectionsApi,
    Configuration,
    InspectionIn
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

let pk: number; // (default to undefined)
let inspectionIn: InspectionIn; //

const { status, data } = await apiInstance.update(
    pk,
    inspectionIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **inspectionIn** | **InspectionIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**InspectionOut**

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

# **updateAuditFields**
> Array<InspectionCriteriaOut> updateAuditFields(inspectionCriteriaIn)

Update fields for an audit.

### Example

```typescript
import {
    InspectionsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new InspectionsApi(configuration);

let pk: number; // (default to undefined)
let inspectionCriteriaIn: Array<InspectionCriteriaIn>; //

const { status, data } = await apiInstance.updateAuditFields(
    pk,
    inspectionCriteriaIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **inspectionCriteriaIn** | **Array<InspectionCriteriaIn>**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**Array<InspectionCriteriaOut>**

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

