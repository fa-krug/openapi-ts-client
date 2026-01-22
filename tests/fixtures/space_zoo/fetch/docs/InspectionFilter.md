
# InspectionFilter


## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`template` | string
`habitat` | string
`lastAudit` | string
`content` | string
`version` | string
`status` | string
`score` | string
`archived` | boolean
`start` | string
`end` | string
`summary` | string

## Example

```typescript
import type { InspectionFilter } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "template": null,
  "habitat": null,
  "lastAudit": null,
  "content": null,
  "version": null,
  "status": null,
  "score": null,
  "archived": null,
  "start": null,
  "end": null,
  "summary": null,
} satisfies InspectionFilter

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as InspectionFilter
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


