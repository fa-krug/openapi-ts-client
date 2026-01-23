# MigrationMetricOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [default to undefined]
**metricId** | **string** | Unique ID of the metric | [optional] [default to undefined]
**datetime** | **string** |  | [optional] [default to undefined]
**habitat_id** | **number** |  | [optional] [default to undefined]
**lastCommit** | **string** |  | [optional] [default to undefined]
**commits** | **number** |  | [optional] [default to undefined]
**lastRelease** | **string** |  | [optional] [default to undefined]
**openIssues** | **number** |  | [optional] [default to undefined]
**closedIssues** | **number** |  | [optional] [default to undefined]
**featureIssues** | **number** |  | [optional] [default to undefined]
**closedFeatureIssues** | **number** |  | [optional] [default to undefined]
**bugIssues** | **number** |  | [optional] [default to undefined]
**closedBugIssues** | **number** |  | [optional] [default to undefined]
**bugTtl** | **number** |  | [optional] [default to undefined]
**doingTime** | **number** |  | [optional] [default to undefined]
**reviewTime** | **number** |  | [optional] [default to undefined]
**codeQuality** | [**CodeQuality**](CodeQuality.md) |  | [optional] [default to undefined]

## Example

```typescript
import { MigrationMetricOut } from './api';

const instance: MigrationMetricOut = {
    id,
    metricId,
    datetime,
    habitat_id,
    lastCommit,
    commits,
    lastRelease,
    openIssues,
    closedIssues,
    featureIssues,
    closedFeatureIssues,
    bugIssues,
    closedBugIssues,
    bugTtl,
    doingTime,
    reviewTime,
    codeQuality,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
