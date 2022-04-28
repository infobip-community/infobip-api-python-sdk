from typing import Optional

from pydantic import conint

from infobip_channels.core.models import QueryParameter


class GetOutboundSMSDeliveryReportsQueryParameters(QueryParameter):
    bulk_id: Optional[str] = None
    message_id: Optional[str] = None
    limit: Optional[conint(ge=1, le=1000)]
