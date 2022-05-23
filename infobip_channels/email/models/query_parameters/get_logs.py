from datetime import datetime
from typing import Optional, Union

from pydantic import Field, validator

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
    sent_since: Optional[Union[datetime, str]] = None
    sent_until: Optional[Union[datetime, str]] = None
    limit: Optional[int] = None

    @validator("sent_since")
    def convert_sent_since_to_correct_format(cls, value):
        return super().convert_time_to_correct_format(value)

    @validator("sent_until")
    def convert_sent_until_to_correct_format(cls, value):
        return super().convert_time_to_correct_format(value)
