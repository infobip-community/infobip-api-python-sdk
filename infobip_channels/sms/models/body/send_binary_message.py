from typing import List, Optional

from pydantic import validator

from infobip_channels.core.models import CamelCaseModel, MessageBodyBase
from infobip_channels.sms.models.body.core import CoreMessage, SendingSpeedLimit


class Binary(CamelCaseModel):
    data_coding: Optional[int] = None
    esm_class: Optional[int] = None
    hex: str

    @validator("hex")
    def validate_string_characters(cls, value: str) -> str:
        remove_whitespace = "".join(value.split())
        try:
            int(remove_whitespace, 16)
            return value
        except ValueError:
            raise ValueError("Not all characters in hex field are hex values")


class Message(CoreMessage):
    binary: Binary


class BinarySMSMessageBody(MessageBodyBase):
    bulk_id: Optional[str] = None
    messages: List[Message]
    sending_speed_limit: Optional[SendingSpeedLimit] = None
