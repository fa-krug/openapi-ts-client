# DependencyTagsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](DependencyTagsApi.md#_delete) | **DELETE** /api/dependency-tags/{pk} | Delete |
| [**clone**](DependencyTagsApi.md#clone) | **POST** /api/dependency-tags/{pk}/clone | Clone |
| [**count**](DependencyTagsApi.md#count) | **GET** /api/dependency-tags/count | Count |
| [**create**](DependencyTagsApi.md#create) | **POST** /api/dependency-tags | Create |
| [**get**](DependencyTagsApi.md#get) | **GET** /api/dependency-tags/{pk} | Get |
| [**listAll**](DependencyTagsApi.md#listall) | **GET** /api/dependency-tags | List All |
| [**listNames**](DependencyTagsApi.md#listnames) | **GET** /api/dependency-tags/names | List Names |
| [**update**](DependencyTagsApi.md#update) | **PUT** /api/dependency-tags/{pk} | Update |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  DependencyTagsApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DependencyTagsApi();

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

> SupplyCategoryOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  DependencyTagsApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DependencyTagsApi();

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

[**SupplyCategoryOut**](SupplyCategoryOut.md)

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
  DependencyTagsApi,
} from '';
import type { CountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DependencyTagsApi();

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

> SupplyCategoryOut create(supplyCategoryIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  DependencyTagsApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DependencyTagsApi();

  const body = {
    // SupplyCategoryIn
    supplyCategoryIn: ...,
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
| **supplyCategoryIn** | [SupplyCategoryIn](SupplyCategoryIn.md) |  | |

### Return type

[**SupplyCategoryOut**](SupplyCategoryOut.md)

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

> SupplyCategoryOut get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  DependencyTagsApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DependencyTagsApi();

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

[**SupplyCategoryOut**](SupplyCategoryOut.md)

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

> Array&lt;SupplyCategoryOut&gt; listAll(id, name)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  DependencyTagsApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DependencyTagsApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    name: name_example,
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

### Return type

[**Array&lt;SupplyCategoryOut&gt;**](SupplyCategoryOut.md)

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

> Array&lt;SupplyCategoryNames&gt; listNames(id, name)

List Names

List all names.

### Example

```ts
import {
  Configuration,
  DependencyTagsApi,
} from '';
import type { ListNamesRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DependencyTagsApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    name: name_example,
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

### Return type

[**Array&lt;SupplyCategoryNames&gt;**](SupplyCategoryNames.md)

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

> SupplyCategoryOut update(pk, supplyCategoryIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  DependencyTagsApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new DependencyTagsApi();

  const body = {
    // number
    pk: 56,
    // SupplyCategoryIn
    supplyCategoryIn: ...,
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
| **supplyCategoryIn** | [SupplyCategoryIn](SupplyCategoryIn.md) |  | |

### Return type

[**SupplyCategoryOut**](SupplyCategoryOut.md)

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

