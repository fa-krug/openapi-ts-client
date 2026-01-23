# SupplyOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_package** | [**FoodPackageOut**](FoodPackageOut.md) |  | [default to undefined]
**habitat** | [**HabitatNames**](HabitatNames.md) |  | [default to undefined]
**image** | [**EnclosureNames**](EnclosureNames.md) |  | [default to undefined]
**tags** | [**Array&lt;SupplyCategoryOut&gt;**](SupplyCategoryOut.md) |  | [default to undefined]
**id** | **number** |  | [optional] [default to undefined]
**purl** | **string** |  | [optional] [default to undefined]
**version** | **string** |  | [optional] [default to undefined]
**bomRef** | **string** | BOM reference identifier for the dependency | [default to undefined]
**type** | **string** |  | [optional] [default to undefined]
**author** | **string** |  | [optional] [default to undefined]
**riskScore** | **number** | Dependency risk score | [optional] [default to 0]
**riskDetails** | **string** |  | [optional] [default to undefined]
**licenses** | **Array&lt;number&gt;** |  | [default to undefined]
**depends_on** | **Array&lt;number&gt;** |  | [default to undefined]

## Example

```typescript
import { SupplyOut } from './api';

const instance: SupplyOut = {
    _package,
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
    depends_on,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
