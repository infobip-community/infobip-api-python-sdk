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
from models.sms_bulk_status import SmsBulkStatus


class SmsBulkStatusResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    bulk_id: Optional[StrictStr] = Field(
        None,
        alias="bulkId",
        description="Unique ID assigned to the request if messaging multiple recipients or sending multiple messages via a single API request.",
    )
    status: Optional[SmsBulkStatus] = None
    __properties = ["bulkId", "status"]

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
    def from_json(cls, json_str: str) -> SmsBulkStatusResponse:
        """Create an instance of SmsBulkStatusResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SmsBulkStatusResponse:
        """Create an instance of SmsBulkStatusResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SmsBulkStatusResponse.parse_obj(obj)

        _obj = SmsBulkStatusResponse.parse_obj(
            {"bulk_id": obj.get("bulkId"), "status": obj.get("status")}
        )
        return _obj
