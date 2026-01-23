
# MigrationMetricFilter


## Properties

Name | Type
------------ | -------------
`id` | string
`metricId` | string
`datetime` | string
`habitat` | string
`lastCommit` | string
`commits` | string
`lastRelease` | string
`openIssues` | string
`closedIssues` | string
`featureIssues` | string
`closedFeatureIssues` | string
`bugIssues` | string
`closedBugIssues` | string
`bugTtl` | string
`doingTime` | string
`reviewTime` | string
`codeQuality` | string

## Example

```typescript
import type { MigrationMetricFilter } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "metricId": null,
  "datetime": null,
  "habitat": null,
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
} satisfies MigrationMetricFilter

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as MigrationMetricFilter
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


