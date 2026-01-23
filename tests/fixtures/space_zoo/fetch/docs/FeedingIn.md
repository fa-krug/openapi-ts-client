
# FeedingIn


## Properties

Name | Type
------------ | -------------
`id` | number
`value` | string
`keeper` | string
`creature` | string
`priority` | string
`start` | Date
`end` | Date
`habitatId` | number
`administered` | boolean
`feedingDate` | Date

## Example

```typescript
import type { FeedingIn } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "value": null,
  "keeper": null,
  "creature": null,
  "priority": null,
  "start": null,
  "end": null,
  "habitatId": null,
  "administered": null,
  "feedingDate": null,
} satisfies FeedingIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FeedingIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


