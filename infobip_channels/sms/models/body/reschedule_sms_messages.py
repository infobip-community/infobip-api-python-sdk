from datetime import datetime, timedelta
from typing import Optional, Union

from pydantic import validator

from infobip_channels.core.models import MessageBodyBase


class RescheduleSMSMessagesMessageBody(MessageBodyBase):
    send_at: Optional[Union[datetime, str]] = None

    @validator("send_at")
    def convert_send_at_to_correct_format(cls, value):
        if not value:
            return

        if isinstance(value, str):
            value = datetime.fromisoformat(value)

        time_with_microseconds = value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        if value > datetime.now() + timedelta(days=180):
            raise ValueError(
                "Scheduled message must me sooner than 180 days from today"
            )
        else:
            return time_with_microseconds.split("Z")[0][:-3] + "Z"
