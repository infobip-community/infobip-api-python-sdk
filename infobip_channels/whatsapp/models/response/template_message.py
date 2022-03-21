from typing import List, Optional

from infobip_channels.core.models import ResponseBase
from infobip_channels.whatsapp.models.response.core import WhatsAppResponseOKPayload


class TemplateMessageResponseOK(ResponseBase):
    messages: List[WhatsAppResponseOKPayload]
    bulk_id: Optional[str] = None
