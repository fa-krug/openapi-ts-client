# FeedingsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](FeedingsApi.md#_delete) | **DELETE** /api/feedings/{pk} | Delete |
| [**clone**](FeedingsApi.md#clone) | **POST** /api/feedings/{pk}/duplicate | Clone |
| [**count**](FeedingsApi.md#count) | **GET** /api/feedings/count | Count |
| [**create**](FeedingsApi.md#create) | **POST** /api/feedings | Create |
| [**decreaseAction**](FeedingsApi.md#decreaseaction) | **PUT** /api/feedings/{pk}/decrease-portion | Decrease Action |
| [**extendAction**](FeedingsApi.md#extendaction) | **PUT** /api/feedings/{pk}/extend-schedule | Extend Action |
| [**get**](FeedingsApi.md#get) | **GET** /api/feedings/{pk} | Get |
| [**increaseAction**](FeedingsApi.md#increaseaction) | **PUT** /api/feedings/{pk}/increase-portion | Increase Action |
| [**listAll**](FeedingsApi.md#listall) | **GET** /api/feedings | List All |
| [**update**](FeedingsApi.md#update) | **PUT** /api/feedings/{pk} | Update |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  FeedingsApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeedingsApi();

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

> FeedingOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  FeedingsApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeedingsApi();

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

[**FeedingOut**](FeedingOut.md)

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
  FeedingsApi,
} from '';
import type { CountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeedingsApi();

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

> FeedingOut create(feedingIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  FeedingsApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeedingsApi();

  const body = {
    // FeedingIn
    feedingIn: ...,
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
| **feedingIn** | [FeedingIn](FeedingIn.md) |  | |

### Return type

[**FeedingOut**](FeedingOut.md)

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


## decreaseAction

> FeedingOut decreaseAction(pk)

Decrease Action

Decrease portion size for feeding.

### Example

```ts
import {
  Configuration,
  FeedingsApi,
} from '';
import type { DecreaseActionRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeedingsApi();

  const body = {
    // number
    pk: 56,
  } satisfies DecreaseActionRequest;

  try {
    const data = await api.decreaseAction(body);
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

[**FeedingOut**](FeedingOut.md)

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


## extendAction

> FeedingOut extendAction(pk)

Extend Action

Extend feeding schedule duration.

### Example

```ts
import {
  Configuration,
  FeedingsApi,
} from '';
import type { ExtendActionRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeedingsApi();

  const body = {
    // number
    pk: 56,
  } satisfies ExtendActionRequest;

  try {
    const data = await api.extendAction(body);
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

[**FeedingOut**](FeedingOut.md)

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


## get

> FeedingOut get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  FeedingsApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeedingsApi();

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

[**FeedingOut**](FeedingOut.md)

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


## increaseAction

> FeedingOut increaseAction(pk)

Increase Action

Increase portion size for feeding.

### Example

```ts
import {
  Configuration,
  FeedingsApi,
} from '';
import type { IncreaseActionRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeedingsApi();

  const body = {
    // number
    pk: 56,
  } satisfies IncreaseActionRequest;

  try {
    const data = await api.increaseAction(body);
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

[**FeedingOut**](FeedingOut.md)

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

> Array&lt;FeedingOut&gt; listAll(id, value, keeper, creature, priority, start, end, habitat, administered, feedingDate)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  FeedingsApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeedingsApi();

  const body = {
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


## update

> FeedingOut update(pk, feedingIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  FeedingsApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FeedingsApi();

  const body = {
    // number
    pk: 56,
    // FeedingIn
    feedingIn: ...,
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
| **feedingIn** | [FeedingIn](FeedingIn.md) |  | |

### Return type

[**FeedingOut**](FeedingOut.md)

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

