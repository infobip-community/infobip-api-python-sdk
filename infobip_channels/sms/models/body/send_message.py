from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import (
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
    MessageBodyBase,
)

MINIMUM_DELIVERY_WINDOW_MINUTES = 60


class ContentTypeEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    APPLICATION_XML = "application/xml"


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


class TransliterationEnum(str, Enum):
    TURKISH = "TURKISH"
    GREEK = "GREEK"
    CYRILLIC = "CYRILLIC"
    SERBIAN_CYRILLIC = "SERBIAN_CYRILLIC"
    CENTRAL_EUROPEAN = "CENTRAL_EUROPEAN"
    BALTIC = "BALTIC"
    NON_UNICODE = "NON_UNICODE"


class LanguageEnum(str, Enum):
    TURKISH = "TR"
    SPANISH = "ES"
    PORTUGUESE = "PORTUGUESE"
    AUTODETECT = "AUTODETECT"


class DaysEnum(str, Enum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


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


class DeliveryTimeWindow(CamelCaseModel):
    days: conlist(DaysEnum, min_items=1)
    from_time: Optional[Time] = Field(alias="from", default=None)
    to: Optional[Time] = None

    @root_validator
    def validate_from_and_to(cls, values):
        if not values.get("from_time") and not values.get("to"):
            return values

        if values.get("from_time") and not values.get("to"):
            raise ValueError("If 'from_time' is set, 'to' has to be set also")

        if values.get("to") and not values.get("from_time"):
            raise ValueError("If 'to' is set, 'from_time' has to be set also")

        cls._validate_time_differences(values["from_time"], values["to"])

        return values

    @classmethod
    def _validate_time_differences(cls, from_time: Time, to_time: Time):
        from_time_in_minutes = from_time.hour * 60 + from_time.minute
        to_time_in_minutes = to_time.hour * 60 + to_time.minute

        if to_time_in_minutes - from_time_in_minutes < MINIMUM_DELIVERY_WINDOW_MINUTES:
            raise ValueError(
                f"Minimum of {MINIMUM_DELIVERY_WINDOW_MINUTES} minutes has to pass "
                f"between from and to delivery window times."
            )


class Message(CamelCaseModel):
    callback_data: Optional[constr(min_length=0, max_length=4000)] = None
    delivery_time_window: Optional[DeliveryTimeWindow] = None
    destinations: List[Destination]
    flash: Optional[StrictBool] = False
    from_name: Optional[str] = Field(alias="from", default=None)
    intermediate_report: Optional[StrictBool] = False
    language: Optional[LanguageEnum] = None
    notify_content_type: Optional[ContentTypeEnum] = None
    notify_url: Optional[str] = None
    regional: Optional[Regional] = None
    send_at: Optional[Union[datetime, str]] = None
    text: Optional[str] = None
    transliteration: Optional[TransliterationEnum]
    validity_period: Optional[conint(gt=0, le=2880)]

    @validator("send_at")
    def convert_send_at_to_correct_format(cls, value):
        if not value:
            return

        if isinstance(value, str):
            value = datetime.fromisoformat(value)

        time_with_microseconds = value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        return time_with_microseconds.split("Z")[0][:-3] + "Z"


class SendingSpeedLimit(CamelCaseModel):
    amount: int
    time_unit: Optional[TimeUnitEnum] = None


class Tracking(CamelCaseModel):
    base_url: Optional[str] = None
    process_key: Optional[str] = None
    track: Optional[TrackEnum] = None
    type: Optional[TypeEnum] = None


class SMSMessageBody(MessageBodyBase):
    bulk_id: Optional[str] = None
    messages: List[Message]
    sending_speed_limit: Optional[SendingSpeedLimit] = None
    tracking: Optional[Tracking] = None
