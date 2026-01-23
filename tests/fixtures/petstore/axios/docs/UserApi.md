# UserApi

All URIs are relative to */api/v3*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**createUser**](#createuser) | **POST** /user | Create user.|
|[**createUsersWithListInput**](#createuserswithlistinput) | **POST** /user/createWithList | Creates list of users with given input array.|
|[**deleteUser**](#deleteuser) | **DELETE** /user/{username} | Delete user resource.|
|[**getUserByName**](#getuserbyname) | **GET** /user/{username} | Get user by user name.|
|[**loginUser**](#loginuser) | **GET** /user/login | Logs user into the system.|
|[**logoutUser**](#logoutuser) | **GET** /user/logout | Logs out current logged in user session.|
|[**updateUser**](#updateuser) | **PUT** /user/{username} | Update user resource.|

# **createUser**
> User createUser()

This can only be done by the logged in user.

### Example

```typescript
import {
    UserApi,
    Configuration,
    User
} from './api';

const configuration = new Configuration();
const apiInstance = new UserApi(configuration);

let user: User; //Created user object (optional)

const { status, data } = await apiInstance.createUser(
    user
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user** | **User**| Created user object | |


### Return type

**User**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | successful operation |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createUsersWithListInput**
> User createUsersWithListInput()

Creates list of users with given input array.

### Example

```typescript
import {
    UserApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new UserApi(configuration);

let user: Array<User>; // (optional)

const { status, data } = await apiInstance.createUsersWithListInput(
    user
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user** | **Array<User>**|  | |


### Return type

**User**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful operation |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteUser**
> deleteUser()

This can only be done by the logged in user.

### Example

```typescript
import {
    UserApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new UserApi(configuration);

let username: string; //The name that needs to be deleted (default to undefined)

const { status, data } = await apiInstance.deleteUser(
    username
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **username** | [**string**] | The name that needs to be deleted | defaults to undefined|


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
|**200** | User deleted |  -  |
|**400** | Invalid username supplied |  -  |
|**404** | User not found |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getUserByName**
> User getUserByName()

Get user detail based on username.

### Example

```typescript
import {
    UserApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new UserApi(configuration);

let username: string; //The name that needs to be fetched. Use user1 for testing (default to undefined)

const { status, data } = await apiInstance.getUserByName(
    username
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **username** | [**string**] | The name that needs to be fetched. Use user1 for testing | defaults to undefined|


### Return type

**User**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | successful operation |  -  |
|**400** | Invalid username supplied |  -  |
|**404** | User not found |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loginUser**
> string loginUser()

Log into the system.

### Example

```typescript
import {
    UserApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new UserApi(configuration);

let username: string; //The user name for login (optional) (default to undefined)
let password: string; //The password for login in clear text (optional) (default to undefined)

const { status, data } = await apiInstance.loginUser(
    username,
    password
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **username** | [**string**] | The user name for login | (optional) defaults to undefined|
| **password** | [**string**] | The password for login in clear text | (optional) defaults to undefined|


### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | successful operation |  * X-Rate-Limit - calls per hour allowed by the user <br>  * X-Expires-After - date in UTC when token expires <br>  |
|**400** | Invalid username/password supplied |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logoutUser**
> logoutUser()

Log user out of the system.

### Example

```typescript
import {
    UserApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new UserApi(configuration);

const { status, data } = await apiInstance.logoutUser();
```

### Parameters
This endpoint does not have any parameters.


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
|**200** | successful operation |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateUser**
> updateUser()

This can only be done by the logged in user.

### Example

```typescript
import {
    UserApi,
    Configuration,
    User
} from './api';

const configuration = new Configuration();
const apiInstance = new UserApi(configuration);

let username: string; //name that need to be deleted (default to undefined)
let user: User; //Update an existent user in the store (optional)

const { status, data } = await apiInstance.updateUser(
    username,
    user
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **user** | **User**| Update an existent user in the store | |
| **username** | [**string**] | name that need to be deleted | defaults to undefined|


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | successful operation |  -  |
|**400** | bad request |  -  |
|**404** | user not found |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

