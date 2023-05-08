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

from pydantic import BaseModel, Field, StrictStr


class MmsAdvancedMessageSegmentUploadReference(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    content_id: Optional[StrictStr] = Field(
        None,
        alias="contentId",
        description="Unique identifier within single message. `[a-zA-Z]` up to 20 characters. Using other characters (e.g. spaces) may cause your message to be rejected by some mobile carriers.",
    )
    uploaded_content_id: Optional[StrictStr] = Field(
        None,
        alias="uploadedContentId",
        description="ID of previously uploaded binary content.",
    )
    __properties = ["contentId", "uploadedContentId"]

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
    def from_json(cls, json_str: str) -> MmsAdvancedMessageSegmentUploadReference:
        """Create an instance of MmsAdvancedMessageSegmentUploadReference from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MmsAdvancedMessageSegmentUploadReference:
        """Create an instance of MmsAdvancedMessageSegmentUploadReference from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MmsAdvancedMessageSegmentUploadReference.parse_obj(obj)

        _obj = MmsAdvancedMessageSegmentUploadReference.parse_obj(
            {
                "content_id": obj.get("contentId"),
                "uploaded_content_id": obj.get("uploadedContentId"),
            }
        )
        return _obj
