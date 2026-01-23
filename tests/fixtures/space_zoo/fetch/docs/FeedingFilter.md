
# FeedingFilter


## Properties

Name | Type
------------ | -------------
`id` | string
`value` | string
`keeper` | string
`creature` | string
`priority` | string
`start` | string
`end` | string
`habitat` | string
`administered` | boolean
`feedingDate` | string

## Example

```typescript
import type { FeedingFilter } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "value": null,
  "keeper": null,
  "creature": null,
  "priority": null,
  "start": null,
  "end": null,
  "habitat": null,
  "administered": null,
  "feedingDate": null,
} satisfies FeedingFilter

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FeedingFilter
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


