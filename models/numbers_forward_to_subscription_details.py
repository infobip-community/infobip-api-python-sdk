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


from pydantic import BaseModel
from models.numbers_voice_action_details import NumbersVoiceActionDetails


class NumbersForwardToSubscriptionDetails(NumbersVoiceActionDetails):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    __properties = ["type", "description"]

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
    def from_json(cls, json_str: str) -> NumbersForwardToSubscriptionDetails:
        """Create an instance of NumbersForwardToSubscriptionDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumbersForwardToSubscriptionDetails:
        """Create an instance of NumbersForwardToSubscriptionDetails from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NumbersForwardToSubscriptionDetails.parse_obj(obj)

        _obj = NumbersForwardToSubscriptionDetails.parse_obj(
            {"type": obj.get("type"), "description": obj.get("description")}
        )
        return _obj
