
# WellnessMetricFilter


## Properties

Name | Type
------------ | -------------
`id` | string
`metricId` | string
`datetime` | string
`habitat` | string
`linesOfCode` | string
`testCoverage` | string
`codeDuplication` | string
`reliabilityRating` | string
`securityRating` | string
`securityReviewRating` | string
`maintainabilityRating` | string

## Example

```typescript
import type { WellnessMetricFilter } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "metricId": null,
  "datetime": null,
  "habitat": null,
  "linesOfCode": null,
  "testCoverage": null,
  "codeDuplication": null,
  "reliabilityRating": null,
  "securityRating": null,
  "securityReviewRating": null,
  "maintainabilityRating": null,
} satisfies WellnessMetricFilter

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as WellnessMetricFilter
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


