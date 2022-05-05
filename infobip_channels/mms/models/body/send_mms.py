from datetime import datetime
from io import IOBase
from typing import List, Optional, Union

from pydantic import (
    AnyHttpUrl,
    Field,
    StrictBool,
    conint,
    conlist,
    constr,
    root_validator,
    validator,
)

from infobip_channels.core.models import (
    XML,
    CamelCaseModel,
    DateTimeValidator,
    DaysEnum,
    FromAndToTimeValidator,
    MessageBodyBase,
    MultipartMixin,
)


class Time(CamelCaseModel):
    hour: conint(ge=0, le=23)
    minute: conint(ge=0, le=59)


class ExternallyHostedMedia(CamelCaseModel):
    content_type: str
    content_id: str
    content_url: AnyHttpUrl


class DeliveryTimeWindow(CamelCaseModel, FromAndToTimeValidator):
    days: conlist(DaysEnum, min_items=1)
    from_time: Optional[Time] = Field(alias="from", default=None)
    to: Optional[Time] = None

    @root_validator
    def validate_from_and_to(cls, values):
        return super().validate_from_and_to(values)


class Head(CamelCaseModel, DateTimeValidator):
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
        return super().convert_time_to_correct_format(value)


class MMSMessageBody(MultipartMixin, MessageBodyBase):
    head: Head
    text: Optional[str] = None
    media: Optional[IOBase] = None
    externally_hosted_media: Optional[List[ExternallyHostedMedia]] = None
    smil: Optional[XML] = None

    class Config(CamelCaseModel.Config):
        arbitrary_types_allowed = True
