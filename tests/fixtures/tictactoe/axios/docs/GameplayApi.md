# GameplayApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**getBoard**](#getboard) | **GET** /board | Get the whole board|
|[**getSquare**](#getsquare) | **GET** /board/{row}/{column} | Get a single board square|
|[**putSquare**](#putsquare) | **PUT** /board/{row}/{column} | Set a single board square|

# **getBoard**
> Status getBoard()

Retrieves the current state of the board and the winner.

### Example

```typescript
import {
    GameplayApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new GameplayApi(configuration);

const { status, data } = await apiInstance.getBoard();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**Status**

### Authorization

[defaultApiKey](../README.md#defaultApiKey), [app2AppOauth](../README.md#app2AppOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getSquare**
> Mark getSquare()

Retrieves the requested square.

### Example

```typescript
import {
    GameplayApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new GameplayApi(configuration);

let row: number; //Board row (vertical coordinate) (default to undefined)
let column: number; //Board column (horizontal coordinate) (default to undefined)

const { status, data } = await apiInstance.getSquare(
    row,
    column
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **row** | [**number**] | Board row (vertical coordinate) | defaults to undefined|
| **column** | [**number**] | Board column (horizontal coordinate) | defaults to undefined|


### Return type

**Mark**

### Authorization

[bearerHttpAuthentication](../README.md#bearerHttpAuthentication), [user2AppOauth](../README.md#user2AppOauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**400** | The provided parameters are incorrect |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putSquare**
> Status putSquare(body)

Places a mark on the board and retrieves the whole board and the winner (if any).

### Example

```typescript
import {
    GameplayApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new GameplayApi(configuration);

let row: number; //Board row (vertical coordinate) (default to undefined)
let column: number; //Board column (horizontal coordinate) (default to undefined)
let body: string; //

const { status, data } = await apiInstance.putSquare(
    row,
    column,
    body
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | **string**|  | |
| **row** | [**number**] | Board row (vertical coordinate) | defaults to undefined|
| **column** | [**number**] | Board column (horizontal coordinate) | defaults to undefined|


### Return type

**Status**

### Authorization

[bearerHttpAuthentication](../README.md#bearerHttpAuthentication), [user2AppOauth](../README.md#user2AppOauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**400** | The provided parameters are incorrect |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

