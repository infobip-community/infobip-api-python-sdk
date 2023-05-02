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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from models.numbers_mo_action import NumbersMoAction


class NumbersHttpForwardAction(NumbersMoAction):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    url: StrictStr = Field(
        ..., description="Specifies URL where message will be pushed."
    )
    http_method: StrictStr = Field(
        ..., alias="httpMethod", description="Specifies push format."
    )
    content_type: Optional[StrictStr] = Field(
        None, alias="contentType", description="Specifies content type."
    )
    __properties = ["type", "description", "url", "httpMethod", "contentType"]

    @validator("http_method")
    def http_method_validate_enum(cls, v):
        if v not in ("GET", "POST"):
            raise ValueError("must validate the enum values ('GET', 'POST')")
        return v

    @validator("content_type")
    def content_type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ("JSON", "XML"):
            raise ValueError("must validate the enum values ('JSON', 'XML')")
        return v

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
    def from_json(cls, json_str: str) -> NumbersHttpForwardAction:
        """Create an instance of NumbersHttpForwardAction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumbersHttpForwardAction:
        """Create an instance of NumbersHttpForwardAction from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NumbersHttpForwardAction.parse_obj(obj)

        _obj = NumbersHttpForwardAction.parse_obj(
            {
                "type": obj.get("type"),
                "description": obj.get("description"),
                "url": obj.get("url"),
                "http_method": obj.get("httpMethod"),
                "content_type": obj.get("contentType"),
            }
        )
        return _obj
