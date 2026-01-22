
# SupplyOut


## Properties

Name | Type
------------ | -------------
`_package` | [FoodPackageOut](FoodPackageOut.md)
`habitat` | [HabitatNames](HabitatNames.md)
`image` | [EnclosureNames](EnclosureNames.md)
`tags` | [Array&lt;SupplyCategoryOut&gt;](SupplyCategoryOut.md)
`id` | number
`purl` | string
`version` | string
`bomRef` | string
`type` | string
`author` | string
`riskScore` | number
`riskDetails` | string
`licenses` | Array&lt;number&gt;
`dependsOn` | Array&lt;number&gt;

## Example

```typescript
import type { SupplyOut } from ''

// TODO: Update the object below with actual values
const example = {
  "_package": null,
  "habitat": null,
  "image": null,
  "tags": null,
  "id": null,
  "purl": null,
  "version": null,
  "bomRef": null,
  "type": null,
  "author": null,
  "riskScore": null,
  "riskDetails": null,
  "licenses": null,
  "dependsOn": null,
} satisfies SupplyOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as SupplyOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


