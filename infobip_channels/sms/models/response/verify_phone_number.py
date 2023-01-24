from typing import Optional

from infobip_channels.core.models import ResponseBase


class VerifyPhoneNumberResponse(ResponseBase):
    attempts_remaining: int
    msisdn: str
    pin_error: Optional[str]
    pin_id: str
    verified: bool