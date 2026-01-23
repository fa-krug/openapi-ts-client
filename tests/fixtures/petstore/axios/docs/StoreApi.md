# StoreApi

All URIs are relative to */api/v3*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**deleteOrder**](#deleteorder) | **DELETE** /store/order/{orderId} | Delete purchase order by identifier.|
|[**getInventory**](#getinventory) | **GET** /store/inventory | Returns pet inventories by status.|
|[**getOrderById**](#getorderbyid) | **GET** /store/order/{orderId} | Find purchase order by ID.|
|[**placeOrder**](#placeorder) | **POST** /store/order | Place an order for a pet.|

# **deleteOrder**
> deleteOrder()

For valid response try integer IDs with value < 1000. Anything above 1000 or non-integers will generate API errors.

### Example

```typescript
import {
    StoreApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new StoreApi(configuration);

let orderId: number; //ID of the order that needs to be deleted (default to undefined)

const { status, data } = await apiInstance.deleteOrder(
    orderId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **orderId** | [**number**] | ID of the order that needs to be deleted | defaults to undefined|


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
|**200** | order deleted |  -  |
|**400** | Invalid ID supplied |  -  |
|**404** | Order not found |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getInventory**
> { [key: string]: number; } getInventory()

Returns a map of status codes to quantities.

### Example

```typescript
import {
    StoreApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new StoreApi(configuration);

const { status, data } = await apiInstance.getInventory();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**{ [key: string]: number; }**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | successful operation |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getOrderById**
> Order getOrderById()

For valid response try integer IDs with value <= 5 or > 10. Other values will generate exceptions.

### Example

```typescript
import {
    StoreApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new StoreApi(configuration);

let orderId: number; //ID of order that needs to be fetched (default to undefined)

const { status, data } = await apiInstance.getOrderById(
    orderId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **orderId** | [**number**] | ID of order that needs to be fetched | defaults to undefined|


### Return type

**Order**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | successful operation |  -  |
|**400** | Invalid ID supplied |  -  |
|**404** | Order not found |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **placeOrder**
> Order placeOrder()

Place a new order in the store.

### Example

```typescript
import {
    StoreApi,
    Configuration,
    Order
} from './api';

const configuration = new Configuration();
const apiInstance = new StoreApi(configuration);

let order: Order; // (optional)

const { status, data } = await apiInstance.placeOrder(
    order
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **order** | **Order**|  | |


### Return type

**Order**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | successful operation |  -  |
|**400** | Invalid input |  -  |
|**422** | Validation exception |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

