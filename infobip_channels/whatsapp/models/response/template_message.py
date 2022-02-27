from typing import List, Optional

from infobip_channels.whatsapp.models.response.core import (
    WhatsAppResponse,
    WhatsAppResponseOKPayload,
)


class TemplateMessageResponseOK(WhatsAppResponse):
    messages: List[WhatsAppResponseOKPayload]
    bulk_id: Optional[str] = None
