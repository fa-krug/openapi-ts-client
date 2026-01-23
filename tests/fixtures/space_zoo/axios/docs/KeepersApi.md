# KeepersApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**me**](#me) | **GET** /api/keepers/me | Me|

# **me**
> KeeperOut me()


### Example

```typescript
import {
    KeepersApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new KeepersApi(configuration);

const { status, data } = await apiInstance.me();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**KeeperOut**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

