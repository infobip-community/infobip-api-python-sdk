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
from pydantic import BaseModel, Field, StrictStr, constr, validator


class PreviewSMSRequestBody(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    text: StrictStr = Field(..., description="Content of the message being sent.")
    language_code: Optional[constr(strict=True)] = Field(
        None,
        alias="languageCode",
        description="Language code for the correct character set. Possible values: `TR` for Turkish, `ES` for Spanish, `PT` for Portuguese, or `AUTODETECT` to let platform select the character set based on message content.",
    )
    transliteration: Optional[constr(strict=True)] = Field(
        None,
        description="The transliteration of your sent message from one script to another. Transliteration is used to replace characters which are not recognized as part of your defaulted alphabet. Possible values: `TURKISH`, `GREEK`, `CYRILLIC`, `SERBIAN_CYRILLIC`, `BULGARIAN_CYRILLIC`, `CENTRAL_EUROPEAN`, `BALTIC` and `NON_UNICODE`.",
    )
    __properties = ["text", "languageCode", "transliteration"]

    @validator("language_code")
    def language_code_validate_regular_expression(cls, v):
        if not re.match(r"^(TR|ES|PT|AUTODETECT)$", v):
            raise ValueError(
                r"must validate the regular expression /^(TR|ES|PT|AUTODETECT)$/"
            )
        return v

    @validator("transliteration")
    def transliteration_validate_regular_expression(cls, v):
        if not re.match(
            r"^(TURKISH|GREEK|CYRILLIC|SERBIAN_CYRILLIC|BULGARIAN_CYRILLIC|CENTRAL_EUROPEAN|BALTIC|NON_UNICODE)$",
            v,
        ):
            raise ValueError(
                r"must validate the regular expression /^(TURKISH|GREEK|CYRILLIC|SERBIAN_CYRILLIC|BULGARIAN_CYRILLIC|CENTRAL_EUROPEAN|BALTIC|NON_UNICODE)$/"
            )
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
    def from_json(cls, json_str: str) -> PreviewSMSRequestBody:
        """Create an instance of SmsPreviewRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PreviewSMSRequestBody:
        """Create an instance of SmsPreviewRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PreviewSMSRequestBody.parse_obj(obj)

        _obj = PreviewSMSRequestBody.parse_obj(
            {
                "text": obj.get("text"),
                "language_code": obj.get("languageCode"),
                "transliteration": obj.get("transliteration"),
            }
        )
        return _obj
