# coding: utf-8

"""
    This class is auto generated from the Infobip OpenAPI specification
    through the OpenAPI Specification Client API libraries (Re)Generator (OSCAR),
    powered by the OpenAPI Generator (https://openapi-generator.tech).
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field
from models.sms_delivery_day import SmsDeliveryDay
from models.sms_delivery_time_from import SmsDeliveryTimeFrom
from models.sms_delivery_time_to import SmsDeliveryTimeTo


class SmsDeliveryTimeWindow(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    days: List[SmsDeliveryDay] = Field(
        ...,
        description="Days of the week which are included in the delivery time window. At least one day must be provided. Separate multiple days with a comma.",
    )
    var_from: Optional[SmsDeliveryTimeFrom] = Field(None, alias="from")
    to: Optional[SmsDeliveryTimeTo] = None
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
    def from_json(cls, json_str: str) -> SmsDeliveryTimeWindow:
        """Create an instance of SmsDeliveryTimeWindow from a JSON string"""
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
    def from_dict(cls, obj: dict) -> SmsDeliveryTimeWindow:
        """Create an instance of SmsDeliveryTimeWindow from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SmsDeliveryTimeWindow.parse_obj(obj)

        _obj = SmsDeliveryTimeWindow.parse_obj(
            {
                "days": obj.get("days"),
                "var_from": SmsDeliveryTimeFrom.from_dict(obj.get("from"))
                if obj.get("from") is not None
                else None,
                "to": SmsDeliveryTimeTo.from_dict(obj.get("to"))
                if obj.get("to") is not None
                else None,
            }
        )
        return _obj
