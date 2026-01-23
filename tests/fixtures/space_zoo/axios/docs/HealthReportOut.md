# HealthReportOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **number** |  | [optional] [default to undefined]
**name** | **string** |  | [default to undefined]
**latestAudits** | **boolean** |  | [optional] [default to false]
**startDate** | **string** |  | [optional] [default to undefined]
**endDate** | **string** |  | [optional] [default to undefined]
**type** | **string** |  | [optional] [default to 'HTML']
**simplify** | **boolean** |  | [optional] [default to false]
**blocks** | **string** |  | [optional] [default to undefined]
**permission** | **string** |  | [optional] [default to 'QMSuite-regular-editAccess']
**privacy** | **string** |  | [optional] [default to 'Internal']
**audit** | **Array&lt;number&gt;** |  | [default to undefined]
**template** | **Array&lt;number&gt;** |  | [default to undefined]

## Example

```typescript
import { HealthReportOut } from './api';

const instance: HealthReportOut = {
    id,
    name,
    latestAudits,
    startDate,
    endDate,
    type,
    simplify,
    blocks,
    permission,
    privacy,
    audit,
    template,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
