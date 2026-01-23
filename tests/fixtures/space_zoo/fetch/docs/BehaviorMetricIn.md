
# BehaviorMetricIn


## Properties

Name | Type
------------ | -------------
`id` | number
`spanId` | string
`start` | Date
`end` | Date
`timespanNs` | number
`httpMetricId` | number
`name` | string
`value` | number
`details` | object
`createdBy` | string
`message` | string
`state` | string

## Example

```typescript
import type { BehaviorMetricIn } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "spanId": null,
  "start": null,
  "end": null,
  "timespanNs": null,
  "httpMetricId": null,
  "name": null,
  "value": null,
  "details": null,
  "createdBy": null,
  "message": null,
  "state": null,
} satisfies BehaviorMetricIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as BehaviorMetricIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


