from typing import Optional

from infobip_channels.core.models import QueryParameter


class SendPINOverVoiceQueryParameters(QueryParameter):
    nc_needed: Optional[bool]
