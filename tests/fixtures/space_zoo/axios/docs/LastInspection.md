# LastInspection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projectName** | **string** |  | [optional] [default to '']
**templateName** | **string** |  | [optional] [default to '']
**id** | **number** |  | [optional] [default to undefined]
**name** | **string** |  | [default to undefined]
**template_id** | **number** |  | [optional] [default to undefined]
**habitat_id** | **number** |  | [optional] [default to undefined]
**last_audit_id** | **number** |  | [optional] [default to undefined]
**content** | **object** |  | [optional] [default to undefined]
**version** | **number** |  | [optional] [default to 0]
**status** | **string** |  | [optional] [default to 'started']
**score** | [**Score**](Score.md) |  | [optional] [default to undefined]
**archived** | **boolean** |  | [optional] [default to false]
**start** | **string** |  | [optional] [default to undefined]
**end** | **string** |  | [optional] [default to undefined]
**summary** | **string** |  | [optional] [default to undefined]

## Example

```typescript
import { LastInspection } from './api';

const instance: LastInspection = {
    projectName,
    templateName,
    id,
    name,
    template_id,
    habitat_id,
    last_audit_id,
    content,
    version,
    status,
    score,
    archived,
    start,
    end,
    summary,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
