from typing import List, Optional

from infobip_channels.core.models import CamelCaseModel, MessageBodyBase
from infobip_channels.sms.models.body.core import CoreMessage, SendingSpeedLimit


class Binary(CamelCaseModel):
    data_coding: Optional[int] = None
    esm_class: Optional[int] = None
    hex: str


class Message(CoreMessage):
    binary: Binary


class SMSMessageBody(MessageBodyBase):
    bulk_id: Optional[str] = None
    messages: List[Message]
    sending_speed_limit: Optional[SendingSpeedLimit] = None
