# HealthReportsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](HealthReportsApi.md#_delete) | **DELETE** /api/health-reports/{pk} | Delete |
| [**clone**](HealthReportsApi.md#clone) | **POST** /api/health-reports/{pk}/duplicate | Clone |
| [**count**](HealthReportsApi.md#count) | **GET** /api/health-reports/count | Count |
| [**create**](HealthReportsApi.md#create) | **POST** /api/health-reports | Create |
| [**get**](HealthReportsApi.md#get) | **GET** /api/health-reports/{pk} | Get |
| [**getAuditRanking**](HealthReportsApi.md#getauditranking) | **GET** /api/reports/{pk}/audit-ranking | Get Audit Ranking |
| [**getAudits**](HealthReportsApi.md#getaudits) | **GET** /api/reports/{pk}/audits | Get Audits |
| [**getOpenActions**](HealthReportsApi.md#getopenactions) | **GET** /api/reports/{pk}/open-actions | Get Open Actions |
| [**getRecentActions**](HealthReportsApi.md#getrecentactions) | **GET** /api/reports/{pk}/recent-actions | Get Recent Actions |
| [**getReportPdf**](HealthReportsApi.md#getreportpdf) | **GET** /api/health-reports/{pk}/export-pdf | Get Report Pdf |
| [**getSubsections**](HealthReportsApi.md#getsubsections) | **GET** /api/reports/{pk}/subsections | Get Subsections |
| [**listAll**](HealthReportsApi.md#listall) | **GET** /api/health-reports | List All |
| [**update**](HealthReportsApi.md#update) | **PUT** /api/health-reports/{pk} | Update |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  const body = {
    // number
    pk: 56,
  } satisfies DeleteRequest;

  try {
    const data = await api._delete(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |

### Return type

`void` (Empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## clone

> HealthReportOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  const body = {
    // number
    pk: 56,
  } satisfies CloneRequest;

  try {
    const data = await api.clone(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |

### Return type

[**HealthReportOut**](HealthReportOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## count

> number count()

Count

Count all feeding records.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { CountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  try {
    const data = await api.count();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters

This endpoint does not need any parameter.

### Return type

**number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## create

> HealthReportOut create(healthReportIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  const body = {
    // HealthReportIn
    healthReportIn: ...,
  } satisfies CreateRequest;

  try {
    const data = await api.create(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **healthReportIn** | [HealthReportIn](HealthReportIn.md) |  | |

### Return type

[**HealthReportOut**](HealthReportOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## get

> HealthReportOut get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  const body = {
    // number
    pk: 56,
  } satisfies GetRequest;

  try {
    const data = await api.get(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |

### Return type

[**HealthReportOut**](HealthReportOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getAuditRanking

> Array&lt;InspectionRanking&gt; getAuditRanking(pk)

Get Audit Ranking

Get audit ranking for a report.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { GetAuditRankingRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  const body = {
    // number
    pk: 56,
  } satisfies GetAuditRankingRequest;

  try {
    const data = await api.getAuditRanking(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |

### Return type

[**Array&lt;InspectionRanking&gt;**](InspectionRanking.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getAudits

> Array&lt;InspectionOut&gt; getAudits(pk)

Get Audits

Get audits for a report.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { GetAuditsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  const body = {
    // number
    pk: 56,
  } satisfies GetAuditsRequest;

  try {
    const data = await api.getAudits(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |

### Return type

[**Array&lt;InspectionOut&gt;**](InspectionOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getOpenActions

> Array&lt;FeedingOut&gt; getOpenActions(pk)

Get Open Actions

Get open actions for a report.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { GetOpenActionsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  const body = {
    // number
    pk: 56,
  } satisfies GetOpenActionsRequest;

  try {
    const data = await api.getOpenActions(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |

### Return type

[**Array&lt;FeedingOut&gt;**](FeedingOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getRecentActions

> Array&lt;FeedingOut&gt; getRecentActions(pk)

Get Recent Actions

Get recent actions for a report.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { GetRecentActionsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  const body = {
    // number
    pk: 56,
  } satisfies GetRecentActionsRequest;

  try {
    const data = await api.getRecentActions(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |

### Return type

[**Array&lt;FeedingOut&gt;**](FeedingOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getReportPdf

> Blob getReportPdf(pk)

Get Report Pdf

Get pdf data for a report.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { GetReportPdfRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  const body = {
    // number
    pk: 56,
  } satisfies GetReportPdfRequest;

  try {
    const data = await api.getReportPdf(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |

### Return type

**Blob**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/pdf`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a pdf |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getSubsections

> Array&lt;SubSection&gt; getSubsections(pk)

Get Subsections

Get subsections for a report.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { GetSubsectionsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  const body = {
    // number
    pk: 56,
  } satisfies GetSubsectionsRequest;

  try {
    const data = await api.getSubsections(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |

### Return type

[**Array&lt;SubSection&gt;**](SubSection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## listAll

> Array&lt;HealthReportOut&gt; listAll(id, name, latestAudits, startDate, endDate, type, simplify, blocks, permission, privacy, audit, template)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    name: name_example,
    // boolean | Filter by exact match (optional)
    latestAudits: true,
    // string | Filter by exact match (optional)
    startDate: startDate_example,
    // string | Filter by exact match (optional)
    endDate: endDate_example,
    // string | Filter by exact match (optional)
    type: type_example,
    // boolean | Filter by exact match (optional)
    simplify: true,
    // string | Filter by exact match (optional)
    blocks: blocks_example,
    // string | Filter by exact match (optional)
    permission: permission_example,
    // string | Filter by exact match (optional)
    privacy: privacy_example,
    // Array<number> (optional)
    audit: ...,
    // Array<number> (optional)
    template: ...,
  } satisfies ListAllRequest;

  try {
    const data = await api.listAll(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **name** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **latestAudits** | `boolean` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **startDate** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **endDate** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **type** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **simplify** | `boolean` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **blocks** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **permission** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **privacy** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **audit** | `Array<number>` |  | [Optional] |
| **template** | `Array<number>` |  | [Optional] |

### Return type

[**Array&lt;HealthReportOut&gt;**](HealthReportOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## update

> HealthReportOut update(pk, healthReportIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  HealthReportsApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new HealthReportsApi();

  const body = {
    // number
    pk: 56,
    // HealthReportIn
    healthReportIn: ...,
  } satisfies UpdateRequest;

  try {
    const data = await api.update(body);
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

// Run the test
example().catch(console.error);
```

### Parameters


| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pk** | `number` |  | [Defaults to `undefined`] |
| **healthReportIn** | [HealthReportIn](HealthReportIn.md) |  | |

### Return type

[**HealthReportOut**](HealthReportOut.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

