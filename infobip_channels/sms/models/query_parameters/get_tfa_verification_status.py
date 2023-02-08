from typing import Optional

from infobip_channels.core.models import QueryParameter


class GetTFAVerificationStatusQueryParameters(QueryParameter):
    msisdn: str
    verified: Optional[bool]
    sent: Optional[bool]
