# StoreApi

All URIs are relative to */api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteOrder**](StoreApi.md#deleteorder) | **DELETE** /store/order/{orderId} | Delete purchase order by identifier. |
| [**getInventory**](StoreApi.md#getinventory) | **GET** /store/inventory | Returns pet inventories by status. |
| [**getOrderById**](StoreApi.md#getorderbyid) | **GET** /store/order/{orderId} | Find purchase order by ID. |
| [**placeOrder**](StoreApi.md#placeorder) | **POST** /store/order | Place an order for a pet. |



## deleteOrder

> deleteOrder(orderId)

Delete purchase order by identifier.

For valid response try integer IDs with value &lt; 1000. Anything above 1000 or non-integers will generate API errors.

### Example

```ts
import {
  Configuration,
  StoreApi,
} from '';
import type { DeleteOrderRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new StoreApi();

  const body = {
    // number | ID of the order that needs to be deleted
    orderId: 789,
  } satisfies DeleteOrderRequest;

  try {
    const data = await api.deleteOrder(body);
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
| **orderId** | `number` | ID of the order that needs to be deleted | [Defaults to `undefined`] |

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
| **200** | order deleted |  -  |
| **400** | Invalid ID supplied |  -  |
| **404** | Order not found |  -  |
| **0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getInventory

> { [key: string]: number; } getInventory()

Returns pet inventories by status.

Returns a map of status codes to quantities.

### Example

```ts
import {
  Configuration,
  StoreApi,
} from '';
import type { GetInventoryRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: api_key
    apiKey: "YOUR API KEY",
  });
  const api = new StoreApi(config);

  try {
    const data = await api.getInventory();
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

**{ [key: string]: number; }**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getOrderById

> Order getOrderById(orderId)

Find purchase order by ID.

For valid response try integer IDs with value &lt;&#x3D; 5 or &gt; 10. Other values will generate exceptions.

### Example

```ts
import {
  Configuration,
  StoreApi,
} from '';
import type { GetOrderByIdRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new StoreApi();

  const body = {
    // number | ID of order that needs to be fetched
    orderId: 789,
  } satisfies GetOrderByIdRequest;

  try {
    const data = await api.getOrderById(body);
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
| **orderId** | `number` | ID of order that needs to be fetched | [Defaults to `undefined`] |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid ID supplied |  -  |
| **404** | Order not found |  -  |
| **0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## placeOrder

> Order placeOrder(order)

Place an order for a pet.

Place a new order in the store.

### Example

```ts
import {
  Configuration,
  StoreApi,
} from '';
import type { PlaceOrderRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new StoreApi();

  const body = {
    // Order (optional)
    order: ...,
  } satisfies PlaceOrderRequest;

  try {
    const data = await api.placeOrder(body);
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
| **order** | [Order](Order.md) |  | [Optional] |

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `application/x-www-form-urlencoded`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid input |  -  |
| **422** | Validation exception |  -  |
| **0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

