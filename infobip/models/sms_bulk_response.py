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
from datetime import datetime
from inspect import getfullargspec
from typing import Optional

from pydantic import BaseModel, Field, StrictStr


class SmsBulkResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    bulk_id: Optional[StrictStr] = Field(
        None,
        alias="bulkId",
        description="Unique ID assigned to the request if messaging multiple recipients or sending multiple messages via a single API request.",
    )
    send_at: Optional[datetime] = Field(
        None,
        alias="sendAt",
        description="Date and time when the message is to be sent. Used for scheduled SMS (see [Scheduled SMS endpoints](#channels/sms/get-scheduled-sms-messages) for more details). Has the following format: `yyyy-MM-dd'T'HH:mm:ss.SSSZ`, and can only be scheduled for no later than 180 days in advance.",
    )
    __properties = ["bulkId", "sendAt"]

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
    def from_json(cls, json_str: str) -> SmsBulkResponse:
        """Create an instance of SmsBulkResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SmsBulkResponse:
        """Create an instance of SmsBulkResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SmsBulkResponse.parse_obj(obj)

        _obj = SmsBulkResponse.parse_obj(
            {"bulk_id": obj.get("bulkId"), "send_at": obj.get("sendAt")}
        )
        return _obj
