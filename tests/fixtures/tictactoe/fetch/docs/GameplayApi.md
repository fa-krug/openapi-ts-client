# GameplayApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBoard**](GameplayApi.md#getboard) | **GET** /board | Get the whole board |
| [**getSquare**](GameplayApi.md#getsquare) | **GET** /board/{row}/{column} | Get a single board square |
| [**putSquare**](GameplayApi.md#putsquare) | **PUT** /board/{row}/{column} | Set a single board square |



## getBoard

> Status getBoard()

Get the whole board

Retrieves the current state of the board and the winner.

### Example

```ts
import {
  Configuration,
  GameplayApi,
} from '';
import type { GetBoardRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // To configure API key authorization: defaultApiKey
    apiKey: "YOUR API KEY",
    // To configure OAuth2 access token for authorization: app2AppOauth application
    accessToken: "YOUR ACCESS TOKEN",
  });
  const api = new GameplayApi(config);

  try {
    const data = await api.getBoard();
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

[**Status**](Status.md)

### Authorization

[defaultApiKey](../README.md#defaultApiKey), [app2AppOauth application](../README.md#app2AppOauth-application)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getSquare

> Mark getSquare(row, column)

Get a single board square

Retrieves the requested square.

### Example

```ts
import {
  Configuration,
  GameplayApi,
} from '';
import type { GetSquareRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerHttpAuthentication
    accessToken: "YOUR BEARER TOKEN",
    // To configure OAuth2 access token for authorization: user2AppOauth accessCode
    accessToken: "YOUR ACCESS TOKEN",
  });
  const api = new GameplayApi(config);

  const body = {
    // number | Board row (vertical coordinate)
    row: 56,
    // number | Board column (horizontal coordinate)
    column: 56,
  } satisfies GetSquareRequest;

  try {
    const data = await api.getSquare(body);
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
| **row** | `number` | Board row (vertical coordinate) | [Defaults to `undefined`] |
| **column** | `number` | Board column (horizontal coordinate) | [Defaults to `undefined`] |

### Return type

[**Mark**](Mark.md)

### Authorization

[bearerHttpAuthentication](../README.md#bearerHttpAuthentication), [user2AppOauth accessCode](../README.md#user2AppOauth-accessCode)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | The provided parameters are incorrect |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## putSquare

> Status putSquare(row, column, body)

Set a single board square

Places a mark on the board and retrieves the whole board and the winner (if any).

### Example

```ts
import {
  Configuration,
  GameplayApi,
} from '';
import type { PutSquareRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const config = new Configuration({ 
    // Configure HTTP bearer authorization: bearerHttpAuthentication
    accessToken: "YOUR BEARER TOKEN",
    // To configure OAuth2 access token for authorization: user2AppOauth accessCode
    accessToken: "YOUR ACCESS TOKEN",
  });
  const api = new GameplayApi(config);

  const body = {
    // number | Board row (vertical coordinate)
    row: 56,
    // number | Board column (horizontal coordinate)
    column: 56,
    // string
    body: ...,
  } satisfies PutSquareRequest;

  try {
    const data = await api.putSquare(body);
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
| **row** | `number` | Board row (vertical coordinate) | [Defaults to `undefined`] |
| **column** | `number` | Board column (horizontal coordinate) | [Defaults to `undefined`] |
| **body** | `string` |  | |

### Return type

[**Status**](Status.md)

### Authorization

[bearerHttpAuthentication](../README.md#bearerHttpAuthentication), [user2AppOauth accessCode](../README.md#user2AppOauth-accessCode)

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `text/html`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | The provided parameters are incorrect |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

