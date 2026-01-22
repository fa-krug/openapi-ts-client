
# ActivityLogSchema

Schema for OTLP traces.

## Properties

Name | Type
------------ | -------------
`resourceSpans` | Array&lt;any&gt;

## Example

```typescript
import type { ActivityLogSchema } from ''

// TODO: Update the object below with actual values
const example = {
  "resourceSpans": null,
} satisfies ActivityLogSchema

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as ActivityLogSchema
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


