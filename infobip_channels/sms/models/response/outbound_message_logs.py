from typing import List, Optional

from infobip_channels.core.models import ResponseBase
from infobip_channels.sms.models.response.core import CoreResult


class Result(CoreResult):
    mcc_mnc: Optional[str] = None


class OutboundMessageLogsResponse(ResponseBase):
    results: List[Result]
