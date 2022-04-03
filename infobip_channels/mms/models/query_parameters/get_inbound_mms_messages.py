from typing import Optional

from infobip_channels.core.models import QueryParameter


class GetInboundMMSMessagesQueryParameters(QueryParameter):
    limit: Optional[int] = None
