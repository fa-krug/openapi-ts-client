# OTLPApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**otlpTraces**](#otlptraces) | **POST** /api/otlp/otlp/v1/traces/ | Otlp Traces|

# **otlpTraces**
> ResultSchema otlpTraces(activityLogSchema)

Receive and process OpenTelemetry protocol (OTLP) trace requests.

### Example

```typescript
import {
    OTLPApi,
    Configuration,
    ActivityLogSchema
} from './api';

const configuration = new Configuration();
const apiInstance = new OTLPApi(configuration);

let activityLogSchema: ActivityLogSchema; //

const { status, data } = await apiInstance.otlpTraces(
    activityLogSchema
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **activityLogSchema** | **ActivityLogSchema**|  | |


### Return type

**ResultSchema**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**201** | Created |  -  |
|**416** | Range Not Satisfiable |  -  |
|**418** | I\&#39;m a Teapot |  -  |
|**451** | Unavailable For Legal Reasons |  -  |
|**425** | Too Early |  -  |
|**429** | Too Many Requests |  -  |
|**400** | Bad Request |  -  |
|**401** | Unauthorized |  -  |
|**402** | Payment Required |  -  |
|**403** | Forbidden |  -  |
|**404** | Not Found |  -  |
|**405** | Method Not Allowed |  -  |
|**406** | Not Acceptable |  -  |
|**407** | Proxy Authentication Required |  -  |
|**408** | Request Timeout |  -  |
|**409** | Conflict |  -  |
|**410** | Gone |  -  |
|**411** | Length Required |  -  |
|**412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

