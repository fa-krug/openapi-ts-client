
# EnvironmentReadingOut


## Properties

Name | Type
------------ | -------------
`id` | number
`spanId` | string
`start` | Date
`end` | Date
`timespanNs` | number
`habitatId` | number
`url` | string
`method` | string
`version` | string
`statusCode` | number

## Example

```typescript
import type { EnvironmentReadingOut } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "spanId": null,
  "start": null,
  "end": null,
  "timespanNs": null,
  "habitatId": null,
  "url": null,
  "method": null,
  "version": null,
  "statusCode": null,
} satisfies EnvironmentReadingOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as EnvironmentReadingOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


