from typing import Optional

from infobip_channels.core.models import ResponseBase


class SendPINOverVoiceResponse(ResponseBase):
    pin_id: str
    to: str
    call_status: Optional[str]
