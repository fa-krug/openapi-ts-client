# TasksApi

All URIs are relative to *http://localhost*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**checkPackages**](#checkpackages) | **POST** /api/tasks/check-packages/ | Check Packages|
|[**collectSbom**](#collectsbom) | **POST** /api/tasks/collect-sbom/ | Collect Sbom|
|[**createMetricsFromGitlab**](#createmetricsfromgitlab) | **POST** /api/tasks/metrics-from-gitlab | Create Metrics From Gitlab|
|[**createMetricsFromSonarqube**](#createmetricsfromsonarqube) | **POST** /api/tasks/metrics-from-sonarqube | Create Metrics From Sonarqube|
|[**createProjectFromGitlab**](#createprojectfromgitlab) | **POST** /api/tasks/projects-from-gitlab | Create Project From Gitlab|
|[**createProjectFromSonarqube**](#createprojectfromsonarqube) | **POST** /api/tasks/projects-from-sonarqube | Create Project From Sonarqube|
|[**createUpdateScoreView**](#createupdatescoreview) | **POST** /api/tasks/update-score-view | Create Update Score View|

# **checkPackages**
> ResultSchema checkPackages()

Collect latest version from packages.

### Example

```typescript
import {
    TasksApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TasksApi(configuration);

const { status, data } = await apiInstance.checkPackages();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**ResultSchema**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
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
|**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collectSbom**
> ResultSchema collectSbom()

Collect SBOM from project docker images.

### Example

```typescript
import {
    TasksApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TasksApi(configuration);

const { status, data } = await apiInstance.collectSbom();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**ResultSchema**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
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
|**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createMetricsFromGitlab**
> ResultSchema createMetricsFromGitlab()

Import project metrics from GitLab.

### Example

```typescript
import {
    TasksApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TasksApi(configuration);

const { status, data } = await apiInstance.createMetricsFromGitlab();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**ResultSchema**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createMetricsFromSonarqube**
> ResultSchema createMetricsFromSonarqube()

Import project metrics from SonarQube.

### Example

```typescript
import {
    TasksApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TasksApi(configuration);

const { status, data } = await apiInstance.createMetricsFromSonarqube();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**ResultSchema**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
|**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createProjectFromGitlab**
> ResultSchema createProjectFromGitlab()

Import projects from GitLab.

### Example

```typescript
import {
    TasksApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TasksApi(configuration);

const { status, data } = await apiInstance.createProjectFromGitlab();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**ResultSchema**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
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

# **createProjectFromSonarqube**
> ResultSchema createProjectFromSonarqube()

Import projects from SonarQube.

### Example

```typescript
import {
    TasksApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TasksApi(configuration);

const { status, data } = await apiInstance.createProjectFromSonarqube();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**ResultSchema**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

# **createUpdateScoreView**
> ResultSchema createUpdateScoreView()

Force update of all scores. This task should only be trigger after score calculation changes.

### Example

```typescript
import {
    TasksApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new TasksApi(configuration);

const { status, data } = await apiInstance.createUpdateScoreView();
```

### Parameters
This endpoint does not have any parameters.


### Return type

**ResultSchema**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | OK |  -  |
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

