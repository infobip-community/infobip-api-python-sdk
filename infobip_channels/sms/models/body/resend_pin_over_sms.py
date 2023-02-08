from typing import Dict, Optional

from infobip_channels.core.models import CamelCaseModel, MessageBodyBase


class ResendPINOverSMSBody(MessageBodyBase, CamelCaseModel):
    placeholders: Optional[Dict[str, str]]
