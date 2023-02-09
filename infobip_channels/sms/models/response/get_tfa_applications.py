from typing import List

from infobip_channels.core.models import ResponseBase
from infobip_channels.sms.models.core.tfa_application import TFAApplication


class GetTFAApplicationsResponse(ResponseBase):
    list: List[TFAApplication]
