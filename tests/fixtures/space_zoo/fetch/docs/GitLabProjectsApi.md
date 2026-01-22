# GitLabProjectsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](GitLabProjectsApi.md#_delete) | **DELETE** /api/gitlab-projects/{pk} | Delete |
| [**clone**](GitLabProjectsApi.md#clone) | **POST** /api/gitlab-projects/{pk}/clone | Clone |
| [**create**](GitLabProjectsApi.md#create) | **POST** /api/gitlab-projects | Create |
| [**get**](GitLabProjectsApi.md#get) | **GET** /api/gitlab-projects/{pk} | Get |
| [**listAll**](GitLabProjectsApi.md#listall) | **GET** /api/gitlab-projects | List All |
| [**update**](GitLabProjectsApi.md#update) | **PUT** /api/gitlab-projects/{pk} | Update |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  GitLabProjectsApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabProjectsApi();

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

> OriginPlanetOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  GitLabProjectsApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabProjectsApi();

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

[**OriginPlanetOut**](OriginPlanetOut.md)

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

> OriginPlanetOut create(originPlanetIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  GitLabProjectsApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabProjectsApi();

  const body = {
    // OriginPlanetIn
    originPlanetIn: ...,
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
| **originPlanetIn** | [OriginPlanetIn](OriginPlanetIn.md) |  | |

### Return type

[**OriginPlanetOut**](OriginPlanetOut.md)

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

> OriginPlanetOut get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  GitLabProjectsApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabProjectsApi();

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

[**OriginPlanetOut**](OriginPlanetOut.md)

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

> Array&lt;OriginPlanetOut&gt; listAll(id, name, habitat)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  GitLabProjectsApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabProjectsApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    name: name_example,
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
| **habitat** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;OriginPlanetOut&gt;**](OriginPlanetOut.md)

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

> OriginPlanetOut update(pk, originPlanetIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  GitLabProjectsApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new GitLabProjectsApi();

  const body = {
    // number
    pk: 56,
    // OriginPlanetIn
    originPlanetIn: ...,
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
| **originPlanetIn** | [OriginPlanetIn](OriginPlanetIn.md) |  | |

### Return type

[**OriginPlanetOut**](OriginPlanetOut.md)

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

