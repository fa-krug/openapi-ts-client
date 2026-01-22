# UserApi

All URIs are relative to */api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUser**](UserApi.md#createuser) | **POST** /user | Create user. |
| [**createUsersWithListInput**](UserApi.md#createuserswithlistinput) | **POST** /user/createWithList | Creates list of users with given input array. |
| [**deleteUser**](UserApi.md#deleteuser) | **DELETE** /user/{username} | Delete user resource. |
| [**getUserByName**](UserApi.md#getuserbyname) | **GET** /user/{username} | Get user by user name. |
| [**loginUser**](UserApi.md#loginuser) | **GET** /user/login | Logs user into the system. |
| [**logoutUser**](UserApi.md#logoutuser) | **GET** /user/logout | Logs out current logged in user session. |
| [**updateUser**](UserApi.md#updateuser) | **PUT** /user/{username} | Update user resource. |



## createUser

> User createUser(user)

Create user.

This can only be done by the logged in user.

### Example

```ts
import {
  Configuration,
  UserApi,
} from '';
import type { CreateUserRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new UserApi();

  const body = {
    // User | Created user object (optional)
    user: ...,
  } satisfies CreateUserRequest;

  try {
    const data = await api.createUser(body);
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
| **user** | [User](User.md) | Created user object | [Optional] |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `application/x-www-form-urlencoded`
- **Accept**: `application/json`, `application/xml`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createUsersWithListInput

> User createUsersWithListInput(user)

Creates list of users with given input array.

Creates list of users with given input array.

### Example

```ts
import {
  Configuration,
  UserApi,
} from '';
import type { CreateUsersWithListInputRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new UserApi();

  const body = {
    // Array<User> (optional)
    user: ...,
  } satisfies CreateUsersWithListInputRequest;

  try {
    const data = await api.createUsersWithListInput(body);
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
| **user** | `Array<User>` |  | [Optional] |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`, `application/xml`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## deleteUser

> deleteUser(username)

Delete user resource.

This can only be done by the logged in user.

### Example

```ts
import {
  Configuration,
  UserApi,
} from '';
import type { DeleteUserRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new UserApi();

  const body = {
    // string | The name that needs to be deleted
    username: username_example,
  } satisfies DeleteUserRequest;

  try {
    const data = await api.deleteUser(body);
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
| **username** | `string` | The name that needs to be deleted | [Defaults to `undefined`] |

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
| **200** | User deleted |  -  |
| **400** | Invalid username supplied |  -  |
| **404** | User not found |  -  |
| **0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## getUserByName

> User getUserByName(username)

Get user by user name.

Get user detail based on username.

### Example

```ts
import {
  Configuration,
  UserApi,
} from '';
import type { GetUserByNameRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new UserApi();

  const body = {
    // string | The name that needs to be fetched. Use user1 for testing
    username: username_example,
  } satisfies GetUserByNameRequest;

  try {
    const data = await api.getUserByName(body);
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
| **username** | `string` | The name that needs to be fetched. Use user1 for testing | [Defaults to `undefined`] |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`, `application/xml`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid username supplied |  -  |
| **404** | User not found |  -  |
| **0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## loginUser

> string loginUser(username, password)

Logs user into the system.

Log into the system.

### Example

```ts
import {
  Configuration,
  UserApi,
} from '';
import type { LoginUserRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new UserApi();

  const body = {
    // string | The user name for login (optional)
    username: username_example,
    // string | The password for login in clear text (optional)
    password: password_example,
  } satisfies LoginUserRequest;

  try {
    const data = await api.loginUser(body);
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
| **username** | `string` | The user name for login | [Optional] [Defaults to `undefined`] |
| **password** | `string` | The password for login in clear text | [Optional] [Defaults to `undefined`] |

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/xml`, `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  * X-Rate-Limit - calls per hour allowed by the user <br>  * X-Expires-After - date in UTC when token expires <br>  |
| **400** | Invalid username/password supplied |  -  |
| **0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## logoutUser

> logoutUser()

Logs out current logged in user session.

Log user out of the system.

### Example

```ts
import {
  Configuration,
  UserApi,
} from '';
import type { LogoutUserRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new UserApi();

  try {
    const data = await api.logoutUser();
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

`void` (Empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## updateUser

> updateUser(username, user)

Update user resource.

This can only be done by the logged in user.

### Example

```ts
import {
  Configuration,
  UserApi,
} from '';
import type { UpdateUserRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new UserApi();

  const body = {
    // string | name that need to be deleted
    username: username_example,
    // User | Update an existent user in the store (optional)
    user: ...,
  } satisfies UpdateUserRequest;

  try {
    const data = await api.updateUser(body);
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
| **username** | `string` | name that need to be deleted | [Defaults to `undefined`] |
| **user** | [User](User.md) | Update an existent user in the store | [Optional] |

### Return type

`void` (Empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`, `application/xml`, `application/x-www-form-urlencoded`
- **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | bad request |  -  |
| **404** | user not found |  -  |
| **0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

