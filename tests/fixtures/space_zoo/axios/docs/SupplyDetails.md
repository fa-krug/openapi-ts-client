# SupplyDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_package** | [**FoodPackageOut**](FoodPackageOut.md) |  | [default to undefined]
**habitat** | [**HabitatNames**](HabitatNames.md) |  | [default to undefined]
**image** | [**EnclosureNames**](EnclosureNames.md) |  | [default to undefined]
**licenses** | [**Array&lt;PermitOut&gt;**](PermitOut.md) |  | [default to undefined]
**tags** | [**Array&lt;SupplyCategoryOut&gt;**](SupplyCategoryOut.md) |  | [default to undefined]
**vulnerabilities** | [**Array&lt;VulnerabilityOut&gt;**](VulnerabilityOut.md) |  | [default to undefined]
**dependsOn** | [**Array&lt;SupplyOut&gt;**](SupplyOut.md) |  | [default to undefined]
**isOutdated** | **boolean** |  | [default to undefined]
**hasAllowedVersion** | **boolean** |  | [default to undefined]
**id** | **number** |  | [optional] [default to undefined]
**purl** | **string** |  | [optional] [default to undefined]
**version** | **string** |  | [optional] [default to undefined]
**bomRef** | **string** | BOM reference identifier for the dependency | [default to undefined]
**type** | **string** |  | [optional] [default to undefined]
**author** | **string** |  | [optional] [default to undefined]
**riskScore** | **number** | Dependency risk score | [optional] [default to 0]
**riskDetails** | **string** |  | [optional] [default to undefined]

## Example

```typescript
import { SupplyDetails } from './api';

const instance: SupplyDetails = {
    _package,
    habitat,
    image,
    licenses,
    tags,
    vulnerabilities,
    dependsOn,
    isOutdated,
    hasAllowedVersion,
    id,
    purl,
    version,
    bomRef,
    type,
    author,
    riskScore,
    riskDetails,
};
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
