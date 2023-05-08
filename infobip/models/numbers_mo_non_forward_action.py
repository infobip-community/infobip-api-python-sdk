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
from typing import Optional

from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

from infobip import models


class NumbersMoNonForwardAction(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    type: StrictStr = Field(
        ...,
        description="Defines action type. It is not possible to create new action type.",
    )
    editable: Optional[StrictBool] = Field(
        None,
        description="Flag which indicates if given action is editable. Ignored on POST/PUT requests.",
    )
    __properties = ["type", "editable"]

    @validator("type")
    def type_validate_enum(cls, v):
        if v not in (
            "PULL",
            "HTTP_FORWARD",
            "SMPP_FORWARD",
            "MAIL_FORWARD",
            "NO_ACTION",
            "BLOCK",
            "AUTORESPONSE",
            "USSD",
            "SEND_BULK_MT",
            "EMAIL_TO_SMS_FORWARD",
            "CNS_FWD",
            "USE_CONVERSATIONS",
            "FORWARD_TO_PSTN",
            "FORWARD_TO_IP",
            "FORWARD_TO_SOFT_PHONE",
            "FORWARD_TO_IVR",
            "VOICE_NUMBER_MASKING",
            "VOICE_CALL_DROP",
            "FORWARD_TO_WEBRTC",
            "VOICE_FORWARD_TO_CONVERSATIONS",
            "VOICE_FORWARD_TO_CONVERSATIONS_WITH_FLOW",
            "CALL_FORWARD_TO_APPLICATION",
            "FORWARD_TO_SUBSCRIPTION",
            "OTHER",
        ):
            raise ValueError(
                "must validate the enum values ('PULL', 'HTTP_FORWARD', 'SMPP_FORWARD', 'MAIL_FORWARD', 'NO_ACTION', 'BLOCK', 'AUTORESPONSE', 'USSD', 'SEND_BULK_MT', 'EMAIL_TO_SMS_FORWARD', 'CNS_FWD', 'USE_CONVERSATIONS', 'FORWARD_TO_PSTN', 'FORWARD_TO_IP', 'FORWARD_TO_SOFT_PHONE', 'FORWARD_TO_IVR', 'VOICE_NUMBER_MASKING', 'VOICE_CALL_DROP', 'FORWARD_TO_WEBRTC', 'VOICE_FORWARD_TO_CONVERSATIONS', 'VOICE_FORWARD_TO_CONVERSATIONS_WITH_FLOW', 'CALL_FORWARD_TO_APPLICATION', 'FORWARD_TO_SUBSCRIPTION', 'OTHER')"
            )
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = "type"

    # discriminator mappings
    __discriminator_value_class_map = {
        "AUTORESPONSE": "NumbersAutoResponseAction",
        "BLOCK": "NumbersBlockAction",
        "NumbersAutoResponseAction": "NumbersAutoResponseAction",
        "NumbersBlockAction": "NumbersBlockAction",
    }

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(
        cls, json_str: str
    ) -> Union(NumbersAutoResponseAction, NumbersBlockAction):
        """Create an instance of NumbersMoNonForwardAction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> Union(NumbersAutoResponseAction, NumbersBlockAction):
        """Create an instance of NumbersMoNonForwardAction from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = getattr(models, object_type)
            return klass.from_dict(obj)
        else:
            raise ValueError(
                "NumbersMoNonForwardAction failed to lookup discriminator value from "
                + json.dumps(obj)
                + ". Discriminator property name: "
                + cls.__discriminator_property_name
                + ", mapping: "
                + json.dumps(cls.__discriminator_value_class_map)
            )
