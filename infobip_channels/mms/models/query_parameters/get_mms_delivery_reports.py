from typing import Optional

from infobip_channels.core.models import QueryParameter


class GetMMSDeliveryReportsQueryParameters(QueryParameter):
    bulk_id: Optional[str] = None
    message_id: Optional[str] = None
    limit: Optional[int] = None
