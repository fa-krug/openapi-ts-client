
# InspectionOut


## Properties

Name | Type
------------ | -------------
`projectName` | string
`templateName` | string
`last` | [LastInspection](LastInspection.md)
`id` | number
`name` | string
`templateId` | number
`habitatId` | number
`lastAuditId` | number
`content` | object
`version` | number
`status` | string
`score` | [Score](Score.md)
`archived` | boolean
`start` | Date
`end` | Date
`summary` | string

## Example

```typescript
import type { InspectionOut } from ''

// TODO: Update the object below with actual values
const example = {
  "projectName": null,
  "templateName": null,
  "last": null,
  "id": null,
  "name": null,
  "templateId": null,
  "habitatId": null,
  "lastAuditId": null,
  "content": null,
  "version": null,
  "status": null,
  "score": null,
  "archived": null,
  "start": null,
  "end": null,
  "summary": null,
} satisfies InspectionOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as InspectionOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


