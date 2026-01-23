# CHANGELOG

<!-- version list -->

## v1.1.1 (2026-01-23)

### Bug Fixes

- **ci**: Configure semantic-release for automatic version bumping
  ([`17a8e51`](https://github.com/fa-krug/openapi-ts-client/commit/17a8e51ad287a0fe74e682ca84733731ee72b805))


## v1.1.0 (2026-01-23)

### Bug Fixes

- Ensure all Angular templates end with trailing newline
  ([`f5d3077`](https://github.com/fa-krug/openapi-ts-client/commit/f5d30770d7ff24879fc54c56cb57289f094a05ae))

- Extract basePath from OpenAPI servers
  ([`85d99c0`](https://github.com/fa-krug/openapi-ts-client/commit/85d99c06ac878091010e6428b73a5300803404e7))

- Match fixture whitespace in service imports
  ([`145be7d`](https://github.com/fa-krug/openapi-ts-client/commit/145be7d264f4647c40b08b6b257895946b191e15))

- Preserve camelCase operationId in method names
  ([`3e231fd`](https://github.com/fa-krug/openapi-ts-client/commit/3e231fd66567e15d3d04d4ad1e95b04b5afdcb74))

- Resolve linting issues in test-rework
  ([`0cf6eef`](https://github.com/fa-krug/openapi-ts-client/commit/0cf6eefb95a8817508b0e4bfd1f8a6f09b39a2ec))

- Sort service methods alphabetically
  ([`775bc57`](https://github.com/fa-krug/openapi-ts-client/commit/775bc574e5a334d9a5a9215a77f6bd85911c02d1))

- Use basePath template variable in api.base.service.ts
  ([`12a25b6`](https://github.com/fa-krug/openapi-ts-client/commit/12a25b69ea0be3bbbf479fc3482578c491934c2e))

- Use Contact email in header comments instead of full description
  ([`f96223d`](https://github.com/fa-krug/openapi-ts-client/commit/f96223de8a0d5674fa5649cc9d50b09b3b539777))

- **angular**: Correct service filename casing and header Contact field
  ([`2f860d0`](https://github.com/fa-krug/openapi-ts-client/commit/2f860d04f22524e2d169dc6b6de4a402c918d20d))

- **angular**: Filter complex anyOf schemas and deduplicate by content
  ([`1e35f74`](https://github.com/fa-krug/openapi-ts-client/commit/1e35f74a92f3e62dc70298b4a461362bf215428b))

- **angular**: Improve fixture compatibility for petstore test
  ([`1a06c5e`](https://github.com/fa-krug/openapi-ts-client/commit/1a06c5e0780860700c114e740a9f004e63a2e338))

- **angular**: Multiple generator fixes for fixture compatibility
  ([`18f2aa5`](https://github.com/fa-krug/openapi-ts-client/commit/18f2aa56e2ecb57b01d46e2faf5ee8d260dc6a11))

- **fetch**: Match fixture output exactly
  ([`8cacdc5`](https://github.com/fa-krug/openapi-ts-client/commit/8cacdc561f5793f60498b2f3e1a15f8dec48c419))

- **generator**: Fetch client generator improvements
  ([`2cb4df9`](https://github.com/fa-krug/openapi-ts-client/commit/2cb4df95ec1cf90cca51b3c379646cd3baea0500))

- **models**: Preserve property order for type imports
  ([`b99e0bd`](https://github.com/fa-krug/openapi-ts-client/commit/b99e0bd27396edbe3994a98989657766c887ac7d))

- **tests**: Update tests for generator implementation changes
  ([`9484c72`](https://github.com/fa-krug/openapi-ts-client/commit/9484c7286cc3990f03424b3fb175f9f19fe2a369))

### Chores

- Add .worktrees to gitignore
  ([`3de320d`](https://github.com/fa-krug/openapi-ts-client/commit/3de320d91c543f30d54ab320a8ec99e590ac65fc))

- Add jinja2 and openapi-core dependencies
  ([`d6cca43`](https://github.com/fa-krug/openapi-ts-client/commit/d6cca438f13c7e729e807af7aebcfb613202e7ae))

- Create generators package structure
  ([`9036c83`](https://github.com/fa-krug/openapi-ts-client/commit/9036c839def571c97116789311ffc425f7c074b1))

- Create templates directory structure
  ([`8eefd02`](https://github.com/fa-krug/openapi-ts-client/commit/8eefd02572a3b4daa7a09e94bdec767ff0ed0c43))

- Create utils package structure
  ([`f6a770a`](https://github.com/fa-krug/openapi-ts-client/commit/f6a770afd15d884304ff8eba48f843c506a5508e))

- Export utils functions from package
  ([`b7111f4`](https://github.com/fa-krug/openapi-ts-client/commit/b7111f4d9a331487c10c037d3692bc50b31865c0))

- Un-ignore and add .claude/settings.local.json
  ([`41dddd4`](https://github.com/fa-krug/openapi-ts-client/commit/41dddd4510956cc5feade5e48a9a91a13a56d7f3))

### Code Style

- Apply ruff formatting
  ([`c0d6514`](https://github.com/fa-krug/openapi-ts-client/commit/c0d651431b602a1c7c3642be7c51e3774cd917c0))

- **models**: Fix import block formatting
  ([`f00e91d`](https://github.com/fa-krug/openapi-ts-client/commit/f00e91d26eeca80435e909a0fc4abc25eee553f8))

### Documentation

- Add Angular generator design document
  ([`41f87e9`](https://github.com/fa-krug/openapi-ts-client/commit/41f87e97f77405840be47296bc3eb91a5104a1b4))

- Add Angular generator implementation plan
  ([`781769b`](https://github.com/fa-krug/openapi-ts-client/commit/781769bfadbb84451803c2e90c2ce39761935623))

- Add anyOf type extraction design
  ([`cf56605`](https://github.com/fa-krug/openapi-ts-client/commit/cf5660507bdbe72f362bf2203e7764f0d66f9c24))

- Add anyOf type extraction implementation plan
  ([`2df2588`](https://github.com/fa-krug/openapi-ts-client/commit/2df258876cffcee71b38a18f513a1c6eec8f9dbb))

- Add fetch client generator design
  ([`526973b`](https://github.com/fa-krug/openapi-ts-client/commit/526973b8c0a8003fed9e10759ca763bc8289e3a2))

- Add fetch client implementation plan
  ([`d076b71`](https://github.com/fa-krug/openapi-ts-client/commit/d076b710a1c1ab9dc13b4f63b6704eaf3a099fbc))

- Add temp folder rule and implementation plans
  ([`55a8294`](https://github.com/fa-krug/openapi-ts-client/commit/55a8294a4f28366c2aa6b555e79f38ac8ed97e9a))

- Add test rework design for structural equivalence + validity
  ([`1fc55df`](https://github.com/fa-krug/openapi-ts-client/commit/1fc55dfecfaed35565d9d78507d4383945b45faf))

- Add test rework implementation plan
  ([`3c2ce92`](https://github.com/fa-krug/openapi-ts-client/commit/3c2ce92e4c693bba4593a20d9d2bcbd499a56b2a))

### Features

- Add Angular generator orchestrator and infrastructure templates
  ([`ba29aa2`](https://github.com/fa-krug/openapi-ts-client/commit/ba29aa2c94fc8a33a96f8ef16aa2583027541257))

- Add Angular service generator with templates
  ([`9906f1f`](https://github.com/fa-krug/openapi-ts-client/commit/9906f1fefbd196139d1725bf20ad0bb011f47f2a))

- Add array and $ref type mapping with import tracking
  ([`57c9ef7`](https://github.com/fa-krug/openapi-ts-client/commit/57c9ef7100bfd88ef7cdf9597845c9a0b4c9316f))

- Add basic OpenAPI to TypeScript type mapping
  ([`6e7a329`](https://github.com/fa-krug/openapi-ts-client/commit/6e7a3299e458d8da8da1cb7318970285b21681a1))

- Add enum generation for model properties
  ([`a711f72`](https://github.com/fa-krug/openapi-ts-client/commit/a711f724f517e9318f74577979bb9fbf474ae3ab))

- Add Jinja2 template for model interfaces
  ([`69b7c65`](https://github.com/fa-krug/openapi-ts-client/commit/69b7c65ea79eba9e72ccae4fcb150e23feb8f241))

- Add nullable type mapping for anyOf patterns
  ([`5ac41b8`](https://github.com/fa-krug/openapi-ts-client/commit/5ac41b8a238deaf0fa9afd26b44ccc442c91b5f5))

- Add OpenAPI spec loading and resolution utility
  ([`d0fadf7`](https://github.com/fa-krug/openapi-ts-client/commit/d0fadf79963fe0153f8b30078511fcfcf72683bf))

- Add operation_id_to_method_name naming utility
  ([`910feb1`](https://github.com/fa-krug/openapi-ts-client/commit/910feb18d72a92d6d1efb6ee6fc7c6e1d7d27a3b))

- Add schema_to_filename naming utility
  ([`6e4fe58`](https://github.com/fa-krug/openapi-ts-client/commit/6e4fe5874c0724137752726f9c4c41a837973e4d))

- Add tag_to_service_filename naming utility
  ([`197dd69`](https://github.com/fa-krug/openapi-ts-client/commit/197dd690135290ce208068b0c1da674bdb4dfb3a))

- Add tag_to_service_name naming utility
  ([`2167b06`](https://github.com/fa-krug/openapi-ts-client/commit/2167b060e245af176c4ebeb5d3808931346d6983))

- Implement Angular models generator
  ([`61cece5`](https://github.com/fa-krug/openapi-ts-client/commit/61cece5b4313e4503567425f945e8668c9523b95))

- Implement typescript structure verification infrastructure
  ([`c01e42f`](https://github.com/fa-krug/openapi-ts-client/commit/c01e42f76fa4f2d2c8a0fd22db430bf815950586))

- **angular**: Add anyof discovery function
  ([`dc72748`](https://github.com/fa-krug/openapi-ts-client/commit/dc72748749cfd32d4a9002063244e91094dddcd2))

- **angular**: Add create_extraction_registry entry point
  ([`19d450b`](https://github.com/fa-krug/openapi-ts-client/commit/19d450b580b2456ef3eb43ef680cb43a2fb6f019))

- **angular**: Add extracted type template
  ([`77706fb`](https://github.com/fa-krug/openapi-ts-client/commit/77706fb5b0a8069b3e3e4deb080222ff272a66ff))

- **angular**: Add generate_extracted_type_file function
  ([`3d7a681`](https://github.com/fa-krug/openapi-ts-client/commit/3d7a681065157fd329650ccfad62ded8046c6441))

- **angular**: Add metadata files and FILES manifest generation
  ([`dd54dd5`](https://github.com/fa-krug/openapi-ts-client/commit/dd54dd5f1321184932e220be19bb97f1477678f1))

- **angular**: Add name assignment with duplicate handling
  ([`e1384f9`](https://github.com/fa-krug/openapi-ts-client/commit/e1384f937796c519556d5110a7103f64b7ed29cc))

- **angular**: Add security credential initialization in configuration
  ([`b09fd8e`](https://github.com/fa-krug/openapi-ts-client/commit/b09fd8e6ee5eb5d9693e9398e7f1e7b0509ff6df))

- **angular**: Add security headers, content-type, and header params support
  ([`b38861d`](https://github.com/fa-krug/openapi-ts-client/commit/b38861df5e973d9f2aced0a21104dcf43f0d0729))

- **angular**: Integrate anyOf extraction into model generation
  ([`69df5e4`](https://github.com/fa-krug/openapi-ts-client/commit/69df5e4b41638383a63569fe69b265c9461cbe01))

- **angular**: Pass registry through model generation
  ([`d0a0a09`](https://github.com/fa-krug/openapi-ts-client/commit/d0a0a09adad74ad5fc28bee93cc5ef06bb34217a))

- **angular**: Update type mapper to use extraction registry
  ([`71ee5ac`](https://github.com/fa-krug/openapi-ts-client/commit/71ee5ac2facd00b9e7b34831add8b239193490b6))

- **generator**: Default to temp directory for output path
  ([`0ccfce2`](https://github.com/fa-krug/openapi-ts-client/commit/0ccfce2de1870882a0b10645dae0bab03665b1b5))

- **generator**: Implement fetch client generator
  ([`23e287b`](https://github.com/fa-krug/openapi-ts-client/commit/23e287b7d99018814e768500fd7d76e2cf5e24fa))

- **tests**: Replace fixture comparison with structural + validity tests
  ([`39f2783`](https://github.com/fa-krug/openapi-ts-client/commit/39f27834a3f682cb2c7adf2f07b112e35bf74e9b))

### Testing

- Add fixture comparison tests for Angular generator
  ([`9a56136`](https://github.com/fa-krug/openapi-ts-client/commit/9a561361386c0e60a3b02ee5550445d2ca4bf36e))

- Add petstore Angular client fixture for comparison testing
  ([`d5abb5c`](https://github.com/fa-krug/openapi-ts-client/commit/d5abb5c2d1dcc36e4daee97322b3000067f6d0c7))

- Add space zoo Angular client fixture for comparison testing
  ([`ca5b2e0`](https://github.com/fa-krug/openapi-ts-client/commit/ca5b2e0e1610171ccaa5a960afa3c2098bbef045))

- Update tests to use complex anyOf schemas
  ([`f59321e`](https://github.com/fa-krug/openapi-ts-client/commit/f59321ed4c610b0dea25bbf8e5dd45e7ddcf64c4))

- **fixtures**: Align fixture imports and properties with generator output
  ([`4696403`](https://github.com/fa-krug/openapi-ts-client/commit/4696403953c783670d09675030432a23cde51b27))


## v1.0.0 (2026-01-22)

- Initial Release
