
# SupplyDetails


## Properties

Name | Type
------------ | -------------
`_package` | [FoodPackageOut](FoodPackageOut.md)
`habitat` | [HabitatNames](HabitatNames.md)
`image` | [EnclosureNames](EnclosureNames.md)
`licenses` | [Array&lt;PermitOut&gt;](PermitOut.md)
`tags` | [Array&lt;SupplyCategoryOut&gt;](SupplyCategoryOut.md)
`vulnerabilities` | [Array&lt;VulnerabilityOut&gt;](VulnerabilityOut.md)
`dependsOn` | [Array&lt;SupplyOut&gt;](SupplyOut.md)
`isOutdated` | boolean
`hasAllowedVersion` | boolean
`id` | number
`purl` | string
`version` | string
`bomRef` | string
`type` | string
`author` | string
`riskScore` | number
`riskDetails` | string

## Example

```typescript
import type { SupplyDetails } from ''

// TODO: Update the object below with actual values
const example = {
  "_package": null,
  "habitat": null,
  "image": null,
  "licenses": null,
  "tags": null,
  "vulnerabilities": null,
  "dependsOn": null,
  "isOutdated": null,
  "hasAllowedVersion": null,
  "id": null,
  "purl": null,
  "version": null,
  "bomRef": null,
  "type": null,
  "author": null,
  "riskScore": null,
  "riskDetails": null,
} satisfies SupplyDetails

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SupplyDetails
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


