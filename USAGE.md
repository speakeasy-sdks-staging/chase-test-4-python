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