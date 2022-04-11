from typing import List, Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus


class SendRCSResponseMessage(CamelCaseModel):
    to: Optional[str] = None
    message_count: Optional[int] = None
    message_id: Optional[str] = None
    status: ResponseStatus


class SendRCSResponse(ResponseBase):
    messages: List[SendRCSResponseMessage]
