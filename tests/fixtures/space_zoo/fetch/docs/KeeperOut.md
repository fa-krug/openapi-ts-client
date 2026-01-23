
# KeeperOut

User output schema.

## Properties

Name | Type
------------ | -------------
`firstName` | string
`lastName` | string
`username` | string
`email` | string
`permissions` | Array&lt;string&gt;
`isSuperuser` | boolean

## Example

```typescript
import type { KeeperOut } from ''

// TODO: Update the object below with actual values
const example = {
  "firstName": null,
  "lastName": null,
  "username": null,
  "email": null,
  "permissions": null,
  "isSuperuser": null,
} satisfies KeeperOut

console.log(example)

// Convert the instance to a JSON string
const exampleJSON: string = JSON.stringify(example)
console.log(exampleJSON)

// Parse the JSON string back to an object
const exampleParsed = JSON.parse(exampleJSON) as KeeperOut
console.log(exampleParsed)
```

[[Back to top]](#) [[Back to API list]](../README.md#api-endpoints) [[Back to Model list]](../README.md#models) [[Back to README]](../README.md)


