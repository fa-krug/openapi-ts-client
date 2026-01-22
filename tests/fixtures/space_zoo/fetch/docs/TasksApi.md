# TasksApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkPackages**](TasksApi.md#checkpackages) | **POST** /api/tasks/check-packages/ | Check Packages |
| [**collectSbom**](TasksApi.md#collectsbom) | **POST** /api/tasks/collect-sbom/ | Collect Sbom |
| [**createMetricsFromGitlab**](TasksApi.md#createmetricsfromgitlab) | **POST** /api/tasks/metrics-from-gitlab | Create Metrics From Gitlab |
| [**createMetricsFromSonarqube**](TasksApi.md#createmetricsfromsonarqube) | **POST** /api/tasks/metrics-from-sonarqube | Create Metrics From Sonarqube |
| [**createProjectFromGitlab**](TasksApi.md#createprojectfromgitlab) | **POST** /api/tasks/projects-from-gitlab | Create Project From Gitlab |
| [**createProjectFromSonarqube**](TasksApi.md#createprojectfromsonarqube) | **POST** /api/tasks/projects-from-sonarqube | Create Project From Sonarqube |
| [**createUpdateScoreView**](TasksApi.md#createupdatescoreview) | **POST** /api/tasks/update-score-view | Create Update Score View |



## checkPackages

> ResultSchema checkPackages()

Check Packages

Collect latest version from packages.

### Example

```ts
import {
  Configuration,
  TasksApi,
} from '';
import type { CheckPackagesRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new TasksApi();

  try {
    const data = await api.checkPackages();
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

[**ResultSchema**](ResultSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
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
| **503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## collectSbom

> ResultSchema collectSbom()

Collect Sbom

Collect SBOM from project docker images.

### Example

```ts
import {
  Configuration,
  TasksApi,
} from '';
import type { CollectSbomRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new TasksApi();

  try {
    const data = await api.collectSbom();
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

[**ResultSchema**](ResultSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
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
| **503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createMetricsFromGitlab

> ResultSchema createMetricsFromGitlab()

Create Metrics From Gitlab

Import project metrics from GitLab.

### Example

```ts
import {
  Configuration,
  TasksApi,
} from '';
import type { CreateMetricsFromGitlabRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new TasksApi();

  try {
    const data = await api.createMetricsFromGitlab();
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

[**ResultSchema**](ResultSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createMetricsFromSonarqube

> ResultSchema createMetricsFromSonarqube()

Create Metrics From Sonarqube

Import project metrics from SonarQube.

### Example

```ts
import {
  Configuration,
  TasksApi,
} from '';
import type { CreateMetricsFromSonarqubeRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new TasksApi();

  try {
    const data = await api.createMetricsFromSonarqube();
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

[**ResultSchema**](ResultSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


## createProjectFromGitlab

> ResultSchema createProjectFromGitlab()

Create Project From Gitlab

Import projects from GitLab.

### Example

```ts
import {
  Configuration,
  TasksApi,
} from '';
import type { CreateProjectFromGitlabRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new TasksApi();

  try {
    const data = await api.createProjectFromGitlab();
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

[**ResultSchema**](ResultSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
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


## createProjectFromSonarqube

> ResultSchema createProjectFromSonarqube()

Create Project From Sonarqube

Import projects from SonarQube.

### Example

```ts
import {
  Configuration,
  TasksApi,
} from '';
import type { CreateProjectFromSonarqubeRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new TasksApi();

  try {
    const data = await api.createProjectFromSonarqube();
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

[**ResultSchema**](ResultSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
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


## createUpdateScoreView

> ResultSchema createUpdateScoreView()

Create Update Score View

Force update of all scores. This task should only be trigger after score calculation changes.

### Example

```ts
import {
  Configuration,
  TasksApi,
} from '';
import type { CreateUpdateScoreViewRequest } from '';

async function example() {
  console.log("🚀 Testing  SDK...");
  const api = new TasksApi();

  try {
    const data = await api.createUpdateScoreView();
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

[**ResultSchema**](ResultSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: `application/json`


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
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

