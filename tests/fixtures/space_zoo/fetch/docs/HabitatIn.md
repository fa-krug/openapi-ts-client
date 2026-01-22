
# HabitatIn


## Properties

Name | Type
------------ | -------------
`originPlanets` | [Array&lt;OriginPlanetIn&gt;](OriginPlanetIn.md)
`biomeTypes` | [Array&lt;BiomeTypeIn&gt;](BiomeTypeIn.md)
`enclosures` | [Array&lt;EnclosureIn&gt;](EnclosureIn.md)
`id` | number
`name` | string

## Example

```typescript
import type { HabitatIn } from ''

// TODO: Update the object below with actual values
const example = {
  "originPlanets": null,
  "biomeTypes": null,
  "enclosures": null,
  "id": null,
  "name": null,
} satisfies HabitatIn

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as HabitatIn
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


