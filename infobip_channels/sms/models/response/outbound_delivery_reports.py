from typing import List

from infobip_channels.core.models import ResponseBase
from infobip_channels.sms.models.response.core import CoreResult


class OutboundDeliveryReportsResponse(ResponseBase):
    results: List[CoreResult]
