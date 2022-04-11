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
    MessageBodyBase,
)


class ValidityPeriodTimeUnitEnum(str, Enum):
    SECONDS = "SECONDS"
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"


class Content(CamelCaseModel):
    pass


class SmsFailover(CamelCaseModel):
    pass


class RCSMessageBody(MessageBodyBase):
    from_number: Optional[str] = Field(alias="from")
    to: str
    validity_period: Optional[int] = None
    validity_period_time_unit: ValidityPeriodTimeUnitEnum
    content: Content
    sms_fail_over: SmsFailover
    notify_url: Optional[str] = None
    callback_data: Optional[str] = None
    message_id: Optional[str] = None
