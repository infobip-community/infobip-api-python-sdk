from datetime import datetime
from typing import Union

from pydantic import validator

from infobip_channels.core.models import DateTimeValidator, MessageBodyBase


class RescheduleMessagesMessageBody(MessageBodyBase, DateTimeValidator):
    send_at: Union[datetime, str]

    @validator("send_at")
    def convert_send_at_to_correct_format(cls, value):
        return super().convert_time_to_correct_format(value)
