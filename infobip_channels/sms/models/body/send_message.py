from typing import List, Optional

from infobip_channels.core.models import (
    CamelCaseModel,
    CoreMixin,
    LanguageEnum,
    MessageBodyBase,
    TransliterationEnum,
)
from infobip_channels.sms.models.body.core import (
    CoreMessage,
    SendingSpeedLimit,
    Tracking,
)


class Message(CoreMessage, CoreMixin):
    text: Optional[str] = None
    language: Optional[LanguageEnum] = None
    transliteration: Optional[TransliterationEnum]


class URLOptions(CamelCaseModel):
    shorten_url: Optional[bool] = None
    track_clicks: Optional[bool] = None
    tracking_url: Optional[str] = None
    remove_protocol: Optional[bool] = None
    custom_domain: Optional[str] = None


class SMSMessageBody(MessageBodyBase):
    bulk_id: Optional[str] = None
    messages: List[Message]
    sending_speed_limit: Optional[SendingSpeedLimit] = None
    url_options: Optional[URLOptions] = None
    tracking: Optional[Tracking] = None
    include_sms_count_in_response: Optional[bool] = None
