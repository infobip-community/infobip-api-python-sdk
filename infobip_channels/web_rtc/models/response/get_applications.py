from typing import List

from infobip_channels.core.models import ResponseBase
from infobip_channels.web_rtc.models.response.core import WebRtcResponseOKPayload


class GetApplicationsResponseOK(ResponseBase):
    list: List[WebRtcResponseOKPayload]
