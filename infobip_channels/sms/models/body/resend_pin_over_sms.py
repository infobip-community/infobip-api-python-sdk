from typing import Optional, Dict

from infobip_channels.core.models import MessageBodyBase, CamelCaseModel


class ResendPINOverSMSBody(MessageBodyBase, CamelCaseModel):
    placeholders: Optional[Dict[str, str]]
