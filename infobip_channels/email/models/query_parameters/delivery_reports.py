from typing import Optional

from infobip_channels.core.models import QueryParameter


class DeliveryReportsQueryParameters(QueryParameter):
    bulkId: Optional[str]
    messageId: Optional[str]
    limit: Optional[str]
