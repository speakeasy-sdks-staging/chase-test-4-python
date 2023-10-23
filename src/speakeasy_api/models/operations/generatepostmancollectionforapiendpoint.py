"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import error as shared_error
from typing import Optional


@dataclasses.dataclass
class GeneratePostmanCollectionForAPIEndpointRequest:
    api_endpoint_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiEndpointID', 'style': 'simple', 'explode': False }})
    r"""The ID of the ApiEndpoint to generate a Postman collection for."""
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    r"""The ID of the Api to generate a Postman collection for."""
    version_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'versionID', 'style': 'simple', 'explode': False }})
    r"""The version ID of the Api to generate a Postman collection for."""
    



@dataclasses.dataclass
class GeneratePostmanCollectionForAPIEndpointResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    postman_collection: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""OK"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    
