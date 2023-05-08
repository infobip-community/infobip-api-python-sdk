# coding: utf-8

"""
    This class is auto generated from the Infobip OpenAPI specification
    through the OpenAPI Specification Client API libraries (Re)Generator (OSCAR),
    powered by the OpenAPI Generator (https://openapi-generator.tech).
"""


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from inspect import getfullargspec

from pydantic import BaseModel, Field, conint


class NumberRegistrationPageInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    page: conint(strict=True, ge=0) = Field(..., description="Requested page number.")
    size: conint(strict=True, ge=1) = Field(..., description="Requested page size.")
    total_pages: conint(strict=True, ge=0) = Field(
        ...,
        alias="totalPages",
        description="The total number of pages of the results matching the requested parameters.",
    )
    total_results: conint(strict=True, ge=0) = Field(
        ...,
        alias="totalResults",
        description="The total number of the results matching the requested parameters.",
    )
    __properties = ["page", "size", "totalPages", "totalResults"]

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
    def from_json(cls, json_str: str) -> NumberRegistrationPageInfo:
        """Create an instance of NumberRegistrationPageInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumberRegistrationPageInfo:
        """Create an instance of NumberRegistrationPageInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NumberRegistrationPageInfo.parse_obj(obj)

        _obj = NumberRegistrationPageInfo.parse_obj(
            {
                "page": obj.get("page"),
                "size": obj.get("size"),
                "total_pages": obj.get("totalPages"),
                "total_results": obj.get("totalResults"),
            }
        )
        return _obj
