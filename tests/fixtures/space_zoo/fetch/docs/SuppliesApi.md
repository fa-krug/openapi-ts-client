# SuppliesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**_delete**](SuppliesApi.md#_delete) | **DELETE** /api/supplies/{pk} | Delete |
| [**clone**](SuppliesApi.md#clone) | **POST** /api/supplies/{pk}/duplicate | Clone |
| [**count**](SuppliesApi.md#count) | **GET** /api/supplies/count | Count |
| [**create**](SuppliesApi.md#create) | **POST** /api/supplies | Create |
| [**get**](SuppliesApi.md#get) | **GET** /api/supplies/{pk} | Get |
| [**listAll**](SuppliesApi.md#listall) | **GET** /api/supplies | List All |
| [**update**](SuppliesApi.md#update) | **PUT** /api/supplies/{pk} | Update |



## _delete

> _delete(pk)

Delete

Remove a feeding schedule.

### Example

```ts
import {
  Configuration,
  SuppliesApi,
} from '';
import type { DeleteRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SuppliesApi();

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

> SupplyOut clone(pk)

Clone

Duplicate a feeding schedule.

### Example

```ts
import {
  Configuration,
  SuppliesApi,
} from '';
import type { CloneRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SuppliesApi();

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

[**SupplyOut**](SupplyOut.md)

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
  SuppliesApi,
} from '';
import type { CountRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SuppliesApi();

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

> SupplyOut create(supplyIn)

Create

Create a new feeding schedule.

### Example

```ts
import {
  Configuration,
  SuppliesApi,
} from '';
import type { CreateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SuppliesApi();

  const body = {
    // SupplyIn
    supplyIn: ...,
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
| **supplyIn** | [SupplyIn](SupplyIn.md) |  | |

### Return type

[**SupplyOut**](SupplyOut.md)

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

> SupplyDetails get(pk)

Get

Get a feeding record.

### Example

```ts
import {
  Configuration,
  SuppliesApi,
} from '';
import type { GetRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SuppliesApi();

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

[**SupplyDetails**](SupplyDetails.md)

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

> Array&lt;SupplyOut&gt; listAll(id, purl, _package, version, image, bomRef, type, author, riskScore, riskDetails, licenses, dependsOn, tags)

List All

List all feeding schedules.

### Example

```ts
import {
  Configuration,
  SuppliesApi,
} from '';
import type { ListAllRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SuppliesApi();

  const body = {
    // string | Filter by exact match (optional)
    id: id_example,
    // string | Filter by exact match (optional)
    purl: purl_example,
    // string | Filter by exact match (optional)
    _package: _package_example,
    // string | Filter by exact match (optional)
    version: version_example,
    // string | Filter by exact match (optional)
    image: image_example,
    // string | Filter by exact match (optional)
    bomRef: bomRef_example,
    // string | Filter by exact match (optional)
    type: type_example,
    // string | Filter by exact match (optional)
    author: author_example,
    // string | Filter by exact match (optional)
    riskScore: riskScore_example,
    // string | Filter by exact match (optional)
    riskDetails: riskDetails_example,
    // Array<number> (optional)
    licenses: ...,
    // Array<number> (optional)
    dependsOn: ...,
    // Array<number> (optional)
    tags: ...,
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
| **purl** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **_package** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **version** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **image** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **bomRef** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **type** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **author** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **riskScore** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **riskDetails** | `string` | Filter by exact match | [Optional] [Defaults to `undefined`] |
| **licenses** | `Array<number>` |  | [Optional] |
| **dependsOn** | `Array<number>` |  | [Optional] |
| **tags** | `Array<number>` |  | [Optional] |

### Return type

[**Array&lt;SupplyOut&gt;**](SupplyOut.md)

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

> SupplyOut update(pk, supplyIn)

Update

Update a feeding schedule.

### Example

```ts
import {
  Configuration,
  SuppliesApi,
} from '';
import type { UpdateRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new SuppliesApi();

  const body = {
    // number
    pk: 56,
    // SupplyIn
    supplyIn: ...,
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
| **supplyIn** | [SupplyIn](SupplyIn.md) |  | |

### Return type

[**SupplyOut**](SupplyOut.md)

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

