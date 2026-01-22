
# FoodPackageOut


## Properties

Name | Type
------------ | -------------
`id` | number
`name` | string
`allowedSpecifier` | string
`latestVersion` | string
`hidden` | boolean
`allowed` | boolean

## Example

```typescript
import type { FoodPackageOut } from ''

// TODO: Update the object below with actual values
const example = {
  "id": null,
  "name": null,
  "allowedSpecifier": null,
  "latestVersion": null,
  "hidden": null,
  "allowed": null,
} satisfies FoodPackageOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as FoodPackageOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


