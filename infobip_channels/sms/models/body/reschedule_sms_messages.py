from datetime import datetime
from typing import Optional, Union

from pydantic import validator

from infobip_channels.core.models import DateTimeValidator, MessageBodyBase


class RescheduleSMSMessagesMessageBody(MessageBodyBase, DateTimeValidator):
    send_at: Optional[Union[datetime, str]] = None

    @validator("send_at")
    def convert_send_at_time_to_correct_format_validate_limit(cls, value):
        return super().convert_time_to_correct_format_validate_limit(value)
