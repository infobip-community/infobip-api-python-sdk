import json
import os
from datetime import datetime
from enum import Enum
from io import IOBase
from typing import Dict, List, Optional, Tuple, Union

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
from urllib3 import encode_multipart_formdata

from infobip_channels.core.models import XML, CamelCaseModel, MessageBodyBase

MINIMUM_DELIVERY_WINDOW_MINUTES = 60


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
    media: Optional[IOBase] = None
    externally_hosted_media: Optional[List[ExternallyHostedMedia]] = None
    smil: Optional[XML] = None

    class Config(CamelCaseModel.Config):
        arbitrary_types_allowed = True

    def to_multipart(self) -> Tuple[bytes, str]:
        multipart_fields = {"head": self._get_model_for_multipart(self.head)}
        self._populate_optional_fields(multipart_fields)
        return encode_multipart_formdata(multipart_fields)

    def _populate_optional_fields(self, multipart_fields: Dict) -> None:
        optional_fields = {}

        if self.text:
            optional_fields["text"] = (None, self.text, "text/plain")

        if self.media:
            optional_fields["media"] = (
                os.path.basename(self.media.name),
                self.media.read(),
            )

        if self.externally_hosted_media:
            optional_fields["externallyHostedMedia"] = self._get_model_for_multipart(
                self.externally_hosted_media
            )

        if self.smil:
            optional_fields["smil"] = (None, self.smil, "application/xml")

        multipart_fields.update(optional_fields)

    def _get_model_for_multipart(
        self, model: Union[CamelCaseModel, List[CamelCaseModel]]
    ) -> Tuple[None, str, str]:

        if isinstance(model, list):
            model_aliased = [item.dict(by_alias=True) for item in model]
        else:
            model_aliased = model.dict(by_alias=True)

        return None, json.dumps(model_aliased), "application/json"
