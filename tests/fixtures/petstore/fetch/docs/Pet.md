
# Pet


## Properties

Name | Type
------------ | -------------
`id` | number
`name` | string
`category` | [Category](Category.md)
`photoUrls` | Array&lt;string&gt;
`tags` | [Array&lt;Tag&gt;](Tag.md)
`status` | string

## Example

```typescript
import type { Pet } from ''

// TODO: Update the object below with actual values
const example = {
  "id": 10,
  "name": doggie,
  "category": null,
  "photoUrls": null,
  "tags": null,
  "status": null,
} satisfies Pet

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as Pet
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


