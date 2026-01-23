# HealthReportsApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**_delete**](#_delete) | **DELETE** /api/health-reports/{pk} | Delete|
|[**clone**](#clone) | **POST** /api/health-reports/{pk}/duplicate | Clone|
|[**count**](#count) | **GET** /api/health-reports/count | Count|
|[**create**](#create) | **POST** /api/health-reports | Create|
|[**get**](#get) | **GET** /api/health-reports/{pk} | Get|
|[**getAuditRanking**](#getauditranking) | **GET** /api/reports/{pk}/audit-ranking | Get Audit Ranking|
|[**getAudits**](#getaudits) | **GET** /api/reports/{pk}/audits | Get Audits|
|[**getOpenActions**](#getopenactions) | **GET** /api/reports/{pk}/open-actions | Get Open Actions|
|[**getRecentActions**](#getrecentactions) | **GET** /api/reports/{pk}/recent-actions | Get Recent Actions|
|[**getReportPdf**](#getreportpdf) | **GET** /api/health-reports/{pk}/export-pdf | Get Report Pdf|
|[**getSubsections**](#getsubsections) | **GET** /api/reports/{pk}/subsections | Get Subsections|
|[**listAll**](#listall) | **GET** /api/health-reports | List All|
|[**update**](#update) | **PUT** /api/health-reports/{pk} | Update|

# **_delete**
> _delete()

Remove a feeding schedule.

### Example

```typescript
import {
    HealthReportsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

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
> HealthReportOut clone()

Duplicate a feeding schedule.

### Example

```typescript
import {
    HealthReportsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

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

**HealthReportOut**

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
    HealthReportsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

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
> HealthReportOut create(healthReportIn)

Create a new feeding schedule.

### Example

```typescript
import {
    HealthReportsApi,
    Configuration,
    HealthReportIn
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

let healthReportIn: HealthReportIn; //

const { status, data } = await apiInstance.create(
    healthReportIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **healthReportIn** | **HealthReportIn**|  | |


### Return type

**HealthReportOut**

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
> HealthReportOut get()

Get a feeding record.

### Example

```typescript
import {
    HealthReportsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

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

**HealthReportOut**

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

# **getAuditRanking**
> Array<InspectionRanking> getAuditRanking()

Get audit ranking for a report.

### Example

```typescript
import {
    HealthReportsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.getAuditRanking(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**Array<InspectionRanking>**

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

# **getAudits**
> Array<InspectionOut> getAudits()

Get audits for a report.

### Example

```typescript
import {
    HealthReportsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.getAudits(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


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

# **getOpenActions**
> Array<FeedingOut> getOpenActions()

Get open actions for a report.

### Example

```typescript
import {
    HealthReportsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.getOpenActions(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


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

# **getRecentActions**
> Array<FeedingOut> getRecentActions()

Get recent actions for a report.

### Example

```typescript
import {
    HealthReportsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.getRecentActions(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


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

# **getReportPdf**
> File getReportPdf()

Get pdf data for a report.

### Example

```typescript
import {
    HealthReportsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.getReportPdf(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Returns a pdf |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getSubsections**
> Array<SubSection> getSubsections()

Get subsections for a report.

### Example

```typescript
import {
    HealthReportsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

let pk: number; // (default to undefined)

const { status, data } = await apiInstance.getSubsections(
    pk
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**Array<SubSection>**

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
> Array<HealthReportOut> listAll()

List all feeding schedules.

### Example

```typescript
import {
    HealthReportsApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

let id: string; //Filter by exact match (optional) (default to undefined)
let name: string; //Filter by exact match (optional) (default to undefined)
let latestAudits: boolean; //Filter by exact match (optional) (default to undefined)
let startDate: string; //Filter by exact match (optional) (default to undefined)
let endDate: string; //Filter by exact match (optional) (default to undefined)
let type: string; //Filter by exact match (optional) (default to undefined)
let simplify: boolean; //Filter by exact match (optional) (default to undefined)
let blocks: string; //Filter by exact match (optional) (default to undefined)
let permission: string; //Filter by exact match (optional) (default to undefined)
let privacy: string; //Filter by exact match (optional) (default to undefined)
let audit: Array<number>; // (optional) (default to undefined)
let template: Array<number>; // (optional) (default to undefined)

const { status, data } = await apiInstance.listAll(
    id,
    name,
    latestAudits,
    startDate,
    endDate,
    type,
    simplify,
    blocks,
    permission,
    privacy,
    audit,
    template
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **id** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **name** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **latestAudits** | [**boolean**] | Filter by exact match | (optional) defaults to undefined|
| **startDate** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **endDate** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **type** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **simplify** | [**boolean**] | Filter by exact match | (optional) defaults to undefined|
| **blocks** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **permission** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **privacy** | [**string**] | Filter by exact match | (optional) defaults to undefined|
| **audit** | **Array&lt;number&gt;** |  | (optional) defaults to undefined|
| **template** | **Array&lt;number&gt;** |  | (optional) defaults to undefined|


### Return type

**Array<HealthReportOut>**

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
> HealthReportOut update(healthReportIn)

Update a feeding schedule.

### Example

```typescript
import {
    HealthReportsApi,
    Configuration,
    HealthReportIn
} from './api';

const configuration = new Configuration();
const apiInstance = new HealthReportsApi(configuration);

let pk: number; // (default to undefined)
let healthReportIn: HealthReportIn; //

const { status, data } = await apiInstance.update(
    pk,
    healthReportIn
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **healthReportIn** | **HealthReportIn**|  | |
| **pk** | [**number**] |  | defaults to undefined|


### Return type

**HealthReportOut**

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

