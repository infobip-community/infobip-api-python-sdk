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
from pydantic import BaseModel, Field, StrictStr
from models.sms_language import SmsLanguage


class SmsLanguageConfiguration(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    language: Optional[SmsLanguage] = None
    transliteration: Optional[StrictStr] = Field(
        None,
        description="Conversion of a message text from one script to another. Possible values: `TURKISH`, `GREEK`, `CYRILLIC`, `SERBIAN_CYRILLIC`, `BULGARIAN_CYRILLIC`, `CENTRAL_EUROPEAN`, `BALTIC` and `NON_UNICODE`.",
    )
    __properties = ["language", "transliteration"]

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
    def from_json(cls, json_str: str) -> SmsLanguageConfiguration:
        """Create an instance of SmsLanguageConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of language
        if self.language:
            _dict["language"] = self.language.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SmsLanguageConfiguration:
        """Create an instance of SmsLanguageConfiguration from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SmsLanguageConfiguration.parse_obj(obj)

        _obj = SmsLanguageConfiguration.parse_obj(
            {
                "language": SmsLanguage.from_dict(obj.get("language"))
                if obj.get("language") is not None
                else None,
                "transliteration": obj.get("transliteration"),
            }
        )
        return _obj
