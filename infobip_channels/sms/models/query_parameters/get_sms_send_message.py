from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyHttpUrl, Field, StrictBool, conint, validator

from infobip_channels.core.models import QueryParameter, url_encoding


class TransliterationEnum(str, Enum):
    TURKISH = "TURKISH"
    GREEK = "GREEK"
    CYRILLIC = "CYRILLIC"
    SERBIAN_CYRILLIC = "SERBIAN_CYRILLIC"
    CENTRAL_EUROPEAN = "CENTRAL_EUROPEAN"
    BALTIC = "BALTIC"
    NON_UNICODE = "NON_UNICODE"


class ContentTypeEnum(str, Enum):
    APPLICATION_JSON = "application/json"
    APPLICATION_XML = "application/xml"


class TrackEnum(str, Enum):
    SMS = "SMS"
    URL = "URL"


class GetSMSSendMessageQueryParameters(QueryParameter):
    username: str
    password: str
    bulk_id: Optional[str] = None
    from_name: Optional[str] = Field(alias="from", default=None)
    to: List[str]
    text: Optional[str] = None
    flash: Optional[StrictBool] = False
    transliteration: Optional[TransliterationEnum]
    language_code: Optional[str] = None
    intermediate_report: Optional[StrictBool] = None
    notify_url: Optional[AnyHttpUrl] = None
    notify_content_type: Optional[ContentTypeEnum] = None
    callback_data: Optional[str] = None
    validity_period: Optional[conint(gt=0, le=2880)]
    send_at: Optional[Union[datetime, str]] = None  # todo validation
    track: Optional[TrackEnum] = None
    process_key: Optional[str] = None
    tracking_type: Optional[str] = None
    india_dlt_content_template_id: Optional[str] = None
    india_dlt_principal_entity_id: Optional[str] = None

    def url_encode(self):
        self.username = url_encoding(self.username)
        self.password = url_encoding(self.password)

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
