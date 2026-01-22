
# SupplyFilter


## Properties

Name | Type
------------ | -------------
`id` | string
`purl` | string
`_package` | string
`version` | string
`image` | string
`bomRef` | string
`type` | string
`author` | string
`riskScore` | string
`riskDetails` | string
`licenses` | Array&lt;number&gt;
`dependsOn` | Array&lt;number&gt;
`tags` | Array&lt;number&gt;

## Example

```typescript
import type { SupplyFilter } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "purl": null,
  "_package": null,
  "version": null,
  "image": null,
  "bomRef": null,
  "type": null,
  "author": null,
  "riskScore": null,
  "riskDetails": null,
  "licenses": null,
  "dependsOn": null,
  "tags": null,
} satisfies SupplyFilter

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SupplyFilter
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


