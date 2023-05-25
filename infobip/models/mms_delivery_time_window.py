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
from typing import List, Optional

from pydantic import BaseModel, Field

from infobip.models.mms_delivery_day import MmsDeliveryDay
from infobip.models.mms_delivery_time import MmsDeliveryTime


class MmsDeliveryTimeWindow(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    days: List[MmsDeliveryDay] = Field(
        ...,
        description="Days of the week which are included in the delivery time window. At least one day must be provided.",
    )
    var_from: Optional[MmsDeliveryTime] = Field(None, alias="from")
    to: Optional[MmsDeliveryTime] = None
    __properties = ["days", "from", "to"]

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
    def from_json(cls, json_str: str) -> MmsDeliveryTimeWindow:
        """Create an instance of MmsDeliveryTimeWindow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_from
        if self.var_from:
            _dict["from"] = self.var_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to
        if self.to:
            _dict["to"] = self.to.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MmsDeliveryTimeWindow:
        """Create an instance of MmsDeliveryTimeWindow from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MmsDeliveryTimeWindow.parse_obj(obj)

        _obj = MmsDeliveryTimeWindow.parse_obj(
            {
                "days": obj.get("days"),
                "var_from": MmsDeliveryTime.from_dict(obj.get("from"))
                if obj.get("from") is not None
                else None,
                "to": MmsDeliveryTime.from_dict(obj.get("to"))
                if obj.get("to") is not None
                else None,
            }
        )
        return _obj
