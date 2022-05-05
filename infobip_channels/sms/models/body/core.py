from datetime import datetime
from enum import Enum
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
    CamelCaseModel,
    ContentTypeEnum,
    DateTimeValidator,
    DaysEnum,
    FromAndToTimeValidator,
)


class TrackEnum(str, Enum):
    SMS = "SMS"
    URL = "URL"


class TypeEnum(str, Enum):
    ONE_TIME_PIN = "ONE_TIME_PIN"
    SOCIAL_INVITES = "SOCIAL_INVITES"


class TimeUnitEnum(str, Enum):
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    DAY = "DAY"


class IndiaDlt(CamelCaseModel):
    content_template_id: Optional[str] = None
    principal_entity_id: str


class Regional(CamelCaseModel):
    india_dlt: Optional[IndiaDlt] = None


class Time(CamelCaseModel):
    hour: conint(ge=0, le=23)
    minute: conint(ge=0, le=59)


class Destination(CamelCaseModel):
    message_id: Optional[str] = None
    to: constr(min_length=0, max_length=50)


class DeliveryTimeWindow(CamelCaseModel, FromAndToTimeValidator):
    days: conlist(DaysEnum, min_items=1)
    from_time: Optional[Time] = Field(alias="from", default=None)
    to: Optional[Time] = None

    @root_validator
    def validate_from_and_to(cls, values):
        return super().validate_from_and_to(values)


class CoreMessage(CamelCaseModel, DateTimeValidator):
    callback_data: Optional[constr(min_length=0, max_length=4000)] = None
    delivery_time_window: Optional[DeliveryTimeWindow] = None
    destinations: List[Destination]
    flash: Optional[StrictBool] = False
    from_name: Optional[str] = Field(alias="from", default=None)
    intermediate_report: Optional[StrictBool] = False
    notify_content_type: Optional[ContentTypeEnum] = None
    notify_url: Optional[AnyHttpUrl] = None
    regional: Optional[Regional] = None
    send_at: Optional[Union[datetime, str]] = None
    validity_period: Optional[conint(gt=0, le=2880)]

    @validator("send_at")
    def convert_send_at_time_to_correct_format_validate_limit(cls, value):
        return super().convert_time_to_correct_format_validate_limit(value)


class SendingSpeedLimit(CamelCaseModel):
    amount: int
    time_unit: Optional[TimeUnitEnum] = None


class Tracking(CamelCaseModel):
    base_url: Optional[str] = None
    process_key: Optional[str] = None
    track: Optional[TrackEnum] = None
    type: Optional[TypeEnum] = None
