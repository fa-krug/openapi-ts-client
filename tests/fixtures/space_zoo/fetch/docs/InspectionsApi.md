# InspectionsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](InspectionsApi.md#_delete) | **DELETE** /api/inspections/{pk} | Delete |
| [**clone**](InspectionsApi.md#clone) | **POST** /api/inspections/{pk}/duplicate | Clone |
| [**countActive**](InspectionsApi.md#countactive) | **GET** /api/audits/count-active | Count Active |
| [**countArchived**](InspectionsApi.md#countarchived) | **GET** /api/audits/count-archived | Count Archived |
| [**create**](InspectionsApi.md#create) | **POST** /api/inspections | Create |
| [**get**](InspectionsApi.md#get) | **GET** /api/inspections/{pk} | Get |
| [**getAuditChart**](InspectionsApi.md#getauditchart) | **GET** /api/audits/{pk}/chart | Get Audit Chart |
| [**getAuditScores**](InspectionsApi.md#getauditscores) | **GET** /api/audits/{pk}/scores | Get Audit Scores |
| [**listAll**](InspectionsApi.md#listall) | **GET** /api/inspections | List All |
| [**listAuditActions**](InspectionsApi.md#listauditactions) | **GET** /api/audits/{pk}/actions | List Audit Actions |
| [**listAuditChanges**](InspectionsApi.md#listauditchanges) | **GET** /api/inspections/{pk}/changes | List Audit Changes |
| [**listAuditFields**](InspectionsApi.md#listauditfields) | **GET** /api/audits/{pk}/fields | List Audit Fields |
| [**listAuditProblems**](InspectionsApi.md#listauditproblems) | **GET** /api/inspections/{pk}/issues | List Audit Problems |
| [**listNames**](InspectionsApi.md#listnames) | **GET** /api/audits/names | List Names |
| [**update**](InspectionsApi.md#update) | **PUT** /api/inspections/{pk} | Update |
| [**updateAuditFields**](InspectionsApi.md#updateauditfields) | **PUT** /api/audits/{pk}/fields | Update Audit Fields |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

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

> InspectionOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

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

[**InspectionOut**](InspectionOut.md)

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


## countActive

> number countActive()

Count Active

Count all active entries.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { CountActiveRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  try {
    const data = await api.countActive();
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


## countArchived

> number countArchived()

Count Archived

Count all archived entries.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { CountArchivedRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  try {
    const data = await api.countArchived();
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

> InspectionOut create(inspectionIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  const body = {
    // InspectionIn
    inspectionIn: ...,
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
| **inspectionIn** | [InspectionIn](InspectionIn.md) |  | |

### Return type

[**InspectionOut**](InspectionOut.md)

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

> InspectionOut get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

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

[**InspectionOut**](InspectionOut.md)

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


## getAuditChart

> ResultSchema getAuditChart(pk, simplify)

Get Audit Chart

Get graph data for an audit.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { GetAuditChartRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  const body = {
    // number
    pk: 56,
    // boolean (optional)
    simplify: true,
  } satisfies GetAuditChartRequest;

  try {
    const data = await api.getAuditChart(body);
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
| **simplify** | `boolean` |  | [Optional] [Defaults to `false`] |

### Return type

[**ResultSchema**](ResultSchema.md)

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


## getAuditScores

> { [key: string]: number; } getAuditScores(pk, simplify)

Get Audit Scores

Get score data for an audit.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { GetAuditScoresRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  const body = {
    // number
    pk: 56,
    // boolean (optional)
    simplify: true,
  } satisfies GetAuditScoresRequest;

  try {
    const data = await api.getAuditScores(body);
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
| **simplify** | `boolean` |  | [Optional] [Defaults to `false`] |

### Return type

**{ [key: string]: number; }**

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

> Array&lt;InspectionOut&gt; listAll(id, name, template, habitat, lastAudit, content, version, status, score, archived, start, end, summary)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    name: name_example,
    // string | Filter by exact match (optional)
    template: template_example,
    // string | Filter by exact match (optional)
    habitat: habitat_example,
    // string | Filter by exact match (optional)
    lastAudit: lastAudit_example,
    // string | Filter by exact match (optional)
    content: content_example,
    // string | Filter by exact match (optional)
    version: version_example,
    // string | Filter by exact match (optional)
    status: status_example,
    // string | Filter by exact match (optional)
    score: score_example,
    // boolean | Filter by exact match (optional)
    archived: true,
    // string | Filter by exact match (optional)
    start: start_example,
    // string | Filter by exact match (optional)
    end: end_example,
    // string | Filter by exact match (optional)
    summary: summary_example,
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
| **template** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **habitat** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **lastAudit** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **content** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **version** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **status** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **score** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **archived** | `boolean` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **start** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **end** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **summary** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |

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


## listAuditActions

> Array&lt;FeedingOut&gt; listAuditActions(pk, id, value, keeper, creature, priority, start, end, habitat, administered, feedingDate)

List Audit Actions

List all actions for an audit.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { ListAuditActionsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  const body = {
    // number
    pk: 56,
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    value: value_example,
    // string | Filter by exact match (optional)
    keeper: keeper_example,
    // string | Filter by exact match (optional)
    creature: creature_example,
    // string | Filter by exact match (optional)
    priority: priority_example,
    // string | Filter by exact match (optional)
    start: start_example,
    // string | Filter by exact match (optional)
    end: end_example,
    // string | Filter by exact match (optional)
    habitat: habitat_example,
    // boolean | Filter by exact match (optional)
    administered: true,
    // string | Filter by exact match (optional)
    feedingDate: feedingDate_example,
  } satisfies ListAuditActionsRequest;

  try {
    const data = await api.listAuditActions(body);
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
| **id** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **value** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **keeper** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **creature** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **priority** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **start** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **end** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **habitat** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **administered** | `boolean` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **feedingDate** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |

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


## listAuditChanges

> Array&lt;InspectionChange&gt; listAuditChanges(pk)

List Audit Changes

List all changes for an audit.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { ListAuditChangesRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  const body = {
    // number
    pk: 56,
  } satisfies ListAuditChangesRequest;

  try {
    const data = await api.listAuditChanges(body);
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

[**Array&lt;InspectionChange&gt;**](InspectionChange.md)

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


## listAuditFields

> Array&lt;InspectionCriteriaOut&gt; listAuditFields(pk)

List Audit Fields

List all fields for an audit.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { ListAuditFieldsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  const body = {
    // number
    pk: 56,
  } satisfies ListAuditFieldsRequest;

  try {
    const data = await api.listAuditFields(body);
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

[**Array&lt;InspectionCriteriaOut&gt;**](InspectionCriteriaOut.md)

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


## listAuditProblems

> Array&lt;InspectionIssue&gt; listAuditProblems(pk)

List Audit Problems

List all problems for an audit.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { ListAuditProblemsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  const body = {
    // number
    pk: 56,
  } satisfies ListAuditProblemsRequest;

  try {
    const data = await api.listAuditProblems(body);
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

[**Array&lt;InspectionIssue&gt;**](InspectionIssue.md)

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


## listNames

> Array&lt;InspectionNames&gt; listNames(id, name, template, habitat, lastAudit, content, version, status, score, archived, start, end, summary)

List Names

List all names.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { ListNamesRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    name: name_example,
    // string | Filter by exact match (optional)
    template: template_example,
    // string | Filter by exact match (optional)
    habitat: habitat_example,
    // string | Filter by exact match (optional)
    lastAudit: lastAudit_example,
    // string | Filter by exact match (optional)
    content: content_example,
    // string | Filter by exact match (optional)
    version: version_example,
    // string | Filter by exact match (optional)
    status: status_example,
    // string | Filter by exact match (optional)
    score: score_example,
    // boolean | Filter by exact match (optional)
    archived: true,
    // string | Filter by exact match (optional)
    start: start_example,
    // string | Filter by exact match (optional)
    end: end_example,
    // string | Filter by exact match (optional)
    summary: summary_example,
  } satisfies ListNamesRequest;

  try {
    const data = await api.listNames(body);
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
| **template** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **habitat** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **lastAudit** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **content** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **version** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **status** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **score** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **archived** | `boolean` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **start** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **end** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **summary** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;InspectionNames&gt;**](InspectionNames.md)

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

> InspectionOut update(pk, inspectionIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  const body = {
    // number
    pk: 56,
    // InspectionIn
    inspectionIn: ...,
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
| **inspectionIn** | [InspectionIn](InspectionIn.md) |  | |

### Return type

[**InspectionOut**](InspectionOut.md)

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


## updateAuditFields

> Array&lt;InspectionCriteriaOut&gt; updateAuditFields(pk, inspectionCriteriaIn)

Update Audit Fields

Update fields for an audit.

### Example

```ts
import {
  Configuration,
  InspectionsApi,
} from '';
import type { UpdateAuditFieldsRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new InspectionsApi();

  const body = {
    // number
    pk: 56,
    // Array<InspectionCriteriaIn>
    inspectionCriteriaIn: ...,
  } satisfies UpdateAuditFieldsRequest;

  try {
    const data = await api.updateAuditFields(body);
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
| **inspectionCriteriaIn** | `Array<InspectionCriteriaIn>` |  | |

### Return type

[**Array&lt;InspectionCriteriaOut&gt;**](InspectionCriteriaOut.md)

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

