from typing import Optional

from infobip_channels.core.models import CamelCaseModel


class TFAApplicationConfiguration(CamelCaseModel):
    allow_multiple_pin_verifications: Optional[bool]
    pin_attempts: Optional[int]
    pin_time_to_live: Optional[str]
    verify_pin_limit: Optional[str]
    send_pin_per_application_limit: Optional[str]
    send_pin_per_phone_number_limit: Optional[str]
