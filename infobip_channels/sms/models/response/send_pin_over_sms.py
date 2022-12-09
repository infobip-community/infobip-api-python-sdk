from typing import Optional

from infobip_channels.core.models import ResponseBase


class SendPINOverSMSResponse(ResponseBase):
    pin_id: str
    to: str
    call_status: Optional[str]
    nc_status: Optional[str]
    sms_status: Optional[str]