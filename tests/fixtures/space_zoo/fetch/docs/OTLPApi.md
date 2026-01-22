# OTLPApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**otlpTraces**](OTLPApi.md#otlptraces) | **POST** /api/otlp/otlp/v1/traces/ | Otlp Traces |



## otlpTraces

> ResultSchema otlpTraces(activityLogSchema)

Otlp Traces

Receive and process OpenTelemetry protocol (OTLP) trace requests.

### Example

```ts
import {
  Configuration,
  OTLPApi,
} from '';
import type { OtlpTracesRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new OTLPApi();

  const body = {
    // ActivityLogSchema
    activityLogSchema: ...,
  } satisfies OtlpTracesRequest;

  try {
    const data = await api.otlpTraces(body);
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
| **activityLogSchema** | [ActivityLogSchema](ActivityLogSchema.md) |  | |

### Return type

[**ResultSchema**](ResultSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: `application/json`
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **416** | Range Not Satisfiable |  -  |
| **418** | I\&#39;m a Teapot |  -  |
| **451** | Unavailable For Legal Reasons |  -  |
| **425** | Too Early |  -  |
| **429** | Too Many Requests |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **406** | Not Acceptable |  -  |
| **407** | Proxy Authentication Required |  -  |
| **408** | Request Timeout |  -  |
| **409** | Conflict |  -  |
| **410** | Gone |  -  |
| **411** | Length Required |  -  |
| **412** | Precondition Failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)

