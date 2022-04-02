from typing import List, Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus


class SendMMSResponseMessage(CamelCaseModel):
    to: Optional[str] = None
    status: ResponseStatus
    message_id: Optional[str] = None


class SendMMSResponse(ResponseBase):
    bulk_id: Optional[str] = None
    messages: List[SendMMSResponseMessage]
    error_message: Optional[str] = None
