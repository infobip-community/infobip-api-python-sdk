from typing import Optional

from pydantic import Field

from infobip_channels.core.models import (
    DateTimeValidator,
    GeneralStatus,
    QueryParameter,
)


class GetLogsQueryParameters(QueryParameter, DateTimeValidator):
    message_id: Optional[str] = None
    from_email: Optional[str] = Field(alias="from")
    to: Optional[str] = None
    bulk_id: Optional[str] = None
    general_status: Optional[GeneralStatus] = None
    sent_since: Optional[str] = None
    sent_until: Optional[str] = None
    limit: Optional[int] = None
