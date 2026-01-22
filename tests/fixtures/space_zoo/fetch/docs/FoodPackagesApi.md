# FoodPackagesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](FoodPackagesApi.md#_delete) | **DELETE** /api/food-packages/{pk} | Delete |
| [**clone**](FoodPackagesApi.md#clone) | **POST** /api/food-packages/{pk}/duplicate | Clone |
| [**count**](FoodPackagesApi.md#count) | **GET** /api/food-packages/count | Count |
| [**create**](FoodPackagesApi.md#create) | **POST** /api/food-packages | Create |
| [**get**](FoodPackagesApi.md#get) | **GET** /api/food-packages/{pk} | Get |
| [**listAll**](FoodPackagesApi.md#listall) | **GET** /api/food-packages | List All |
| [**update**](FoodPackagesApi.md#update) | **PUT** /api/food-packages/{pk} | Update |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  FoodPackagesApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FoodPackagesApi();

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

> FoodPackageOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  FoodPackagesApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FoodPackagesApi();

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

[**FoodPackageOut**](FoodPackageOut.md)

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
  FoodPackagesApi,
} from '';
import type { CountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FoodPackagesApi();

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

> FoodPackageOut create(foodPackageIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  FoodPackagesApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FoodPackagesApi();

  const body = {
    // FoodPackageIn
    foodPackageIn: ...,
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
| **foodPackageIn** | [FoodPackageIn](FoodPackageIn.md) |  | |

### Return type

[**FoodPackageOut**](FoodPackageOut.md)

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

> FoodPackageOut get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  FoodPackagesApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FoodPackagesApi();

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

[**FoodPackageOut**](FoodPackageOut.md)

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

> Array&lt;FoodPackageOut&gt; listAll(id, name, allowedSpecifier, latestVersion, hidden, allowed)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  FoodPackagesApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FoodPackagesApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    name: name_example,
    // string | Filter by exact match (optional)
    allowedSpecifier: allowedSpecifier_example,
    // string | Filter by exact match (optional)
    latestVersion: latestVersion_example,
    // boolean | Filter by exact match (optional)
    hidden: true,
    // boolean | Filter by exact match (optional)
    allowed: true,
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
| **allowedSpecifier** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **latestVersion** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **hidden** | `boolean` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **allowed** | `boolean` | Filter by exact match | [Optional] [Defaults to `undefined`] |

### Return type

[**Array&lt;FoodPackageOut&gt;**](FoodPackageOut.md)

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

> FoodPackageOut update(pk, foodPackageIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  FoodPackagesApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new FoodPackagesApi();

  const body = {
    // number
    pk: 56,
    // FoodPackageIn
    foodPackageIn: ...,
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
| **foodPackageIn** | [FoodPackageIn](FoodPackageIn.md) |  | |

### Return type

[**FoodPackageOut**](FoodPackageOut.md)

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

