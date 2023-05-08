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
from typing import Optional

from pydantic import BaseModel, Field, conint


class MmsDeliveryTime(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    hour: Optional[conint(strict=True, le=23, ge=0)] = Field(
        None,
        description="Hour when the time window opens when used in the `from` property or closes when used in the `to` property.",
    )
    minute: Optional[conint(strict=True, le=59, ge=0)] = Field(
        None,
        description="Minute when the time window opens when used in the `from` property or closes when used in the `to` property.",
    )
    __properties = ["hour", "minute"]

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
    def from_json(cls, json_str: str) -> MmsDeliveryTime:
        """Create an instance of MmsDeliveryTime from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MmsDeliveryTime:
        """Create an instance of MmsDeliveryTime from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MmsDeliveryTime.parse_obj(obj)

        _obj = MmsDeliveryTime.parse_obj(
            {"hour": obj.get("hour"), "minute": obj.get("minute")}
        )
        return _obj
