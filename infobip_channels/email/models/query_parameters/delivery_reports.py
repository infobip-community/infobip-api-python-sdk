from typing import Optional

from infobip_channels.core.models import QueryParameter


class DeliveryReportsQueryParameters(QueryParameter):
    bulk_id: Optional[str]
    message_id: Optional[str]
    limit: Optional[str]
