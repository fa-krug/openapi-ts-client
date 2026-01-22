# EnclosuresApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](EnclosuresApi.md#_delete) | **DELETE** /api/docker-images/{pk} | Delete |
| [**clone**](EnclosuresApi.md#clone) | **POST** /api/docker-images/{pk}/clone | Clone |
| [**count**](EnclosuresApi.md#count) | **GET** /api/docker-images/count | Count |
| [**create**](EnclosuresApi.md#create) | **POST** /api/docker-images | Create |
| [**get**](EnclosuresApi.md#get) | **GET** /api/docker-images/{pk} | Get |
| [**listAll**](EnclosuresApi.md#listall) | **GET** /api/docker-images | List All |
| [**update**](EnclosuresApi.md#update) | **PUT** /api/docker-images/{pk} | Update |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  EnclosuresApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new EnclosuresApi();

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

> EnclosureOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  EnclosuresApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new EnclosuresApi();

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

[**EnclosureOut**](EnclosureOut.md)

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
  EnclosuresApi,
} from '';
import type { CountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new EnclosuresApi();

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

> EnclosureOut create(enclosureIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  EnclosuresApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new EnclosuresApi();

  const body = {
    // EnclosureIn
    enclosureIn: ...,
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
| **enclosureIn** | [EnclosureIn](EnclosureIn.md) |  | |

### Return type

[**EnclosureOut**](EnclosureOut.md)

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

> EnclosureOut get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  EnclosuresApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new EnclosuresApi();

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

[**EnclosureOut**](EnclosureOut.md)

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

> Array&lt;EnclosureOut&gt; listAll(id, name, timestamp, habitat)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  EnclosuresApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new EnclosuresApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    name: name_example,
    // string | Filter by exact match (optional)
    timestamp: timestamp_example,
    // string | Filter by exact match (optional)
    habitat: habitat_example,
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
| **timestamp** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **habitat** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;EnclosureOut&gt;**](EnclosureOut.md)

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

> EnclosureOut update(pk, enclosureIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  EnclosuresApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new EnclosuresApi();

  const body = {
    // number
    pk: 56,
    // EnclosureIn
    enclosureIn: ...,
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
| **enclosureIn** | [EnclosureIn](EnclosureIn.md) |  | |

### Return type

[**EnclosureOut**](EnclosureOut.md)

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

