
# MigrationMetricOut


## Properties

Name | Type
------------ | -------------
`id` | number
`metricId` | string
`datetime` | Date
`habitatId` | number
`lastCommit` | Date
`commits` | number
`lastRelease` | Date
`openIssues` | number
`closedIssues` | number
`featureIssues` | number
`closedFeatureIssues` | number
`bugIssues` | number
`closedBugIssues` | number
`bugTtl` | number
`doingTime` | number
`reviewTime` | number
`codeQuality` | [CodeQuality](CodeQuality.md)

## Example

```typescript
import type { MigrationMetricOut } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "metricId": null,
  "datetime": null,
  "habitatId": null,
  "lastCommit": null,
  "commits": null,
  "lastRelease": null,
  "openIssues": null,
  "closedIssues": null,
  "featureIssues": null,
  "closedFeatureIssues": null,
  "bugIssues": null,
  "closedBugIssues": null,
  "bugTtl": null,
  "doingTime": null,
  "reviewTime": null,
  "codeQuality": null,
} satisfies MigrationMetricOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MigrationMetricOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


