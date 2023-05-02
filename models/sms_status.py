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
from pydantic import BaseModel, Field, StrictInt, StrictStr


class SmsStatus(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    group_id: Optional[StrictInt] = Field(
        None, alias="groupId", description="Status group ID."
    )
    group_name: Optional[StrictStr] = Field(
        None,
        alias="groupName",
        description="Status group name that describes which category the status code belongs to, e.g. PENDING, UNDELIVERABLE, DELIVERED, EXPIRED, REJECTED.",
    )
    id: Optional[StrictInt] = Field(None, description="Status ID.")
    name: Optional[StrictStr] = Field(
        None,
        description="[Status name](https://www.infobip.com/docs/essentials/response-status-and-error-codes).",
    )
    description: Optional[StrictStr] = Field(
        None, description="Human-readable description of the status."
    )
    action: Optional[StrictStr] = Field(
        None, description="Action that should be taken to recover from the error."
    )
    __properties = ["groupId", "groupName", "id", "name", "description", "action"]

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
    def from_json(cls, json_str: str) -> SmsStatus:
        """Create an instance of SmsStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SmsStatus:
        """Create an instance of SmsStatus from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SmsStatus.parse_obj(obj)

        _obj = SmsStatus.parse_obj(
            {
                "group_id": obj.get("groupId"),
                "group_name": obj.get("groupName"),
                "id": obj.get("id"),
                "name": obj.get("name"),
                "description": obj.get("description"),
                "action": obj.get("action"),
            }
        )
        return _obj
