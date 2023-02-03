from typing import Optional

from infobip_channels.core.models import CamelCaseModel


class PINVerification(CamelCaseModel):
    attempts_remaining: int
    msisdn: str
    pin_error: Optional[str]
    pin_id: str
    verified: bool
