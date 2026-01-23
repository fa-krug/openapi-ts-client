# PetApi

All URIs are relative to */api/v3*

|Method | HTTP request | Description|
|------------- | ------------- | -------------|
|[**addPet**](#addpet) | **POST** /pet | Add a new pet to the store.|
|[**deletePet**](#deletepet) | **DELETE** /pet/{petId} | Deletes a pet.|
|[**findPetsByStatus**](#findpetsbystatus) | **GET** /pet/findByStatus | Finds Pets by status.|
|[**findPetsByTags**](#findpetsbytags) | **GET** /pet/findByTags | Finds Pets by tags.|
|[**getPetById**](#getpetbyid) | **GET** /pet/{petId} | Find pet by ID.|
|[**updatePet**](#updatepet) | **PUT** /pet | Update an existing pet.|
|[**updatePetWithForm**](#updatepetwithform) | **POST** /pet/{petId} | Updates a pet in the store with form data.|
|[**uploadFile**](#uploadfile) | **POST** /pet/{petId}/uploadImage | Uploads an image.|

# **addPet**
> Pet addPet(pet)

Add a new pet to the store.

### Example

```typescript
import {
    PetApi,
    Configuration,
    Pet
} from './api';

const configuration = new Configuration();
const apiInstance = new PetApi(configuration);

let pet: Pet; //Create a new pet in the store

const { status, data } = await apiInstance.addPet(
    pet
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pet** | **Pet**| Create a new pet in the store | |


### Return type

**Pet**

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful operation |  -  |
|**400** | Invalid input |  -  |
|**422** | Validation exception |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletePet**
> deletePet()

Delete a pet.

### Example

```typescript
import {
    PetApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new PetApi(configuration);

let petId: number; //Pet id to delete (default to undefined)
let apiKey: string; // (optional) (default to undefined)

const { status, data } = await apiInstance.deletePet(
    petId,
    apiKey
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **petId** | [**number**] | Pet id to delete | defaults to undefined|
| **apiKey** | [**string**] |  | (optional) defaults to undefined|


### Return type

void (empty response body)

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Pet deleted |  -  |
|**400** | Invalid pet value |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findPetsByStatus**
> Array<Pet> findPetsByStatus()

Multiple status values can be provided with comma separated strings.

### Example

```typescript
import {
    PetApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new PetApi(configuration);

let status: 'available' | 'pending' | 'sold'; //Status values that need to be considered for filter (default to 'available')

const { status, data } = await apiInstance.findPetsByStatus(
    status
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **status** | [**&#39;available&#39; | &#39;pending&#39; | &#39;sold&#39;**]**Array<&#39;available&#39; &#124; &#39;pending&#39; &#124; &#39;sold&#39;>** | Status values that need to be considered for filter | defaults to 'available'|


### Return type

**Array<Pet>**

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | successful operation |  -  |
|**400** | Invalid status value |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **findPetsByTags**
> Array<Pet> findPetsByTags()

Multiple tags can be provided with comma separated strings. Use tag1, tag2, tag3 for testing.

### Example

```typescript
import {
    PetApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new PetApi(configuration);

let tags: Array<string>; //Tags to filter by (default to undefined)

const { status, data } = await apiInstance.findPetsByTags(
    tags
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **tags** | **Array&lt;string&gt;** | Tags to filter by | defaults to undefined|


### Return type

**Array<Pet>**

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | successful operation |  -  |
|**400** | Invalid tag value |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getPetById**
> Pet getPetById()

Returns a single pet.

### Example

```typescript
import {
    PetApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new PetApi(configuration);

let petId: number; //ID of pet to return (default to undefined)

const { status, data } = await apiInstance.getPetById(
    petId
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **petId** | [**number**] | ID of pet to return | defaults to undefined|


### Return type

**Pet**

### Authorization

[petstore_auth](../README.md#petstore_auth), [api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | successful operation |  -  |
|**400** | Invalid ID supplied |  -  |
|**404** | Pet not found |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatePet**
> Pet updatePet(pet)

Update an existing pet by Id.

### Example

```typescript
import {
    PetApi,
    Configuration,
    Pet
} from './api';

const configuration = new Configuration();
const apiInstance = new PetApi(configuration);

let pet: Pet; //Update an existent pet in the store

const { status, data } = await apiInstance.updatePet(
    pet
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **pet** | **Pet**| Update an existent pet in the store | |


### Return type

**Pet**

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: application/json, application/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | Successful operation |  -  |
|**400** | Invalid ID supplied |  -  |
|**404** | Pet not found |  -  |
|**422** | Validation exception |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updatePetWithForm**
> Pet updatePetWithForm()

Updates a pet resource based on the form data.

### Example

```typescript
import {
    PetApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new PetApi(configuration);

let petId: number; //ID of pet that needs to be updated (default to undefined)
let name: string; //Name of pet that needs to be updated (optional) (default to undefined)
let status: string; //Status of pet that needs to be updated (optional) (default to undefined)

const { status, data } = await apiInstance.updatePetWithForm(
    petId,
    name,
    status
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **petId** | [**number**] | ID of pet that needs to be updated | defaults to undefined|
| **name** | [**string**] | Name of pet that needs to be updated | (optional) defaults to undefined|
| **status** | [**string**] | Status of pet that needs to be updated | (optional) defaults to undefined|


### Return type

**Pet**

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | successful operation |  -  |
|**400** | Invalid input |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploadFile**
> ApiResponse uploadFile()

Upload image of the pet.

### Example

```typescript
import {
    PetApi,
    Configuration
} from './api';

const configuration = new Configuration();
const apiInstance = new PetApi(configuration);

let petId: number; //ID of pet to update (default to undefined)
let additionalMetadata: string; //Additional Metadata (optional) (default to undefined)
let body: File; // (optional)

const { status, data } = await apiInstance.uploadFile(
    petId,
    additionalMetadata,
    body
);
```

### Parameters

|Name | Type | Description  | Notes|
|------------- | ------------- | ------------- | -------------|
| **body** | **File**|  | |
| **petId** | [**number**] | ID of pet to update | defaults to undefined|
| **additionalMetadata** | [**string**] | Additional Metadata | (optional) defaults to undefined|


### Return type

**ApiResponse**

### Authorization

[petstore_auth](../README.md#petstore_auth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
|**200** | successful operation |  -  |
|**400** | No file uploaded |  -  |
|**404** | Pet not found |  -  |
|**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

