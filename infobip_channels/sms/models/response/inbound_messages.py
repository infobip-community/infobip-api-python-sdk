from typing import List, Optional

from pydantic import Field

from infobip_channels.core.models import CamelCaseModel, ResponseBase
from infobip_channels.sms.models.response.core import Price


class Result(CamelCaseModel):
    message_id: Optional[str] = None
    from_name: Optional[str] = Field(alias="from", default=None)
    to: Optional[str] = None
    text: Optional[str] = None
    clean_text: Optional[str] = None
    keyword: Optional[str] = None
    received_at: Optional[str] = None
    sms_count: Optional[int] = None
    price: Optional[Price] = None
    callback_data: Optional[str] = None


class InboundSMSMessagesResponse(ResponseBase):
    results: List[Result]
    message_count: Optional[int] = None
    pending_message_count: Optional[int] = None
