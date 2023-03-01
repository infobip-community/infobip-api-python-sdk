from typing import List, Optional

from infobip_channels.core.models import ResponseBase
from infobip_channels.sms.models.response.core import CoreResult


class SMSReport(CoreResult):
    mcc_mnc: Optional[str] = None
    callback_data: Optional[str] = None


class OutboundDeliveryReportsResponse(ResponseBase):
    results: List[SMSReport]
