from typing import Optional

from infobip_channels.core.models import CamelCaseModel


class TFAApplicationConfiguration(CamelCaseModel):
    allow_multiple_pin_verifications: Optional[bool]
    pin_attempts: Optional[int]
    pinTimeToLive: Optional[str]
    verifyPinLimit: Optional[str]
    sendPinPerApplicationLimit: Optional[str]
    sendPinPerPhoneNumberLimit: Optional[str]
