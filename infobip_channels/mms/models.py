from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, Field, StrictBool, conint, conlist, constr, validator

from infobip_channels.core.models import CamelCaseModel, MessageBodyBase


class DaysEnum(str, Enum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


class Time(CamelCaseModel):
    hour: conint(ge=0, le=23)
    minute: conint(ge=0, le=59)


class ExternallyHostedMedia(CamelCaseModel):
    content_type: str
    content_id: str
    content_url: AnyHttpUrl


class DeliveryTimeWindow(CamelCaseModel):
    days: conlist(DaysEnum, min_items=1)
    from_time: Optional[Time] = Field(alias="from", default=None)
    to: Optional[Time] = None


class Head(CamelCaseModel):
    from_number: str = Field(alias="from")
    to: str
    id: Optional[str] = None
    subject: Optional[str] = None
    validity_period_minutes: Optional[int] = None
    callback_data: Optional[constr(max_length=200)] = None
    notify_url: Optional[AnyHttpUrl] = None
    send_at: Optional[Union[datetime, str]] = None
    intermediate_report: Optional[StrictBool] = False
    delivery_time_window: Optional[DeliveryTimeWindow] = None

    @validator("send_at")
    def convert_send_at_to_correct_format(cls, value):
        if not value:
            return

        if isinstance(value, str):
            value = datetime.fromisoformat(value)

        time_with_microseconds = value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        return time_with_microseconds.split("Z")[0][:-3] + "Z"


class MMSMessageBody(MessageBodyBase):
    head: Head
    text: Optional[str] = None
    media: Optional[str] = None
    externally_hosted_media: Optional[List[ExternallyHostedMedia]] = None
    smil: Optional[str] = None
