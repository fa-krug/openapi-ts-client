
# SupplyIn


## Properties

Name | Type
------------ | -------------
`id` | number
`purl` | string
`packageId` | number
`version` | string
`imageId` | number
`bomRef` | string
`type` | string
`author` | string
`riskScore` | number
`riskDetails` | string
`licenses` | Array&lt;number&gt;
`dependsOn` | Array&lt;number&gt;
`tags` | Array&lt;number&gt;

## Example

```typescript
import type { SupplyIn } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "purl": null,
  "packageId": null,
  "version": null,
  "imageId": null,
  "bomRef": null,
  "type": null,
  "author": null,
  "riskScore": null,
  "riskDetails": null,
  "licenses": null,
  "dependsOn": null,
  "tags": null,
} satisfies SupplyIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SupplyIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


