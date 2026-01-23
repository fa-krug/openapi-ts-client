# WellnessMetricOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [default to undefined]
**metricId** | **string** | Unique ID of the metric | [optional] [default to undefined]
**datetime** | **string** |  | [optional] [default to undefined]
**habitat_id** | **number** |  | [optional] [default to undefined]
**linesOfCode** | **number** |  | [optional] [default to undefined]
**testCoverage** | [**TestCoverage**](TestCoverage.md) |  | [optional] [default to undefined]
**codeDuplication** | [**CodeDuplication**](CodeDuplication.md) |  | [optional] [default to undefined]
**reliabilityRating** | [**ReliabilityRating**](ReliabilityRating.md) |  | [optional] [default to undefined]
**securityRating** | [**SecurityRating**](SecurityRating.md) |  | [optional] [default to undefined]
**securityReviewRating** | [**SecurityReviewRating**](SecurityReviewRating.md) |  | [optional] [default to undefined]
**maintainabilityRating** | [**MaintainabilityRating**](MaintainabilityRating.md) |  | [optional] [default to undefined]

## Example

```typescript
import { WellnessMetricOut } from './api';

const instance: WellnessMetricOut = {
    id,
    metricId,
    datetime,
    habitat_id,
    linesOfCode,
    testCoverage,
    codeDuplication,
    reliabilityRating,
    securityRating,
    securityReviewRating,
    maintainabilityRating,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
