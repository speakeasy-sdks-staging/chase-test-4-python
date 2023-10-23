"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apiendpoint as shared_apiendpoint
from ..shared import error as shared_error
from typing import List, Optional


@dataclasses.dataclass
class GetAllAPIEndpointsRequest:
    api_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'apiID', 'style': 'simple', 'explode': False }})
    r"""The ID of the Api to retrieve ApiEndpoints for."""
    



@dataclasses.dataclass
class GetAllAPIEndpointsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    api_endpoints: Optional[List[shared_apiendpoint.APIEndpoint]] = dataclasses.field(default=None)
    r"""OK"""
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    r"""Default error response"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

