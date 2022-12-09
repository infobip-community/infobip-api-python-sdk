from typing import Optional, Dict

from infobip_channels.core.models import CamelCaseModel, MessageBodyBase


class SendPINOverSMSBody(MessageBodyBase, CamelCaseModel):
        application_id: str
        message_id: str
        from_id: Optional[str]
        to: str
        placeholders: Optional[Dict[str, str]]