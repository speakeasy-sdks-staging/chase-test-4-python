# Speakeasy-API

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks-staging/chase-test-4-python.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks-staging/chase-test-4-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README
<!-- Start SDK Installation -->
# SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks-staging/chase-test-4-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->


```python
import speakeasy_api
from speakeasy_api.models import operations, shared

s = speakeasy_api.SpeakeasyAPI(
    api_key="",
)

req = operations.GetApisRequest(
    metadata={
        "key": [
            'string',
        ],
    },
    op=operations.GetApisOp(
        and_=False,
    ),
)

res = s.apis.get_apis(req)

if res.apis is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
# Available Resources and Operations


## [api_endpoints](docs/sdks/apiendpoints/README.md)

* [delete_api_endpoint](docs/sdks/apiendpoints/README.md#delete_api_endpoint) - Delete an ApiEndpoint.
* [find_api_endpoint](docs/sdks/apiendpoints/README.md#find_api_endpoint) - Find an ApiEndpoint via its displayName.
* [generate_open_api_spec_for_api_endpoint](docs/sdks/apiendpoints/README.md#generate_open_api_spec_for_api_endpoint) - Generate an OpenAPI specification for a particular ApiEndpoint.
* [generate_postman_collection_for_api_endpoint](docs/sdks/apiendpoints/README.md#generate_postman_collection_for_api_endpoint) - Generate a Postman collection for a particular ApiEndpoint.
* [get_all_api_endpoints](docs/sdks/apiendpoints/README.md#get_all_api_endpoints) - Get all Api endpoints for a particular apiID.
* [get_all_for_version_api_endpoints](docs/sdks/apiendpoints/README.md#get_all_for_version_api_endpoints) - Get all ApiEndpoints for a particular apiID and versionID.
* [get_api_endpoint](docs/sdks/apiendpoints/README.md#get_api_endpoint) - Get an ApiEndpoint.
* [upsert_api_endpoint](docs/sdks/apiendpoints/README.md#upsert_api_endpoint) - Upsert an ApiEndpoint.

## [apis](docs/sdks/apis/README.md)

* [delete_api](docs/sdks/apis/README.md#delete_api) - Delete an Api.
* [generate_open_api_spec](docs/sdks/apis/README.md#generate_open_api_spec) - Generate an OpenAPI specification for a particular Api.
* [generate_postman_collection](docs/sdks/apis/README.md#generate_postman_collection) - Generate a Postman collection for a particular Api.
* [get_all_api_versions](docs/sdks/apis/README.md#get_all_api_versions) - Get all Api versions for a particular ApiEndpoint.
* [get_apis](docs/sdks/apis/README.md#get_apis) - Get a list of Apis for a given workspace
* [upsert_api](docs/sdks/apis/README.md#upsert_api) - Upsert an Api

## [embeds](docs/sdks/embeds/README.md)

* [get_embed_access_token](docs/sdks/embeds/README.md#get_embed_access_token) - Get an embed access token for the current workspace.
* [get_valid_embed_access_tokens](docs/sdks/embeds/README.md#get_valid_embed_access_tokens) - Get all valid embed access tokens for the current workspace.
* [revoke_embed_access_token](docs/sdks/embeds/README.md#revoke_embed_access_token) - Revoke an embed access EmbedToken.

## [metadata](docs/sdks/metadata/README.md)

* [delete_version_metadata](docs/sdks/metadata/README.md#delete_version_metadata) - Delete metadata for a particular apiID and versionID.
* [get_version_metadata](docs/sdks/metadata/README.md#get_version_metadata) - Get all metadata for a particular apiID and versionID.
* [insert_version_metadata](docs/sdks/metadata/README.md#insert_version_metadata) - Insert metadata for a particular apiID and versionID.

## [requests](docs/sdks/requests/README.md)

* [generate_request_postman_collection](docs/sdks/requests/README.md#generate_request_postman_collection) - Generate a Postman collection for a particular request.
* [get_request_from_event_log](docs/sdks/requests/README.md#get_request_from_event_log) - Get information about a particular request.
* [query_event_log](docs/sdks/requests/README.md#query_event_log) - Query the event log to retrieve a list of requests.

## [schemas](docs/sdks/schemas/README.md)

* [delete_schema](docs/sdks/schemas/README.md#delete_schema) - Delete a particular schema revision for an Api.
* [download_schema](docs/sdks/schemas/README.md#download_schema) - Download the latest schema for a particular apiID.
* [download_schema_revision](docs/sdks/schemas/README.md#download_schema_revision) - Download a particular schema revision for an Api.
* [get_schema](docs/sdks/schemas/README.md#get_schema) - Get information about the latest schema.
* [get_schema_diff](docs/sdks/schemas/README.md#get_schema_diff) - Get a diff of two schema revisions for an Api.
* [get_schema_revision](docs/sdks/schemas/README.md#get_schema_revision) - Get information about a particular schema revision for an Api.
* [get_schemas](docs/sdks/schemas/README.md#get_schemas) - Get information about all schemas associated with a particular apiID.
* [register_schema](docs/sdks/schemas/README.md#register_schema) - Register a schema.
<!-- End SDK Available Operations -->

<!-- Start Dev Containers -->



<!-- End Dev Containers -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
