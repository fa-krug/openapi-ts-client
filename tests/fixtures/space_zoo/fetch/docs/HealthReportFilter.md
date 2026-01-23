
# HealthReportFilter


## Properties

Name | Type
------------ | -------------
`id` | string
`name` | string
`latestAudits` | boolean
`startDate` | string
`endDate` | string
`type` | string
`simplify` | boolean
`blocks` | string
`permission` | string
`privacy` | string
`audit` | Array&lt;number&gt;
`template` | Array&lt;number&gt;

## Example

```typescript
import type { HealthReportFilter } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "latestAudits": null,
  "startDate": null,
  "endDate": null,
  "type": null,
  "simplify": null,
  "blocks": null,
  "permission": null,
  "privacy": null,
  "audit": null,
  "template": null,
} satisfies HealthReportFilter

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as HealthReportFilter
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


