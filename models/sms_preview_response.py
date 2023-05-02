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
from pydantic import BaseModel, Field, StrictStr
from models.sms_preview import SmsPreview


class PreviewSMSResponseBody(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    original_text: Optional[StrictStr] = Field(
        None,
        alias="originalText",
        description="Message content supplied in the request.",
    )
    previews: Optional[List[SmsPreview]] = Field(
        None,
        description="Allows for previewing the original message content once additional language configuration has been applied to it.",
    )
    __properties = ["originalText", "previews"]

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
    def from_json(cls, json_str: str) -> PreviewSMSResponseBody:
        """Create an instance of SmsPreviewResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in previews (list)
        _items = []
        if self.previews:
            for _item in self.previews:
                if _item:
                    _items.append(_item.to_dict())
            _dict["previews"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PreviewSMSResponseBody:
        """Create an instance of SmsPreviewResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PreviewSMSResponseBody.parse_obj(obj)

        _obj = PreviewSMSResponseBody.parse_obj(
            {
                "original_text": obj.get("originalText"),
                "previews": [
                    SmsPreview.from_dict(_item) for _item in obj.get("previews")
                ]
                if obj.get("previews") is not None
                else None,
            }
        )
        return _obj
