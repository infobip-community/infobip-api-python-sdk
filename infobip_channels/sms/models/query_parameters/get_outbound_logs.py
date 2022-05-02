from datetime import datetime
from typing import List, Optional, Union

from pydantic import Field, conint, validator

from infobip_channels.core.models import (
    DateTimeValidator,
    GeneralStatus,
    QueryParameter,
)


class GetOutboundSMSLogsQueryParameters(QueryParameter, DateTimeValidator):
    from_name: Optional[str] = Field(alias="from", default=None)
    to: Optional[str] = None
    bulk_id: Optional[List[str]] = None
    message_id: Optional[List[str]] = None
    general_status: Optional[GeneralStatus] = None
    sent_since: Optional[Union[datetime, str]] = None
    sent_until: Optional[Union[datetime, str]] = None
    limit: Optional[conint(ge=1, le=1000)] = None
    mcc: Optional[str] = None
    mnc: Optional[str] = None

    @validator("sent_since")
    def convert_send_at_to_correct_format(cls, value):
        return super().convert_time_to_correct_format(value)

    @validator("sent_until")
    def convert_sent_until_to_correct_format(cls, value):
        return super().convert_time_to_correct_format(value)
