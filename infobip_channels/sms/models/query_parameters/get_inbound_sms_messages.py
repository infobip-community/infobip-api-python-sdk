from typing import Optional

from pydantic import conint

from infobip_channels.core.models import QueryParameter


class GetInboundSMSMessagesQueryParameters(QueryParameter):
    limit: Optional[conint(ge=1, le=1000)]
