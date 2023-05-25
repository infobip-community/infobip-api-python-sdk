from __future__ import annotations

import json
import pprint
from typing import Optional

from pydantic import Field
from pydantic.main import BaseModel
from pydantic.types import StrictInt


class GetInboundMessagesQueryParameters(BaseModel):
    limit: Optional[StrictInt] = Field(
        None,
        alias="limit",
        description="Maximum number of delivery reports that will be returned.",
    )

    __properties = [
        "limit",
    ]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GetInboundMessagesQueryParameters:
        """Create an instance of GetInboundMessagesQueryParameters from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetInboundMessagesQueryParameters:
        """Create an instance of GetInboundMessagesQueryParameters from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GetInboundMessagesQueryParameters.parse_obj(obj)

        _obj = GetInboundMessagesQueryParameters.parse_obj({"limit": obj.get("limit")})
        return _obj
