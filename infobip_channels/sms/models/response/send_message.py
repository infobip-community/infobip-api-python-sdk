from typing import List, Optional

from infobip_channels.core.models import CamelCaseModel, ResponseBase, ResponseStatus


class SendSMSResponseMessage(CamelCaseModel):
    message_id: Optional[str] = None
    status: ResponseStatus
    to: Optional[str] = None


class SendSMSResponse(ResponseBase):
    bulk_id: Optional[str] = None
    messages: List[SendSMSResponseMessage]
    error_message: Optional[str] = None
