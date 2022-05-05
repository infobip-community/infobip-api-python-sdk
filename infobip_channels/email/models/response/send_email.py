from typing import List, Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus


class SendEmailResponseMessage(CamelCaseModel):
    to: Optional[str] = None
    message_count: Optional[int] = None
    message_id: Optional[str] = None
    status: ResponseStatus


class SendEmailResponse(ResponseBase):
    messages: List[SendEmailResponseMessage]
