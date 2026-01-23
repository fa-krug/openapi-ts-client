# SupplyOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | **[FoodPackageOut](FoodPackageOut.md)** |  | [optional] [default to undefined]
**habitat** | **[HabitatNames](HabitatNames.md)** |  | [optional] [default to undefined]
**image** | **[EnclosureNames](EnclosureNames.md)** |  | [optional] [default to undefined]
**tags** | **[Array&lt;SupplyCategoryOut&gt;](SupplyCategoryOut.md)** |  | [optional] [default to undefined]
**id** | **number** |  | [optional] [default to undefined]
**purl** | **string** |  | [optional] [default to undefined]
**version** | **string** |  | [optional] [default to undefined]
**bomRef** | **string** |  | [optional] [default to undefined]
**type** | **string** |  | [optional] [default to undefined]
**author** | **string** |  | [optional] [default to undefined]
**riskScore** | **number** |  | [optional] [default to undefined]
**riskDetails** | **string** |  | [optional] [default to undefined]
**licenses** | **Array&lt;number&gt;** |  | [optional] [default to undefined]
**dependsOn** | **Array&lt;number&gt;** |  | [optional] [default to undefined]

## Example

```typescript
import { SupplyOut } from './api';

const instance: SupplyOut = {
    package,
    habitat,
    image,
    tags,
    id,
    purl,
    version,
    bomRef,
    type,
    author,
    riskScore,
    riskDetails,
    licenses,
    dependsOn,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
