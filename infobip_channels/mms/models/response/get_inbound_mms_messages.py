from typing import List, Optional

from pydantic import Field

from infobip_channels.core.models import CamelCaseModel, ResponseBase
from infobip_channels.mms.models.response.core import Price


class Result(CamelCaseModel):
    message_id: Optional[str] = None
    to: Optional[str] = None
    from_id: Optional[str] = Field(default=None, alias="from")
    message: Optional[str] = None
    received_at: Optional[str] = None
    mms_count: Optional[int] = None
    callback_data: Optional[str] = None
    price: Optional[Price] = None


class GetInboundMMSMessagesResponse(ResponseBase):
    results: Optional[List[Result]] = None
