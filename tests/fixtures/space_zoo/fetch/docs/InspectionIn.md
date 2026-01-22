
# InspectionIn


## Properties

Name | Type
------------ | -------------
`id` | number
`name` | string
`templateId` | number
`habitatId` | number
`lastAuditId` | number
`content` | object
`version` | number
`status` | string
`score` | [Score1](Score1.md)
`archived` | boolean
`start` | Date
`end` | Date
`summary` | string

## Example

```typescript
import type { InspectionIn } from ''

// TODO: Update the object below with actual values
const example = {
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
} satisfies InspectionIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as InspectionIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


